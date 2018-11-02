---
title: whatperftime
description: The whatperftime extension converts a high-resolution performance counter value into a standard time value.
ms.assetid: ff11a51f-4e25-4cf3-be19-d38361c441e9
keywords: ["performance count", "whatperftime Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- whatperftime
api_type:
- NA
ms.localizationpriority: medium
---

# !whatperftime


The **!whatperftime** extension converts a high-resolution performance counter value into a standard time value.

```dbgcmd
!whatperftime Count
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
The performance counter clock value.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can use **!whatperftime** to convert values retrieved by calling **QueryPerformanceCounter**. Performance counter time values are also found in software traces.

The output is displayed as *HH:MM:SS.mmm*. Here is an example:

```dbgcmd
kd> !whatperftime 304589
3163529 Performance Counter in Standard Time: .004.313s
```

 

 





