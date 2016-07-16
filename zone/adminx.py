#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: adminx������
Desc :
"""
import xadmin
import xadmin.views as xviews
from .models import  Post
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(xviews.BaseAdminView, BaseSetting)


class AdminSettings(object):
    # ����base_site.html��Title
    site_title = '���͹����̨'
    # ����base_site.html��Footer
    site_footer = 'Winhong Inc.'
    menu_style = 'default'

    # �˵�����
    def get_site_menu(self):
        return (
            {'title': '���͹���', 'perm': self.get_model_perm(Page, 'change'), 'menus': (
                {'title': '����ҳ��', 'icon': 'fa fa-vimeo-square'
                    , 'url': self.get_model_url(Page, 'changelist')},
                {'title': '����Ŀ¼', 'icon': 'fa fa-vimeo-square'
                    , 'url': self.get_model_url(Category, 'changelist')},
            )},
        )
xadmin.site.register(xviews.CommAdminView, AdminSettings)

xadmin.site.register(Page)
xadmin.site.register(Category)
# xadmin.site.register(Tag)
# xadmin.site.register(Post)
# xadmin.site.register(Comment)
# xadmin.site.register(Evaluate)