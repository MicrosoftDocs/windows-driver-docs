---
title: Bug Check 0xF6 PCI_VERIFIER_DETECTED_VIOLATION
description: The PCI_VERIFIER_DETECTED_VIOLATION bug check has a value of 0x000000F6. This indicates that an error occurred in the BIOS or another device being verified by the PCI driver.
keywords: ["Bug Check 0xF6 PCI_VERIFIER_DETECTED_VIOLATION", "PCI_VERIFIER_DETECTED_VIOLATION"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- PCI_VERIFIER_DETECTED_VIOLATION
api_type:
- NA
---

# Bug Check 0xF6: PCI\_VERIFIER\_DETECTED\_VIOLATION


The PCI\_VERIFIER\_DETECTED\_VIOLATION bug check has a value of 0x000000F6. This indicates that an error occurred in the BIOS or another device being verified by the PCI driver.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## PCI\_VERIFIER\_DETECTED\_VIOLATION Parameters


Parameter 1 is the only parameter of interest; this identifies the nature of the failure detected.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x01</p></td>
<td align="left"><p>An active bridge was reprogrammed by the BIOS during a docking event.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x02</p></td>
<td align="left"><p>The PMCSR register was not updated within the spec-mandated time.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x03</p></td>
<td align="left"><p>A driver has written to Windows-controlled portions of a PCI device's configuration space.</p></td>
</tr>
</tbody>
</table>

 

## Cause

The PCI driver detected an error in a device or BIOS being verified.

 

 




