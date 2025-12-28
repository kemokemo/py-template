from jinja2 import Environment, FileSystemLoader
import seaborn as sns

## create data
diamondsDf = sns.load_dataset('diamonds')
cut_totals = diamondsDf.groupby('cut', observed=True)['carat'].count().reset_index().rename(columns={"carat": "count"}).sort_values("count", ascending=False)
color_totals = diamondsDf.groupby('color', observed=True)['carat'].count().reset_index().rename(columns={"carat": "count"}).sort_values("count", ascending=False)

## render
env = Environment(
    loader=FileSystemLoader('templates'),
    trim_blocks=True
)
template = env.get_template("report_template.html")

report_name = 'Issue Report'
summary_title = 'まとめ'
duration = '2025/12/1 - 2025/12/5'
content = '内容1の案件が最も多く、案件がX件増加した。'

rendered_content = template.render(
	report_name=report_name,
	summary_title=summary_title,
	duration=duration,
	summary_content=content,
	pie1_labels=cut_totals['cut'].to_list(),
	pie1_series=cut_totals['count'].to_list(),
	pie2_labels=color_totals['color'].to_list(),
	pie2_series=color_totals['count'].to_list()
)

#print(rendered_content)

with open('report.html', 'w') as f:
	f.write(rendered_content)
