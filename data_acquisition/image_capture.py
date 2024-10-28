import cv2

def capture_image(output_path='captured_image.jpg'):
    """カメラから画像を撮影し、保存する。"""
    try:
        cap = cv2.VideoCapture(0)  # 0はデフォルトのカメラ。必要に応じて変更
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return None

        ret, frame = cap.read()
        if not ret:
            print("Error: Could not capture image.")
            return None

        cv2.imwrite(output_path, frame)
        cap.release()
        return output_path

    except Exception as e:
        print(f"An error occurred during image capture: {e}")
        return None