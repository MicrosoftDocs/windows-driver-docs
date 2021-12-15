---
title: MB Collecting Logs
description: MB Collecting Logs
ms.date: 03/10/2021
---

# Mobile Broadband Collecting Logs

Follow these steps to collect the logs related to mobile broadband on a Windows Desktop Device:
```
*  Open an Administrator Command Prompt window
*  Run the below command to start tracing
    *  netsh trace start wireless_dbg,provisioning overwrite=yes maxSize=999 level=5
*  <Repro the scenario for which you need to collect logs>
*  Run the below command to stop tracing
    *  netsh trace stop
```
The steps above generate two files:
1.  NetTrace.etl - Contains the traces for the run
2.  NetTrace.cab - Contains additional details about the system that will be useful for debugging

## Collecting logs across a reboot

If the repro scenario includes a reboot update the start tracing command as follows:
```
*  netsh trace start wireless_dbg,provisioning overwrite=yes persist=yes level=5
```

**Please note that PII will be captured in the logs collected using the above method.**

## Decoding Logs

Run one of these commands to convert the .etl file to a .txt file that can be used for analysis:

  ```*  ```[```tracefmt```](../devtest/tracefmt-commands.md)``` <ETL file location>  ```<br/>
  ```    or ```<br/>
  ```*  netsh trace convert <ETL file location>```
