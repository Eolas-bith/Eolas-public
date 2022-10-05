def string_cleaner(string_to_clean):
    import re
    import demoji
    def remove_emoji(string):
        emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F" # emoticons
                           u"\U0001F300-\U0001F5FF" # symbols & pictographs
                           u"\U0001F680-\U0001F6FF" # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF" # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'',string)
    string_to_clean=remove_emoji(string_to_clean)
    #print(string_to_clean)
    clean_string=str(string_to_clean).strip("'<>() []").replace('\'', '\"')
    print("String cleaned, output type: ",type(clean_string))
    return str(clean_string)  