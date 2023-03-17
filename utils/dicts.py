# файл dicts.py




def get_value(dictionary, key, default=None):
    """
    Возвращает значение из словаря по переданному ключу, если ключ существует. В ином случае возвращается значение default.
    :param dictionary: Словарь
    :param key: Ключ для поиска значения
    :param default: Значение по умолчанию, которое будет возвращено, если ключ не найден в словаре
    :return: Значение из словаря или значение default, если ключ не найден
    """
    if key in dictionary:
        return dictionary[key]
    else:
        return default

