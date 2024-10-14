from joblib import load
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import numpy as np
import xgboost
import subprocess
test_3 = load('tuned_xgb_pipeline_145_files_3_class.joblib')

test_data = pd.read_csv("pcap2csv/capture.pcap.csv")

X_columns = ['flow_duration', 'Header_Length', 'Protocol Type', 'Duration', 'Rate',
       'Srate', 'Drate', 'fin_flag_number', 'syn_flag_number',
       'rst_flag_number', 'psh_flag_number', 'ack_flag_number',
       'ece_flag_number', 'cwr_flag_number', 'ack_count', 'syn_count',
       'fin_count', 'urg_count', 'rst_count', 'HTTP', 'HTTPS','TCP', 'UDP',  'ICMP',
       'Tot sum', 'Min', 'Max', 'AVG', 'Std', 'Tot size', 'IAT', 'Number',
       'Magnitue', 'Radius', 'Covariance', 'Variance', 'Weight']
y_column = 'label'
X = test_data[X_columns]
y_pred_test = test_3.predict(X)
test_data["Predictions"] = y_pred_test
idx_to_class = {0:"Benign",1:"DDOS", 2:"DOS"}
non_zero_indices = np.nonzero(y_pred_test)[0]
port = 22
if len(non_zero_indices) > 10:
    max_pred = y_pred_test.max().item()
    for i in non_zero_indices:
        print(f"Possible {idx_to_class[max_pred]} attack at port: {port} by IP: {test_data.loc[i,"Source IP"]}")
    attack_data = test_data[test_data["Predictions"].isin([1,2])]
    hostile_ips = list(attack_data["Source IP"].unique())
    for ip in hostile_ips:
        _ = subprocess.run(['sudo','iptables','-A','INPUT','-s',ip,'-j','DROP'],capture_output = False)
        print(f"Further packets from {ip} will be dropped")

else:
    print("No anomalies found")
