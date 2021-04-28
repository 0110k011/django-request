from django.shortcuts import render
from django.http import HttpResponse
import requests
import re

def home_view(request, *args, **kwargs):
    pattern = 'v-n.*?n>(.*?)<.*?-d.*?n>(.*?)<.*?-q.*?n>(.*?)<.*?-u.*?n>(.*?)<.*?-v.*?n>(.*?)<'
    s = requests.Session()
    s.get('http://nfe.sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe?p=52210475315333013197655140001626571048579177|2|1|1|EF90F4E81318C154BA14C277574A8A8142E8B203')
    r = s.get('http://nfe.sefaz.go.gov.br/nfeweb/sites/nfce/render/NFCe?chNFe=52210475315333013197655140001626571048579177')
    data = re.findall(pattern, r.text)
    res = {
        'title': 'Home',
        'data': data
    }
    return render(request, 'home.html', res)
