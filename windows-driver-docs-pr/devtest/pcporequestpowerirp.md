---
title: PcPoRequestPowerIrp rule (audio)
description: This rule verifies that a PortCls miniport driver should not call PoRequestPowerIrp with IRP\_MN\_SET\_POWER.
ms.assetid: 9AF26E98-CB8A-41F1-BF40-1B5FBFD04550
ms.date: 05/21/2018
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


This rule verifies that a PortCls miniport driver should not call [**PoRequestPowerIrp**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-porequestpowerirp) with [**IRP\_MN\_SET\_POWER**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-set-power).

|              |       |
|--------------|-------|
| Driver model | Audio |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) (0x0007100A) |

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
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 





