from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
from os import path
import jieba


def wordcloud_generate(word_file, cloud_pic, userdict, load_to, restrict_word):
    jieba.load_userdict(path.join(path.dirname(__file__), userdict))  # 导入用户自定义词典
    ###当前文件路径
    d = path.dirname(__file__)

    # Read the whole text.
    file = open(path.join(d, word_file)).read()
    ##进行分词
    # 刚开始是分完词放进txt再打开却总是显示不出中文很奇怪
    default_mode = jieba.cut(file, cut_all=False)
    data = []
    for word in default_mode:
        data.append(word)
    dataDict = Counter(data)
    with open('doc/词频统计.txt', 'w') as fw:
        for k, v in dataDict.items():
            if v != 1 and k is not restrict_word:
                fw.write("%s,%d\n" % (k, v))

    default_mode = jieba.cut(file, cut_all=False)
    jieba_dic = ""
    for word in default_mode:
        if word not in restrict_word:
            jieba_dic += word + " "

    text = " ".join(jieba_dic)
    alice_mask = np.array(Image.open(path.join(d, cloud_pic)))
    # alice_mask = plt.imread(cloud_pic)
    stopwords = set(STOPWORDS)
    stopwords.add("said")
    wc = WordCloud(
        # 设置字体，不指定就会出现乱码,这个字体文件需要下载
        font_path=r'/Users/mac/PycharmProjects/demoWorldcloud/plotWordcloud/font/msyh.ttf',
        background_color="white",
        max_words=1000,
        mask=alice_mask,
        stopwords=stopwords,
        random_state=30,
        max_font_size=150
    )
    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, load_to))

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    # 图片高质量处理
    img = Image.open(path.join(d, load_to))

    img_suffix = img_path[-3:]

    changed_img_name = img_path





# def generate_wordcloud(text):
#     '''
#     输入文本生成词云,如果是中文文本需要先进行分词处理
#     '''
#     # 设置显示方式
#     d=path.dirname(__file__)
#     # alice_mask = np.array(Image.open(path.join(d, "Images//alice_mask.png")))
#     font_path=path.join(d,"font//msyh.ttf")
#     stopwords = set(STOPWORDS)
#     wc = WordCloud(background_color="white",# 设置背景颜色
#            max_words=2000, # 词云显示的最大词数
#            # mask=alice_mask,# 设置背景图片
#            stopwords=stopwords, # 设置停用词
#            font_path=font_path, # 兼容中文字体，不然中文会显示乱码
#             max_font_size=50,
#             min_font_size=50,
#             mode = 'RGBA'
#                   )
#
#     # 生成词云
#     wc.generate(text)
#
#     # 生成的词云图像保存到本地
#     wc.to_file(path.join(d, "Images/alice.png"))
#
#     # 显示图像
#     plt.imshow(wc, interpolation='bilinear')
#     # interpolation='bilinear' 表示插值方法为双线性插值
#     plt.axis("off")# 关掉图像的坐标
#     plt.show()
