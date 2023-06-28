import serial
import time
import numpy as np
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

attendance_list = []
attendance_data = []


def get_data_from_arduino():
    arduino = serial.Serial("COM3", 9600)  # Change "COM3" to the port the Arduino is connected to
    time.sleep(2)  # Wait for connection to establish
    while True:
        data = arduino.readline()
        data = data.decode()
        if "AttendanceData:" in data:
            _, hour, minute, rssi = data.split(" ")
            return int(hour), int(minute), int(rssi)


def scan_beacon():
    hour, minute, rssi = get_data_from_arduino()
    attendance_data.append([hour, minute, rssi])

    attendance_result = model.predict_classes(scaler.transform(np.array([[hour, minute, rssi]])))[0]
    if attendance_result == 1:
        print("참석 중")
    else:
        print("결석 중")
    attendance_list.append(attendance_result)


time_interval = 5 * 60  # 5분
total_duration = 60 * 60  # 1시간
start_time = time.time()

# 아두이노로부터 데이터를 수신하는 동안 5분 간격으로 스캔 실행
while time.time() - start_time < total_duration:
    scan_beacon()
    time.sleep(time_interval)

attendance_data = np.array(attendance_data)

# 샘플 참석 여부 (1: 참석, 0: 결석)
attended = np.random.randint(0, 2, size=len(attendance_data))

# 학습 데이터와 테스트 데이터로 나누기
X_train, X_test, y_train, y_test = train_test_split(attendance_data, attended, test_size=0.2, random_state=42)

# 데이터 정규화
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 딥러닝 모델 생성 및 학습
model = Sequential([
    Dense(32, activation='relu', input_shape=(3,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# 학습된 모델의 정확도 출력
accuracy = model.evaluate(X_test, y_test)[1]
print(f"모델 정확도: {accuracy:.4f}")


def calculate_attendance_percentage(attendance_list):
    total_entries = len(attendance_list)
    attended_count = sum(attendance_list)
    attendance_percentage = (attended_count / total_entries) * 100
    return attendance_percentage


# 스캔이 완료된 후 참석율 계산
attendance_percentage = calculate_attendance_percentage(attendance_list)
print(f"수업 참석율: {attendance_percentage:.2f}%")
