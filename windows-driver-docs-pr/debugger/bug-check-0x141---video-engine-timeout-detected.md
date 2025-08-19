---
title: Bug Check 0x141 VIDEO_ENGINE_TIMEOUT_DETECTED
description: The VIDEO_ENGINE_TIMEOUT_DETECTED live dump has a value of 0x00000141. This indicates that one of the display engines failed to respond in timely fashion.
keywords: ["Bug Check 0x141 VIDEO_ENGINE_TIMEOUT_DETECTED", "VIDEO_ENGINE_TIMEOUT_DETECTED"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- VIDEO_ENGINE_TIMEOUT_DETECTED
api_type:
- NA
---

# Bug Check 0x141: VIDEO\_ENGINE\_TIMEOUT\_DETECTED


The VIDEO\_ENGINE\_TIMEOUT\_DETECTED live dump has a value of 0x00000141. This indicates that one of the display engines failed to respond in timely fashion.

(This code can never be used for a real bug check; it is used to identify live dumps.)

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## VIDEO\_ENGINE\_TIMEOUT\_DETECTED Parameters


| Parameter | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| 1         | Optional pointer to internal TDR recovery context (TDR\_RECOVERY\_CONTEXT). |
| 2         | The pointer into responsible device driver module (e.g owner tag).          |
| 3         | The secondary driver specific bucketing key.                                |
| 4         | Optional internal context dependent data.                                   |

 

## Remarks

The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

Secondary data of tag {270A33FD-3DA6-460D-BA89-3C1BAE21E39B} contains additional TDR related data. Use [**.enumtag**](../debuggercmds/-enumtag--enumerate-secondary-callback-data-.md) to view the data.

 

 




