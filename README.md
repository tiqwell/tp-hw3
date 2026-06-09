# Дз 3

## Инструкция по запуску

Все команды выполняются через run.sh:

1. Посмотреть структуру проекта:
   ./run.sh structure

2. Сборка и запуск генератора данных:
   ./run.sh build_generator
   ./run.sh run_generator

3. Сборка и запуск аналитика данных:
   ./run.sh build_reporter
   ./run.sh run_reporter

4. Проверить, что контейнеры видят данные на хосте:
   ./run.sh inside_generator
   ./run.sh inside_reporter

5. Очистить  файлы из папки data:
   ./run.sh clear_data
