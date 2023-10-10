# Nama Aplikasi: ***LiteraTour***

# Pengembang Aplikasi
> Proyek ini dibuat oleh kelompok C10 dengan anggota sebagai berikut:
1. Fathi Qushoyyi Ahimsa (2206082120)
2. Matthew Hotmaraja Johan Turnip (2206081231)
3. Michelle Elizabeth Amanda Hutasoit (2206028573)
4. Nadya Aysha (2206081635)
5. Roger Moreno (2206029872)

# Deskripsi Aplikasi
Kongres Bahasa Indonesia adalah forum tertinggi yang membahas masalah kebahasaan dan kesastraan di Indonesia. Kongres Bahasa Indonesia diselenggarakan setiap lima tahun sekali oleh Badan Pengembangan dan Pembinaan Bahasa, Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi. Sesuai dengan tema Kongres Bahasa Indonesia XII yang akan diselenggarakan pada tanggal 25—28 Oktober 2023, yaitu "Literasi dalam Kebhinekaan untuk Kemajuan Bangsa.", LiteraTour diciptakan dengan visi untuk meningkatkan minat literasi masyarakat Indonesia melalui pembentukan komunitas yang aman sekaligus tempat bertransaksi yang terpercaya.

LiteraTour memiliki fitur-fitur yang dapat memudahkan pengguna dalam membeli buku yang ingin dibaca. Pengguna dapat mencari buku dengan kategori tertentu seluruh penjuru negeri melalui satu buah klik dan dapat melihat serta meninggalkan ulasan pada buku terkait. Selain itu, LiteraTour tidak hanya digunakan untuk membeli buku saja, tetapi juga dapat digunakan sebagai platform bagi pecinta buku untuk mencari dan membangun komunitasnya sendiri. Dalam komunitas tersebut, pengguna dapat menampilkan buku-buku yang direkomendasikan dan melihat buku yang direkomendasikan oleh anggota komunitas lainnya. Anggota komunitas juga dapat saling bertukar pendapat dan berbincang-bincang. LiteraTour juga menawarkan kemudahan bagi pengguna dalam mengatur dan mengelola buku favoritnya melalui fitur “My Library”.

# Daftar Modul

**1. Sign In & Sign Up**
* Developer: _Nadya Aysha_
* Description:
Sign In & Sign Up adalah modul dimana pengguna dapat melakukan registrasi akun LiteraTour dan Log-In ke dalam website untuk mengakses fitur-fitur yang ditawarkan LiteraTour.
* Feature details:
  * Registrasi/ pendaftaran akun
  * Sign-In dengan akun yang telah dibuat
  * Log-Out dari website

**Book Finds**
* Developer: _Matthew Hotmaraja Johan Turnip_
* Description:
Book Finds adalah modul dimana pengguna dapat melihat semua buku yang tersedia pada website. Selain itu, pengguna dapat membeli dan melihat review dari masing-masing buku.
* Feature details:
  * Katalog buku
  * Deskripsi buku
  * Review button
  * Add to Cart button
* Form:
  * Pengguna bisa request untuk menambahkan buku yang belum ada di katalog (pengguna bukan penulis buku tersebut).
* Filter: Buku berdasarkan genre, published year, dan rating.

**Book Shop**
* Developer: _Roger Moreno_
* Description:
Book Shop adalah modul dimana pengguna dapat membeli buku dari katalog yang ada dengan menerima tiap input data dan terdapat list barang yang sudah kita order.
* Feature details:
  * Harga Buku
  * Banyak pembelian
  * Metode Pengiriman
  * List Order
* Form: Checklist buku yang ingin dicheckout.
* Filter: Buku berdasarkan 

**Book Talk**
* Developer: _Fathi Qushoyyi Ahimsa_
* Description:
Book Talk adalah modul dimana pengguna dapat memberikan ulasan terkait dengan buku. Ulasan yang diberikan memuat dua hal, rating dalam skala 1–5 dan komentar ulasan dari buku tersebut. Pengguna dapat melihat ulasan yang diberikan oleh pengguna lain. 
* Feature details:
  * Menambahkan ulasan buku (dalam 1 form)
  * Memberikan rating buku (dalam 1 form)
  * Melihat ulasan setiap buku
* Form: Post Ulasan (Deskripsi Ulasan, Rating, dan Buku yang diulas)
* Filter:
  * Filtering berdasarkan Model Buku
  * Hanya bisa melihat ulasan dia

**Book Club**
* Developer: _Michelle Elizabeth Amanda Hutasoit_
* Description:
Book Club adalah modul dimana pengguna dapat membentuk komunitasnya sendiri atau bergabung dengan komunitas yang sudah ada. Pada modul ini, pengguna dapat memberikan rekomendasi buku dan melihat rekomendasi buku yang diberikan oleh anggota komunitas lainnya. Anggota komunitas juga dapat memberikan pendapat/berkomunikasi dalam format forum. 
* Feature details:
  * Membuat komunitas
  * Menghapus komunitas (jika pengguna merupakan owner komunitas)
  * Bergabung ke komunitas
  * Keluar dari komunitas
  * Memberikan rekomendasi buku
  * Mengirimkan pendapat dalam format forum
* Form:
  * Membuat komunitas
  * Memberikan rekomendasi buku
  * Mengunggah pendapat
* Filter: 

**My Library**
* Developer: _Nadya Aysha_
* Description:
My Library adalah modul dimana pengguna dapat membuat virtual library di LiteraTour dengan mengoleksi berbagai macam buku dari katalog kami. Modul ini menawarkan fitur-fitur yang akan menyimpan riwayat buku pengguna yang telah disimpan dan beli.
* Feature details:
  * Menyimpan buku yang ingin beli
  * Menampilkan list buku yang telah dibeli
  * Memorisasi quotes-quotes buku pilihan pengguna
  * Tracking progres membaca buku-buku pengguna
* Form: Post quotes dan reading tracker buku pengguna
* Filter: Filter reading tracker berdasarkan progress bar dan waktu rilis

**Profile**
* Developer: _Fathi Qushoyyi Ahimsa_
* Description:
Profile adalah modul dimana pengguna dapat melihat informasi akunnya seperti foto profil, nama pengguna, nama akun (username), dan email pengguna. Pengguna juga dapat mengubah informasi akun seperti foto profil, nama pemilik akun, nama akun (username), dan email.
* Feature details:
  * Melihat informasi akun
  * Mengubah informasi akun
  * Menghapus akun

# Role
***1. Admin***
* Mengakses semua modul
* Menghapus buku
* Menghapus komunitas

***2. User (Authorized)***
* Mengunjungi dan melakukan aksi pada Sign In & Sign Up page
* Mengunjungi dan melakukan aksi pada Book Finds page
* Mengunjungi dan melakukan aksi pada Book Shop page
* Mengunjungi dan melakukan aksi pada Book Talk page
* Mengunjungi dan melakukan aksi pada Book Club page
* Mengunjungi dan melakukan aksi pada My Library page
* Mengunjungi dan melakukan aksi pada Profile page

# Dataset
[https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata)
