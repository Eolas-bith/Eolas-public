def deepl_usage():
    import requests
    import json
    import VAR_deepl_auth
    from VAR_deepl_auth import auth_key
    from VAR_deepl_auth import api_url
    auth_key=auth_key
    api_url=api_url
    #target_lang='EN'
    data=data={'auth_key':auth_key}
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    r=requests.post(api_url,params=data)
    json_data=json.loads(r.text)
    #print(json_data)
    char_count=(json_data["character_count"])
    char_limit=(json_data["character_limit"])
    char_left=char_limit-char_count
    print("API limit; Characters left: ",char_left)
    #return translated_text