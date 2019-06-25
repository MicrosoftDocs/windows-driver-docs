---
title: KsTimedDeviceCallbacks rule ()
description: The KsTimedDeviceCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a device callback function within 500 ms.
ms.assetid: 05393761-9018-4DAA-B8B5-EFEBBCDAB955
ms.date: 05/21/2018
keywords: ["KsTimedDeviceCallbacks rule ()"]
topic_type:
- apiref
api_name:
- KsTimedDeviceCallbacks
api_type:
- NA
ms.localizationpriority: medium
---

# KsTimedDeviceCallbacks rule ()


The KsTimedDeviceCallbacks rule specifies that a kernel-streaming (KS) miniport driver returns from a device callback function within 500 ms.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) (0x00082002) |

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
<td align="left"><p>To verify this rule, open a Command Prompt window. Enter a Driver Verifier command and specify <strong>/domain ks</strong>.</p>
<p>For example:</p>
<p><strong>verifier /domain ks</strong> [<em>options</em>] <strong>/driver</strong> <em>&lt;yourdriver&gt;</em></p>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

See also
--------

[Locking and Unlocking Stream Pointers](https://docs.microsoft.com/windows-hardware/drivers/stream/locking-and-unlocking-stream-pointers)
 

 





