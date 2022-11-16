# bauman.itog
 ## Description
 Qualification work for Bauman University data science course.

 There are two folders. In */jupyter/* catalogue you'll find original dataset (files: ebw_data), notebook.ipynb file, that's where dataset preprocessing, analysis and models fitting took place. Results of this process also in the same folder. Scikit-learn models of LinearRegression, RandomForestRegressor and StandartScaler were saved to .pkl files. Also Tensorflow.Keras neural net were saved there in *nn_model* using standart *.save() method.

LinearRegression were choosen since it's light and easy and provides seamingly good results for the particular dataset. RandomForestRegressor is a second one, powerfull and surprisingly accurate tool even with default parameters. Scaler.pkl is a saved StandartScaler object trained on the original dataset, it's being used for scaling user input in an application, providing normal models functioning in production.

Simple multi-layer neural net in this project based on tensorflow.keras. It had a few configurations in jupyter dataset exploration process, but I stayed with the most stable/accurate/tiny version. 

In */flask.itog/* there's a basic flask application tuned for Heroku deployment. Main python file is an app.py where all the magic getting done. In *fitted_models* all the models are hiding. While webapp execution nothing being trained and only loading during the handling process. So all pretrained and presaved model sequentially loading, process user input and give predictions according to their pretrained state.

That's all for now, a lot of room for improvement anyway.

## Описание
Квалификационная работа по курсу Аналитик данных МГТУ им. Баумана

Есть две папки. В каталоге */jupyter/* вы найдете исходный набор данных (файлы: ebw_data), файл Notebook.ipynb, в котором происходила предварительная обработка набора данных, анализ и обучение моделей. Результаты этого процесса в этой же папке. Модели Scikit-learn LinearRegression, RandomForestRegressor и Scaler были сохранены в файлах .pkl. Там же была сохранена нейросеть Tensorflow.Keras в *nn_model* стандартным методом *.save().

Линейная регрессия была выбрана из-за того, что она легкая и простая и дает, на первый взгляд, хорошие результаты для конкретного набора данных. RandomForestRegressor — второй, мощный и удивительно точный инструмент, даже с параметрами по умолчанию. Scaler.pkl — это сохраненный объект StandardScaler, натренированный на исходном наборе данных. Он используется для масштабирования пользовательского ввода в приложении, обеспечивая нормальное функционирование моделей в производственной среде.

Простая многослойная нейронная сеть в этом проекте сделана на основе tensorflow.keras. У неё было несколько конфигураций в процессе исследования набора данных в jupyter, но я остановился на самой стабильной/точной/крошечной версии.

В */flask.itog/* есть базовое приложение flask, настроенное для развертывания на Heroku. Основной файл python — это app.py, в котором выполняется вся обработка. В *fitted_models* находятся все модели. Во время выполнения веб-приложения ничего не обучается и загружается только в процессе обработки. Таким образом, все предварительно обученные и предварительно сохраненные модели последовательно загружаются, обрабатывают пользовательский ввод и выдают прогнозы в соответствии с их предварительно обученным состоянием.

На этом пока все, в любом случае есть пространство для совершенствования.