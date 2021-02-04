# pip install googletrans==3.1.0a0
from googletrans import Translator

translater = Translator()

t = translater.translate('Bom dia', dest='vi')

print(t.text)
# out = translater.translate("How are you", dest = 'vi')
# print(out)