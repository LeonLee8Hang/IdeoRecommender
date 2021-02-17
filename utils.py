import config
import sys,os

def run_kmeans(data,k,converge_dist):
    ''' Execute kmeans.py from pySpark home '''

    os.system("./" + config.PYSPARK_HOME + " " + config.SPARKLER_HOME + "/kmeans.py " + config.CLUSTER_CONFIG + " " + data + " " + str(k) + " " + str(converge_dist))

def run_usercf(data):
    ''' Execute user_cf.py from pySpark home '''

    os.system("./" + config.PYSPARK_HOME + " " + config.SPARKLER_HOME + "/userBasedRecommender.py " + config.CLUSTER_CONFIG + " " + data)

def run_itemcf(data):
    ''' Execute item_cf.py from pySpark home '''

    os.system("./" + config.PYSPARK_HOME + " " + config.SPARKLER_HOME + "/itemBasedRecommender.py " + config.CLUSTER_CONFIG + " " + data)