def getValue(obj, key):
    if key in list(obj.keys()):
        return obj[key]
    else:
        for k in list(obj.keys()):
            try:
                return getValue(dict(obj[k]), key)
            except:
                pass
