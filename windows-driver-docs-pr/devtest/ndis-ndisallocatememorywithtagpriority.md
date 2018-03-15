---
title: NdisAllocateMemoryWithTagPriority rule (ndis)
description: The NdisAllocateMemoryWithTagPriority rule specifies that a driver must not call NdisAllocateMemoryWithTagPriority without providing a Tag.Every memory allocation should use a unique pool tag to ensure that kernel debuggers and Driver Verifier can identify a distinct allocated block of memory.
ms.assetid: e27fe997-366d-4fe1-ad1e-3f145dc55f30
keywords: ["NdisAllocateMemoryWithTagPriority rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisAllocateMemoryWithTagPriority
api_type:
- NA
---

# NdisAllocateMemoryWithTagPriority rule (ndis)


The **NdisAllocateMemoryWithTagPriority** rule specifies that a driver must not call **NdisAllocateMemoryWithTagPriority** without providing a *Tag*.

Every memory allocation should use a unique pool tag to ensure that kernel debuggers and Driver Verifier can identify a distinct allocated block of memory.

|              |      |
|--------------|------|
| Driver model | NDIS |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisAllocateMemoryWithTagPriority</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**NdisAllocateMemoryWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff561606)
 

 





