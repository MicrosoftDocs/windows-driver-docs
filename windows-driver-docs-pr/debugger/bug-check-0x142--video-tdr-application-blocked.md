---
title: Bug Check 0x142 VIDEO_TDR_APPLICATION_BLOCKED
description: The VIDEO_TDR_APPLICATION_BLOCKED live dump has a value of 0x00000142. This indicates that an application has been blocked from accessing graphics hardware.
keywords: ["Bug Check 0x142 VIDEO_TDR_APPLICATION_BLOCKED", "VIDEO_TDR_APPLICATION_BLOCKED"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- VIDEO_TDR_APPLICATION_BLOCKED
api_type:
- NA
---

# Bug Check 0x142: VIDEO\_TDR\_APPLICATION\_BLOCKED


The VIDEO\_TDR\_APPLICATION\_BLOCKED live dump has a value of 0x00000142. This indicates that an application has been blocked from accessing graphics hardware.

(This code can never be used for a real bug check; it is used to identify live dumps.)

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## VIDEO\_TDR\_APPLICATION\_BLOCKED Parameters


| Parameter | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| 1         | Optional pointer to internal TDR recovery context (TDR\_RECOVERY\_CONTEXT). |
| 2         | The pointer into responsible device driver module (e.g owner tag).          |
| 3         | The secondary driver specific bucketing key.                                |
| 4         | Id of the process being blocked from accessing the GPU.                     |

 

## Remarks

The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

Secondary data of tag {270A33FD-3DA6-460D-BA89-3C1BAE21E39B} contains additional TDR related data. Use [**.enumtag (Enumerate Secondary Callback Data)**](../debuggercmds/-enumtag--enumerate-secondary-callback-data-.md) to view the data.
