# LocalGem

Nama : Adinda Maharani Wardhana
Kelas: PBP C
NPM  : 2306165856
Colaborator : ChatGPT

1) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Pertama, saya membuat direktori kerja untuk proyek ini dan mengaktifkan virtual environment untuk memastikan bahwa dependensi proyek terisolasi. Setelah mengaktifkan virtual environment, saya menginstal Django dan membuat proyek Django baru. Ini menghasilkan struktur direktori dasar untuk proyek Django
- Setelah membuat proyek, saya membuat aplikasi baru di dalam proyek tersebut untuk menangani fitur spesifik. Ini menghasilkan direktori main dengan struktur dasar aplikasi Django, termasuk file-file seperti models.py, views.py, dan urls.py yang harus dikonfigurasi.
- Lalu, Untuk mengintegrasikan aplikasi main ke dalam proyek, saya menambahkan nama aplikasi main ke dalam daftar INSTALLED_APPS di file settings.py. Selanjutnya, saya mengatur routing di local_gem/urls.py untuk menyertakan URL dari aplikasi main.
- Untuk membuat model pada aplikasi main, saya mendefinisikan model Product dengan atribut yang diperlukan seperti name, price, description, rating, dan discount di file models.py. Tidak lupa saya membuat migrasi dan menjalankan migrasi untuk menerapkan perubahan pada database
- Untuk menampilkan nama aplikasi dan informasi saya, saya membuat fungsi show_info pada file views.py di dalam aplikasi main.Saya kemudian menyiapkan file urls.py di dalam aplikasi main untuk mendefinisikan rute yang memetakan URL ke fungsi show_info. Terakhir, saya memastikan file urls.py proyek utama (local_gem/urls.py) mengarahkan URL ke aplikasi main.
- Di file views.py, saya membuat sebuah fungsi bernama show_info yang mengembalikan HttpResponse. Fungsi ini dirancang untuk mengambil nama aplikasi (Local Gem) dan informasi mengenai nama serta kelas saya, kemudian ditampilkan di dalam template HTML yang telah saya buat.
- Setelah itu, saya membuat berkas urls.py di aplikasi main dan menambahkan path untuk mengarahkan URL ke fungsi show_info pada views.py. Saya kemudian memastikan routing aplikasi terhubung dengan urls.py di direktori proyek utama (local_gem/urls.py), agar bisa diakses saat mengunjungi halaman tersebut.
- Untuk melakukan deployment, saya menyiapkan akun, mengupload proyek Django, dan melakukan konfigurasi seperti pengaturan virtual environment dan database. Setelah memastikan aplikasi berjalan dengan baik secara lokal, saya melakukan deploy ke PWS dengan mengatur domain publik dan mengecek aplikasi saya bisa diakses melalui Internet.
- Terakhir saya membuat file README.md untuk menjawab beberapa pertanyaan yang ada. 

2) Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
- BAGAN : CLIENT REQUEST -> URL ROUTING(urls.py) -> VIEW FUNCTION(views.py) -> TEMPLATE HTML(Templates) -> HTTP RESPONSE(HTML Page) -> CLIENT RECEIVES RESPONSE
- Klien (misalnya, browser) mengirimkan permintaan HTTP ke server, misalnya ke URL http://localhost:8000/about/.
- Django menerima permintaan dan menggunakan file urls.py untuk menentukan URL yang diminta. urls.py memetakan URL ke fungsi view yang sesuai.
- Fungsi view menerima permintaan dan berfungsi sebagai penghubung antara URL dan data. Fungsi ini mungkin mengambil data dari model (jika diperlukan) dan mempersiapkan konteks untuk template.
- Template HTML menerima konteks dari fungsi view dan merender HTML sesuai dengan data yang dikirimkan.
- Setelah template HTML dirender, Django mengirimkan respons HTTP ke klien. Respons ini berupa halaman HTML yang ditampilkan di browser klien.

3) Jelaskan fungsi git dalam pengembangan perangkat lunak!
- Git memfasilitasi kolaborasi antar pengembang dengan memungkinkan pembuatan cabang (branch) untuk fitur atau perbaikan baru. Setiap cabang dapat dikembangkan secara terpisah tanpa mempengaruhi kode utama. Git mendukung kolaborasi tim dengan fitur seperti pull request dan review code.
- Git mempermudah penggabungan (merge) perubahan dari berbagai cabang dan menyimpan salinan dari setiap perubahan, menyediakan cadangan yang bisa dipulihkan jika terjadi masalah. 

4) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Django menyediakan secara default banyak fitur yang sering dibutuhkan dalam pengembangan web. Ini termasuk sistem autentikasi, formulir, dan admin interface, sehingga mempermudah pengembang baru untuk membangun aplikasi web tanpa harus mengkonfigurasi banyak hal dari awal.
- Memiliki dokumentasi yang sangat baik dan terperinci. Dokumentasi ini mencakup panduan, tutorial, dan referensi API yang memudahkan pemula untuk memahami dan menggunakan framework ini.
- Django mengikuti pola Model-View-Template (MVT) yang terstruktur dengan jelas. 
- Django memiliki komunitas pengembang yang besar dan aktif.

5) Mengapa model pada Django disebut sebagai ORM?
Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena ia menghubungkan objek di dalam kode Python dengan tabel dalam database relasional. ORM adalah teknik yang memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek dan metode Python alih-alih menulis query SQL secara langsung.