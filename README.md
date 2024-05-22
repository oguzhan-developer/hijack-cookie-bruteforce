# hijack-cookie-bruteforce
Hijack CTF'ini çözerken, web sitesinde PHPSESSID karşısında değer olarak username:password şeklinde cookie kaydı tutulduğunu fark ettim. Parola, önce md5 ile şifrelenmiş, ardından username:md5li-parola şeklinde tekrar base64 ile encode edilmiş. Elimde admin için pass list var, ancak login sayfasında brute force engellenmiş, bende bu parola listesini md5'e çevirdim, başlarına "admin:" yazdım ve ardından base64 ile encode ettim. 
Bu listeyi kullanarak cookie brute force saldırısı yapmak için **cookiebrute** aracımı kullandım.

cookiebrute tool'u her bir cookie ile index.php sayfasına get requesti yapıyor, response text'i "welcome admin" yazısını içeriyorsa success case'i dönüyor.
