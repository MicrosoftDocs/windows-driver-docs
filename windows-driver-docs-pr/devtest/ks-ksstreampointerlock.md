---
title: KsStreamPointerLock rule ()
description: The KsStreamPointerLock rule specifies that a kernel-streaming (KS) miniport driver uses the KsStreamPointerLock and KsStreamPointerUnlock functions in the correct sequence.
ms.date: 05/21/2018
keywords: ["KsStreamPointerLock rule ()"]
topic_type:
- apiref
api_name:
- KsStreamPointerLock
api_type:
- NA
ms.localizationpriority: medium
---

# KsStreamPointerLock rule ()


The KsStreamPointerLock rule specifies that a kernel-streaming (KS) miniport driver uses the [**KsStreamPointerLock**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerlock) and [**KsStreamPointerUnlock**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerunlock) functions in the correct sequence.

That is, the miniport driver must not try to lock a stream pointer that is already locked, or try to unlock a stream pointer that is not already locked.

**Driver model: KS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00081003)


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

 

