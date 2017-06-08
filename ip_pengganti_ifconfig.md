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





### Sumber
[ifconfig vs ip](https://tty1.net/blog/2010/ifconfig-ip-comparison_en.html)
[iproute2: Life after ifconfig](http://andys.org.uk/bits/2010/02/24/iproute2-life-after-ifconfig/)
[ifconfig sucks](http://inai.de/2008/02/19)
[Should I quit using Ifconfig?](https://serverfault.com/questions/458628/should-i-quit-using-ifconfig)
[Linux Advanced Routing & Traffic Control HOWTO](http://lartc.org/howto/index.html)


