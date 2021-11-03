import json
import urllib.request


def translator(text):
    client_id = "CLIENT_ID"
    client_secret = "CLIENT_SECRET"

    encText = urllib.parse.quote(text)

    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read().decode('utf-8')
        response_dict = json.loads(response_body)
        translatedText = response_dict["message"]["result"]["translatedText"]
        return translatedText
    else:
        error = "Error Code:" + rescode
        return error


