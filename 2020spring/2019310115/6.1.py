{
  "cells": [
   {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
     "### 一个简单的例子"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 6,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "\n",
       "This page serves as the primary guide for my students who want to learn Python.\n",
       "\n"
      ]
     }
    ],
    "source": [
     "from urllib.request import urlopen\n",
     "from bs4 import BeautifulSoup\n",
     "\n",
     "html = urlopen('https://feng.li/python/')#打开网页\n",
     "bs = BeautifulSoup(html.read(), 'html.parser')\n",
     "nameList = bs.findAll('div', {'class':'entry-content'})#寻找满足一定条件的内容，关键\n",
     "for name in nameList:\n",
     "    print(name.get_text())#得到里面的文本"
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 97,
    "metadata": {},
    "outputs": [
     {
      "name": "stdout",
      "output_type": "stream",
      "text": [
       "葡萄牙新增852例新冠肺炎确诊病例 累计9886例\u00012020-04-03\u0001海外网\u0001　　原标题：葡萄牙新增852例新冠肺炎确诊病例 累计9886例   　　[海外网4月3日|战疫全时区]据葡萄牙媒体“TVi24”报道 葡萄牙卫生部4月3日通报称 过去24小时\u0001https://news.sina.com.cn/w/2020-04-03/doc-iimxxsth3544230.shtml\n",
       "约翰斯·霍普金斯大学：中国以外新冠肺炎死亡病例超5万例\u00012020-04-03\u0001中国网直播\u0001截至北京时间4月3日下午6时02分 全球新冠肺炎累计确诊病例达1026974例 累计死亡病例达53975例 据中国卫健委4月3日最新通报 截至4月2日24时 据31个省（自治区、直辖市）和新疆生产建设兵团报告\u0001https://k.sina.com.cn/article_1884488621_m705303ad03300qnaa.html?from=news&subch=onews\n",
       "葡萄牙新冠肺炎确诊病例增加9.4%至9886例。\u00012020-04-03\u0001新浪财经\u0001葡萄牙新冠肺炎确诊病例增加9.4%至9886例 \u0001https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxyqwa4981913.shtml\n",
       "台湾新冠肺炎确诊个案增至348人\u00012020-04-03\u0001新华网\u0001 　　新华社台北4月3日电（记者吴济海、傅双琪）台湾地区流行疫情指挥中心3日举行记者会公布\u0001https://news.sina.com.cn/c/2020-04-03/doc-iimxyqwa4971629.shtml\n",
       "新冠肺炎疫情带来什么启示？钟南山这样说\u00012020-04-03\u0001贵阳校园头条\u0001 新冠肺炎疫情带来什么启示？钟南山这样说  \u0001https://k.sina.com.cn/article_6424076363_m17ee7a04b03300uvv7.html?from=health\n",
       "美国患新冠肺炎护士上街抗议：我已感染 还被要求继续工作\u00012020-04-03\u0001一抹景色Yk\u0001\u0001https://k.sina.com.cn/article_3703570897_mdcc001d100101t0aj.html?from=health&subch=intl\n",
       "北京市人民政府办公厅关于贯彻国务院办公厅通知精神为新冠肺炎疫情牺牲烈士和逝世同胞举行全国性哀悼活动的通知\u00012020-04-03\u0001北京市政府网站\u0001来源：北京市人民政府办公厅   京政办发〔2020〕13号  各区人民政府 市政府各委、办、局 各市属机构：\u0001https://news.sina.com.cn/c/2020-04-03/doc-iimxyqwa4983508.shtml\n",
       "英国首相约翰逊持续出现新冠肺炎症状，将继续自我隔离。\u00012020-04-03\u0001新浪财经\u0001英国首相约翰逊持续出现新冠肺炎症状 将继续自我隔离 \u0001https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxyqwa4980693.shtml\n",
       "英首相约翰逊持续出现新冠肺炎症状 将继续自我隔离\u00012020-04-03\u0001海外网\u0001　　原标题：英国首相约翰逊持续出现新冠肺炎症状 将继续自我隔离   　　[海外网4月3日电|战疫全时区]英国首相约翰逊在个人推特上表示 他持续出现新冠肺炎症状 将继续自我隔离   \u0001https://news.sina.com.cn/w/2020-04-03/doc-iimxyqwa4981257.shtml\n",
       "钟南山院士和四国专家探讨新冠肺炎防控对策\u00012020-04-03\u0001民主与法制社\u0001那将变成全球问题 ”4月2日 中国工程院院士钟南山在“新冠疫情防控经验国际分享会暨健康中国国际公共卫生管理培训项目启动会”的网络直播中 面对美国专家坦言 美国每天都有1万余例检测出阳性的确诊患者 必须要开始采取更激烈的举措了 \u0001https://k.sina.com.cn/article_1831059072_6d23be8002000o306.html?from=society\n",
       "约翰斯·霍普金斯大学：中国以外新冠肺炎死亡病例超5万例\u00012020-04-03\u0001中国网直播\u0001  约翰斯·霍普金斯大学：中国以外新冠肺炎死亡病例超5万例  \u0001https://k.sina.com.cn/article_1884488621_m705303ad05300qn9t.html?from=health\n",
       "全球新冠肺炎确诊超100万例 中国以外累计死亡逾5万例\u00012020-04-03\u0001证券时报\u0001  证券时报e公司讯 据约翰斯·霍普金斯实时数据统计 截至北京时间3日19时20分 全球新冠肺炎确诊病例增至1026974例 逾100万例 累计死亡53975例 全球除中国以外累计死亡人数已经超过5万  (海外网)  \u0001https://k.sina.com.cn/article_1664176597_633151d502000ter2.html?from=health\n",
       "瑞士和列支敦士登新冠肺炎确诊病例达19303例 专家：尚未达到峰值\u00012020-04-03\u0001环球网\u0001【来源：央视新闻客户端】  截至当地时间4月2日 根据瑞士联邦公共卫生部最新数据 瑞士和列支敦士登共确诊新冠肺炎感染病例19303例 累计死亡484例 \u0001https://k.sina.com.cn/article_1686546714_6486a91a020011488.html?from=international\n",
       "墨西哥累计50人死于新冠肺炎 当局暂无计划关闭边境\u00012020-04-03\u0001环球网\u0001【来源：中国新闻网】  中新网4月3日电 据外媒报道 当地时间2日 墨西哥新增13例新冠肺炎死亡病例 累计50人死亡 墨西哥卫生部副部长拉米雷斯表示 该国目前没有关闭边境的计划    据报道\u0001https://k.sina.com.cn/article_1686546714_6486a91a020011489.html?from=international\n",
       "如果你们好奇新冠肺炎检测是什么样的……\u00012020-04-03\u0001东三环高圆圆\u0001  如果你们好奇新冠肺炎检测是什么样的……推上网友 PanamaRedin215录了自己做检测的视频供大家参考（看起来真的好痛苦??  \u0001https://k.sina.com.cn/article_1824962671_m6cc6b86f033016y29.html?from=health\n",
       "墨西哥累计50人死于新冠肺炎 当局暂无计划关闭边境\u00012020-04-03\u0001中国新闻网\u0001中新网4月3日电 据外媒报道 当地时间2日 墨西哥新增13例新冠肺炎死亡病例 累计50人死亡 墨西哥卫生部副部长拉米雷斯表示 该国目前没有关闭边境的计划   　　据报道\u0001https://mil.news.sina.com.cn/2020-04-03/doc-iimxxsth3540022.shtml\n",
       "最新！约翰斯·霍普金斯大学：中国以外新冠肺炎死亡病例超5万例\u00012020-04-03\u0001环球网\u0001截至北京时间4月3日下午6时02分 全球新冠肺炎累计确诊病例达1026974例 累计死亡病例达53975例   据中国卫健委4月3日最新通报 截至4月2日24时 据31个省（自治区、直辖市）和新疆生产建设兵团报告\u0001https://k.sina.com.cn/article_1686546714_6486a91a02001147k.html?from=news&subch=onews\n",
       "丹麦新冠肺炎死亡病例从123例增至139例。\u00012020-04-03\u0001新浪财经\u0001丹麦新冠肺炎死亡病例从123例增至139例 \u0001https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxyqwa4974068.shtml\n",
       "保加利亚两名国民议会议员新冠肺炎病毒测试呈阳性\u00012020-04-03\u0001界面新闻\u0001原标题：保加利亚两名国民议会议员新冠肺炎病毒测试呈阳性  当地时间4月3日 索非亚通讯社消息 4月2日\u0001https://tech.sina.com.cn/roll/2020-04-03/doc-iimxyqwa4976386.shtml\n",
       "挪威新冠肺炎确诊病例从4935例增至5208例，死亡44例。\u00012020-04-03\u0001新浪财经\u0001挪威新冠肺炎确诊病例从4935例增至5208例 死亡44例 \u0001https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxyqwa4973034.shtml\n",
       "从核酸检测到进入ICU，治疗新冠肺炎要花多少钱？谁承担？\u00012020-04-03\u0001新浪财经综合\u0001　　从核酸检测到进入ICU 治疗新冠肺炎要花多少钱？谁承担？   　　来源：中国经济周刊   　　《中国经济周刊》记者 陈惟杉 侯隽 | 北京报道   　　从核酸检测开始 治疗新冠肺炎到底要花多少钱？ \u0001https://finance.sina.com.cn/china/gncj/2020-04-03/doc-iimxyqwa4972669.shtml\n",
       "保加利亚两名国民议会议员新冠肺炎病毒测试呈阳性。（央视）\u00012020-04-03\u0001新浪财经\u0001保加利亚两名国民议会议员新冠肺炎病毒测试呈阳性 （央视）\u0001https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxyqwa4972227.shtml\n",
       "香港新增43例新冠肺炎确诊病例 累计报告845例\u00012020-04-03\u0001新华网\u0001累计报告845例  　　新华社香港4月3日电　香港特区政府卫生署3日介绍 截至3日16时\u0001https://news.sina.com.cn/o/2020-04-03/doc-iimxyqwa4972353.shtml\n",
       "约翰逊仍在发烧 称将自我隔离至新冠肺炎症状消失\u00012020-04-03\u0001中国新闻网\u0001中新网4月3日电 据英国天空电视台消息 4月3日 英国首相约翰逊透露 他将继续进行自我隔离 因为他仍有新冠肺炎患病轻微症状 他仍在发烧   　　据报道\u0001https://mil.news.sina.com.cn/2020-04-03/doc-iimxxsth3548690.shtml\n",
       "累计348例 台湾新增9例新冠肺炎确诊病例 7例境外输入\u00012020-04-03\u0001中国台湾网\u0001  台湾地区流行疫情指挥中心今天公布 台湾新增9例新冠肺炎确诊病例 其中7例境外输入、2例本地个案 台湾目前累计确诊348例   \u0001https://k.sina.com.cn/article_1709286740_m65e1a55403300nyz5.html?from=health\n",
       "中东地区新冠肺炎疫情继续蔓延 多国官员确诊！\u00012020-04-03\u0001一枚军粉\u0001 中东地区新冠肺炎疫情继续蔓延 多国官员确诊！伊朗议会公共关系部门当地时间2日晚间宣布 伊朗伊斯兰议会议长拉里贾尼新冠病毒检测结果为阳性 目前已在家中隔离并接受治疗\u0001https://k.sina.com.cn/article_6203200278_m171bd531603300qtt7.html?from=mil\n",
       "主持人: 美国航母上的新冠肺炎是哪来的？\u00012020-04-03\u0001电影院菌\u0001  主持人: 美国航母上的新冠肺炎是哪来的？那里可是不允许中国人登上去的！  \u0001https://k.sina.com.cn/article_6206068829_m171e9185d03300mtvm.html?from=mil\n",
       "因给新冠肺炎疑似患者提供咨询，印度多名医护遭约200民众扔石块\u00012020-04-03\u0001环球网\u0001【环球网报道】据美国有线电视新闻网（CNN）3日报道 印度中央邦近200民众4月1日向多名前线医护人员扔石块 因为后者正试图治疗一名疑似感染新冠肺炎的病人   报道称\u0001https://k.sina.com.cn/article_1686546714_6486a91a02001144z.html?from=international\n",
       "广东省人民政府办公厅转发国务院办公厅关于为新冠肺炎疫情牺牲烈士和逝世同胞举行全国性哀悼活动的通知\u00012020-04-03\u0001广东省政府网站\u0001来源：本网   各地级以上市人民政府 各县（市、区）人民政府 省政府各部门、各直属机构：\u0001https://news.sina.com.cn/c/2020-04-03/doc-iimxyqwa4976792.shtml\n",
       "西班牙新冠肺炎确诊病例达117710例 新增7472例\u00012020-04-03\u0001证券时报e公司\u0001原标题：西班牙新冠肺炎确诊病例达117710例 新增7472例  来源：央视新闻                                                           e公司讯 当地时间3日 据西班牙卫生部官网通报\u0001https://finance.sina.com.cn/roll/2020-04-03/doc-iimxxsth3524075.shtml\n",
       "摩洛哥新增27例新冠肺炎确诊病例和3例死亡病例\u00012020-04-03\u0001环球网\u0001【来源：央视新闻客户端】  摩洛哥卫生部当地时间4月3日8时证实 该国当天新增27例新冠肺炎确诊病例和3例死亡病例    截至目前 摩洛哥新冠肺炎确诊病例累计735例 累计死亡47人\u0001https://k.sina.com.cn/article_1686546714_6486a91a02001146i.html?from=international\n",
       "沙特政府将向境内私营企业部分员工支付工资以帮助企业应对新冠肺炎\u00012020-04-03\u0001环球网\u0001并积极寻求有助于为员工提供替代性收入的解决方案 减少新型冠状病毒肺炎疫情对本地劳动力市场和经济的负面影响    沙特财政大臣贾丹表示\u0001https://k.sina.com.cn/article_1686546714_6486a91a02001146f.html?from=news&subch=onews\n",
       "日本国内累计确诊新冠肺炎病例超过3000人 单日新增227例\u00012020-04-03\u0001海外网\u0001　　原标题：日本国内累计确诊新冠肺炎病例超过3000人 单日新增227例   　　 [海外网4月3日|战疫全时区] 据日本放送协会（NHK）3日报道 日本厚生劳动省和各地政府最新公布的数据显示\u0001https://news.sina.com.cn/w/2020-04-03/doc-iimxxsth3530977.shtml\n",
       "瑞士新冠肺炎确诊人数增加至19303人，死亡人数增加至484人。\u00012020-04-03\u0001新浪财经\u0001瑞士新冠肺炎确诊人数增加至19303人 死亡人数增加至484人 \u0001https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3530957.shtml\n",
       "日本国内累计确诊新冠肺炎病例超过3000人，单日新增227例\u00012020-04-03\u0001界面\u0001据日本放送协会（NHK）3日报道 日本厚生劳动省和各地政府最新公布的数据显示 截至当地时间3日晚上19时 日本各都道府县和机场检疫机构3日共测出227例新增新冠肺炎病例\u0001https://k.sina.com.cn/article_6192937794_17120bb42020018ns7.html?from=news&subch=onews\n",
       "黎巴嫩新冠肺炎确诊总人数上升至508人\u00012020-04-03\u0001环球网\u0001【来源：央视新闻客户端】  黎巴嫩卫生部官网公布 截至当地时间3日中午黎巴嫩新冠肺炎确诊总人数为508人 较昨日增加14人    根据卫生部所公布 过去24小时内有3名患者被治愈 治愈总人数已达46人\u0001https://k.sina.com.cn/article_1686546714_6486a91a020011467.html?from=international\n",
       "伊朗新增新冠肺炎确诊病例2715例 累计53183例\u00012020-04-03\u0001证券时报e公司\u0001原标题：伊朗新增新冠肺炎确诊病例2715例 累计53183例  来源：人民日报                                                           e公司讯 伊朗卫生部4月3日宣布 过去24小时\u0001https://finance.sina.com.cn/roll/2020-04-03/doc-iimxyqwa4962125.shtml\n",
       "荷兰新增1026例新冠肺炎确诊病例 累计15723例\u00012020-04-03\u0001海外网\u0001　　原标题：荷兰新增1026例新冠肺炎确诊病例 累计15723例   　　[海外网4月3日|战疫全时区]据荷兰卫生部官网最新数据 过去24小时 该国新增1026例新冠肺炎确诊病例\u0001https://news.sina.com.cn/w/2020-04-03/doc-iimxyqwa4985415.shtml\n",
       "新开发银行发行债券支持中国抗击新冠肺炎疫情\u00012020-04-03\u0001新华网\u0001原标题：新开发银行发行债券支持中国抗击新冠肺炎疫情 \u0001https://finance.sina.com.cn/roll/2020-04-03/doc-iimxxsth3545222.shtml\n",
       "荷兰新冠肺炎确诊病例新增1026例至15723例。\u00012020-04-03\u0001新浪财经\u0001荷兰新冠肺炎确诊病例新增1026例至15723例 \u0001https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3545093.shtml\n",
       "【防疫科普】新冠肺炎治愈后，如何进行康复锻炼？\u00012020-04-03\u0001界面新闻\u0001 原标题：【防疫科普】新冠肺炎治愈后 如何进行康复锻炼？  来源：光明网       【防疫科普】新冠肺炎治愈后 如何进行康复锻炼？ \u0001https://tech.sina.com.cn/roll/2020-04-03/doc-iimxxsth3533255.shtml\n",
       "据日本放送协会NHK报道，日本境内新冠肺炎确诊连续第4天新增超过200人，...\u00012020-04-03\u0001新浪财经\u0001据日本放送协会NHK报道 日本境内新冠肺炎确诊连续第4天新增超过200人 目前累计3003例 \u0001https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3531886.shtml\n",
       "比利时新增1422例新冠肺炎确诊病例，累计16770例\u00012020-04-03\u0001澎湃新闻\u0001央视新闻4月3日消息 当地时间3日上午 据比利时卫生部门官方通报 在过去24小时内比利时新增新冠肺炎确诊病例1422例 累计确诊16770例 死亡病例新增132例 累计1143例  \u0001https://mil.news.sina.com.cn/2020-04-03/doc-iimxyqwa4969806.shtml\n",
       "摩洛哥新增27例新冠肺炎确诊病例和3例死亡病例\u00012020-04-03\u0001环球网\u0001【来源：央视新闻客户端】  摩洛哥卫生部当地时间4月3日8时证实 该国当天新增27例新冠肺炎确诊病例和3例死亡病例    截至目前 摩洛哥新冠肺炎确诊病例累计735例 累计死亡47人\u0001https://k.sina.com.cn/article_1686546714_6486a91a02001146i.html?from=international\n",
       "瑞士新增1036例新冠肺炎确诊病例 累计19303例\u00012020-04-03\u0001海外网\u0001　　原标题：瑞士新增1036例新冠肺炎确诊病例 累计19303例   　　[海外网4月3日|战疫全时区]据瑞士卫生部最新数据 截至当地时间3日上午8时 该国新增1036例新冠肺炎确诊病例\u0001https://news.sina.com.cn/w/2020-04-03/doc-iimxyqwa4968770.shtml\n",
       "西班牙新增7472例新冠肺炎确诊病例 累计确诊人数超过意大利\u00012020-04-03\u0001中国网直播\u0001  据西班牙卫生部官网通报 过去24小时 该国新增7472例新冠肺炎确诊病例 累计确诊117710例 累计确诊人数超过意大利；新增死亡932例 累计死亡10935例   \u0001https://k.sina.com.cn/article_1884488621_m705303ad03300qn85.html?from=health\n",
       "日本国内累计确诊新冠肺炎2989例 连续4天单日新增超200人\u00012020-04-03\u0001环球网\u0001日本厚生劳动省和各地政府最新公布的数据显示 截至当地时间3日晚上18时30分 日本各都道府县和机场检疫机构3日共测出213例新增新冠肺炎病例 这也是日本国内连续四天单日新增确诊病例超过200人  \u0001https://k.sina.com.cn/article_1686546714_6486a91a02001145x.html?from=international\n",
       "《新闻第一线》4月3日安徽省报告新冠肺炎疫情情况\u00012020-04-03\u0001安徽卫视\u0001\u0001https://k.sina.com.cn/article_1782599645_m6a404fdd03900wusu.html?from=news\n",
       "国家医保局专题研究新冠肺炎患者医保费用结算工作：各地医保部门要继续认真贯彻...\u00012020-04-03\u0001新浪财经\u0001切实抓紧抓实抓细医保费用结算 主动与相关部门沟通对接\u0001https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3528337.shtml\n",
       "国家医保局专题研究新冠肺炎患者医保费用结算工作\u00012020-04-03\u0001界面\u0001国家医保局专题研究新冠肺炎患者医保费用结算工作  国家医保局专题研究新冠肺炎患者医保费用结算工作 各地医保部门要继续认真贯彻党中央、国务院决策部署\u0001https://k.sina.com.cn/article_6192937794_17120bb42020018nrb.html?from=news&subch=onews\n",
       "沙特政府将向境内私营企业部分员工支付工资以帮助企业应对新冠肺炎\u00012020-04-03\u0001新浪财经\u0001沙特国王萨勒曼当地时间3日上午发布国王令 责成政府相关部门从4月起通过失业保险基金向沙特境内私营企业中部分沙特员工支付其原工资的60％ 该措施为期三个月\u0001https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3527917.shtml\n",
       "拉脱维亚报告首例新冠肺炎死亡病例\u00012020-04-03\u0001潇湘晨报\u0001新华社里加4月3日电 据拉脱维亚电视台报道 拉脱维亚3日报告首例新冠肺炎死亡病例 另据拉脱维亚疾控中心3日公布的最新疫情数据 该国累计确诊病例增至493例 单日增长35例 \u0001https://k.sina.com.cn/article_1655444627_62ac14930200146f3.html?from=local\n"
      ]
     },
    "source": [
     "import logging#每隔一段时间刷新，用来记录日志\n",
     "import requests\n",
     "import sys\n",
     "import urllib\n",
     "import collections\n",
     "\n",
     "from bs4 import BeautifulSoup\n",
     "from collections import OrderedDict\n",
     "from urllib.parse import urlencode\n",
     "\n",
     "def get_list(comp, page):\n",
     "    \"\"\"Function to get  web list pages for a given company and page number.\n",
     "\n",
     "    Args:\n",
     "        comp: Company name.\n",
     "        page: The page number.\n",
     "\n",
     "    Returns:\n",
     "        newsData: A dictionary with news title as its key and other details as values.\n",
     "\n",
     "    \"\"\"#三个双引号，是对这个函数的说明，用help get_list就可以得到\n",
     "    newsData = OrderedDict()\n",
     "    href = 'http://search.sina.com.cn/?%s&range=title&c=news&num=20&col=1_7&page=%s' % (comp, page) # comp -> first %s; page -> 2nd %s; col=1_7 -> financial news in sina\n",
     "    #用%s标记出来\n",
     "    html = requests.get(href)\n",
     "    # Parsing html\n",
     "    soup = BeautifulSoup(html.content, 'html.parser')\n",
     "    divs = soup.findAll('div', {\"class\": \"r-info r-info2\"})\n",
     "    for div in divs:\n",
     "        head = div.findAll('h2')[0]\n",
     "        # News title\n",
     "        titleinfo = head.find('a')\n",
     "        title = titleinfo.get_text()\n",
     "        # News url\n",
     "        url = titleinfo['href']\n",
     "        # Other info\n",
     "        otherinfo = head.find('span', {\"class\": \"fgray_time\"}).get_text()\n",
     "        source, date, time = otherinfo.split()\n",
     "        # News abstract\n",
     "        abstract = div.find('p', {\"class\": \"content\"}).get_text()\n",
     "        newsData[title] = [date, source, abstract, url]\n",
     "    return newsData\n",
     "\n",
     "\n",
     "\n",
     "if __name__ == \"__main__\":\n",
     "    compRawStr = '新冠肺炎'\n",
     "    # Dealing with character encoding\n",
     "    comp = compRawStr.encode('gbk')\n",
     "    d = {'q': comp}\n",
     "    pname = urlencode(d)\n",
     "    # Scraping and printing the first two pages\n",
     "    fileObject = open('Corvir', 'w') \n",
     "    for page in range(13)[2:]:\n",
     "        newsData = get_list(pname, page)\n",
     "        \n",
     "        for ky in newsData:\n",
     "            a = str('\\001'.join([ky] + newsData[ky]))# \"\\001\" as separator\n",
     "            print(a)\n",
     "            fileObject.write(a)  \n",
     "            fileObject.write('\\n') \n",
     "    fileObject.close()  "
    ]
   },
   {
    "cell_type": "code",
    "execution_count": 106,
    "metadata": {},
    "outputs": [
     {
      "name": "stderr",
      "output_type": "stream",
      "text": [
       "INFO:root:Scraping https://mil.news.sina.com.cn/2020-04-03/doc-iimxxsth3548690.shtml\n",
       "INFO:root:Scraping https://news.sina.com.cn/w/2020-04-03/doc-iimxyqwa4985415.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/roll/2020-04-03/doc-iimxxsth3545222.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3545093.shtml\n",
       "INFO:root:Scraping https://news.sina.com.cn/w/2020-04-03/doc-iimxxsth3544230.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1884488621_m705303ad03300qnaa.html?from=news&subch=onews\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxyqwa4981913.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_3703570897_mdcc001d100101t0aj.html?from=health&subch=intl\n",
       "INFO:root:Scraping https://news.sina.com.cn/c/2020-04-03/doc-iimxyqwa4983508.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxyqwa4980693.shtml\n",
       "INFO:root:Scraping https://news.sina.com.cn/w/2020-04-03/doc-iimxyqwa4981257.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1831059072_6d23be8002000o306.html?from=society\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1884488621_m705303ad05300qn9t.html?from=health\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1664176597_633151d502000ter2.html?from=health\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a020011488.html?from=international\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a020011489.html?from=international\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1824962671_m6cc6b86f033016y29.html?from=health\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a02001147k.html?from=news&subch=onews\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxyqwa4974068.shtml\n",
       "INFO:root:Scraping https://tech.sina.com.cn/roll/2020-04-03/doc-iimxyqwa4976386.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxyqwa4973034.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/china/gncj/2020-04-03/doc-iimxyqwa4972669.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxyqwa4972227.shtml\n",
       "INFO:root:Scraping https://news.sina.com.cn/o/2020-04-03/doc-iimxyqwa4972353.shtml\n",
       "INFO:root:Scraping https://news.sina.com.cn/c/2020-04-03/doc-iimxyqwa4971629.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_6424076363_m17ee7a04b03300uvv7.html?from=health\n",
       "INFO:root:Scraping https://tech.sina.com.cn/roll/2020-04-03/doc-iimxxsth3533255.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3531886.shtml\n",
       "INFO:root:Scraping https://mil.news.sina.com.cn/2020-04-03/doc-iimxyqwa4969806.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a02001146i.html?from=international\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a02001146i.html?from=international\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a02001146f.html?from=news&subch=onews\n",
       "INFO:root:Scraping https://news.sina.com.cn/w/2020-04-03/doc-iimxxsth3530977.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3530957.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_6192937794_17120bb42020018ns7.html?from=news&subch=onews\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a020011467.html?from=international\n",
       "INFO:root:Scraping https://news.sina.com.cn/w/2020-04-03/doc-iimxyqwa4968770.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1884488621_m705303ad03300qn85.html?from=health\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a02001145x.html?from=international\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1782599645_m6a404fdd03900wusu.html?from=news\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3528337.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_6192937794_17120bb42020018nrb.html?from=news&subch=onews\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3527917.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1655444627_62ac14930200146f3.html?from=local\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1655444627_62ac14930200146f3.html?from=local\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_5787187353_158f1789902000zcz0.html?from=health\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1884488621_m705303ad05300qn7y.html?from=health\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1730243272_m67216ac803300safp.html?from=health\n",
       "INFO:root:Scraping https://news.sina.com.cn/w/2020-04-03/doc-iimxyqwa4966319.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a02001145e.html?from=international\n",
       "INFO:root:Scraping https://mil.news.sina.com.cn/2020-04-03/doc-iimxxsth3526637.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3524636.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1709286740_m65e1a55403300nyz5.html?from=health\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_6203200278_m171bd531603300qtt7.html?from=mil\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_6206068829_m171e9185d03300mtvm.html?from=mil\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a02001144z.html?from=international\n",
       "INFO:root:Scraping https://news.sina.com.cn/c/2020-04-03/doc-iimxyqwa4976792.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/roll/2020-04-03/doc-iimxxsth3524075.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/roll/2020-04-03/doc-iimxyqwa4962125.shtml\n",
       "INFO:root:Scraping https://news.sina.com.cn/w/2020-04-03/doc-iimxxsth3524053.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_2553604372_9834e91402000r3it.html?from=health\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_2316271560_m8a0f7fc803300qo08.html?from=news&subch=onews\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_1686546714_6486a91a02001144n.html?from=international\n",
       "INFO:root:Scraping https://finance.sina.com.cn/stock/relnews/us/2020-04-03/doc-iimxxsth3524095.shtml\n",
       "INFO:root:Scraping https://finance.sina.com.cn/7x24/2020-04-03/doc-iimxxsth3522298.shtml\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_5720842545_m154fd2131033018mip.html?from=health\n",
       "INFO:root:Scraping https://k.sina.com.cn/article_6206068829_m171e9185d05300mtvc.html?from=mil\n"
      ]
     }
    ],
    "source": [
     "import logging\n",
     "import requests\n",
     "import sys\n",
     "from bs4 import BeautifulSoup\n",
     "\n",
     "\n",
     "def get_body(href):\n",
     "    \"\"\"Function to retrieve news content given its url.\n",
     "\n",
     "    Args:\n",
     "        href: url of the news to be crawled.\n",
     "\n",
     "    Returns:\n",
     "        content: the crawled news content.\n",
     "\n",
     "    \"\"\"\n",
     "    html = requests.get(href)\n",
     "    soup = BeautifulSoup(html.content, 'html.parser')\n",
     "    div = soup.find('div', {\"class\": \"article\"})\n",
     "    paras = div.findAll('p')\n",
     "    content = ''\n",
     "    for p in paras:\n",
     "        ptext = p.get_text().strip().replace(\"\\n\", \"\")\n",
     "        content += ptext\n",
     "    return content\n",
     "\n",
     "\n",
     "\n",
     "if __name__ == \"__main__\":\n",
     "    logging.getLogger().setLevel(logging.INFO)\n",
     "    # Getting and printing content for each url in the crawled web list pages\n",
     "    fileObject = open('Coronavirus_data', 'w') \n",
     "    with open(\"Corvir\") as f:\n",
     "        \n",
     "        for line in f:\n",
     "            title, date, source, abstract, href = line.strip().split('\\001')\n",
     "            # Printing progress onto console\n",
     "            logging.info('Scraping ' + href)\n",
     "            content = get_body(href)\n",
     "            content = str('\\001'.join([title, date, source, abstract, href, content]))\n",
     "            fileObject.write(content)  \n",
     "            fileObject.write('\\n') \n",
     "    fileObject.close()  "
    ]
   }
  ],
  "metadata": {
   "kernelspec": {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
   },
   "language_info": {
    "codemirror_mode": {
     "name": "ipython",
     "version": 3
    },
    "file_extension": ".py",
    "mimetype": "text/x-python",
    "name": "python",
    "nbconvert_exporter": "python",
    "pygments_lexer": "ipython3",
    "version": "3.7.4"
   }
  },
  "nbformat": 4,
  "nbformat_minor": 2
 }