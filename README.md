# Тестовое задание:

* Напишите скрипт, асинхронно, в 3 одновременных задачи, скачивающий содержимое HEAD репозитория https://gitea.radium.group/radium/project-configuration во временную папку.
* После выполнения всех асинхронных задач скрипт должен посчитать sha256 хэши от каждого файла.
* Код должен проходить без замечаний проверку линтером wemake-python-styleguide. Конфигурация nitpick - https://gitea.radium.group/radium/project-configuration
* Обязательно 100% покрытие тестами
* При выполнении в ChatGPT - обязательна переработка

## For start application:

* Clone application from Github:
  ```bash
  git clone https://github.com/mephit24/AsyncGettingHEAD.git
  ```
  Or download it:
  https://github.com/mephit24/AsyncGettingHEAD/archive/refs/heads/master.zip

* Go to app directory:
  ```bash
  cd /path/to/app
* Run only for first time:
  ```bash
  python3 -m pip install -r requirements.txt
* Run:
  ```bash
  python3 main.py