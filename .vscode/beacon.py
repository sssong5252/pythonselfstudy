import asyncio
import sqlite3
import pandas as pd
from datetime import datetime
from aioblescan.plugins.beacon import IBeacon
from aioblescan import BleScanRequester, EventHook
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import time

attendance_list = []
attendance_data = []

async def scan_beacon():
    global scanner, event_loop
    scanner.process = EventHook()
    scanner.process += process_scan_response
    await scanner.connect(event_loop)
    await scanner.start_scan()

def process_scan_response(scan_response):
    beacons = [dev for dev in scan_response.retrieve() if isinstance(dev, IBeacon)]
    for beacon in beacons:
        if beacon.uuid == "비콘이 필요해용":
            current_time = datetime.now()
            hour, minute = current_time.hour, current_time.minute
            rssi = beacon.rssi
            attendance_data.append([hour, minute, rssi])

            attendance_result = model.predict_classes(scaler.transform(np.array([[hour, minute, rssi]])))[0]
            if attendance_result == 1:
                print("참석 중")
            else:
                print("결석 중")
            attendance_list.append(attendance_result)

time_interval = 5 * 60  # 5분
total_duration = 60 * 60  # 1시간

scanner = BleScanRequester("hci0")
event_loop = asyncio.get_event_loop()
start_time = time.time()

# 1시간 동안 5분 간격으로 비콘 신호 읽기 실행
while time.time() - start_time < total_duration:
    event_loop.run_until_complete(scan_beacon())
    time.sleep(time_interval)
    scanner.stop_scan()

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

# 수업 참석율을 계산합니다.
def calculate_attendance_percentage(attendance_list):
    total_entries = len(attendance_list)
    attended_count = sum(attendance_list)
    attendance_percentage = (attended_count / total_entries) * 100
    return attendance_percentage

# 스캔이 완료된 후 참석율 계산
attendance_percentage = calculate_attendance_percentage(attendance_list)
print(f"수업 참석율: {attendance_percentage:.2f}%")
