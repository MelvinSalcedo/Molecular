from UI_molecular import *
import numpy as np
from matplotlib import pyplot as plt
import cv2
import time
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from kmedoids_image import *
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import pairwise_distances

class Clustering():
    def __init__(self, img, image):
        self.img = img
        self.image = image
        
    def K_Means(self):
        km = KMeans(n_clusters=4,max_iter=300)
        km.fit(self.image)
        centers = km.cluster_centers_
        point_distances = cdist(centers, self.image, 'euclidean')
        cluster_indexes = np.argmin(point_distances, axis=0)
        segmented = centers[cluster_indexes]
        segmented_image = segmented.reshape(self.img.shape).astype(np.uint8)
        return segmented_image
    def DB_SCAN(self):
        db = DBSCAN(eps=255*0.01, min_samples=20, metric='euclidean')
        db.fit(self.image)
        number_of_clusters = np.max(db.labels_) + 1
        centers = np.zeros((number_of_clusters, 3))
        for i in range(0, number_of_clusters):
            cluster_points = self.image[db.labels_ == i]
            cluster_mean = np.mean(cluster_points, axis=0)
            centers[i, :] = cluster_mean
        point_distances = cdist(centers, self.image, 'euclidean')
        cluster_indexes = np.argmin(point_distances, axis=0)
        segmented = centers[cluster_indexes]
        segmented_image = segmented.reshape(self.img.shape).astype(np.uint8)
        return segmented_image
    
    def K_MEDOIDS(self):
        LLamar()
        
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):       
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)  
        self.ImagenEntrada.setText("Haz clic en el botón")
        #self.OpenImage.setText("Presióname")
        
        self.OpenImage.clicked.connect(self.OpemImage)
        
        self.Qmeans.clicked.connect(self.Kmeans)
        self.DbScan.clicked.connect(self.DBscan)
        self.Qmedois.clicked.connect(self.Kmedoids)    
        self.path="Entrada/cerebro3.jpg"
        
    def actualizar(self):
        self.ImagenEntrada.setText("¡Acabas de hacer clic en el botón!")
        
    
    def OpemImage(self):
        # Create widget
        
        
        label = QLabel(self)
        pixmap = QPixmap(self.path)
        
        self.ImagenEntrada.setPixmap(pixmap)

    def Kmeans(self):
        
        img = cv2.imread(self.path,1)
        img2 = cv2.resize(img,(256,256))
        
        image = img2.reshape(-1, img2.shape[-1])
        cluster = Clustering(img2,image)
        
        start = time.time()
        segmented_image = cluster.K_Means()
        end = time.time()
        print(end - start)
        
        img2 = cv2.resize(segmented_image,(256,256))
        cv2.imwrite('KMeans.jpg',img2)
        
        label = QLabel(self)
        pixmap = QPixmap('KMeans.jpg')
        self.EimagenSalida.setPixmap(pixmap)
        
    
    def DBscan(self):
        img = cv2.imread(self.path,1)
        img2 = cv2.resize(img,(32,32))
        
        image = img2.reshape(-1, img2.shape[-1])
        cluster = Clustering(img2,image)
        
        start = time.time()
        segmented_image = cluster.DB_SCAN()
        end = time.time()
        print(end - start)
        
        img3 = cv2.resize(segmented_image,(256,256))
        cv2.imwrite('DBSCAN.jpg',img3)

       
        
        label = QLabel(self)
        pixmap = QPixmap('DBSCAN.jpg')
        self.EimagenSalida.setPixmap(pixmap)
        
    def Kmedoids(self):
        img = cv2.imread(self.path,1)
        
        img2 = cv2.resize(img,(32,32))
        
        image = img2.reshape(-1, img2.shape[-1])
        cluster = Clustering(img2,image)
        start = time.time()
        segmented_image = cluster.K_MEDOIDS()
        end = time.time()
        print(end - start)
        
        img__ = cv2.imread("Kmedios.jpg",1)
        img2 = cv2.resize(img__,(256,256))
        cv2.imwrite('KmediosResize.jpg',img2)

       
        
        label = QLabel(self)
        pixmap = QPixmap('KmediosResize.jpg')
        self.EimagenSalida.setPixmap(pixmap)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()