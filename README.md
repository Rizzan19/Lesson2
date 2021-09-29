# openweatherapi

## Описание задачи
Написать реализацию функции  ```get_weather_data(place, api_key=None)```, в которой необходимо получить данные о погоде с сайта https://openweathermap.org/. 

Функция должна возвращать объект в формате JSON, включающий: 
- информацию о названии города (в контексте openweathermap),
- код страны (2 символа),
- широту и долготу, на которой он находится,
- его временной зоне,
- а также о значении температуры (как она ощущается).

Значение временной зоны выводить в формате UTC±N, где N - цифра временного сдвига.
Протестировать выполнение программы со следующими городами: Чикаго, СПб, Дакка.

Пример вызова функции и получаемого результата.

```python
get_weather_data('Kiev', api_key=key)
>>> {"name": "Kyiv", "coord": {"lon": 30.52, "lat": 50.43}, "country": "UA", "feels_like": 21.96, "timezone": "UTC+3"}

```

При реализации программы, не публикуйте свой ключ для осуществления запросов. Сразу же после создания репозитория в классруме исключите из коммитов подключаемый файл, где разместите ключ, с помощью ```.gitignore```.
Для организации запросов используйте модуль ```requests```. Для кодирования и декодирования ```json``` - одноименный модуль.