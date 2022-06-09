from lxml import etree
import re

'''模板
丁丁消息内容：
接口自动化结果：
服务名称，共XX个接口，其中：
成功：XX个，失败：XX个
失败的详细内容请看测试报告：URL地址
'''
def readhtml(path,url,name0):
    html = etree.parse(path, etree.HTMLParser(encoding='utf-8'))
    total1 = re.findall("\d+",html.xpath('/html/body/p[2]/text()')[0])[0]
    passed2 =  re.findall("\d+",html.xpath("//span[@class='passed']/text()")[0])[0]
    failed3 =  re.findall("\d+",html.xpath("//span[@class='failed']/text()")[0])[0]
    skipped4 = re.findall("\d+",html.xpath("//span[@class='skipped']/text()")[0])[0]
    error5 = re.findall("\d+",html.xpath("//span[@class='error']/text()")[0])[0]
    middle_pass6 = 0
    middle_failed7 = 0
    middle_error8 = 0
    xby_pass9 = 0
    xby_failed10 = 0
    xby_error11 = 0
    dk_pass12 = 0
    dk_failed13 = 0
    dk_error14 = 0
    xxl_pass15 = 0
    xxl_failed16 = 0
    xxl_error17 = 0
    gxpt_pass18 = 0
    gxpt_failed19 = 0
    gxpt_error20 = 0

    for i in range(int(total1)):
        xpath_case = '//*[@id="results-table"]/tbody[%d]/tr[1]/td[2]/text()'%(i+1)
        caselist = re.search("case/(test.*?)/test",html.xpath(xpath_case)[0], re.I | re.M).group(1)
        xpath_result = '//*[@id="results-table"]/tbody[%d]/tr[1]/td[1]/text()' % (i + 1)
        resultList = html.xpath(xpath_result)[0]
        if caselist == "test_dake":
            if resultList == "Passed":
                dk_pass12 += 1
            elif resultList == "Failed":
                dk_failed13 += 1
            elif resultList == "Error":
                dk_error14 += 1
        elif caselist == "test_xiaobaiying":
            if resultList == "Passed":
                xby_pass9 += 1
            elif resultList == "Failed":
                xby_failed10 += 1
            elif resultList == "Error":
                xby_error11 += 1
        elif caselist == "test_middle_center":
            if resultList == "Passed":
                middle_pass6 += 1
            elif resultList == "Failed":
                middle_failed7 += 1
            elif resultList == "Error":
                middle_error8 += 1
        elif caselist == "test_traffic_dashboard":
            if resultList == "Passed":
                xxl_pass15 += 1
            elif resultList == "Failed":
                xxl_failed16 += 1
            elif resultList == "Error":
                xxl_error17 += 1
        elif caselist == "test_sharing_platform" or caselist == "test_dushuhui":
            if resultList == "Passed":
                gxpt_pass18 += 1
            elif resultList == "Failed":
                gxpt_failed19 += 1
            elif resultList == "Error":
                gxpt_error20 += 1

    reportURL = url
    messageDing = '共{1}个接口，其中：\n' \
                  '成功：{2}个，失败：{3}个\n' \
                  '跳过:{4}个，错误:{5}个\n'\
                  '----------------------------------------\n'\
                  '中 台：\n' \
                  '成功：{6}个，失败：{7}个，错误:{8}个\n'\
                  '小白营：\n' \
                  '成功：{9}个，失败：{10}个，错误:{11}个\n'\
                  '大 课：\n' \
                  '成功：{12}个，失败：{13}个，错误:{14}个\n' \
                  '信息流：\n' \
                  '成功：{15}个，失败：{16}个，错误:{17}个\n' \
                  '共享平台：\n' \
                  '成功：{18}个，失败：{19}个，错误:{20}个\n' \
                  '详细报告：{21} '.format(name0, total1, passed2, failed3,skipped4,error5,
                                      middle_pass6,middle_failed7,middle_error8,
                                      xby_pass9,xby_failed10,xby_error11,
                                      dk_pass12,dk_failed13,dk_error14,
                                      xxl_pass15,xxl_failed16,xxl_error17,
                                      gxpt_pass18,gxpt_failed19,gxpt_error20,reportURL)

    return messageDing
