from transformers import AutoFeatureExtractor, DetrForObjectDetection, DetrImageProcessor
import torch
from PIL import Image
from PIL import UnidentifiedImageError
import requests

try:
    from timm.models.resnet import ResNet
    timm_available = True
except ImportError:
    timm_available = False
    print("Warning: timm library not found. DETR might not be available.")

feature_extractor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")

if timm_available:
    try:
        model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")
    except Exception as e:
        print(f"Failed to load model: {e}")
        model = None  # モデルのロードに失敗した場合、model を None に設定
else:
    model = None  # timm が利用できない場合は model を None に設定

def classify_image(image_path):
    """画像を分類し、食材名と推定重量を返す。"""
    if model is None:
        print("Error: Model is not loaded. Please install timm or check the model path.")
        return None, None  # food_type と weight の両方を None に設定

    try:
        image = Image.open(image_path)

        inputs = feature_extractor(images=image, return_tensors="pt")
        outputs = model(**inputs)

        logits = outputs.logits
        probas = outputs.logits.softmax(-1)[0, :, :-1]
        keep = probas.max(-1).values > 0.7  # 閾値

        predicted_labels = [model.config.id2label[prediction.item()] for prediction in probas[keep].argmax(-1)]

        # 現時点では重量推定は未実装なので、ダミー値またはセンサー値を使用
        estimated_weight = 0.5  # ダミー値。sensor_readerからの値などに置き換える

        return predicted_labels[0] if predicted_labels else None, estimated_weight

    except (FileNotFoundError, UnidentifiedImageError) as e:
        print(f"Error processing image: {e}")
        return None, None # food_type と weight の両方を None に設定
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None # food_type と weight の両方を None に設定