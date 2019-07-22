import csv
from numpy import *
from PIL import Image
from scipy.spatial.distance import pdist

def loadimage(fname):
    fp = open(fname, "rb")
    ImageSet=[]
    im = Image.open(fp)
    m,n = im.size
    for i in range(m):
        for j in range(n):
            tmp = []
            x, y, z = im.getpixel((i, j))
            tmp.append(x / 256.0)
            tmp.append(y / 256.0)
            tmp.append(z / 256.0)
            ImageSet.append(tmp)
    fp.close()
    return ImageSet,m,n

def pearson_distance(vector1, vector2):
    X = vstack([vector1, vector2])
    d2 = pdist(X)
    return d2

distances_cache = {}

def totalcost(dataset, medoids_idx):
    size = len(dataset)
    total_cost = 0.0
    medoids = {}
    
    for idx in medoids_idx:
        medoids[idx] = []
    for i in range(size):
        choice = None
        min_cost = inf
        for m in medoids:
            tmp = distances_cache.get((m, i), None)
            if tmp is None:
                tmp = pearson_distance(dataset[m], dataset[i])
                distances_cache[(m, i)] = tmp
            if tmp < min_cost:
                choice = m
                min_cost = tmp
        medoids[choice].append(i)
        total_cost += min_cost
    #print(distances_cache)
    return total_cost, medoids

def kmedoids(dataset, k):
    size = len(dataset)
    medoids_idx = random.choice(size,k,replace=False)
    medoids_idx = medoids_idx.tolist()
    print(medoids_idx)
    pre_cost, medoids = totalcost(dataset, medoids_idx)
    print(pre_cost)
    
    current_cost = inf
    best_medoids_idx = []
    best_medoids = {}
    iter_count = 0
    int_y=0
    while 1:
        int_y+=1
        print(int_y)
        if(int_y==10):
            break
        for m in medoids:
            for item in medoids[m]:
                if item != m:
                    idx = medoids_idx.index(m)
                    swap_temp = medoids_idx[idx]
                    medoids_idx[idx] = item
                    tmp, medoids_ = totalcost(dataset, medoids_idx)
                    if tmp < current_cost:
                        best_medoids_idx = list(medoids_idx)
                        best_medoids = dict(medoids_)
                        current_cost = tmp
                    medoids_idx[idx] = swap_temp
        iter_count += 1
        #print(current_cost)
        #print(iter_count)
        if best_medoids_idx == medoids_idx: break
        if current_cost <= pre_cost:
            pre_cost = current_cost
            medoids = best_medoids
            medoids_idx = best_medoids_idx

    return current_cost, best_medoids_idx, best_medoids


def LLamar():

    ImageSet,m,n=loadimage(r"Entrada/cerebro1_32.jpg")
    best_cost, best_medoids_idx, best_medoids=kmedoids(ImageSet,4)
    print(best_cost)
    print(best_medoids_idx)
    print(best_medoids)
    medoids_new={}
    for m1 in best_medoids_idx:
        medoids_new[m1]=[]
        for y in range(len(ImageSet[m1])):
            temp=int(ImageSet[m1][y]*256)
            medoids_new[m1].append(temp)

    pic_new = Image.new("RGB", (m, n)) 
    for m2 in best_medoids:
            for item in best_medoids[m2]:
                pic_new.putpixel((int(item/n),int(item%n)),tuple((medoids_new[m2])))

    pic_new.save("Kmedios.jpg","JPEG")
    


