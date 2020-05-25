import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url='http://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Start code:",r.status_code)

response_dict=r.json()
print("Total repositories:",response_dict['total_count'])

repo_dicts=response_dict['items']
print("Repositories returned:",len(repo_dicts))

names,plot_dicts=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict={'value':repo_dict['stargazers_count'],'label':repo_dict['description'],}

    plot_dicts.append(plot_dict)

my_style=LS('#333366',base_style=LCS)

chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title='Python Projects'
chart.x_labels=names
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')