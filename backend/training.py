import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
import string
import re
from collections import Counter
from nltk.corpus import stopwords
stopwords = stopwords.words('english')

df = pd.read_csv('/home/pi/assistant/backend/data.csv')