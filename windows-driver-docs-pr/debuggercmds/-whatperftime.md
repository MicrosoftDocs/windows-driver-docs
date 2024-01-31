---
title: whatperftime
description: The whatperftime extension converts a high-resolution performance counter value into a standard time value.
keywords: ["performance count", "whatperftime Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- whatperftime
api_type:
- NA
---

# !whatperftime


The **!whatperftime** extension converts a high-resolution performance counter value into a standard time value.

```dbgcmd
!whatperftime Count
```

## Parameters


<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
The performance counter clock value.

## DLL

Windows XP and later - Kdexts.dll

 

## Remarks

You can use **!whatperftime** to convert values retrieved by calling **QueryPerformanceCounter**. Performance counter time values are also found in software traces.

The output is displayed as *HH:MM:SS.mmm*. Here is an example:

```dbgcmd
kd> !whatperftime 304589
3163529 Performance Counter in Standard Time: .004.313s
```

 

 





