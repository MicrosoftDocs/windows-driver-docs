---
title: KsProcessingMutex Rule ()
ms.date: 05/21/2018
description: "Learn more about: KsProcessingMutex rule ()"
keywords: ["KsProcessingMutex rule ()"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KsProcessingMutex
api_type:
- NA
---

# KsProcessingMutex rule ()


The KsProcessingMutex rule specifies that a KS miniport driver uses the processing mutex in the correct sequence:

-   The processing mutex cannot be obtained recursively.
-   A thread that has acquired the processing mutex should not subsequently attempt to acquire the filter control mutex.
-   A thread should not release the processing mutex without acquiring it first.

**Driver model: KS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x0008100B)


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

 

## See also

[Processing Mutex in AVStream](../stream/processing-mutex-in-avstream.md)
