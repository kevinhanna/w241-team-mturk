#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# import webapp2
#
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('Hello world!')
#
# app = webapp2.WSGIApplication([
#     ('/', MainHandler)
# ], debug=True)
import os

from flask import Flask, render_template, request, redirect, session, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.secret_key = os.environ.get('APP_SECRET_KEY')

@app.route('/foo', methods=['POST', 'GET'])
def login():
    return render_template('draw_bounding.html')

