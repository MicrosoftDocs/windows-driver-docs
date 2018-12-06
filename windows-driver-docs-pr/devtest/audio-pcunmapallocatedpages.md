---
title: PcUnmapAllocatedPages rule (audio)
description: The PcUnmapAllocatedPages rule specifies that A PortCls miniport driver doesn't map an MDL that is currently mapped without first unmapping it.A PortCls miniport driver unmaps the memory prior to freeing it using the IMiniportWaveRTStream interface.
ms.assetid: 0ADF523C-9480-4AD2-8B98-23C95571CB0B
ms.date: 05/21/2018
keywords: ["PcUnmapAllocatedPages rule (audio)"]
topic_type:
- apiref
api_name:
- PcUnmapAllocatedPages
api_type:
- NA
ms.localizationpriority: medium
---

# PcUnmapAllocatedPages rule (audio)


The PcUnmapAllocatedPages rule specifies that:

-   A PortCls miniport driver doesn't map an MDL that is currently mapped without first unmapping it.
-   A PortCls miniport driver unmaps the memory prior to freeing it using the [IMiniportWaveRTStream](https://msdn.microsoft.com/library/windows/hardware/ff536738) interface.

|              |       |
|--------------|-------|
| Driver model | Audio |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00071004) |

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

 

 

 





