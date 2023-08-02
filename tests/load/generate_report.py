import sys
import pandas as pd
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader
import os
curr_path = os.getcwd()


# 读取CSV文件
df = pd.read_csv('/Users/genosho/Documents/automation/reports/load_test_stats.csv')

# 使用Matplotlib生成请求响应时间的柱状图
df.plot(kind='bar', x='Name', y='Average Response Time', color='blue')
plt.title('Average Response Time')
plt.ylabel('Response Time (ms)')

plt.savefig('response_time.png')

# 使用Jinja2生成HTML报告
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('report_template.html')
output = template.render(data=df.to_html(), image='response_time.png')
with open('report.html', 'w') as f:
    f.write(output)
