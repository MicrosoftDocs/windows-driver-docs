---
title: KsFilterMutex rule ()
description: The KsFilterMutex rule specifies that a KS miniport driver acquires and releases the filter mutex in the correct sequence.
ms.date: 05/21/2018
keywords: ["KsFilterMutex rule ()"]
topic_type:
- apiref
api_name:
- KsFilterMutex
api_type:
- NA
ms.localizationpriority: medium
---

# KsFilterMutex rule ()


The KsFilterMutex rule specifies that a KS miniport driver acquires and releases the filter mutex in the correct sequence.

-   A KS miniport driver cannot obtain the filter mutex recursively.
-   A thread should not release the filter mutex without acquiring it first.

**Driver model: KS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x0008100A)


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
<p></p>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a>.</p></td>
</tr>
</tbody>
</table>

 

**verifier /domain ks** \[*options*\] **/driver** *&lt;yourdriver&gt;*
## See also

[Filter Control Mutex in AVStream](../stream/filter-control-mutex-in-avstream.md)
