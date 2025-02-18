import json

def update_records(dict_rec, id_, prop, value):
    value = value.strip("'")
    try:
        dict_ = json.loads(dict_rec.replace("\'", "\""))
    except json.JSONDecodeError:
        return 'Invalid'

    if id_ == '':
        return 'Invalid'
    
    if id_ not in dict_:
        return 'Invalid'
    
    if prop not in ['albumTitle', 'artist', 'tracks']:
        return 'Invalid'
    
    if value == '':
        if prop not in dict_[id_]:
            return 'Invalid'
        dict_[id_].pop(prop)
    
    else:
        if prop == 'tracks':
            if 'tracks' not in dict_[id_]:
                dict_[id_][prop] = []
            dict_[id_][prop].append(value)
        else:
            dict_[id_][prop] = value
            
    return dict_

dict_rec, id_, prop, value = input().split(' | ')

print(update_records(dict_rec, id_, prop, value))