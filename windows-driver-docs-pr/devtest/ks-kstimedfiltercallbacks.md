---
title: KsTimedFilterCallbacks rule ()
description: The KsTimedFilterCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a filter callback function within 500 ms.
ms.assetid: 5F631D49-405F-4F1A-A280-FEFB4ADA460D
ms.date: 05/21/2018
keywords: ["KsTimedFilterCallbacks rule ()"]
topic_type:
- apiref
api_name:
- KsTimedFilterCallbacks
api_type:
- NA
ms.localizationpriority: medium
---

# KsTimedFilterCallbacks rule ()


The KsTimedFilterCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a filter callback function within 500 ms.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00082003) |

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
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 





