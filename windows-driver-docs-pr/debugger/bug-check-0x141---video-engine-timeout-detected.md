---
title: Bug Check 0x141 VIDEO_ENGINE_TIMEOUT_DETECTED
description: The VIDEO_ENGINE_TIMEOUT_DETECTED bug check has a value of 0x00000141. This indicates that one of the display engines failed to respond in timely fashion.
ms.assetid: 0912495D-DE6D-4064-BD66-DA6145889821
keywords: ["Bug Check 0x141 VIDEO_ENGINE_TIMEOUT_DETECTED", "VIDEO_ENGINE_TIMEOUT_DETECTED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- VIDEO_ENGINE_TIMEOUT_DETECTED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x141: VIDEO\_ENGINE\_TIMEOUT\_DETECTED


The VIDEO\_ENGINE\_TIMEOUT\_DETECTED bug check has a value of 0x00000141. This indicates that one of the display engines failed to respond in timely fashion.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## VIDEO\_ENGINE\_TIMEOUT\_DETECTED Parameters


| Parameter | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| 1         | Optional pointer to internal TDR recovery context (TDR\_RECOVERY\_CONTEXT). |
| 2         | The pointer into responsible device driver module (e.g owner tag).          |
| 3         | The secondary driver specific bucketing key.                                |
| 4         | Optional internal context dependent data.                                   |

 

Remarks
-------

Secondary data of tag {270A33FD-3DA6-460D-BA89-3C1BAE21E39B} contains additional TDR related data. Use .enumtag to view the data.

 

 




