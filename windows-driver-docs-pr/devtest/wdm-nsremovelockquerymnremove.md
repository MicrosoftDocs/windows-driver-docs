---
title: NsRemoveLockQueryMnRemove rule (wdm)
description: The NsRemoveLockQueryMnRemove rule verifies a driver does not return STATUS\_NOT\_SUPPORTED when processing IRP\_MJ\_PNP with MinorFunction IRP\_MN\_QUERY\_REMOVE. This rule only applies to FDO and FIDO drivers.
ms.assetid: D6B22269-96D0-449A-B32D-F038D4AA065F
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["NsRemoveLockQueryMnRemove rule (wdm)"]
topic_type:
- apiref
api_name:
- NsRemoveLockQueryMnRemove
api_type:
- NA
ms.localizationpriority: medium
---

# NsRemoveLockQueryMnRemove rule (wdm)


The **NsRemoveLockQueryMnRemove** rule verifies a driver does not return STATUS\_NOT\_SUPPORTED when processing IRP\_MJ\_PNP with MinorFunction IRP\_MN\_QUERY\_REMOVE. This rule only applies to FDO and FIDO drivers.

|              |     |
|--------------|-----|
| Driver model | WDM |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NsRemoveLockQueryMnRemove</strong> rule.</p>
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

[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
 

 





