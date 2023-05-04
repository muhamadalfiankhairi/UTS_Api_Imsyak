from rest_framework import serializers
from . models import JadwalModels

class jadwalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JadwalModels
        fields = "__all__"

"""
Serializer di Django adalah sebuah kelas yang digunakan untuk mengubah objek model Django menjadi bentuk yang bisa dipindahkan atau ditransmisikan seperti JSON, XML, atau YAML. Serializer ini memungkinkan kita untuk menentukan struktur dari data yang akan dikirim, termasuk mengatur tipe data, nama field, dan validasi data.

Django memiliki built-in serializer yang dapat digunakan dengan mudah. Serializer yang disediakan oleh Django adalah serializers.Serializer dan serializers.ModelSerializer. serializers.Serializer digunakan untuk membuat serializer yang lebih fleksibel, sedangkan serializers.ModelSerializer adalah subclass dari serializers.Serializer dan digunakan untuk membuat serializer berdasarkan model Django.

Dalam penggunaannya, kita bisa menggunakan serializer untuk mengubah objek model Django menjadi format yang sesuai untuk dikirim melalui HTTP response, baik itu dalam bentuk JSON, XML, atau lainnya. Sebaliknya, serializer juga dapat digunakan untuk mengubah data yang diterima melalui HTTP request menjadi objek model Django. Hal ini memungkinkan kita untuk mengubah data yang dikirim melalui HTTP request menjadi bentuk yang bisa diproses oleh Django dan disimpan ke dalam database.

class meta
sebuah kelas yang digunakan untuk menyediakan konfigurasi tambahan untuk sebuah serializer. Dalam class Meta, kita dapat menentukan berbagai atribut tambahan seperti model yang akan digunakan sebagai sumber data, field apa saja yang akan disertakan dalam serializer, dan pengaturan lain yang berkaitan dengan serialisasi.
Dengan menggunakan class Meta, kita dapat dengan mudah mengatur konfigurasi tambahan pada serializer dan membuat kode kita lebih terstruktur dan mudah dibaca.
"""