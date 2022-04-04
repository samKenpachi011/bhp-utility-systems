"""
Django settings for bhp_utility_systems project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import sys

import configparser
from django.core.management.color import color_style
from pathlib import Path

# from .logging import LOGGING
style = color_style()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = 'bhp_utility_systems'

INDEX_PAGE = 'bhpus.bhp.org.bw'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8g!)(+a#0*pv1n+ui5*dqw2axymk+)dh=^3zec#n4sels7!h1p'

# SECURITY WARNING: don't run with debug turned on in production!

ETC_DIR = '/etc/bhp_utility_systems'

SITE_ID = 40

REVIEWER_SITE_ID = 1

LOGIN_REDIRECT_URL = 'home_url'

DEBUG = True

ALLOWED_HOSTS = ['bhpus.bhp.org.bw', 'localhost', '127.0.0.1']

CONFIG_FILE = f'{APP_NAME}.ini'

MAX_UPLOAD_SIZE = "1001440"

CONFIG_PATH = os.path.join(ETC_DIR, CONFIG_FILE)
sys.stdout.write(style.SUCCESS(f'  * Reading config from {CONFIG_PATH}\n'))
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# email configurations
EMAIL_BACKEND = config['email_conf'].get('email_backend')
EMAIL_HOST = config['email_conf'].get('email_host')
EMAIL_USE_TLS = config['email_conf'].get('email_use_tls')
EMAIL_PORT = config['email_conf'].get('email_port')
EMAIL_HOST_USER = config['email_conf'].get('email_user')
EMAIL_HOST_PASSWORD = config['email_conf'].get('email_host_pwd')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'django_extensions',
    'django_q',
    'django_js_reverse',
    'crispy_forms',
    'edc_data_manager.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'procurement_dashboard.apps.AppConfig',
    'procurement.apps.AppConfig',
    'bhp_personnel.apps.AppConfig',
    'cms_dashboard.apps.AppConfig',
    'timesheet.apps.AppConfig',
    'timesheet_dashboard.apps.AppConfig',
    'bhp_utility_systems.apps.EdcBaseAppConfig',
    'bhp_utility_systems.apps.EdcProtocolAppConfig',
    'bhp_utility_systems.apps.EdcIdentifierAppConfig',
    'bhp_utility_systems.apps.EdcFacilityAppConfig',
    'bhp_utility_systems.apps.EdcNavBarAppConfig',
    'bhp_utility_systems.apps.AppConfig',
    'document_tracking.apps.AppConfig',
    'document_tracking_dashboard.apps.AppConfig',
    'django_admin_listfilter_dropdown',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware'
]

ROOT_URLCONF = 'bhp_utility_systems.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bhp_utility_systems.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
mysql_config = configparser.ConfigParser()
mysql_config.read(os.path.join(ETC_DIR, 'mysql.ini'))

HOST = mysql_config['mysql']['host']
DB_USER = mysql_config['mysql']['user']
DB_PASSWORD = mysql_config['mysql']['password']
DB_NAME = mysql_config['mysql']['database']
PORT = mysql_config['mysql']['port']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'test.sqlite',
#     }
#  }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': HOST,  # Or an IP Address that your DB is hosted on
        'PORT': PORT,
        "init_command": "SET foreign_key_checks = 0;",
    }

}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = False

USE_TZ = True

SITE_CODE = '40'

DEFAULT_STUDY_SITE = '40'

# edc_facility
HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')
COUNTRY = 'botswana'

CELLPHONE_REGEX = '^[7]{1}[12345678]{1}[0-9]{6}$|^[2-8]{1}[0-9]{6}$'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'bhp_utility_systems', 'static')
X_FRAME_OPTIONS = 'SAMEORIGIN'

DASHBOARD_URL_NAMES = {
    'data_manager_listboard_url': 'edc_data_manager:data_manager_listboard_url',
    'procurement_url': 'procurement_dashboard:procurement_url',
    'purchase_order_listboard_url': 'procurement_dashboard:purchase_order_listboard_url',
    'purchase_order_report_url': 'procurement_dashboard:purchase_order_report_url',
    'purchase_req_listboard_url': 'procurement_dashboard:purchase_req_listboard_url',
    'email_report_url': 'procurement_dashboard:email_report_url',
    'credit_card_listboard_url': 'procurement_dashboard:credit_card_listboard_url',

    # CMS url name
    'appraisal_dashboard_url': 'cms_dashboard:appraisal_dashboard_url',
    'appraisal_listboard_url': 'cms_dashboard:appraisal_listboard_url',
    'employee_dashboard_url': 'cms_dashboard:employee_dashboard_url',
    'employee_listboard_url': 'cms_dashboard:employee_listboard_url',
    'emp_contract_listboard_url': 'cms_dashboard:emp_contract_listboard_url',
    'pi_contract_listboard_url': 'cms_dashboard:pi_contract_listboard_url',
    'pi_listboard_url': 'cms_dashboard:pi_listboard_url',
    'pi_dashboard_url': 'cms_dashboard:pi_dashboard_url',
    'consultant_contract_listboard_url': 'cms_dashboard:'
                                         'consultant_contract_listboard_url',
    'consultant_listboard_url': 'cms_dashboard:consultant_listboard_url',
    'consultant_dashboard_url': 'cms_dashboard:consultant_dashboard_url',
    'contract_listboard_url': 'cms_dashboard:contract_listboard_url',
    'contact_listboard_url': 'edc_sms:contact_listboard_url',
    'cms_url': 'cms_dashboard:cms_url',
    'reports_url': 'cms_dashboard:reports_url',

    # Document tracking
    'document_dashboard_url': 'document_tracking_dashboard:document_dashboard_url',
    'document_listboard_url': 'document_tracking_dashboard:document_listboard_url',
    'document_url': 'document_tracking_dashboard:document_url',
    'hard_copy_document_listboard_url': 'document_tracking_dashboard:hard_copy_document_listboard_url',
    'reception_docs_listboard_url': 'document_tracking_dashboard:reception_docs_listboard_url',
    'group_documents_listboard_url': 'document_tracking_dashboard:group_documents_listboard_url',
    'send_hard_copy_listboard_url': 'document_tracking_dashboard:send_hard_copy_listboard_url',
    'sent_to_me_listboard_url': 'document_tracking_dashboard:sent_to_me_listboard_url',
    'shared_documents_listboard_url': 'document_tracking_dashboard:shared_documents_listboard_url',
    'sent_listboard_url': 'document_tracking_dashboard:sent_listboard_url',

    # Timesheet
    'timesheet_listboard_url': 'timesheet_dashboard:timesheet_listboard_url',
    'timesheet_employee_listboard_url': 'timesheet_dashboard:timesheet_employee_listboard_url',
    'timesheet_home_url': 'timesheet:timesheet_home_url',
    'timesheet_calendar_table_url': 'timesheet_dashboard:timesheet_calendar_table_url',
    'reports_dashboard_url': 'timesheet_dashboard:reports_dashboard_url',

    # Reports
    'employees_report_listboard_url': 'bhp_utility_reports:employees_report_listboard_url',
    'employee_timesheet_report_listboard_url': 'bhp_utility_reports:employee_timesheet_report_listboard_url',
    'departments_timesheet_report_listboard_url': 'bhp_utility_reports:departments_timesheet_report_listboard_url'
}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'bhp_utility_systems/base.html',
    'purchase_order_listboard_template': 'procurement_dashboard/purchase_order/listboard.html',
    'purchase_req_listboard_template': 'procurement_dashboard/purchase_requisition/listboard.html',
    'purchase_order_report_template': 'procurement_dashboard/purchase_order/report.html',
    'credit_card_listboard_template': 'procurement_dashboard/credit_card/listboard.html',

    'data_manager_listboard_template': 'edc_data_manager/listboard.html',
    # CMS templates
    'appraisal_dashboard_template': 'cms_dashboard/employee/appraisal_dashboard.html',
    'appraisal_listboard_template': 'cms_dashboard/employee/appraisal_listboard.html',
    'contract_listboard_template': 'cms_dashboard/contract/contract_listboard.html',
    'allcontracts_listboard_template': 'cms_dashboard/contract/'
                                       'allcontracts_listboard.html',
    'dashboard_base_template': 'cms/base.html',
    'employee_dashboard_template': 'cms_dashboard/employee/employee_dashboard.html',
    'employee_listboard_template': 'cms_dashboard/employee/employee_listboard.html',
    'pi_dashboard_template': 'cms_dashboard/pi/pi_dashboard.html',
    'pi_listboard_template': 'cms_dashboard/pi/pi_listboard.html',
    'consultant_listboard_template': 'cms_dashboard/consultant/consultant_listboard.html',
    'consultant_dashboard_template': 'cms_dashboard/consultant/consultant_dashboard.html',
    # Document Tracking
    'document_dashboard_template': 'document_tracking_dashboard/document/document_dashboard.html',
    'document_listboard_template': 'document_tracking_dashboard/document/document_listboard.html',
    'reception_docs_listboard_template': 'document_tracking_dashboard/document/reception_docs_listboard.html',
    'hard_copy_document_listboard_template': 'document_tracking_dashboard/document/hard_copy_document_listboard.html',
    'send_hard_copy_listboard_template': 'document_tracking_dashboard/document/send_hard_copy_listboard.html',
    'sent_document_listboard_template': 'document_tracking_dashboard/document/sent_document_listboard.html',
    'sent_to_me_listboard_template': 'document_tracking_dashboard/document/sent_to_me_listboard.html',
    'shared_documents_listboard_template': 'document_tracking_dashboard/document/shared_documents_listboard.html',
    # Timesheet
    'timesheet_listboard_template': 'timesheet_dashboard/timesheet_listboard.html',
    'timesheet_employee_listboard_template': 'timesheet_dashboard/employee_listboard.html',
    'reports_dashboard_template': 'timesheet_dashboard/reports/dashboard.html',

    # Reports
    'employees_report_listboard_template': 'bhp_utility_reports/employees_listboard.html',
    'employee_timesheet_report_listboard_template': 'bhp_utility_reports/employee_timesheet_listboard.html',
    'departments_timesheet_report_listboard_template': 'bhp_utility_reports/departments_timesheet_listboard.html'
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'
GIT_DIR = BASE_DIR
