import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 학습 데이터 준비 (예: [특성1, 특성2, 특성3])
X = np.array([[1, 1, 1], [1, 2, 1], [2, 1, 2], [2, 2, 2], [3, 2, 1], [3, 3, 3]])
y = np.array(['A', 'A', 'B+', 'B', 'C+', 'C'])

# 훈련 및 테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 인공지능 모델 생성 및 학습 (랜덤 포레스트 사용)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 테스트 데이터로 예측 및 평가
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# 학습한 모델로 새로운 과제 평가
new_assignment = np.array([[1, 2, 2]])  # 새로운 과제의 특성 입력
predicted_grade = clf.predict(new_assignment)
print("예측된 학점:", predicted_grade[0])
