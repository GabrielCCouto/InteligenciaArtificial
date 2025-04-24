import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
from tensorflow.python.client import device_lib

print("Dispositivos disponíveis:")
print(device_lib.list_local_devices())
print("GPU disponível:", tf.config.list_physical_devices('GPU'))

# Caminhos do dataset
base_dataset_path = './Pneumonia_Torax'  # substitua pelo caminho correto se necessário
train_dir = os.path.join(base_dataset_path, 'train')
val_dir = os.path.join(base_dataset_path, 'val')
test_dir = os.path.join(base_dataset_path, 'test')

# Configurações
img_height, img_width = 224, 224
batch_size = 32

# Pré-processamento com normalização (rescale)
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

# Carregar imagens
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary'
)

validation_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary'
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    shuffle=False  # Importante para avaliação consistente
)

# Modelo pré-treinado
base_model = MobileNetV2(input_shape=(img_height, img_width, 3),
                         include_top=False,
                         weights='imagenet')
base_model.trainable = False

# Construção do modelo
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Treinamento
epochs = 300
history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)

# Avaliação
loss, accuracy = model.evaluate(test_generator)
print(f'\n✅ Acurácia no conjunto de teste: {accuracy * 100:.2f}%')

# Salvamento
model.save('modelo_pneumonia_torax.h5')
print("\n📁 Modelo salvo como 'modelo_pneumonia_torax.h5'")
