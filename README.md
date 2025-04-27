# Proyek Klasifikasi Gambar Menggunakan CNN

Proyek ini adalah model klasifikasi gambar menggunakan Convolutional Neural Network (CNN) yang dibangun dengan menggunakan TensorFlow dan Keras. Model ini dilatih untuk mengklasifikasikan gambar ke dalam beberapa kelas yang ditentukan.

Deskripsi

Model ini menggunakan arsitektur CNN untuk melakukan klasifikasi gambar. Gambar yang diberikan melalui model akan diproses dan diprediksi ke dalam kelas yang sesuai. Model ini dilatih menggunakan dataset gambar yang dibagi menjadi tiga subset: data latih (train), data validasi (validation), dan data uji (test).

Fitur

- Klasifikasi Gambar: Mengklasifikasikan gambar ke dalam beberapa kelas.
- Model CNN: Menggunakan lapisan Conv2D, MaxPooling2D, Flatten, dan Dense untuk klasifikasi.
- TensorFlow Lite: Model dapat diekspor ke format TFLite untuk digunakan dalam aplikasi mobile atau perangkat yang lebih ringan.

Instruksi Pemasangan

Untuk menjalankan proyek ini, pastikan Anda memiliki Python 3.x dan pip yang terinstal. Kemudian, instal dependensi berikut:

```bash
pip install tensorflow numpy matplotlib
Jika Anda menggunakan Google Colab, Anda bisa langsung mengimpor library tersebut tanpa perlu instalasi.

Penggunaan
Menjalankan Proyek
Persiapkan Dataset: Pastikan dataset gambar Anda sudah terorganisir dalam folder terpisah untuk masing-masing kelas di direktori yang telah ditentukan.

Latih Model: Gunakan kode berikut untuk melatih model:

- Kode untuk melatih model CNN
model_12 = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(train_generator.num_classes, activation='softmax')
])

model_12.compile(optimizer=Adam(learning_rate=0.0001),
                 loss='categorical_crossentropy',
                 metrics=['accuracy'])

history_12 = model_12.fit(
    train_generator,
    epochs=30,
    validation_data=val_generator,
    callbacks=[early_stop, reduce_lr]
)
Menyimpan Model: Setelah model selesai dilatih, Anda dapat menyimpan model dalam format SavedModel atau TFLite seperti berikut:


- Menyimpan model dalam format TFLite
model_12.save('model_12.tflite')
Inferensi Gambar: Untuk melakukan prediksi pada gambar baru, gunakan kode berikut:


import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

- Load TFLite model
interpreter = tf.lite.Interpreter(model_path="model_12.tflite")
interpreter.allocate_tensors()

- Cek input/output
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

- Baca label kelas dari train_generator
labels = list(train_generator.class_indices.keys())

- Path file gambar yang ingin diprediksi
image_path = 'path_to_image.png'

- Load gambar
img = image.load_img(image_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = img_array / 255.0  # Normalisasi
img_array = np.expand_dims(img_array, axis=0).astype(np.float32)  # Tambah batch dimensi

- Set input ke interpreter
interpreter.set_tensor(input_details[0]['index'], img_array)

- Jalankan inferensi
interpreter.invoke()

- Ambil output dan prediksi kelas
output_data = interpreter.get_tensor(output_details[0]['index'])
predicted_class_index = np.argmax(output_data)

- Tampilkan nama kelas prediksi
predicted_class = labels[predicted_class_index]
print(f"Prediksi kelas: {predicted_class}")

- Tampilkan gambar dan prediksi
plt.imshow(img)
plt.title(f"Prediksi: {predicted_class}")
plt.axis('off')  # Matikan axis
plt.show()


Penulis
Proyek ini dibuat oleh Arya Mulahernawan.

Catatan:

- Ganti `path_to_image.png` dengan path gambar yang ingin Anda prediksi.
- Pastikan struktur folder dan file sesuai dengan yang ada pada proyek Anda.

Template ini akan memberi gambaran lengkap mengenai cara menggunakan proyek Anda, mulai dari pengaturan, pelatihan, hingga inferensi model. Anda bisa menyesuaikan isi file ini sesuai dengan kebutuhan proyek Anda. 😊
