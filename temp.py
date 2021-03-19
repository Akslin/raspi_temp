# Copyright (c) Akslin

import linecache

file_name = 'actual_temp.log'
file = open(file_name, 'a+', encoding='utf-8')

file_html_name = 'index.html'
file_html = open(file_html_name, 'w+', encoding='utf-8')

time_line = str(linecache.getline(file_name, 1))
gpu_line = str(linecache.getline(file_name, 2))
cpu_line = str(linecache.getline(file_name, 3))

gpu_temp = gpu_line[9:13]
cpu_temp = cpu_line[9:11]


file_html.write('<html>\n')
file_html.write('<head>\n')
file_html.write('<title>\n')
file_html.write('Raspberry temperature \n')
file_html.write('</title>\n')

file_html.write('</head>\n')
file_html.write('<body>\n')
file_html.write('<h2>Raspberry temperature:</h2>\n')
file_html.write('Last update: {}\n'.format(time_line))
file_html.write('<br>\n')
file_html.write('<br>\n')
file_html.write('GPU temp: {}\n'.format(gpu_temp))
file_html.write('<br>\n')
file_html.write('CPU temp: {}\n'.format(cpu_temp))
file_html.write('<br>\n')
file_html.write('<br>\n')


file_html.write('</body>\n')
file_html.write('</html>\n')
