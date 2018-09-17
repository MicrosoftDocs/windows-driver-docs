---
title: NsRemoveLockMnRemove rule (wdm)
description: The NsRemoveLockMnRemove rule verifies a driver does not return STATUS\_NOT\_SUPPORTED when processing IRP\_MJ\_PNP with MinorFunction IRP\_MN\_REMOVE\_DEVICE. This rule only applies to FDO and FIDO drivers.
ms.assetid: 1151343D-9CFD-4808-A885-D477F199C004
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["NsRemoveLockMnRemove rule (wdm)"]
topic_type:
- apiref
api_name:
- NsRemoveLockMnRemove
api_type:
- NA
ms.localizationpriority: medium
---

# NsRemoveLockMnRemove rule (wdm)


The **NsRemoveLockMnRemove** rule verifies a driver does not return STATUS\_NOT\_SUPPORTED when processing IRP\_MJ\_PNP with MinorFunction IRP\_MN\_REMOVE\_DEVICE. This rule only applies to FDO and FIDO drivers.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NsRemoveLockMnRemove</strong> rule.</p>
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
 

 





