---
title: PendedCompletedRequest rule (wdm)
description: The PendedCompletedRequest rule specifies that a driver's dispatch routine does not return STATUS\_PENDING on an IRP if the driver has called IoCompleteRequest on the incoming IRP.
ms.assetid: 875409b0-b91c-44e6-8240-c5e656b70048
keywords: ["PendedCompletedRequest rule (wdm)"]
topic_type:
- apiref
api_name:
- PendedCompletedRequest
api_type:
- NA
---

# PendedCompletedRequest rule (wdm)


The **PendedCompletedRequest** rule specifies that a driver's dispatch routine does not return STATUS\_PENDING on an IRP if the driver has called [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) on the incoming IRP.

This rule is not applied if the driver begins executing any dispatch routines.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PendedCompletedRequest</strong> rule.</p>
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

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)
[**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137)
[**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 





