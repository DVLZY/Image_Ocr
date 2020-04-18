from aip import AipOcr
'''
百度的API库
安装：pip install baidu-aip
文档：https://ai.baidu.com/ai-doc/OCR/Ek3h7yeiq
'''
# 配置信息
config={
    'appId':'19491494',
    'apiKey':'GBw20bEOyabIk8mACGClMIuq',
    'secretKey':'SusejTuIxyhuM3CWU1sUTMH2K4GioiVx'
}
client = AipOcr(**config)

# 获取图像内容
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别文字
def img_to_str(image_path):
    '''
    识别图片中的文字
    :param image_path: 文件路径
    :return: 文字识别结果
    '''
    image=get_file_content(image_path) # 载入图片
    result=client.handwriting(image) # 手写文字识别
    # result=client.basicGeneral(image) # 通用文字识别
    # result=client.basicGeneralUrl("https//www.x.com/sample.jpg") # 网络图片文字识别 jpg/png/bmp
    print(result)
    print()
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])

if __name__ == '__main__'
    res = img_to_str(r'D:\Desktop\Snipaste_2020-04-18_21-49-06.png')
    print(res)