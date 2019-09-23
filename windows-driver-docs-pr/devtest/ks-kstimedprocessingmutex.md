---
title: KsTimedProcessingMutex rule ()
description: The KsTimedProcessingMutex rule specifies that a KS miniport driver should not hold a processing mutex for more than 100 milliseconds.
ms.assetid: 18246AAE-6328-4171-973E-4C762CF719AE
ms.date: 05/21/2018
keywords: ["KsTimedProcessingMutex rule ()"]
topic_type:
- apiref
api_name:
- KsTimedProcessingMutex
api_type:
- NA
ms.localizationpriority: medium
---

# KsTimedProcessingMutex rule ()


The KsTimedProcessingMutex rule specifies that a KS miniport driver should not hold a processing mutex for more than 100 milliseconds.

|              |     |
|--------------|-----|
| Driver model | KS  |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) (0x00082005) |

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

[Processing Mutex in AVStream](https://docs.microsoft.com/windows-hardware/drivers/stream/processing-mutex-in-avstream)
 

 





