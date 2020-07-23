import  numpy as np
point_1=[img.shape[1]-60,40]
point_2=[img.shape[1]-420,510]
new_point_1=np.dot(M_scale.T,point_1)
new_point_2=np.dot(M_scale.T,point_2)