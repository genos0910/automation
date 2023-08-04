#!/bin/bash

cd /Users/genosho/Documents/automation/

locust -f tests/load/locustfile.py  --users 100 --spawn-rate 10 --csv=reports/
<<comment 生成100個虛擬用戶，每秒生成10個新用戶，直到達到100個用戶為止 comment
