import jieba

word='我来到北京清华大学门口送外卖'
w1=jieba.cut(word, cut_all=False)
print("精确模式:" + " ".join(w1))
w2=jieba.cut(word, cut_all=True)
print("全匹配:" + " ".join(w2))
w3=jieba.cut_for_search(word)
print("搜索引擎:" + " ".join(w3))
w4=jieba.cut(word, use_paddle=True)
print("paddle:" + " ".join(w4))
