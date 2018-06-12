---
title: PendedCompletedRequest3 rule (wdm)
description: The PendedCompletedRequest3 rule specifies that a pending IRP should not be completed with a call to IoCompleteRequest.
ms.assetid: 051D8E8C-4C06-4497-A099-D038DC9152FA
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["PendedCompletedRequest3 rule (wdm)"]
topic_type:
- apiref
api_name:
- PendedCompletedRequest3
api_type:
- NA
---

# PendedCompletedRequest3 rule (wdm)


The **PendedCompletedRequest3** rule specifies that a pending IRP should not be completed with a call to [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PendedCompletedRequest3</strong> rule.</p>
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
[**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422)
[**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 





