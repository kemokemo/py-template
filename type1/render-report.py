from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('templates'),
    trim_blocks=True
)

template = env.get_template("report_template.html")

report_name = 'Issue Report'
summary_title = 'まとめ'
duration = '2025/12/1 - 2025/12/5'
content = '内容1の案件が最も多く、案件がX件増加した。'
links1 = [{'href': "#", 'caption': "Issue 1"}, {'href': "#", 'caption': "Issue 2"}]
links2 = [{'href': "#", 'caption': "Issue 3"}, {'href': "#", 'caption': "Issue 4"}]

rendered_content = template.render(
	report_name=report_name,
	summary_title=summary_title,
	duration=duration,
	summary_content=content,
	links1=links1,
	links2=links2
	)

#print(rendered_content)

with open('dist/index.html', 'w') as f:
	f.write(rendered_content)
