from flask import Flask
import os

temp_dir = os.getcwd()
app = Flask(__name__, template_folder=temp_dir)

from app import views