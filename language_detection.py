def language_detection(text):
    import requests
    import requests
    import json
    import string_cleaner
    import VAR_deepl_auth
    from VAR_deepl_auth import auth_key
    from VAR_deepl_auth import api_url_translate
    auth_key=auth_key
    api_url=api_url_translate
    text=string_cleaner(text)
    target_lang='EN'
    if len(text)>200:
        text=text[:200]
    data=data={'auth_key':auth_key,'text':text,'target_lang':target_lang}
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    r=requests.post(api_url,params=data)
    json_data=json.loads(r.text)
    translated_text=json_data["translations"][0]["detected_source_language"]