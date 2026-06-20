import cv2
import numpy as np
import easyocr

# OCR ENGINE (load once)
reader = easyocr.Reader(['en'], gpu=False)

# PREPROCESS (LIGHT + SAFE)
def preprocess(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Resize small images (important for OCR accuracy)
    h, w = img.shape[:2]
    if max(h, w) < 1000:
        img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # Light enhancement only (DO NOT destroy image with grayscale/threshold)
    img = cv2.convertScaleAbs(img, alpha=1.1, beta=10)

    return img

# OCR FUNCTION (SAFE PARSING)
def extract_text(image):
    results = reader.readtext(image)

    texts = []
    confidences = []

    for item in results:
        if len(item) == 3:
            bbox, text, conf = item
        else:
            continue

        if conf > 0.25:
            texts.append(text)
            confidences.append(conf * 100)

    return texts, confidences, results

# DRAW RESULTS
def draw_results(image, results):
    output = image.copy()

    for item in results:
        if len(item) != 3:
            continue

        bbox, text, conf = item
        pts = np.array(bbox, np.int32)

        cv2.polylines(output, [pts], True, (0, 255, 0), 2)

        cv2.putText(
            output,
            text,
            tuple(pts[0]),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

    return output

# SAVE TEXT OUTPUT
def save_text(text_list):
    with open("ocr_output.txt", "w", encoding="utf-8") as f:
        for line in text_list:
            f.write(line + "\n")

    print(" Image saved: ocr_output.txt")

# BENCHMARK
def benchmark(confidences):
    if not confidences:
        print("\n⚠ No text detected.")
        return

    avg = sum(confidences) / len(confidences)

    print("\n OCR METRICS")
    print("----------------")
    print(f"Average Confidence: {avg:.2f}%")

    if avg > 80:
        print("Status:  High Quality")
    elif avg > 60:
        print("Status:  Medium Quality")
    else:
        print("Status:  Low Quality")


# MAIN PIPELINE
def run_pipeline(image_path):
    print("AI OCR SCANNER STARTED\n")

    image = preprocess(image_path)

    texts, confidences, raw = extract_text(image)

    print("\n EXTRACTED TEXT:")
    print("------------------")
    print("\n".join(texts) if texts else "No text found")

    save_text(texts)

    output_img = draw_results(image, raw)

    cv2.imwrite("ocr_output.jpg", output_img)
    print(" Image saved: ocr_output.jpg")

    benchmark(confidences)
    
# RUN
if __name__ == "__main__":
    image_path = r"C:\Users\notab\OneDrive\Desktop\toyota.jpg"
    run_pipeline(image_path)