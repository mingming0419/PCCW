import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")

class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")

class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class Careers_with_us(Model):
   __tablename__ = 'Careers_with_us'
   id = Column(Integer, primary_key=True)
   Job_title = Column(String(255), nullable=False)
   Location = Column(String(255), nullable=False)
   Job_category = Column(String(255), nullable=False)
   Posted = Column(Date, default=datetime.date.today(), nullable=True)

class Investor_Relations(Model):
    __tablename__ = 'Investor_Relations'
    id = Column(Integer, primary_key=True)
    Investor_Relations_title = Column(String(255), nullable=False)
    Investor_Relations_link = Column(String(255), nullable=False)

class Investing_in_PCCW(Model):
    __tablename__ = 'Investing_in_PCCW'
    id = Column(Integer, primary_key=True)
    Investing_in_PCCW_title = Column(String(255), nullable=False)
    Investing_in_PCCW_content = Column(String(10000), nullable=False)

class Financial_Results_table(Model):
    __tablename__ = "Financial_Results_table"
    id = Column(Integer, primary_key=True)
    Annual_Results = Column(String(255), nullable=False)
    Interim_Results = Column(String(255), nullable=False)
    
    
class Annual_Results_table(Model):
    __tablename__ = "Annual_Results_table"
    id = Column(Integer, primary_key=True)
    Annual_Results = Column(String(255), nullable=False)

class Interim_Results_table(Model):
    __tablename__ = "Interim_Results_table"
    id = Column(Integer, primary_key=True)
    Interim_Results = Column(String(255), nullable=False)

'This Investing_in_PCCW table is stored are html code for render investing_in_PCCW.html'
    
class Investor_Contacts(Model):
    __tablename__= 'Investor_Contacts'
    id = Column(Integer, primary_key=True)
    Investor_Contacts_title = Column(String(255), nullable=False)
    Investor_Contacts_content = Column(String(10000), nullable=False)

class FAQs(Model):
    __tablename__= 'FAQs'
    id = Column(Integer, primary_key=True)
    FAQs_title = Column(String(255), nullable=False)
    FAQs_content = Column(String(10000), nullable=False)

class Fast_Facts_PCCW_Limited(Model):
    __tablename__='Fast_Facts_PCCW_Limited'
    id = Column(Integer, primary_key=True)
    Fast_Facts_PCCW_Limited_title = Column(String(255), nullable=False)
    Fast_Facts_PCCW_Limited_content = Column(String(10000), nullable=False)
    
class Report(Model):
    __tablename__='report'
    id = Column(Integer, primary_key=True)
    year = Column(String(255), nullable=False)
    report_name = Column(String(255), nullable=False)
    report_link = Column(String(255), nullable=False)
   
class Leadership(Model):
    __tablename__ = 'leadership'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    contect = Column(String(500), nullable=False)
    
class Senior_corporate(Model):
  tablename = 'senior_corporate'
  id = Column(Integer, primary_key=True)
  name = Column(String(50), nullable=False)
  contect = Column(String(500), nullable=False)
