# Download-Gdrive-Protected-PDFs
Browser's console code to download the read-only Gdrive pdfs.    
When the Download, print and copy has been disabled for a Google drive shared PDF file then you can simply run this code in your browser's console(ctrl+shift+j).   
Change the width according to your need.   
```
var width = 1500; //put the width in px according to your quality requirement

//Dont change anything from below
let raw = document.querySelector("head").innerHTML;
let token = raw.match(/https:\/\/drive\.google\.com\/viewer2\/prod-0\d\/meta\?ck\\u003ddrive\\u0026ds\\u003d(.+?)"/)[1];
let img_url = `https://drive.google.com/viewer2/prod-01/img?ck=drive&ds=${token}&authuser=0&skiphighlight=true&webp=true&w=${width}&page=`;
let height;
var s = document.createElement("script");
s.type = "text/javascript";
s.src = "https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js";
$("head").append(s);
await(async () => {
  const img = new Image();
  img.src = img_url + "0";
  await img.decode();
  // img is ready to use
  height = img.height;
})();

console.log("https://github.com/bunnykek");
console.log(`Page dimensions: ${width} X ${height}`);

const doc = new jspdf.jsPDF({
  orientation: 'p',
  unit: 'px',
  format: [width, height],
  putOnlyUsedFonts: true,
  floatPrecision: "smart" // or "smart", default is 16
});

doc.addImage(img_url + "0", "WEBP", 0, 0, width, height);
console.log(`Page 1 done!`);

for (var i = 1; ; i++) {
  try {
    doc.addPage([width, height]);
    doc.addImage(img_url + `${i}`, "WEBP", 0, 0, width, height);
    //console.log(img_url.replace(reg,`page=${i}`));
    console.log(`Page ${i + 1} done!`);
  } catch {
    doc.deletePage(i + 1)
    break;
  }
}

doc.save("file.pdf");
//script made by bunnykek @ Github
```
