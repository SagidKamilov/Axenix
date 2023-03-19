import numpy as np
import random
import pandas as pd
import datetime

# Симуляция метаданных сообщений
# Создаем массив данных для 2-6 месяцев
start_date = datetime.date(2022, 1, 1)
end_date = start_date + datetime.timedelta(days=182)
date_range = pd.date_range(start=start_date, end=end_date, freq='H')
n_messages = len(date_range)
messages_data = np.random.normal(10, 3, n_messages)
messages_df = pd.DataFrame({'id_message': np.arange(1, n_messages+1),
                            'date': date_range.date,
                            'time': date_range.time,
                            'text': messages_data})

# Добавляем аномалии
anomaly_indices = random.sample(range(len(messages_df)), k=50)
messages_df.loc[anomaly_indices, 'text'] = np.random.normal(30, 5, len(anomaly_indices))

# Симуляция метаданных о коммитах
# Создаем массив данных для 2-6 месяцев
commits_data = np.random.normal(10, 3, n_messages)
commits_df = pd.DataFrame({'id_commit': np.arange(1, n_messages+1),
                           'date creation': date_range.date,
                           'time creation': date_range.time,
                           'text': commits_data})

# Добавляем аномалии
anomaly_indices = random.sample(range(len(commits_df)), k=50)
commits_df.loc[anomaly_indices, 'text'] = np.random.normal(30, 5, len(anomaly_indices))

# Симуляция метаданных о задачах с таск-менеджера
# Создаем массив данных для 2-6 месяцев
tasks_data = np.random.normal(10, 3, n_messages)
tasks_df = pd.DataFrame({'id_task': np.arange(1, n_messages+1),
                         'name': ['Task ' + str(i) for i in range(1, n_messages+1)],
                         'description': tasks_data,
                         'date of creation': date_range.date,
                         'status': np.random.choice(['open', 'in progress', 'closed'], size=n_messages, p=[0.4, 0.4, 0.2])})

# Добавляем аномалии
anomaly_indices = random.sample(range(len(tasks_df)), k=50)
tasks_df.loc[anomaly_indices, 'description'] = np.random.normal(30, 5, len(anomaly_indices))

# Симуляция времени активности приложений
# Создаем массив данных для 2-6 месяцев
app_data = np.random.normal(10, 3, n_messages)
app_opening_time = [date_range[i] - pd.Timedelta(minutes=app_data[i]) for i in range(len(app_data))]
app_closing_time = [date_range[i] + pd.Timedelta(minutes=app_data[i]) for i in range(len(app_data))]

app_df = pd.DataFrame({'id_app': np.arange(1, n_messages+1),
                       'name': ['App ' + str(i) for i in range(1, n_messages+1)],
                       'opening time': app_opening_time,
                       'closing time': app_closing_time})

# Добавляем аномалии
anomaly_indices = random.sample(range(len(app_df)), k=50)

print(messages_df, commits_df, tasks_df, app_df)