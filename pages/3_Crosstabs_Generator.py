from module.crossart_generator.component_crosstabs import init_crossgen_tab
from module.utils.ui_components import page_style
from module.utils.security import check_password

if check_password():
    page_style(title="Crosstabs Generator")
    init_crossgen_tab()
