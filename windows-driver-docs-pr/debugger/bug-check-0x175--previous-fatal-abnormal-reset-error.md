---
title: Bug Check 0x175 PREVIOUS_FATAL_ABNORMAL_RESET_ERROR
description: The PREVIOUS_FATAL_ABNORMAL_RESET_ERROR bug check has a value of 0x00000175.
ms.assetid: C1F74858-DAF4-466C-9696-6FE5390574C3
keywords: ["Bug Check 0x175 PREVIOUS_FATAL_ABNORMAL_RESET_ERROR", "PREVIOUS_FATAL_ABNORMAL_RESET_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PREVIOUS_FATAL_ABNORMAL_RESET_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x175: PREVIOUS\_FATAL\_ABNORMAL\_RESET\_ERROR


The PREVIOUS\_FATAL\_ABNORMAL\_RESET\_ERROR bug check has a value of 0x00000175. This indicates that an unrecoverable system error occurred or the system has abnormally reset on Windows phone devices. The system generated a live dump to collect device crash data from the previous error.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PREVIOUS\_FATAL\_ABNORMAL\_RESET\_ERROR Parameters


| Parameter | Description |
|-----------|-------------|
| 1         | Reserved    |
| 2         | Reserved    |
| 3         | Reserved    |
| 4         | Reserved    |

 

Cause
-----

The system on Windows Phone devices encountered an unexpected error and restarted. Issues that may cause this error include: hardware watchdog timer in application or auxiliary processors indicating a system hang, user-initiated key sequence because of a hang, etc.

 

 




