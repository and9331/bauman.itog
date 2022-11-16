# Qualification work for Bauman University data science course
 ## Case: Predicting the size of the weld in electron beam welding

Inputs:

1. Welding current value (IW);
2. Electron beam focusing current (IF);
3. Welding speed (VW);
4. Distance from the surface to the electron-optical system (FP).

Outputs:

Weld *Depth*
Weld *Width*

Task:

Predict the **Depth** and **Width** of the weld depending on the technological process parameters (IW, IF, VW, FP).

 ## Description

There are two folders. In */jupyter/* catalogue you'll find original dataset (files: ebw_data), notebook.ipynb file, that's where dataset preprocessing, analysis and models fitting took place. Results of this process also in the same folder. Scikit-learn models of LinearRegression, RandomForestRegressor and StandartScaler were saved to .pkl files. Also Tensorflow.Keras neural net were saved there in *nn_model* using standart *.save() method.

LinearRegression were choosen since it's light and easy and provides seamingly good results for the particular dataset. RandomForestRegressor is a second one, powerfull and surprisingly accurate tool even with default parameters. Scaler.pkl is a saved StandartScaler object trained on the original dataset, it's being used for scaling user input in an application, providing normal models functioning in production.

Simple multi-layer neural net in this project based on tensorflow.keras. It had a few configurations in jupyter dataset exploration process, but I stayed with the most stable/accurate/tiny version. 

In */flask.itog/* there's a basic flask application tuned for Heroku deployment. Main python file is an app.py where all the magic getting done. In *fitted_models* all the models are hiding. While webapp execution nothing being trained and only loading during the handling process. So all pretrained and presaved model sequentially loading, process user input and give predictions according to their pretrained state.

That's all for now, a lot of room for improvement anyway.

Web app deployed [here](https://bauman-itog.herokuapp.com)

# Квалификационная работа по курсу Аналитик данных МГТУ им. Баумана
## Задача: «Прогнозирование размеров сварного шва при электронно-лучевой сварке тонкостенных конструкций аэрокосмического назначения»

В качестве исходных данных были взяты результаты экспериментальных исследований, проводимых в целях улучшения технологического процесса электронно-лучевой сварки изделия, сборка которого состоит из элементов, состоящих из разнородного материала. Установка электронно-лучевой сварки, на которой проводились исследования, предназначена для сварки электронным лучом в глубоком вакууме деталей сборочных единиц из нержавеющих сталей, титановых, алюминиевых и специальных сплавов. Существующая установка электронно-лучевой сварки обеспечивает повторяемость режимов в рамках возможностей реализованной системы управления. Работы по сварке выполнялись на образцах-имитаторах, соответствующих технологическому изделию. Для уменьшения вложения энергии при сварке:

1.	Снижалась величина сварочного тока (IW);
2.	Увеличивался ток фокусировки электронного пучка (IF);
3.	Увеличивалась скорость сварки (VW);
4.	Менялось расстояние от поверхности образцов до электронно-оптической системы (FP). 

По совокупности параметров технологических режимов обеспечивались минимально возможные размеры сварных швов: глубина шва (Depth) и ширина шва (Width).
В процессе выполнения работ была произведена электронно-лучевая сварка 18-ти единиц образцов. Результаты металлографического контроля по размерам сварного шва для каждого образца проводились в 4-х поперечных сечениях сварного шва. Ускоряющее напряжение было постоянным в диапазоне 19,8 – 20 кВ. Набор полученных данных собраны в составе режимов сварки, размеров сварочных швов в поперечных сечениях всех образцов.

Требуется: провести прогнозирование глубины (Depth) и ширины (Width) сварного шва в зависимости от параметров технологического процесса (IW, IF, VW, FP).


## Описание


Есть две папки. В каталоге */jupyter/* вы найдете исходный набор данных (файлы: ebw_data), файл Notebook.ipynb, в котором происходила предварительная обработка набора данных, анализ и обучение моделей. Результаты этого процесса в этой же папке. Модели Scikit-learn LinearRegression, RandomForestRegressor и Scaler были сохранены в файлах .pkl. Там же была сохранена нейросеть Tensorflow.Keras в *nn_model* стандартным методом *.save().

Линейная регрессия была выбрана из-за того, что она легкая и простая и дает, на первый взгляд, хорошие результаты для конкретного набора данных. RandomForestRegressor — второй, мощный и удивительно точный инструмент, даже с параметрами по умолчанию. Scaler.pkl — это сохраненный объект StandardScaler, натренированный на исходном наборе данных. Он используется для масштабирования пользовательского ввода в приложении, обеспечивая нормальное функционирование моделей в производственной среде.

Простая многослойная нейронная сеть в этом проекте сделана на основе tensorflow.keras. У неё было несколько конфигураций в процессе исследования набора данных в jupyter, но я остановился на самой стабильной/точной/крошечной версии.

В */flask.itog/* есть базовое приложение flask, настроенное для развертывания на Heroku. Основной файл python — это app.py, в котором выполняется вся обработка. В *fitted_models* находятся все модели. Во время выполнения веб-приложения ничего не обучается и загружается только в процессе обработки. Таким образом, все предварительно обученные и предварительно сохраненные модели последовательно загружаются, обрабатывают пользовательский ввод и выдают прогнозы в соответствии с их предварительно обученным состоянием.

На этом пока все, в любом случае есть пространство для совершенствования.

Веб приложение развёрнуто [здесь](https://bauman-itog.herokuapp.com)