# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import os


class InkuMail(object):

    def __init__(self):
        super().__init__()
        with open(os.path.join("templates", "mail.html"), "r") as file_handle:
            self.mail = BS(file_handle.read(), "html.parser")

        self.articles_by_category = self.read_articles()

    def main(self):
        self.add_banner()
        self.add_title()
        self.add_intro()
        self.add_table_of_contents()
        self.add_body()
        self.add_outro()

    def add_banner(self):
        self.mail.find(id="main_banner").append(
            BS("<img src='http://www.inkubio.fi/sites/default/files/kuvat/inkumail-header.png' width='530' alt='' style='width:100%; max-width:530 px'>", "html.parser"))

    def add_title(self):
        title = self._read_title()
        self.mail.find(id="title").contents = BS(title, "html.parser")

    def add_intro(self):
        intro = self._read_intro()
        self.mail.find(id="intro").contents = BS(intro, "html.parser")

    def add_table_of_contents(self):
        for category in self.articles_by_category:
            category_title_soup = self._create_title_soup(category["title"], category["color"])
            self._add_category_title(category_title_soup)
            with open(os.path.join("templates", "table_of_contents", "articles.html")) as file_handle:
                article_title_html = BS(file_handle.read(), "html.parser")
            tag = article_title_html.find(id="articles")
            for num, article in enumerate(category["articles"]):
                tag.append(
                    BS(self._article_title_html(num+1, article["title"], category["title"]), "html.parser"))
            self.mail.find(id="table_of_contents").append(tag)

    def _add_category_title(self, title_soup):
        self.mail.find(id="table_of_contents").append(title_soup)

    def _article_title_html(self, num, article_title, category_title):
        title = f"<a href='#{category_title}_title{num}' style='color:#0ba360; text-decoration:none; padding:0 0 5px 0'>{num}. <b>{article_title}</b></a><br>"
        return title

    def add_body(self):
        tbody = self.mail.find(id="table_of_articles")
        for category in self.articles_by_category:
            for num, article in enumerate(category["articles"]):
                article_html = self._create_article_html(article, category, num+1)
                tbody.append(article_html)

    def _create_article_html(self, article, category, num):
        with open(os.path.join("templates", "articles", "article.html")) as file_handle:
            article_html = BS(file_handle.read(), "html.parser")
        article_html.find(id="link_target").append(BS(f"<a name='{category['title']}_title{num}' target='_blank' rel='noopener noreferrer'></a>", "html.parser"))
        article_html.find(id="title").append(BS(f"<b>{num}. <b>{article['title']}</b></b><br>", "html.parser"))
        article_html.find(id="body").append(BS(article["body"], "html.parser"))
        article_html.find("table")["bgcolor"] = category["color"]
        return article_html

    def add_outro(self):
        outro = self._read_outro()
        self.mail.find(id="outro").append(outro)

    def _read_title(self):
        return "Viikkomaili X/20"

    def _read_intro(self):
        return "Tässä kiva introteksti :)"

    def _read_outro(self):
        return "Tässä kiva outroteksti :)"

    def read_articles(self):
        return articles

    def _create_title_soup(self, title, color):
        with open(os.path.join("templates", "table_of_contents", "category_title.html")) as file_handle:
            category_title = BS(file_handle.read(), "html.parser")
        category_title.find(id="table_of_contents_category_title").append(title)
        category_title.table["color"] = f"{color}"
        category_title.table["bgcolor"] = f"{color}"
        return category_title
