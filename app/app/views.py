from app import app
from flask import render_template,request, redirect
import os
import nilearn
from nilearn import plotting
import nibabel as nib

path = os.getcwd()
path_total = path+ "/app/static/img/uploads"

@app.route("/",methods=["GET","POST"])
def upload_image1():
    if request.method == "POST":

        if request.files:
            image1= request.files["image1"]
            image2= request.files["image2"]
            link1 = os.path.join(path_total, "image1.nii.gz")
            link2 = os.path.join(path_total, "image2.nii.gz")
            image1.save(link1)
            image2.save(link2)

            img1 = nib.load(link1)
            img2 = nib.load(link2)
            view1 = plotting.view_img(img1, threshold=3)
            view2 = plotting.view_img(img2, threshold=3)
            view1.save_as_html('input_image1.html')
            view2.save_as_html('input_image2.html')
            print("images saved")

            c= add(img1,img2)
            view3 = plotting.view_img(c, threshold=3)
            view3.save_as_html('output.html')
            
            return redirect(request.url)

    return render_template("upload_image.html")


@app.route("/input1")
def input1():
    return render_template("input_image1.html" )

@app.route("/input2")
def input2():
    return render_template("input_image2.html" )

@app.route("/output")
def output():
    return render_template("output.html" )


# Backend code which takes two images as input parameters and returns the output image
def add(i1,i2):
    c1= i1.get_data() + i2.get_data()
    c = nilearn.image.new_img_like(i1,c1)
    return c