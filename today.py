import datetime # need to import the all module to mock it in ut

def _now():
    return datetime.datetime.now()

def nday():
    return _now().timetuple().tm_yday

def year():
    return _now().year
