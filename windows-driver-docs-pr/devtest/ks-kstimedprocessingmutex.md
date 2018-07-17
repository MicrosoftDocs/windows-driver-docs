---
title: KsTimedProcessingMutex rule ()
description: The KsTimedProcessingMutex rule specifies that a KS miniport driver should not hold a processing mutex for more than 100 milliseconds.
ms.assetid: 18246AAE-6328-4171-973E-4C762CF719AE
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["KsTimedProcessingMutex rule ()"]
topic_type:
- apiref
api_name:
- KsTimedProcessingMutex
api_type:
- NA
---

# KsTimedProcessingMutex rule ()


The KsTimedProcessingMutex rule specifies that a KS miniport driver should not hold a processing mutex for more than 100 milliseconds.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00082005) |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>To verify this rule, open a Command Prompt window. Enter a Driver Verifier command and specify <strong>/domain ks</strong>.</p>
<p>For example:</p>
<p><strong>verifier /domain ks</strong> [<em>options</em>] <strong>/driver</strong> <em>&lt;yourdriver&gt;</em></p>
<p>For more information, see [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).</p></td>
</tr>
</tbody>
</table>

 

See also
--------

[Processing Mutex in AVStream](https://msdn.microsoft.com/library/windows/hardware/ff567790)
 

 





