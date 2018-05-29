---
title: KsIrqlDDIs rule ()
description: The KsIrqlDDIs rule specifies that a kernel-streaming (KS) miniport driver calls KS DDIs at the correct IRQL level.
ms.assetid: 060CAFBC-3BA6-40C7-91A1-8AFCB082A683
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["KsIrqlDDIs rule ()"]
topic_type:
- apiref
api_name:
- KsIrqlDDIs
api_type:
- NA
---

# KsIrqlDDIs rule ()


The KsIrqlDDIs rule specifies that a kernel-streaming (KS) miniport driver calls KS DDIs at the correct IRQL level.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00081009) |

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

 

 

 





