---
title: KsDeviceMutex rule ()
description: The KsDeviceMutex rule specifies that a kernel streaming miniport driver uses KsAcquireDevice and KsReleaseDevice in the correct sequence. That is, every call to KsAcquireDevice must have a corresponding call to KsReleaseDevice.
ms.date: 05/21/2018
keywords: ["KsDeviceMutex rule ()"]
topic_type:
- apiref
api_name:
- KsDeviceMutex
api_type:
- NA
ms.localizationpriority: medium
---

# KsDeviceMutex rule ()


The **KsDeviceMutex** rule specifies that a kernel streaming miniport driver uses [**KsAcquireDevice**](/windows-hardware/drivers/ddi/ks/nf-ks-ksacquiredevice) and [**KsReleaseDevice**](/windows-hardware/drivers/ddi/ks/nf-ks-ksreleasedevice) in the correct sequence. That is, every call to **KsAcquireDevice** must have a corresponding call to **KsReleaseDevice**.

**Driver model: KS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00081001)


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

 

