# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QWidget {{
    background-color: {_bg_color};
}}

QTabWidget {{
    border-radius: {_radius}px;
    background-color: {_bg_color};
}}

QTabBar::tab {{
    background-color: {_bg_color};
    border-radius: {_radius}px;
    padding: 5px;
    margin: 2px;
}}

QTabBar::tab:selected {{
    /*border: 1px solid lightgray;*/
    background-color: {_selection_color};
}}

QTabWidget::pane {{
    background-color: {_bg_color};
}}
'''
