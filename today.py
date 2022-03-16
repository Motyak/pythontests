from datetime import datetime

def _now():
    return datetime.now()

def nday():
    return _now().timetuple().tm_yday

def year():
    return _now().year
