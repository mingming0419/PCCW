from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, NewsCategory, Careers_with_us, News, Investor_Relations, Investing_in_PCCW, Financial_Results_table, Annual_Results_table, Interim_Results_table, Fast_Facts_PCCW_Limited, FAQs, Investor_Contacts, Report, Leadership, Senior_corporate
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


class leadership(ModelView):
 datamodel = SQLAInterface(Leadership)
 list_columns = ['id', 'name', 'contect']
 
class leadershipPageView(BaseView):
    default_view = 'Leadershipview'
  
    @expose('/Leadershipview/')
    def Leadershipview(self):
        data = db.session.query(Leadership).all()
        self.update_redirect()
        return self.render_template('leadership.html', data=data)
        
class senior_corporate(ModelView):
 datamodel = SQLAInterface(Senior_corporate)
 list_columns = ['id', 'name', 'contect']
 
class Senior_corporatePageView(BaseView):
    default_view = 'Senior_corporateview'
    
    @expose('/Senior_corporateview/')
    def Senior_corporateview(self):
        data = db.session.query(Senior_corporate).all()
        self.update_redirect()
        return self.render_template('Senior_corporate.html', data=data)
      
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
        newsdata = db.session.query(News).filter(News.newsCat_id == '1')
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1, newsdata = newsdata)

    @expose('/global_news/')
    def global_news(self):
        newsdata = db.session.query(News).filter(News.newsCat_id == '2')
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1, newsdata = newsdata)

class Fast_Facts_PCCW_Limited_view(ModelView):
    datamodel = SQLAInterface(Fast_Facts_PCCW_Limited)
    list_columns = ['id', 'Fast_Facts_PCCW_Limited_title', 'Fast_Facts_PCCW_Limited_content']

class Fast_Facts_PCCW_Limited_pageview(BaseView):
    default_view = 'Fast_Facts_PCCW_Limited_view'
                                                    
    @expose('/Fast_Facts_PCCW_Limited_view/')
    def Fast_Facts_PCCW_Limited_view(self):
        result = db.session.query(Fast_Facts_PCCW_Limited.Fast_Facts_PCCW_Limited_content).first()
        param1 = "Fast_Facts_PCCW_Limited_view"
        param2 = result
        self.update_redirect()
        return self.render_template('Fast_Facts_PCCW_Limited.html', param1 = param1, param2 = param2, result = result)
        

class FAQs_view(ModelView):
    datamodel = SQLAInterface(FAQs)
    list_columns = ['id', 'FAQs_title', 'FAQs_content']

class FAQs_pageview(BaseView):
    default_view = 'FAQs_view'
                                                    
    @expose('/FAQs_view/')
    def FAQs_view(self):
        result = db.session.query(FAQs.FAQs_content).first()
        param1 = "FAQs_view"
        param2 = result
        self.update_redirect()
        return self.render_template('FAQs.html', param1 = param1, param2 = param2, result = result)
        
class Investor_Contacts_view(ModelView):
    datamodel = SQLAInterface(Investor_Contacts)
    list_columns = ['id', 'Investor_Contacts_title', 'Investor_Contacts_content']

class Investor_Contacts_pageview(BaseView):
    default_view = 'Investor_Contacts_view'
                                                    
    @expose('/Investor_Contacts_view/')
    def Investor_Contacts_view(self):
        result = db.session.query(Investor_Contacts.Investor_Contacts_content).first()
        param1 = "Investor_Contacts_view_view"
        param2 = result
        self.update_redirect()
        return self.render_template('Investor_Contacts.html', param1 = param1, param2 = param2, result = result)
                                                                            
class Reportview(ModelView):
    datamodel = SQLAInterface(Report)
    list_columns = ['id', 'year', 'report_name', 'report_link']
    
class Report_pageview(BaseView):
    default_view = 'Report_view'
    
    @expose('Report_view')
    def Report_view(self):
        data = db.session.query(Report).all()
        self.update_redirect()
        return self.render_template('report.html', data = data)
    
db.create_all()

""" Page View """
appbuilder.add_view(Careers_with_usPageView, 'Careers With Us', category="Careers")
appbuilder.add_view(NewsPageView, 'Local News', category="News")
appbuilder.add_link("Global News", href="/newspageview/global_news/", category="News")
appbuilder.add_view(investing_in_pccw_pageview, 'investing in pccw', category="Investor Relations")
appbuilder.add_view(Investing_in_PCCW_view_inputed_data, 'Investing_in_PCCW_view_inputed_data', category="Investor Relations")
'''appbuilder.add_link("investing in pccw", href="/investor_relations_view/investing_in_pccw_view/", category="Investor Relations")'''
appbuilder.add_view(Financial_Results_table_view, 'Financial_Results_table', category="Investor Relations")
appbuilder.add_view(Investor_Contacts_pageview, 'Investor_Contacts', category="Investor Relations")
appbuilder.add_view(FAQs_pageview, 'FAQs', category="Investor Relations")
appbuilder.add_view(Fast_Facts_PCCW_Limited_pageview, 'Fast_Facts_PCCW_Limited', category="Investor Relations")
appbuilder.add_view(Report_pageview, "Environmental, Social and Governance Report", category="CSR")
appbuilder.add_view(leadershipPageView, "Leadership", category="About Us")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")                                                                                                                                                                                        
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(Careers_with_usView, "Jobs",icon="fa-folder-open-o" , category="Admin")
appbuilder.add_view(Reportview, "Report",icon="fa-folder-open-o" , category="Admin")
appbuilder.add_view(FAQs_view, 'FAQs',icon="fa-folder-open-o" , category="Admin")
appbuilder.add_view(Investor_Contacts_view, 'Investor_Contacts',icon="fa-folder-open-o" , category="Admin")
appbuilder.add_view(Fast_Facts_PCCW_Limited_view, 'Fast_Facts_PCCW_Limited',icon="fa-folder-open-o" , category="Admin")

