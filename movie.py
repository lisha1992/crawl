# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:33:52 2016

@author: ceciliaLee
"""

from bs4 import BeautifulSoup, Tag
import urllib2
import re
import sys


def LOG(*argv):
    sys.stderr.write(*argv) # sys.stderr: error 
    sys.stderr.write('\n')
 
class Grab():
    url = ''
    soup = None
    def GetPage(self, url):
        if url.find('http://',0,7) != 0:
            url = 'http://' + url
        self.url = url
        LOG('input url is: %s' % self.url)
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        try:
            page = urllib2.urlopen(req)
        except:
            return
        return page.read()  
 
    def ExtractInfo(self,buf):
        if not self.soup:
            try:
                self.soup = BeautifulSoup(buf)
            except:
                LOG('soup failed in ExtractInfo :%s' % self.url)
            return
        try:
            items = self.soup.findAll(attrs={'class':'item'})
        except:
            LOG('failed on find items:%s' % self.url)
            return
        links = []
        objs = [] 
        titles = []
        scores = []
        comments = []
        intros = []
        for item in items:
            try:
                pic = item.find(attrs={'class':'nbg'})
                link = pic['href']
                obj = pic.img['src']
                info = item.find(attrs={'class':'pl2'})
                title = re.sub('[ \t]+',' ',info.a.getText().replace('&amp;nbsp','').replace('\n',''))
                star = info.find(attrs={'class':'star clearfix'})
                score = star.find(attrs={'class':'rating_nums'}).getText().replace('&amp;nbsp','')
                comment = star.find(attrs={'class':'pl'}).getText().replace('&amp;nbsp','')
                intro = info.find(attrs={'class':'pl'}).getText().replace('&amp;nbsp','')
            except Exception,e:
                LOG('process error in ExtractInfo: %s' % self.url)
                continue
            links.append(link)
            objs.append(obj)
            titles.append(title)    
            scores.append(score)
            comments.append(comment)
            intros.append(intro)
        return(links, objs, titles, scores, comments, intros)
 
    def ExtractPageTurning(self,buf):
        links = set([])
        if not self.soup:
            try:
                self.soup = BeautifulSoup(buf)
            except:
                LOG('soup failed in ExtractPageTurning:%s' % self.url)
                return
        try:
            pageturning = self.soup.find(attrs={'class':'paginator'})
            a_nodes = pageturning.findAll('a')
            for a_node in a_nodes:
                href = a_node['href']
                if href.find('http://',0,7) == -1:
                    href = self.url.split('?')[0] + href
                links.add(href)
        except:
            LOG('get pageturning failed in ExtractPageTurning:%s' % self.url)
 
        return links
 
    def Destroy(self):
        del self.soup
        self.soup = None
