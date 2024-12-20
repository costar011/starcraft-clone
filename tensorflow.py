import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# 데이터셋 로드
(train_images, train_labels), (test_images, test_labels) = datasets.load_data()
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

# 픽셀 값을 0과 1 사이로 정규화
train_images, test_images = train_images / 255.0, test_images / 255.0

# 모델 생성
model = models.Sequential()

# 첫 번째 합성곱 층 추가
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
# 두 번째 합성곱 층 추가
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
# 세 번째 합성곱 층 추가
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# 완전 연결 층 추가
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# 모델 요약 출력
model.summary()

# 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# 모델 학습
model.fit(train_images, train_labels, epochs=5)

import matplotlib.pyplot as plt

# 모델 학습 (history 객체 반환)
history = model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))

# 손실 그래프 그리기
plt.figure(figsize=(12, 6))

# 학습 손실과 검증 손실 그래프
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], 'b-', label='loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')
plt.title('Loss over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# 정확도 그래프 그리기
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# 그래프 표시
plt.show()

from PIL import Image
import numpy as np

# 손글씨 이미지 로드
image = Image.open('test.png').convert('L')
image = image.resize((28, 28))

image = np.array(image)
image = image.reshape(1, 28, 28, 1)

# 예측 수행
prediction = model.predict(image)
prediction = np.argmax(prediction)

# 예측 결과 출력
print(f"Predicted number: {prediction}")