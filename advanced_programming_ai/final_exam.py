# QUESTION 1 : TASK 1
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt

# i
p_df = pd.read_csv("C:\\Work\\Nano\\advanced_programming_ai\\datasets\\Pumpkin.csv", encoding='latin1')

# ii
print(p_df.shape, p_df.head(), p_df.tail())

# iii
print(p_df['Class'].value_counts())
# 1300 (Cercevelik) and 1200 (Urgup) 

# iv
print(p_df.isnull().sum())
# 2500 in all columns, no missing values

# v
print(p_df.corr)

# QUESTION 1 : TASK 2

# i
p_df.fillna(p_df.mean(numeric_only=True), inplace=True)
print(p_df.isnull().sum())

# ii
p_df.drop(['Convex_Area'], axis=1, inplace=True)

# iii
label_encoder = LabelEncoder()
p_df['Class'] = label_encoder.fit_transform(p_df['Class'])

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    p_df.drop('Class', axis=1), p_df['Class'], test_size=0.2, random_state=42
)

# iv
X = p_df.drop('Class', axis=1)
y = p_df['Class']

# v
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# QUESTION 2
def plot_bar(categories, values, is_vertical=True):
    if is_vertical == True:
        plt.bar(categories, values, color='orange')
    else :
        plt.barh(categories, values, color='orange')
    plt.xlabel('Brand')
    plt.ylabel('Shares (%)')
    plt.title('Phone Brand Shares')
    plt.grid(axis='y')
    plt.show()
    
plot_bar(['Samsung', 'Apple', 'Xiomi', 'Oppo', 'Huawei', 'Vivo'], [28.33, 27.48, 12.97, 6.28, 4.98, 4.59], False)

def plot_pie(categories, values):
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Phone Brand Shares')
    plt.axis('equal')
    plt.legend()
    plt.show()
    
plot_pie(['Samsung', 'Apple', 'Xiomi', 'Oppo', 'Huawei', 'Vivo'], [28.33, 27.48, 12.97, 6.28, 4.98, 4.59])


# QUESTION 3

# TASK 1
one_d_array = np.array((1, 3, 4, 5))
two_d_array = np.array([[1, 2], [3, 4]])
three_d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# TASK 2
print("Dimensions of n_dimension_array:", three_d_array.ndim)

# TASK 3
print("First index: ", three_d_array[0])

# TASK 4
arr = np.array([1,2,3,4,5,6,7])
print("Sliced array from n_dimension_array:\n", arr[2:5])

# TASK 5
print("Shape:", three_d_array.shape)

# TASK 6
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
concatenated_array = np.concatenate((array1, array2), axis=0)
print("Concatenated array along axis 0:\n", concatenated_array)

# TASK 7
random_integers = np.random.randint(0, 100)
print(random_integers)