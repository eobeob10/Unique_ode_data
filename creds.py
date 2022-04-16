#!/usr/bin/env python

import base64
import pickle
import codecs
import random
from string import ascii_lowercase

username = "Pindaric"
password = "Stesich0ru5_R0cK5"

data = []

for index, character in zip(ascii_lowercase, username):
	data.append((f"u{index}", character))

for index, character in zip(ascii_lowercase, password):
	data.append((f"p{index}", character))


random.shuffle(data)
pre_rot = base64.b64encode(pickle.dumps(data))
print(codecs.encode(str(pre_rot),'rot_13'))