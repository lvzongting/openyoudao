from BeautifulSoup import BeautifulSoup
import os
import re
import popen2
soup = BeautifulSoup(open("index.html"))
head = soup.html.head.extract()
#sousuo = soup.html.body.div#doc.div#scontainer.div#container.div#results.extract()
result = soup.find('div',{"id":"results"})
sousuo = soup.find('form',{"id":"f"})
sousuo  = str(sousuo).replace("action=\"/search\"","action=\"http://dict.youdao.com/search\"")
os.system("rm  history.html")
fin,fout = popen2.popen2("tee -a history.html")
fout.write("<html>")
fout.write(str(head))
fout.write(str(sousuo))
fout.write(str(result))
fout.write("</html>")
fout.close()
#os.system("/bin/echo -e  \'"+ str(head) + "\' >> history.html")
#os.system("/bin/echo -e  \'"+ str(sousuo) + "\' >> history.html")
#ad1=soup.html
#soup.html.body.div#doc.div.c-topbar.c-subtopbar.extract()
#soup.html.body.div#doc.div.c-header.a.extract()
#soup.html.body.div#doc.div.scontainer.div#container.div#topimgAd.iframe.html.body.div#uptown.uptown.table.tbody.tr.td.div.a#dish0.img.extract()
#soup.html.body.div#doc.div.scontainer.div#container.div#ads.ads.extract()
#str1=str(ad1)
#os.system("echo -e \'"+ str1 + "\' >> history.html")
