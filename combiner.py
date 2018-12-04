import pandas

data_class = pandas.read_csv('CSV/ClassLevel/_data-class.csv')
god_class = pandas.read_csv('CSV/ClassLevel/_god-class.csv')

feature_envy = pandas.read_csv('CSV/MethodLevel/_feature-envy.csv')
long_method = pandas.read_csv('CSV/MethodLevel/_long-method.csv')

blank_data_class = data_class.copy(deep=True)
blank_data_class['SMELLS'] = False

blank_god_class = god_class.copy(deep=True)
blank_god_class['SMELLS'] = False

blank_feature_envy = feature_envy.copy(deep=True)
blank_feature_envy['SMELLS'] = False

blank_long_method = long_method.copy(deep=True)
blank_long_method['SMELLS'] = False

cl_data_class = pandas.concat([data_class, blank_god_class])
cl_god_class = pandas.concat([god_class, blank_data_class])

ml_feature_envy = pandas.concat([feature_envy, blank_long_method])
ml_long_method = pandas.concat([long_method, blank_feature_envy])

cl_data_class.to_csv(path_or_buf='CSV/cl-data-class.csv')
cl_god_class.to_csv(path_or_buf='CSV/cl-god-class.csv')
ml_feature_envy.to_csv(path_or_buf='CSV/ml-feature-envy.csv')
ml_long_method.to_csv(path_or_buf='CSV/ml-long-method.csv')
