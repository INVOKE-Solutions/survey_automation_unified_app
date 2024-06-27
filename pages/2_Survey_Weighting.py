from module.utils.ui_components import page_style
from module.utils.security import check_password
from module.survey_weighting_R.component_weighting import init_survey_weighting
if check_password():
    page_style(title="Survey Weighting")
    init_survey_weighting()