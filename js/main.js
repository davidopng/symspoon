// console.log("The best preparation for tomorrow is doing your best today")




// var contohstring = "yayayayayaya";
// console.log(contohstring);




// var a = 20 > 50;
// if (a = true) {
//     console.log("benar")
// } else{
//     alert("salah");
// }



// var contoharray = [1,2,3,4,5, 2.4, "apple", "jeruk", "semangka"];
// console.log(contoharray);

// var buah = prompt("Tuliskan nama buah yang memiliki wangi menyengat");
// if (buah == "durian"){
//     document.write("<duh1>Yeayyyy</h1>");
// } else {
//     document.write("<h1>Oooops Salah</h1>");
// }




// var pertanyaan = prompt("aku suka buah yang harum", "masukan jawabanmu");

// if (pertanyaan != "durian") {
//     document.write("<h1>Yap Benar, aku suka buah ini!</h1>");
// } else {
//     document.write("<h1>nope, saya suka semua buah kecuali durian</h1>")
// }

// var angka1 = "4" === 4;     >>>>>> maka akan true
// var angka = 4 === 4;        >>>>>> maka akan false
// console.log(angka);




// var a = 20;
// var b = 19;

// var hasil;
// var hasil1 = a > b;
// var hasil2 = a < b;

// hasil = !hasil1;
// document.write(`!${hasil1} = ${hasil} <br>`);

// hasil = hasil1 || hasil2;
// document.write(`${hasil1} || ${hasil2} = ${hasil} <br>`);

// hasil1 = hasil1 && hasil2;
// document.write(`${hasil1} && ${hasil2}`);




// var a = 20;
// var b = 19;

// var hasil;
// var hasil1 = a > b; // true
// var hasil2 = a < b; // false

// hasil = hasil1 && hasil2; // false, karena true && false = false
// document.write(`${hasil1} && ${hasil2} = ${hasil}`);



Array:
var keranjang_buah = ["Anggur", "pepaya", "apel", "duren", "kelapa", "pisang"];

Looping:
for (var angka = 4; angka < keranjang_buah.length; angka ++) {
    console.log(keranjang_buah[angka]);
}