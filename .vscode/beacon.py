
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

attendance_list = []

async def scan_beacon():
    global scanner, event_loop
    scanner.process = EventHook()
    scanner.process += process_scan_response
    await scanner.connect(event_loop)
    await scanner.start_scan()

def process_scan_response(scan_response):
    beacons = [dev for dev in scan_response.retrieve() if isinstance(dev, IBeacon)]
    for beacon in beacons:
        if beacon.uuid == "4ddf1a6c-7dfd-11ea-8d80-9e82b1d4fa51":
            callback(beacon.mac, beacon.rssi, scan_response, beacon.data)

def callback(bt_addr, rssi, ts_packet, data):
    print(f"비콘 MAC 주소: {bt_addr}, RSSI: {rssi}")
    current_time = datetime.now()
    hour, minute = current_time.hour, current_time.minute
    attendance_result = model.predict_classes(
        scaler.transform(np.array([[hour, minute, rssi]])))[0]

    if attendance_result == 1:
        print("참석 중")
    else:
        print("결석 중")
    attendance_list.append(attendance_result)

# 수업 참석율을 계산합니다.
def calculate_attendance_percentage(attendance_list):
    total_entries = len(attendance_list)
    attended_count = sum(attendance_list)
    attendance_percentage = (attended_count / total_entries) * 100
    return attendance_percentage

conn = sqlite3.connect("attendance.db")
...

# 학습과 테스트 데이터를 정규화합니다.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 딥러닝 모델 생성
model = Sequential([
    Dense(32, activation='relu', input_shape=(3,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# 비콘 스캔 시작
scanner = BleScanRequester("hci0")
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(scan_beacon())
time.sleep(5)
scanner.stop_scan()

# 스캔이 완료된 후 참석율 계산
attendance_percentage = calculate_attendance_percentage(attendance_list)
print(f"수업 참석율: {attendance_percentage:.2f}%")

# 데이터베이스 연결 종료
conn.close()
