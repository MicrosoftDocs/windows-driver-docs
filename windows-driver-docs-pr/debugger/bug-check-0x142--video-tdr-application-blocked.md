---
title: Bug Check 0x142 VIDEO_TDR_APPLICATION_BLOCKED
description: The VIDEO_TDR_APPLICATION_BLOCKED bug check has a value of 0x00000142. This indicates that an application has been blocked from accessing graphics hardware.
ms.assetid: B97FCA51-C368-4144-A364-50135A8DE836
keywords: ["Bug Check 0x142 VIDEO_TDR_APPLICATION_BLOCKED", "VIDEO_TDR_APPLICATION_BLOCKED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- VIDEO_TDR_APPLICATION_BLOCKED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x142: VIDEO\_TDR\_APPLICATION\_BLOCKED


The VIDEO\_TDR\_APPLICATION\_BLOCKED bug check has a value of 0x00000142. This indicates that an application has been blocked from accessing graphics hardware.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## VIDEO\_TDR\_APPLICATION\_BLOCKED Parameters


| Parameter | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| 1         | Optional pointer to internal TDR recovery context (TDR\_RECOVERY\_CONTEXT). |
| 2         | The pointer into responsible device driver module (e.g owner tag).          |
| 3         | The secondary driver specific bucketing key.                                |
| 4         | Id of the process being blocked from accessing the GPU.                     |

 

Remarks
-------

Secondary data of tag {270A33FD-3DA6-460D-BA89-3C1BAE21E39B} contains additional TDR related data. Use [**.enumtag (Enumerate Secondary Callback Data)**](-enumtag--enumerate-secondary-callback-data-.md) to view the data.

 

 




