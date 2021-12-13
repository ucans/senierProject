# senierProject
Recognizing the formula.

Welcome to the senierProject README!

**1. Handwritten Mathematical Expressions Recognition**
     
Our project takes pictures of handwritten expressions and makes them automatically recognized. 
A web server was created to build math recognition function project.
It's a rather difficult project, but we did it.

**2. Project goal**

* Building **training model** and **math recognition model**.
* Making a **Web Flask application** so user can upload the images and perform recognition.

**BUILDING MODEL**
*******

**1. Dataset**

[Aida Calculus Math Handwriting Recognition Dataset | Kaggle](https://www.kaggle.com/aidapearson/ocr-data)

-> It contains contain 100,000 formula image and latex 

**2. LaTex**

When an equation image is introduced using **latex**, it is converted into a latex format and rendered so that a clean equation image can be obtained.

We bring images provided by this site [(Online Latex Equation Editor - Sciweavers)](http://www.sciweavers.org/free-online-latex-equation-editor)

```python
self.mode = 0 
        print(self.mode)
    
        image=pag.screenshot(region=(self.x1, self.y1+28, capture_width, capture_height))       
        self.showMainWidgets()

        imageq = ImageQt(image)
        pixmap = QtGui.QPixmap.fromImage(imageq)
        pixmap = pixmap.scaled(QtCore.QSize(660, 400), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.label_capture.setPixmap(pixmap)
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))      
        self.showNormal()
        self.setWindowOpacity(1)

        data = ""
        data = inf.getLatext(image)[0]
        print(data)  
        self.latext.setText(data)
        
        urlString = "http://www.sciweavers.org/tex2img.php?eq=1%2Bsin%28mc%5E2%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0"
        url = urlparse(urlString)

        qs = dict(parse_qsl(url.query))
        qs['eq'] = data
        parts = url._replace(query=urlencode(qs))
        url = urlunparse(parts)
        
        img = urllib.request.urlopen(url).read()

        pixmap = QPixmap()
```
![image](https://user-images.githubusercontent.com/76080523/145786766-a9b52a9a-58b3-42ed-8089-94c94f453302.png)
![image](https://user-images.githubusercontent.com/76080523/145786802-f1ae5108-8889-4c83-b136-ede1a68fc8cc.png)


-> It outputs latex phrases as clean image files.
Convert the handwritten image into a latex format with the model learned and output it back to a mathematical image.


**BUILDING THE WEB SERVER (FLASK APP)**
***
![image](https://user-images.githubusercontent.com/76080523/145774275-e2bbd6d7-3447-41e3-8783-ceb626fe6346.png)

![image](https://user-images.githubusercontent.com/76080523/145787003-b467f80c-ad09-4ac6-a550-a07783516213.png)
