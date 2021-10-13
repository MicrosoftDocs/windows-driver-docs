---
title: PcRegisterAdapterPower rule (audio)
description: The PcRegisterAdapterPower rule specifies that a PortCls miniport driver should not Call PcRegisterAdapterPowerManagement twice without an intervening call to PcUnregisterAdapterPowerManagement.Call PcUnregisterAdapterPowerManagement without calling PcRegisterAdapterPowerManagement first.
ms.date: 05/21/2018
keywords: ["PcRegisterAdapterPower rule (audio)"]
topic_type:
- apiref
api_name:
- PcRegisterAdapterPower
api_type:
- NA
ms.localizationpriority: medium
---

# PcRegisterAdapterPower rule (audio)


The PcRegisterAdapterPower rule specifies that a PortCls miniport driver should not:

-   Call [**PcRegisterAdapterPowerManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisteradapterpowermanagement) twice without an intervening call to [**PcUnregisterAdapterPowerManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcunregisteradapterpowermanagement).
-   Call [**PcUnregisterAdapterPowerManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcunregisteradapterpowermanagement) without calling [**PcRegisterAdapterPowerManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisteradapterpowermanagement) first.

**Driver model: Audio**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00071006)


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

 

