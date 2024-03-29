# Simple-Image-adder-web-application

## Introduction:

A simple Flask based web application that accepts two 3D images of same size, adds those images and returns an output image. This output image is an interactive 3D image which allows the user to fix one axis and view the image in the other two axes, exposing different cross sections of the image.

## Technologies used:

Flask

Python 3.7

HTML/CSS/JS

nilearn library

## Instructions: 

### A. Set up:

•	Install python 3.7

•	Install Flask using command:
~~~
pip install Flask
~~~

•	Install nilearn using command:

~~~
pip install nilearn
~~~
    

### B.  How to run:

  1.	Download the repository by following the github link https://github.com/Lubdha/Simple-Image-adder.git 
  Once the repository is downloaded, a folder "app" will be created.
  
  2. Open terminal, Make "app" from above step as your current working directory. 
  
  3. Run the below commands in the terminal
  
       ~~~
       
       export FLASK_ENV=development
       export FLASK_APP=app.py
       flask run 
       
       ~~~

  'flask run' launches the application.
  
  4. Open any browser and go to http://localhost:5000/ (Works best in full screen)

  5. To upload images to the server for processing, click the 'Choose File' button and select the two 3D images and click   the Upload button. You should upload images of same size. Images with extension '.gz' are accepted by the application.
  
  <img width="1439" alt="upload" src="https://user-images.githubusercontent.com/39939776/70932741-4ac09000-1fef-11ea-908a-dcc6a77eced2.png">


Once the images are uploaded and the server completes the addition process, click the link 'Output Image' to view the resultant interactive 3D image.

  <img width="774" alt="output" src="https://user-images.githubusercontent.com/39939776/70932778-5dd36000-1fef-11ea-8ff2-426aa53b429a.png">


Both input images can also be viewed in the interactive visualization by navigating to "Input Image 1" or "Input Image 2"

   <img width="1323" alt="Screen Shot 2019-12-16 at 12 13 06 PM" src="https://user-images.githubusercontent.com/39939776/70939673-911ceb80-1ffd-11ea-9660-5e1bf88088fc.png">




## References:

•	https://www.w3schools.com/html/

•	https://www.w3schools.com/css/

•	https://www.w3schools.com/js/

•	https://nilearn.github.io/plotting/index.html

•	https://www.youtube.com/watch?v=BUmUV8YOzgM&list=PLF2JzgCW6-YY_TZCmBrbOpgx5pSNBD0_L




