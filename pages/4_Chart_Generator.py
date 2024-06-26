from module.crossart_generator.component_charts import init_chart_gen
from module.utils.ui_components import page_style
from module.utils.security import check_password

if check_password():
    page_style(title="Chart Generator")
    init_chart_gen()