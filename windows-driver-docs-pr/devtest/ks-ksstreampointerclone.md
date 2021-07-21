---
title: KsStreamPointerClone rule ()
description: The KsStreamPointerClone rule specifies that a kernel-stream (KS) miniport driver correctly uses the KsStreamPointerClone and KsStreamPointerDelete functions.
ms.date: 05/21/2018
keywords: ["KsStreamPointerClone rule ()"]
topic_type:
- apiref
api_name:
- KsStreamPointerClone
api_type:
- NA
ms.localizationpriority: medium
---

# KsStreamPointerClone rule ()


The KsStreamPointerClone rule specifies that a kernel-stream (KS) miniport driver correctly uses the [**KsStreamPointerClone**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerclone) and [**KsStreamPointerDelete**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerdelete) functions.

**Driver model: KS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00081002)


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
<td align="left"><p>To verify this rule, open a Command Prompt window. Enter a Driver Verifier command and specify <strong>/domain ks</strong>.</p>
<p>For example:</p>
<p><strong>verifier /domain ks</strong> [<em>options</em>] <strong>/driver</strong> <em>&lt;yourdriver&gt;</em></p>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

