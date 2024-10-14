#!/bin/bash
cd pcap2csv
packet_count=$(sudo timeout 5 tcpdump -i enp0s3 -c 1000 -w capture.pcap 2>&1 | grep 'packets captured' |
awk '{print $1}')

if [ $packet_count -ne 0 ]; then
	echo "read $packet_count"
	python3 Generating_dataset.py
	cd ..
	python3 predict.py
else
	cd ..
fi
