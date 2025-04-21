import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
from tensorflow.python.client import device_lib

print("Dispositivos disponíveis:")
print(device_lib.list_local_devices())
print("GPU disponível:", tf.config.list_physical_devices('GPU'))

dataset_path = './Brain_Tumor_Organizado'

img_height, img_width = 224, 224
batch_size = 32

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

validation_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)

base_model = MobileNetV2(input_shape=(img_height, img_width, 3),
                         include_top=False,
                         weights='imagenet')
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

epochs = 50
history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)

loss, accuracy = model.evaluate(validation_generator)
print(f'\n✅ Acurácia na validação: {accuracy * 100:.2f}%')

model.save('modelo_tumor_cerebral.h5')
print("\n📁 Modelo salvo como 'modelo_tumor_cerebral.h5'")
