from jinja2 import Environment, FileSystemLoader
import base64

# copy from https://qiita.com/_meki/items/8b3b51024f55deb3797b
def get_base64_image_tag(image_path, mime_type):
    with open(image_path, "rb") as f:
        src = base64.b64encode(f.read()).decode('utf-8')
        return f'''<img src="data:image/{mime_type};base64,{src}" />'''

env = Environment(
    loader=FileSystemLoader('templates'),
    trim_blocks=True
)

template = env.get_template("report_template.html")

report_name = 'Issue Report'
summary_title = 'まとめ'
duration = '2025/12/1 - 2025/12/5'
content = '内容1の案件が最も多く、案件がX件増加した。'
image_pie = get_base64_image_tag('images/pie-chart.png', 'png')
image_column = get_base64_image_tag('images/column-chart.png', 'png')
links1 = [{'href': "#", 'caption': "Issue 1"}, {'href': "#", 'caption': "Issue 2"}]
links2 = [{'href': "#", 'caption': "Issue 3"}, {'href': "#", 'caption': "Issue 4"}]

rendered_content = template.render(
	report_name=report_name,
	summary_title=summary_title,
	duration=duration,
	summary_content=content,
    image_pie=image_pie,
    image_column=image_column,
	links1=links1,
	links2=links2
	)

#print(rendered_content)

with open('report.html', 'w') as f:
	f.write(rendered_content)
