# matan_integration
Лабораторная по интегралам

## Установка

Для установки рекомендую поставить [Anaconda](https://docs.anaconda.com/anaconda/install/).

Установка зависимостей с помощью Anaconda:

```bash
conda env create -f environment.yml
```

Затем нужно активировать среду:

```bash
conda activate integrator
```

Установка зависимостей с помощью Pip (нужен Python версии >= 3.6, а также модуль pip):

```bash
python -m pip install -r requirements.txt
```

## Запуск

Аргументы программы:
* `n`: отвечает за количество точек при интегрировании
* `e`: отвечает за тип оснащения (`left` = левая точка отрезка, `right` = правая точка отрезка, `mid` = середина отрезка, `random` = случайная точка на отрезке)
* `save_to`: отвечает за сохранение графика по пути. По умолчанию график не сохраняется, но только отображается. Если задано, график не отображается.

Пример запуска:

```bash
python integrator.py -n 100 -e random
python integrator.py -n 100 -e mid --save_to sample_plot.png
```
