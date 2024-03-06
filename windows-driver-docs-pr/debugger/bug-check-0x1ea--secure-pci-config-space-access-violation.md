---
title: Bug Check 0x1EA SECURE_PCI_CONFIG_SPACE_ACCESS_VIOLATION
description: The SECURE_PCI_CONFIG_SPACE_ACCESS_VIOLATION bug check has a value of 0x000001EA. This indicates that the the access to the PCI config space region from VTL0 by directly mapping the PCI MCFG range is prohibited because secure PCI is enabled.
keywords: ["Bug Check 0x1EA SECURE_PCI_CONFIG_SPACE_ACCESS_VIOLATION", "SECURE_PCI_CONFIG_SPACE_ACCESS_VIOLATION"]
ms.date: 08/03/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- SECURE_PCI_CONFIG_SPACE_ACCESS_VIOLATION
api_type:
- NA
---

# Bug Check 0x1EA: SECURE\_PCI\_CONFIG\_SPACE\_ACCESS\_VIOLATION

The SECURE\_PCI\_CONFIG\_SPACE\_ACCESS\_VIOLATION bug check has a value of 0x000001EA. This indicates that the access to the PCI config space region from VTL0 by directly mapping the PCI MCFG range is prohibited because secure PCI is enabled.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## SECURE_PCI_CONFIG\_SPACE\_ACCESS\_VIOLATION Parameters

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">1</td>
<td align="left">Opcode that caused the exception.</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">RID of the device that caused the exception.</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Config space access offset.</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Address of the instruction that caused the exception.</td>
</tr>
</tbody>
</table>


## Resolution

The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
