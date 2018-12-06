---
title: PcIrqlIport rule (audio)
description: The PcIrqlIport rule specifies that a PortCls miniport driver must call PortCls IPort interfaces at the correct IRQL level.
ms.assetid: 59E22F37-3377-4B98-8613-EF5ED0CB63D9
ms.date: 05/21/2018
keywords: ["PcIrqlIport rule (audio)"]
topic_type:
- apiref
api_name:
- PcIrqlIport
api_type:
- NA
ms.localizationpriority: medium
---

# PcIrqlIport rule (audio)


The PcIrqlIport rule specifies that a PortCls miniport driver must call PortCls IPort interfaces at the correct IRQL level.

|              |       |
|--------------|-------|
| Driver model | Audio |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00071003) |

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

 

 

 





