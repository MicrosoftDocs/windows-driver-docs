---
title: Bug Check 0x14C FATAL_ABNORMAL_RESET_ERROR
description: The FATAL_ABNORMAL_RESET_ERROR bug check has a value of 0x0000014C. This indicates that an unrecoverable system error occurred or the system has abnormally reset.
keywords: ["Bug Check 0x14C FATAL_ABNORMAL_RESET_ERROR", "FATAL_ABNORMAL_RESET_ERROR"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- FATAL_ABNORMAL_RESET_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x14C: FATAL\_ABNORMAL\_RESET\_ERROR


The FATAL\_ABNORMAL\_RESET\_ERROR bug check has a value of 0x0000014C. This indicates that an unrecoverable system error occurred or the system has abnormally reset.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## FATAL\_ABNORMAL\_RESET\_ERROR Parameters


None

## Cause

The system encountered an unexpected error and restarted. Issues that may cause this error include: hardware watchdog timer in application or auxiliary processors indicating a system hang, user-initiated key sequence because of a hang, a brownout, or failures in the default bugcheck path. The cache may not be flushed and the resulting full memory dump may not contain the current thread context.

Secondary data of tag {E1D08891-D5A3-45F9-B811-AD711DFB2607} contains additional “Blackbox” data. Use [**.enumtag (Enumerate Secondary Callback Data)**](-enumtag--enumerate-secondary-callback-data-.md) to view the data.

 

 




