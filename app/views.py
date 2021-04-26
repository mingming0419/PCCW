from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, NewsCategory, Careers_with_us, News, Investor_Relations, Investing_in_PCCW, Financial_Results_table, Annual_Results_table, Interim_Results_table, Fast_Facts_PCCW_Limited
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)
    

class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']
    
class Careers_with_usView(ModelView):
    datamodel = SQLAInterface(Careers_with_us)
    list_columns = ['id', 'Job_title', 'Location', 'Job_category', 'Posted']

class Careers_with_usPageView(BaseView):
    default_view = 'Careers_with_usView'

    @expose('/Careers_with_usView/')
    def Careers_with_usView(self):
        data = db.session.query(Careers_with_us).all()
        self.update_redirect()
        return self.render_template('Job.html', data=data)

class Investor_Relations_view(ModelView):
    datamodel = SQLAInterface(Investor_Relations)
    list_columns = ['id', 'Investor_Relations_title', 'Investor_Relations_link_id']

class Investing_in_PCCW_view_inputed_data(ModelView):
    datamodel = SQLAInterface(Investing_in_PCCW)
    list_columns = ['id', 'Investing_in_PCCW_title', 'Investing_in_PCCW_content']

class Investing_in_PCCW_view(ModelView):
    datamodel = SQLAInterface(Investing_in_PCCW)

class investing_in_pccw_pageview(BaseView):
    default_view = 'investing_in_pccw_view'
    
    @expose('/investing_in_pccw_view/')
    def investing_in_pccw_view(self):
        result = db.session.query(Investing_in_PCCW.Investing_in_PCCW_content).first()
        param1 = "investing in pccw view"
        param2 = result
        self.update_redirect()
        return self.render_template('investing_in_PCCW.html', param1 = param1, param2 = param2, result = result)

class Financial_Results_table_view(ModelView):
    datamodel = SQLAInterface(Financial_Results_table)

'''class Financial_Results_table_pageview(BaseView):
    default_view = 'Financial_Results_table_view'''

class Annual_Results_table_view(ModelView):
    datamodel = SQLAInterface(Annual_Results_table)

'''class Annual_Results_table_pageview(BaseView):
    default_view = 'Annual_Results_table_view'''

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']

class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

class Fast_Facts_PCCW_Limited_view(ModelView):
    datamodel = SQLAInterface(Fast_Facts_PCCW_Limited)
    
class Fast_Facts_PCCW_Limited_pageview(BaseView):
    default_view = 'Fast_Facts_PCCW_Limited_view'
                                                    
    @expose('/Fast_Facts_PCCW_Limited_view/')
    def investing_in_pccw_view(self):
        result = db.session.query(Fast_Facts_PCCW_Limited.Fast_Facts_PCCW_Limited_content).first()
        param1 = "Fast_Facts_PCCW_Limited_view"
        param2 = result
        self.update_redirect()
        return self.render_template('Fast_Facts_PCCW_Limited.html', param1 = param1, param2 = param2, result = result)

db.create_all()

""" Page View """
appbuilder.add_view(Careers_with_usView, 'Careers with us', category="Job")
appbuilder.add_view(Careers_with_usPageView, 'Careers_with_usView', category="Job")
appbuilder.add_view(NewsPageView, 'Local News', category="News")
appbuilder.add_link("Global News", href="/newspageview/global_news/", category="News")
appbuilder.add_view(investing_in_pccw_pageview, 'investing in pccw', category="Investor Relations")
appbuilder.add_view(Investing_in_PCCW_view_inputed_data, 'Investing_in_PCCW_view_inputed_data', category="Investor Relations")
'''appbuilder.add_link("investing in pccw", href="/investor_relations_view/investing_in_pccw_view/", category="Investor Relations")'''
appbuilder.add_view(Financial_Results_table_view, 'Financial_Results_table', category="Investor Relations")
appbuilder.add_view(Fast_Facts_PCCW_Limited_view, 'Fast_Facts_PCCW_Limited', category="Investor Relations")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")                                                                                                                                                                                        
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")
