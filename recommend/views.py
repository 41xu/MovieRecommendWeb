from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import numpy as np
import pandas as pd
from numpy import linalg as la
import random
from django.views.decorators.csrf import csrf_exempt
from .models import Movies

# 读入数据的存储方式为行表示用户列表示电影值表示用户评分
# 由于用户数大于电影数，因此我们选择基于电影的相似度做推荐

data = pd.read_csv("data.csv")
user_score = data[['user_id', 'user_score', 'id']]
movies = set()
users = set()
user_index = {}
movie_index = {}
movie_reindex = {}
user_reindex = {}
global usernum
global movienum


# 计算相似度
def cosSim(inA, inB):  # inA inB两个列向量
    num = float(inA.T * inB)
    denom = la.norm(inA) * la.norm(inB)  # linalg.norm()计算范数
    return 0.5 + 0.5 * (num / denom)


def SVD(dataMat):  # 压缩矩阵dataMat
    dataMat = np.mat(dataMat)
    U, Sigma, VT = la.svd(dataMat)
    Sig4 = np.mat(np.eye(4) * Sigma[:4])
    # print(dataMat.T.shape,U[:,:4].shape,Sig4.I.shape)
    xformedItems = dataMat.T * U[:, :4] * Sig4.I
    return xformedItems


def preprocess():
    global usernum
    global movienum
    s = user_score['user_id'].value_counts()[:1000]
    usernum = len(s)
    users = s.index
    nu = 0
    for x in users:
        user_reindex[nu] = x
        user_index[x] = nu
        nu += 1

    m = user_score['id'].value_counts()[:]
    movies = m.index
    movienum = len(movies)
    nm = 0
    for x in movies:
        movie_index[x] = nm
        movie_reindex[nm] = x
        nm += 1
    mat = np.zeros((usernum, movienum))
    for i in range(len(data)):
        cu = data.loc[i, 'user_id']
        cm = data.loc[i, 'id']
        if cu in users:
            if cm in movies:
                mat[user_index[cu], movie_index[cm]] = data.loc[i, 'user_score']
    return mat


def get_sim(xformedItems):
    global usernum  # 1000
    global movienum  #
    SIM = np.zeros((movienum, movienum))
    for i in range(movienum):
        for j in range(movienum):
            SIM[i][j] = cosSim(xformedItems[i, :].T, xformedItems[j, :].T)
    return SIM


def svdEst(dataMat, user, simMeas, item):
    n = np.shape(dataMat)[1]
    simTotal = 0.0;
    ratSimTotal = 0.0
    U, Sigma, VT = la.svd(dataMat)
    Sig4 = np.mat(np.eye(4) * Sigma[:4])
    xformedItems = dataMat.T * U[:, :4] * Sig4.I
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0 or j == item: continue
        similarity = simMeas(xformedItems[item, :].T, xformedItems[j, :].T)
        # print("the %d and %d similarity is: %f"%(item,j,similarity))
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal / simTotal


def recommend(SIM, dataMat, user, simMeas=cosSim, estMethod=svdEst):
    dataMat = np.mat(dataMat)
    unratedItems = np.nonzero(dataMat[user, :] == 0)[1]
    itemScores = []
    for item in unratedItems:
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        itemScores.append((item, estimatedScore))
    return sorted(itemScores, key=lambda x: x[1], reverse=True)


def recommend_movie():
    dataMat = preprocess()
    xformedItems = SVD(dataMat)
    print("SVD has been done.")
    SIM = get_sim()
    print("SIM matrix has been done.")
    pointed_user = random.randint(0, usernum - 1)
    print(user_reindex[pointed_user])
    REC = recommend(SIM, dataMat, pointed_user)
    result = []
    for i in range(0, 5):
        result.append(movie_reindex[REC[i][0]])
    print(result)  # 这里的result就已经是推荐电影的结果 输出的是电影的ID
    # 打印电影信息让你具体了解一下！
    result = iter(result)
    info = []
    cur = next(result)
    while len(info) < 5:
        for i in range(len(data)):
            if data.loc[i, 'id'] == cur:
                info.append(data.loc[i, ['id', 'title', 'year', 'director', 'writer', 'actor', 'type',
                                         'country', 'language', 'length', 'score']])
                try:
                    cur = next(result)
                except:
                    break
                break
    print(info)


def search_form(request):
    return render_to_response('recommend.html')


@csrf_exempt
def search(request):
    if request.method == "POST":

        dataMat = preprocess()
        xformedItems = SVD(dataMat)
        SIM = get_sim(xformedItems)
        user_id = int(request.POST.get('user_id'))
        # message="你搜索的内容为："+request.GET['user_id']
        # point_user=int(request.GET['user_id'])
        # message+="\n经过查询之后这个id对应的用户名称是："+user_reindex[point_user]
        # message+="\n"
        user_name=user_reindex[user_id]
        REC = recommend(SIM, dataMat, user_id)
        result = []
        for i in range(0, 5):
            result.append(movie_reindex[REC[i][0]])  # result中是推荐的电影id
        movie_dic=[]

        for i in range(5):
            movie = Movies.objects.get(id=result[i])
            movie_dic.append(
                {"id":movie.id,
                 "title":movie.title,
                 "type":movie.type,
                 "year":movie.year,
                 "director":movie.director,
                 "actor":movie.actor,
                 "writer":movie.writer,
                 "country":movie.country,
                 "language":movie.language,
                 "length":movie.length,
                 "score":movie.score


                 }
            )


        return render_to_response("recommend.html",{"flag":True,"movie_dic":movie_dic,"userid":user_id ,"username":user_name})
    return render_to_response("recommend.html", {
        "id": ['null']
    })

    #     result = iter(result)
    #     info = []
    #     cur = next(result)
    #     while len(info) < 5:
    #         for i in range(len(data)):
    #             if data.loc[i, 'id'] == cur:
    #                 info.append(data.loc[i, ['id', 'title', 'year', 'director', 'writer', 'actor', 'type',
    #                                          'country', 'language', 'length', 'score']])
    #                 try:
    #                     cur = next(result)
    #                 except:
    #                     break
    #                 break
    #     message+="以下是为您推荐的电影！"
    #     message+=str(info)
    #
    # else:
    #     message="你提交了空表单"
    # return HttpResponse(message)
