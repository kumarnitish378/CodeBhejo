from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, flash

import os

from datetime import datetime

import mimetypes

from mydatabase import MyDB

import bcrypt

import qrcode

import sqlite3

import time

from mask_qr_generation import create_image_with_text

import re





app = Flask(__name__)

app.secret_key = 'nitish_sumita'  # Set your own secret key



db = MyDB()



# Database connection details (you can modify as needed)

DB_NAME = "printpro.db"



def get_base_url():

    return request.url_root


def remove_html_and_entities(text):

    # Remove HTML tags

    clean_text = re.sub(r'', '', text)

    # Remove   and similar entities

    clean_text = re.sub(r'&[a-zA-Z]+;', ' ', clean_text)

    clean_text = clean_text.replace("\n\n", "\n")

    return clean_text

