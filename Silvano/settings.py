import yaml

def __parse_settings():
    with open('settings.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

def __dump_settings(data):
    with open("settings.yaml", "w") as f:
        yaml.safe_dump(data,f)

def get_setting(setting):
    data = __parse_settings()
    setting = data[setting]
    return setting

def update_setting(setting,newcontent):
    
    data = __parse_settings()
    data[setting] = newcontent
    __dump_settings(data)

