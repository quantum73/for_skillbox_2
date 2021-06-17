## Запуск приложения

- Запустите скрипт `run.sh`
- После создания контейнеров и применения миграций,
  доступ к API будет доступен по адресу http://0.0.0.0:8000/api/
  
### API

#### Направления

- GET /api/directions/ - Получить все направления
- POST /api/directions/ - Добавить направление

```json
{
    "title": "Название",
    "position": 1 
}
```
- PUT /api/directions/:id - Редактировать направление

```json
{
    "title": "Новое название",
    "position": 2 
}
```

- DELETE /api/directions/:id - Удалить направление

#### Курсы

- GET /api/courses/ - Получить все курсы
- GET /api/courses/:id - Получить курс по id
- POST /api/courses/ - Добавить курс

```json
{
    "title": "Название",
    "position": 1,
    "direction": 1,
    "lessons": [1,2,3]
}
```

- PUT /api/courses/:id - Редактировать курс

```json
{
    "title": "Новое название",
    "position": 2,
    "direction": 2,
    "lessons": [] - отвязать все уроки, если пустой массив
}
```

- DELETE /api/courses/:id - Удалить курс

#### Уроки

- GET /api/lessons/ - Получить все уроки
- GET /api/lessons/:id - Получить урок по id 
- POST /api/lessons/ - Добавить урок

```json
{
    "title": "Название",
    "position": 1,
    "anons": "Анонс",
    "description": "Описание",
    "link_to_video": "/link/to/video",
    "link_to_file": "/link/to/file",
    "materials": [1,2,3,4]
}
```

- PUT /api/lessons/:id - Редактировать урок

```json
{
    "title": "Новое название",
    "position": 2,
    "anons": "Анонс",
    "description": "Описание",
    "link_to_video": "/link/to/video",
    "link_to_file": "/link/to/file",
    "materials": [] - отвязать все материалы, если пустой массив
}
```
- DELETE /api/lessons/:id - Удалить урок

#### Материалы для уроков

- GET /api/lessons-material/ - Получить все материалы
- GET /api/lessons-material/:id - Получить материал по id 
- POST /api/lessons-material/ - Добавить материал

```json
{
    "title": "Название",
    "description": "Какой то текст",
    "image": "/link/to/image",
    "file": "/link/to/file"
}
```

- PUT /api/lessons-material/:id - Редактировать материал

```json
{
    "title": "Новое название",
    "description": "Какой то текст",
    "image": "/link/to/image",
    "file": "/link/to/file"
}
```

- DELETE /api/lessons-material/:id - Удалить материал
