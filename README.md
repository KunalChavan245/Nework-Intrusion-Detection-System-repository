# Nework-Intrusion-Detection-System-repository

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Network Intrusion Detection System</title>
</head>
<body>
    <h1>Network Intrusion Detection System</h1>
    <p>This repository contains the implementation of a <strong>Network Intrusion Detection System (NIDS)</strong> using various machine learning models. The system processes network traffic data and classifies it to detect potential intrusions.</p>
    <h2>Project Structure</h2>
    <ul>
        <li><strong>pcap2csv</strong>: Script to convert <code>pcap</code> files (captured network traffic) into <code>csv</code> format for analysis.</li>
        <li><strong>README.md</strong>: The initial README file (to be replaced by this detailed version).</li>
        <li><strong>capture.pcap</strong>: Sample packet capture file containing network traffic used for intrusion detection testing.</li>
        <li><strong>cicids-model.ipynb</strong>: Jupyter notebook containing the CICIDS2017 dataset model, demonstrating the preprocessing steps and model training process.</li>
        <li><strong>eda.ipynb</strong>: Jupyter notebook for Exploratory Data Analysis (EDA) on the dataset used, providing insights and visualizations into the data distribution and trends.</li>
        <li><strong>example.ipynb</strong>: Example Jupyter notebook for running basic commands and demonstrating model inference.</li>
        <li><strong>model_pipeline_100_files_3_class.joblib</strong>: Pre-trained model pipeline file (with 100 files) using a 3-class classification model to detect intrusion attempts.</li>
        <li><strong>predict.py</strong>: Python script to load the trained model and make predictions on new data.</li>
        <li><strong>run.sh</strong>: Shell script to automate the running of the NIDS pipeline.</li>
        <li><strong>tuned_xgb_pipeline_145_files_3_class.joblib</strong>: Fine-tuned XGBoost model trained on 145 files, specifically for a 3-class classification.</li>
        <li><strong>xgb_pipeline_100_files_3_class.joblib</strong>: Initial XGBoost model trained with 100 files for 3-class classification.</li>
    </ul>
    <h2>Dataset</h2>
    <p>The dataset used for this project is the <strong>CICIDS2017</strong> dataset, which is widely used for network intrusion detection research.</p>
    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/KunalChavan245/Network-Intrusion-Detection-System-repository</code></pre>
        </li>
        <li>Install the necessary dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>
    <h2>Usage</h2>
    <ol>
        <li>Convert <code>pcap</code> files to <code>csv</code>:
            <pre><code>python pcap2csv.py capture.pcap</code></pre>
        </li>
        <li>To run the trained model and predict intrusion attempts:
            <pre><code>python predict.py</code></pre>
        </li>
        <li>For detailed analysis and model training, refer to the Jupyter notebooks:
            <ul>
                <li><code>cicids-model.ipynb</code></li>
                <li><code>eda.ipynb</code></li>
            </ul>
        </li>
    </ol>
    <h2>Models</h2>
    <p>This project utilizes several machine learning pipelines:</p>
    <ul>
        <li><strong>XGBoost</strong>: A gradient boosting algorithm.</li>
        <li><strong>Pre-trained models</strong>: The repository contains pipelines saved as <code>.joblib</code> files, which can be directly loaded for predictions.</li>
    </ul>
    <h2>License</h2>
    <p>This project is open-source and licensed under the MIT License.</p>
</body>
</html>
