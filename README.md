# CI/CD Practice - Практическая работа

[![CI/CD Pipeline](https://github.com/CICDProjectUniversity/ci-cd-practice/actions/workflows/main.yml/badge.svg)](https://github.com/CICDProjectUniversity/ci-cd-practice/actions)

## Описание
Учебный проект для практики по настройке CI/CD.

## Функциональность
- Базовый калькулятор с операциями: сложение, вычитание, умножение, деление
- Автоматическое тестирование через pytest
- CI/CD pipeline на GitHub Actions
- Автоматическая проверка кода при каждом коммите

## Структура проекта
```
.
├── .github/workflows/main.yml  # CI/CD конфигурация
├── app.py                       # Основной код
├── test_app.py                  # Тесты
├── requirements.txt             # Зависимости
├── docs/README.md               # Документация
├── VERSION                      # Версия проекта
└── CHANGELOG.md                 # История изменений
```

## Ветки
- `main` - основная ветка
- `development` - разработка
- `release` - подготовка релизов

## Установка
```bash
git clone https://github.com/CICDProjectUniversity/ci-cd-practice.git
cd ci-cd-practice
pip install -r requirements.txt
```

## Использование
```bash
python app.py
```

## Запуск тестов
```bash
python -m pytest test_app.py -v
```

## Версия
1.0.0

## Автор
Практическая работа по курсу "Технологии разработки программного обеспечения цифровых продуктов"

## Тестирование CI/CD
Эта строка добавлена для проверки автоматического запуска CI/CD.