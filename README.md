# kipia_crm_fastapi
CRM based on FastAPI engine



## Подготовка базы данных

Для накатывания миграций, если файла alembic.ini ещё нет, нужно запустить в терминале команду:

```shell
alembic init migrations
```
После этого будет создана папка с миграциями и конфигурационный файл для алембика.

В alembic.ini нужно задать адрес базы данных, в которую будем катать миграции.
Дальше идём в папку с миграциями и открываем env.py, там вносим изменения в блок, где написано

```python3
from myapp import mymodel
```
Дальше вводим:
```shell 
alembic revision --autogenerate -m "comment"
```
Будет создана миграция
Дальше вводим:
```shell
alembic upgrade heads
```