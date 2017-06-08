# Belajar Menggunakan iproute

Bismillah,


Setelah cukup lama menghindari distro linux berbasis Red hat, saat ini saya mulai mempelajari lagi CentOS 7, yang merupakan salah satu turunan Red hat. Saya menginstall ke virtualbox dengan file iso minimal_install. Setelah selesai setting instalasi, lalu seperti biasa yang coba lihat configurasi jaringan dengan perintah:

```
$ ifconfig
-bash: ifconfig: command not found
```

Waw, ifconfig tiada lagi ? bagaimana nih setting jaringan nya?

Ternyata, menggunakan perintah:
```
ip
```

OK, karena saya sudah terbiasa dengan perintah "ifconfig" dan "route", disini saya akan tampilkan contoh-contoh penggunaan perintah "ip" yang menjadi padanannya.





