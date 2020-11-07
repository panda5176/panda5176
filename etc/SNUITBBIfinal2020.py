'''
2020-1 IT basics for bioinformatics final, part 2.
Written in Python v3.7, Scikit-learn v0.22.
'''

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import mode
from numpy import mean

from sklearn.model_selection import train_test_split, KFold

from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.manifold import TSNE
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.metrics.cluster \
    import homogeneity_score, completeness_score, v_measure_score, \
        adjusted_rand_score, adjusted_mutual_info_score, silhouette_score


def Q1():
    '''
    1.	(regression and PCA) Perform regression analysis using \
        all the attributes given ‘qsar’ dataset. (10 points)
        A. (regression) Perform linear regression using all the attributes \
            and report R2 and MSE value of your model. (3 points)
        B. (regression) What are the significant attributes \
            (predictor variables) to the response from your model? (3 points)
        C. (PCA) How much variance can be explained by using both 1st \
            and 2nd principal components (in percentage)? (4 points)

    Attribute Information:
        8 molecular descriptors and 1 quantitative experimental response:
            1) TPSA(Tot)
            2) SAacc
            3) H-050
            4) MLOGP
            5) RDCHI
            6) GATS1p
            7) nN
            8) C-040
            9) quantitative response, LC50 [-LOG(mol/L)]
    '''

    f1 = "qsar_aquatic_toxicity.csv"

    df = pd.read_csv(
        f1, sep = ';', header = None, names = [
            "TPSA", "SAacc", "H-050", "MLOGP", 
            "RDCHI", "GATS1p", "nN", "C-040", 
            "LC50"
            ]
        )
    print(df.head())
    print(df.describe())

    df_x = df.iloc[:, :-1]
    df_y = df.iloc[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(
        df_x, df_y, test_size = 0.2, random_state = 28)

    lr_model = LinearRegression()
    lr_model.fit(x_train, y_train)
    y_pred = lr_model.predict(x_test)

    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    print("Variance score: %.2f" % r2_score(y_test, y_pred))
    # Mean squared error: 1.48
    # Variance score: 0.52

    print("Coefficients: \n", lr_model.coef_)
    # Coefficients: [
    #     0.02824191 -0.01556324  0.03466202  0.47842656
    #     0.43164233 -0.41294179 -0.19186772  0.02021045
    #     ]
    # Significant attributes:
    # "MLOGP" & "RDCHI": moderate positive (Pearson r: 0.48 & 0.43)
    # "GATS1p": moderate negative (Pearson r: -0.41)
    # "nN": weak negative (Pearson r: -0.19)

    pca = PCA(n_components = 2)
    PCs = pca.fit_transform(df_x)
    df_principal = pd.DataFrame(data = PCs, columns = ['PC1', 'PC2'])
    df_final = pd.concat([df_principal, df_y], axis = 1)
    print(pca.explained_variance_ratio_)
    # Explained variances of PC1 & PC2: 93.87% & 6.04%


def Q2():
    '''
    2.	Perform clustering of ‘seeds’ dataset using K-means (K=3) \
        and hierarchical clustering. (20 points)
        A. (K-means) Report homogeneity, completeness, V-means, ARI, AMI, \
            and silhouette score of your clustering result. (3 points)
        B. (K-means) Report accuracy and the list of instances \
            of which predictions are inconsistent with the true label \
            (use 5-fold cross validation and report averaged performance). \
            (7 points)
        C. (K-means) How much improvement was achieved \
            when the data was transformed using t SNE in terms of the metrics \
            used in ‘question 2-A’? Explain why. (7 points)
        D. (Hierarchical clustering) Using ‘Ward’ clustering method, \
            perform hierarchical clustering with distances \
            ‘Euclidean and Manhattan’. Which distance metric is the better \
            in terms of silhouette score? (n_clusters = 3) (3 points)
    
    Attribute Information:
        To construct the data, seven geometric parameters of wheat kernels \
        were measured:
            1. area A,
            2. perimeter P,
            3. compactness C = 4*pi*A/P^2,
            4. length of kernel,
            5. width of kernel,
            6. asymmetry coefficient
            7. length of kernel groove.
        All of these parameters were real-valued continuous.
            (8. three different varieties of wheat)
    '''

    f2 = "seeds_dataset.txt"

    df = pd.read_csv(
        f2, delim_whitespace = True, header = None, names = [
            "area A", "perimeter P", "compactness C", "length of kernel", 
            "width of kernel", "assymmetry coefficient", 
            "length of kernel groove", "varieties"
            ]
        )
    print(df.head())
    print(df.describe())

    df_x = df.iloc[:, :-1]
    df_y = df.iloc[:, -1]

    km_model = KMeans(n_clusters = 3).fit(df_x)
    pred_y = km_model.predict(df_x)

    print("Homogeneity score: %.2f" % homogeneity_score(df_y, pred_y))
    print("Completeness score: %.2f" % completeness_score(df_y, pred_y))
    print("V-means score: %.2f" % v_measure_score(df_y, pred_y))
    print("ARI score: %.2f" % adjusted_rand_score(df_y, pred_y))
    print("AMI score: %.2f" % adjusted_mutual_info_score(df_y, pred_y))
    print("Silhouette score: %.2f" % silhouette_score(df_x, pred_y))
    # Homogeneity score: 0.69
    # Completeness score: 0.70
    # V-means score: 0.69
    # ARI score: 0.72
    # AMI score: 0.69
    # Silhouette score: 0.47

    kf = KFold(n_splits = 5, shuffle = True)
    accuracy_score_list = []
    labels_list = []

    for idx_train, idx_test in kf.split(df_x):
        x_train, x_test = df_x.to_numpy()[idx_train], df_x.to_numpy()[idx_test]
        y_train, y_test = df_y.to_numpy()[idx_train], df_y.to_numpy()[idx_test]

        km_model = KMeans(n_clusters = 3).fit(x_train)
        y_pred = km_model.predict(x_test)

        labels = np.zeros_like(y_pred)

        for i in range(3):
            mask = (y_pred == i)
            labels[mask] = mode(y_test[mask])[0]

        accuracy_score_list.append(accuracy_score(y_test, labels))
        labels_list += idx_test[y_test != labels].tolist()

    print("Accuracy score: %.2f" % mean(accuracy_score_list))
    print("The list of instances of which predictions are inconsistent \
        with the true label: ", sorted(labels_list))
    # Accuracy score: 0.90
    # The list of instances of which predictions are inconsistent \
    #     with the true label: [
    #         16, 19, 26, 27, 37, 39, 60, 61, 62, 63, 69, 100, 
    #         122, 124, 132, 133, 134, 135, 137, 138, 139
    #         ]

    ts_model = TSNE(n_components = 2, init = 'random').fit_transform(df_x)
    km_model = KMeans(n_clusters = 3).fit(ts_model)
    pred_y = km_model.predict(ts_model)

    print("Homogeneity score: %.2f" % homogeneity_score(df_y, pred_y))
    print("Completeness score: %.2f" % completeness_score(df_y, pred_y))
    print("V-means score: %.2f" % v_measure_score(df_y, pred_y))
    print("ARI score: %.2f" % adjusted_rand_score(df_y, pred_y))
    print("AMI score: %.2f" % adjusted_mutual_info_score(df_y, pred_y))
    print("Silhouette score: %.2f" % silhouette_score(df_x, pred_y))
    # Homogeneity score: 0.69 -> 0.71
    # Completeness score: 0.70 -> 0.71
    # V-means score: 0.69 -> 0.71
    # ARI score: 0.72 -> 0.73
    # AMI score: 0.69 -> 0.71
    # Silhouette score: 0.47 -> 0.47
    # 차원이 매우 크지 않기 때문에 embedding의 효과가 크지 않다.

    pred_y_euclidean = AgglomerativeClustering(
        n_clusters = 3, affinity = 'euclidean', linkage = 'ward'
        ).fit_predict(df_x)
    pred_y_model_manhattan = AgglomerativeClustering(
        n_clusters = 3, affinity = 'manhattan', linkage = 'average'
        ).fit_predict(df_x)

    print("Silhouette score with Euclidean metric: %.2f" \
        % silhouette_score(df_x, pred_y_euclidean))
    print("Silhouette score with Manhattan metric: %.2f" \
        % silhouette_score(df_x, pred_y_model_manhattan))
    # Silhouette score with Euclidean metric: 0.45
    # Silhouette score with Manhattan metric: 0.44
    # Euclidean distance metric is better than Manhattan \
    #     in terms of silhouette score.


def Q3():
    '''
    3.	Perform classification of ‘Ecoli’ dataset using \
        all Naive Bayes / KNN / Decision Tree / Random Forests / SVM methods. \
        (15 points)
        A. Which of the methods show the best performance \
            in terms of accuracy? Explain why \
            (use 5-fold cross validation and report averaged performance). \
            (10 points)
        B. In random forests model, list THREE most important attributes \
            in classifying localization site. (5 points)

    Attribute Information:
        1. Sequence Name: Accession number for the SWISS-PROT database
        2. mcg: McGeoch's method for signal sequence recognition.
        3. gvh: von Heijne's method for signal sequence recognition.
        4. lip: von Heijne's Signal Peptidase II consensus sequence score. \
            Binary attribute.
        5. chg: Presence of charge on N-terminus of predicted lipoproteins. \
            Binary attribute.
        6. aac: score of discriminant analysis of the amino acid content of \
            outer membrane and periplasmic proteins.
        7. alm1: score of the ALOM membrane spanning region prediction program.
        8. alm2: score of ALOM program after excluding \
            putative cleavable signal regions from the sequence.
        (9. protein localization sites)
    '''

    f3 = "ecoli.data"

    df = pd.read_csv(
        f3, delim_whitespace = True, header = None, names = [
            "Sequence Name", "mcg", "gvh", "lip", "chg", 
            "aac", "alm1", "alm2", "protein localization sites"
            ]
        )
    # print(df.head())
    # print(df.describe())

    df_x = df.iloc[:, 1:-1]
    df_y = df.iloc[:, -1]

    kf = KFold(n_splits = 5, shuffle = True)
    accuracy_score_list_GNB = []
    accuracy_score_list_BNB = []
    accuracy_score_list_MNB = []
    accuracy_score_list_KNN = []
    accuracy_score_list_DT = []
    accuracy_score_list_RF = []
    accuracy_score_list_SVM = []
    features = df_x.columns

    for idx_train, idx_test in kf.split(df_x):
        x_train, x_test = df_x.to_numpy()[idx_train], df_x.to_numpy()[idx_test]
        y_train, y_test = df_y.to_numpy()[idx_train], df_y.to_numpy()[idx_test]

        GNB_model = GaussianNB().fit(x_train, y_train)
        y_GNB = GNB_model.predict(x_test)
        BNB_model = BernoulliNB().fit(x_train, y_train)
        y_BNB = BNB_model.predict(x_test)
        MNB_model = MultinomialNB().fit(x_train, y_train)
        y_MNB = MNB_model.predict(x_test)
        KNN_model = KNeighborsClassifier().fit(x_train, y_train)
        y_KNN = KNN_model.predict(x_test)
        DT_model = DecisionTreeClassifier().fit(x_train, y_train)
        y_DT = DT_model.predict(x_test)
        RF_model = RandomForestClassifier(n_jobs = -1).fit(x_train, y_train)
        y_RF = RF_model.predict(x_test)
        SVM_model = SVC(kernel = 'rbf').fit(x_train, y_train) # high-dimension
        y_SVM = SVM_model.predict(x_test)

        accuracy_score_list_GNB.append(accuracy_score(y_test, y_GNB))
        accuracy_score_list_BNB.append(accuracy_score(y_test, y_BNB))
        accuracy_score_list_MNB.append(accuracy_score(y_test, y_MNB))
        accuracy_score_list_KNN.append(accuracy_score(y_test, y_KNN))
        accuracy_score_list_DT.append(accuracy_score(y_test, y_DT))
        accuracy_score_list_RF.append(accuracy_score(y_test, y_RF))
        accuracy_score_list_SVM.append(accuracy_score(y_test, y_SVM))

        importances = RF_model.feature_importances_
        indices = np.argsort(importances)
        # print(features[indices], importances[indices])
        # Rank of attributes are always same in every fold.

    print("Accuracy score using Gaussian Naive Bayes: %.2f" \
        % mean(accuracy_score_list_GNB))
    print("Accuracy score using Bernoulli Naive Bayes: %.2f" \
        % mean(accuracy_score_list_BNB))
    print("Accuracy score using Multinomial Naive Bayes: %.2f" \
        % mean(accuracy_score_list_MNB))
    print("Accuracy score using KNN: %.2f" % mean(accuracy_score_list_KNN))
    print("Accuracy score using Decision Tree: %.2f" \
        % mean(accuracy_score_list_DT))
    print("Accuracy score using Random Forests: %.2f" \
        % mean(accuracy_score_list_RF))
    print("Accuracy score using SVM: %.2f" % mean(accuracy_score_list_SVM))
    # Accuracy score using Gaussian Naive Bayes: 0.76
    # Accuracy score using Bernoulli Naive Bayes: 0.42
    # Accuracy score using Multinomial Naive Bayes: 0.43
    # Accuracy score using KNN: 0.86
    # Accuracy score using Decision Tree: 0.80
    # Accuracy score using Random Forests: 0.87
    # Accuracy score using SVM: 0.87

    important_attributes = features[indices][:3].format()
    print("THREE most important attributes: ", important_attributes)
    # THREE most important attributes:  ['chg', 'lip', 'aac']


def Q4():
    '''
    4.	(Longest Common Sequence) Perform dynamic programming \
        on given two sequences X and Y. (15 points)
            X: TCTATATGCACCTGC
            Y: ATGCCCCCCATGAC
        A. Define an optimal structure to find length of \
            longest common sequence (LCS). (3 points)
        B. Report the length of the LCS between X and Y with DP table. \
            Make DP table using numpy array. (5 points)
        C. What is the LCS between X and Y? Show the LCS using DP table. \
            (2 points)
        D. (Smith-Waterman algorithm) Find a local alignment of X and Y \
            using match_score: +2, mismatch_penalty: -3, gap_penalty: -2. \
            (5 points)
    '''
    X = "TCTATATGCACCTGC"
    Y = "ATGCCCCCCATGAC"

    def LCS_opti_struct(x, y):
        '''
        (Memoization Version)
        LCS optimal structure:
            양 서열의 마지막 글자가 동일할 경우:
                마지막 글자를 제외한 두 서열의 LCS optimal substructure + 1 계산.
            양 서열(x, y)의 마지막 글자가 다를 경우:
                x 서열의 마지막 글자를 제외한 서열과 y 서열의 LCS optimal substructure
                또는 y 서열의 마지막 글자를 제외한 서열과 x 서열의 LCS optimal substructure
                중 최댓값.
        '''

        if (len(x) == 0 or len(y) == 0):
            return 0

        elif x[-1] == y[-1]:
            return 1 + LCS_opti_struct(x[:-1], y[:-1])

        else:
            return max(LCS_opti_struct(x, y[:-1]), LCS_opti_struct(x[:-1],y))
        
        return None

    # print("The length of LCS: ", LCS_opti_struct(X, Y))

    def LCS_DP_table(x, y):
        '''
        (Tabulation Version)
        '''

        x_len = len(x)
        y_len = len(y)
        x_dim = x_len + 1
        y_dim = y_len + 1

        DP_table = np.array([[0] * y_dim] * x_dim)

        for i in range(1, x_dim):

            for j in range(1, y_dim):
                # print(i,j)

                if x[i-1] == y[j-1]:
                    DP_table[i][j] = DP_table[i-1][j-1] + 1

                else:
                    DP_table[i][j] = max(DP_table[i-1][j], DP_table[i][j-1])
                
                # print(DP_table)

        LCS = ""
        curr_x = x_len
        curr_y = y_len

        while (curr_x > 0 and curr_y > 0):
            # print(curr_x, curr_y, LCS[::-1])

            if x[curr_x - 1] == y[curr_y - 1]:
                LCS += x[curr_x - 1]
                curr_x -= 1
                curr_y -= 1

            elif DP_table[curr_x - 1][curr_y] > DP_table[curr_x][curr_y - 1]:
                curr_x -= 1
            
            else:
                curr_y -= 1

        return DP_table, DP_table[x_len][y_len], LCS[::-1]

    LCS_result = LCS_DP_table(X, Y)
    print("The length of LCS: ", LCS_result[1])
    print("The LCS between X and Y: ", LCS_result[2])

    def Smith_Waterman(x, y, m, mm, g):
        x_len = len(x)
        y_len = len(y)
        x_dim = x_len + 1
        y_dim = y_len + 1

        DP_table = np.array([[0] * y_dim] * x_dim)

        for i in range(1, x_dim):

            for j in range(1, y_dim):
                # print(i,j)
                scores = [0]

                if x[i-1] == y[j-1]:
                    scores.append(DP_table[i-1][j-1] + m)

                else:
                    scores.append(DP_table[i-1][j-1] + mm)

                scores.append(DP_table[i][j-1] + g)
                scores.append(DP_table[i-1][j] + g)
                # print(scores)
                
                DP_table[i][j] = max(scores)
                # print(DP_table)

        max_value = np.amax(DP_table)
        max_idx = np.where(DP_table == max_value)
        max_idx = list(zip(max_idx[0], max_idx[1]))[0]
        # print(max_idx)

        ALN_x = ""
        ALN_y = ""
        curr_x = max_idx[0]
        curr_y = max_idx[1]

        while (curr_x > 0 and curr_y > 0):
            # print(curr_x, curr_y, ALN_x[::-1], ALN_y[::-1])

            if x[curr_x - 1] == y[curr_y - 1]:
                ALN_x += x[curr_x - 1]
                ALN_y += y[curr_y - 1]
                curr_x -= 1
                curr_y -= 1

            elif DP_table[curr_x - 1][curr_y] > DP_table[curr_x][curr_y - 1]:
                ALN_x += x[curr_x - 1]
                ALN_y += "-"
                curr_x -= 1
            
            else:
                ALN_x += "-"
                ALN_y += y[curr_y - 1]
                curr_y -= 1

        return DP_table, ALN_x[::-1], ALN_y[::-1]

    SW_result = Smith_Waterman(X, Y, +2, -3, -2)
    print("The local alignment of X and Y: \n%s\n%s" \
        % (SW_result[1], SW_result[2]))


if __name__ == "__main__":
    Q1()
    Q2()
    Q3()
    Q4()

# The end of source code.
