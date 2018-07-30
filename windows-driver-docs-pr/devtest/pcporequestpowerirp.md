---
title: PcPoRequestPowerIrp rule (audio)
description: This rule verifies that a PortCls miniport driver should not call PoRequestPowerIrp with IRP\_MN\_SET\_POWER.
ms.assetid: 9AF26E98-CB8A-41F1-BF40-1B5FBFD04550
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["PcPoRequestPowerIrp rule (audio)"]
topic_type:
- apiref
api_name:
- PcPoRequestPowerIrp
api_type:
- NA
ms.localizationpriority: medium
---

# PcPoRequestPowerIrp rule (audio)


This rule verifies that a PortCls miniport driver should not call [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) with [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744).

|              |       |
|--------------|-------|
| Driver model | Audio |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0007100A) |

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
<p>For more information, see [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).</p></td>
</tr>
</tbody>
</table>

 

 

 





