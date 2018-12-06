---
title: KsStreamPointerLock rule ()
description: The KsStreamPointerLock rule specifies that a kernel-streaming (KS) miniport driver uses the KsStreamPointerLock and KsStreamPointerUnlock functions in the correct sequence.
ms.assetid: 365C8656-57F1-4774-9859-B67D64403BB3
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


The KsStreamPointerLock rule specifies that a kernel-streaming (KS) miniport driver uses the [**KsStreamPointerLock**](https://msdn.microsoft.com/library/windows/hardware/ff567134) and [**KsStreamPointerUnlock**](https://msdn.microsoft.com/library/windows/hardware/ff567137) functions in the correct sequence.

That is, the miniport driver must not try to lock a stream pointer that is already locked, or try to unlock a stream pointer that is not already locked.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00081003) |

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
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 





