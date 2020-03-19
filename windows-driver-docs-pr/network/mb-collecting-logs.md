---
title: MB Collecting Logs
description: MB Collecting Logs
ms.date: 03/17/2020
ms.localizationpriority: medium
---

# MobileBroadband Collecting logs

Please use the below steps to collect the logs related to Mobilebroadband on Windows Desktop Device
```
*  Open an Administrator Command Prompt window
*  Run the below command to start tracing
    *  netsh trace start provisioning overwrite=yes
*  <Repro the scenario for which you need to collect logs>
*  Run the below command to stop tracing
    *  netsh trace stop
```
The above steps generate two files
1.  NetTrace.etl - Contains the traces for the run
2.  NetTrace.cab - Contains additional details about the system that will be useful for debugging

## Collecting logs across a reboot

If the repro scenario includes a reboot please update the start tracing command as below
```
*  netsh trace start provisioning overwrite=yes persist=yes
```

Please note that PII will be captured in the logs collected using the above method.

## Decoding Logs

Run the below command to convert the .etl file to a .txt file that can be used for analysis
```
*  netsh trace convert <ETL file location>
```

