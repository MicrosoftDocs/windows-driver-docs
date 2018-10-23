---
title: CompleteRequest rule (wdm)
description: The CompleteRequest rule verifies that the IoCompleteRequest routine is not called after a completion routine runs and that it does not return STATUS\_MORE\_PROCESSING\_REQUIRED.
ms.assetid: 2F6BA5D9-EC31-4C5D-8C98-EE33CE487498
ms.date: 05/21/2018
keywords: ["CompleteRequest rule (wdm)"]
topic_type:
- apiref
api_name:
- CompleteRequest
api_type:
- NA
ms.localizationpriority: medium
---

# CompleteRequest rule (wdm)


The **CompleteRequest** rule verifies that the [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) routine is not called after a completion routine runs and that it does not return STATUS\_MORE\_PROCESSING\_REQUIRED.

This rule reports a defect if:

-   The driver calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) when the driver does not own the request.

-   The driver fails to call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) when completion is required.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>CompleteRequest</strong> rule.</p>
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

[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)
[**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 





