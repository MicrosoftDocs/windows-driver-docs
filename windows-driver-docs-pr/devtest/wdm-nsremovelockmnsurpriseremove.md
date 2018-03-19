---
title: NsRemoveLockMnSurpriseRemove rule (wdm)
description: The NsRemoveLockMnSurpriseRemove rule verifies that a driver does not return STATUS\_NOT\_SUPPORTED when processing an IRP\_MJ\_PNP request with minorFunction IRP\_MN\_SUPRISE\_REMOVAL. This rule only applies to FDO and FIDO drivers.
ms.assetid: A7F444B1-615F-4DE2-B1AF-C179C5103DD9
keywords: ["NsRemoveLockMnSurpriseRemove rule (wdm)"]
topic_type:
- apiref
api_name:
- NsRemoveLockMnSurpriseRemove
api_type:
- NA
---

# NsRemoveLockMnSurpriseRemove rule (wdm)


The **NsRemoveLockMnSurpriseRemove** rule verifies that a driver does not return STATUS\_NOT\_SUPPORTED when processing an IRP\_MJ\_PNP request with minorFunction IRP\_MN\_SUPRISE\_REMOVAL. This rule only applies to FDO and FIDO drivers.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NsRemoveLockMnSurpriseRemove</strong> rule.</p>
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
 

 





