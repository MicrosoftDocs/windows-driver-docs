---
title: PcPoRequestPowerIrp rule (audio)
description: This rule verifies that a PortCls miniport driver should not call PoRequestPowerIrp with IRP\_MN\_SET\_POWER.
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


This rule verifies that a PortCls miniport driver should not call [**PoRequestPowerIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-porequestpowerirp) with [**IRP\_MN\_SET\_POWER**](../kernel/irp-mn-set-power.md).

**Driver model: Audio**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x0007100A)


## How to test

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
<p>For more information, see <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

