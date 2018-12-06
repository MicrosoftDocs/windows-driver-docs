---
title: PcAllocatedPages rule (audio)
description: The PcAllocatedPages rule specifies that a PortCls miniport driver frees previous allocated pages by calling AllocatePagesForMdl or AllocateContiguousPagesForMdl methods.
ms.assetid: C27B8D30-AE94-4B17-A45B-EBECB8A7B132
ms.date: 05/21/2018
keywords: ["PcAllocatedPages rule (audio)"]
topic_type:
- apiref
api_name:
- PcAllocatedPages
api_type:
- NA
ms.localizationpriority: medium
---

# PcAllocatedPages rule (audio)


The PcAllocatedPages rule specifies that a PortCls miniport driver frees previous allocated pages by calling AllocatePagesForMdl or AllocateContiguousPagesForMdl methods.

|              |       |
|--------------|-------|
| Driver model | Audio |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00071005) |

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
<td align="left"><p>To verify this rule, open a Command Prompt window. Enter a Driver Verifier command and specify <strong>/domain audio</strong>.</p>
<p>For example:</p>
<p><strong>verifier /domain audio</strong> [<em>options</em>] <strong>/driver</strong> <em>&lt;yourdriver&gt;</em></p>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 





