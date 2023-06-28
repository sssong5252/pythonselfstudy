import cv2
import pytesseract
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def extract_text(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_image)
    return text

def preprocess_data(text_data):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text_data).toarray()
    return X

# 예제 이미지 파일 경로
image_paths = [
    "image1_A+.jpg", "image2_A+.jpg", "image3_A+.jpg",
    "image1_A.jpg", "image2_A.jpg", "image3_A.jpg",
    "image4_B+.jpg", "image5_B+.jpg", "image6_B+.jpg",
    "image7_B.jpg", "image8_B.jpg", "image9_B.jpg",
    "image10_C+.jpg", "image11_C+.jpg", "image12_C+.jpg",
    "image13_C.jpg", "image14_C.jpg", "image15_C.jpg"
]

text_data = [extract_text(image_path) for image_path in image_paths]

y = np.array([
    'A+', 'A+', 'A+'
    'A', 'A', 'A',
    'B+', 'B+', 'B+',
    'B', 'B', 'B',
    'C+', 'C+', 'C+',
    'C', 'C', 'C'
])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# 새로운 이미지 파일에서 텍스트 추출
new_image_path = "new_image.jpg"
new_text = extract_text(new_image_path)

# 텍스트 데이터 전처리 및 예측
new_X = preprocess_data([new_text])
predicted_grade = clf.predict(new_X)
print("예측된 학점:", predicted_grade[0])