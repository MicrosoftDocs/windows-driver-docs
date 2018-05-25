---
title: PcRegisterAdapterPower rule (audio)
description: The PcRegisterAdapterPower rule specifies that a PortCls miniport driver should not Call PcRegisterAdapterPowerManagement twice without an intervening call to PcUnregisterAdapterPowerManagement.Call PcUnregisterAdapterPowerManagement without calling PcRegisterAdapterPowerManagement first.
ms.assetid: 8F6E6B1D-F19C-469A-BC5A-061996BEA532
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["PcRegisterAdapterPower rule (audio)"]
topic_type:
- apiref
api_name:
- PcRegisterAdapterPower
api_type:
- NA
---

# PcRegisterAdapterPower rule (audio)


The PcRegisterAdapterPower rule specifies that a PortCls miniport driver should not:

-   Call [**PcRegisterAdapterPowerManagement**](https://msdn.microsoft.com/library/windows/hardware/ff537724) twice without an intervening call to [**PcUnregisterAdapterPowerManagement**](https://msdn.microsoft.com/library/windows/hardware/ff537735).
-   Call [**PcUnregisterAdapterPowerManagement**](https://msdn.microsoft.com/library/windows/hardware/ff537735) without calling [**PcRegisterAdapterPowerManagement**](https://msdn.microsoft.com/library/windows/hardware/ff537724) first.

|              |       |
|--------------|-------|
| Driver model | Audio |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00071006) |

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

 

 

 





