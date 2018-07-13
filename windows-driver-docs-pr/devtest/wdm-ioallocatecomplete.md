---
title: IoAllocateComplete rule
description: The IoAllocateComplete rule specifies that a driver should not call IoCompleteRequest if the IRP was created with IoAllocateIrp.
ms.assetid: BCF1F1DF-3586-46D0-85B5-1F5A2DEE18D1
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IoAllocateComplete rule"]
topic_type:
- apiref
api_name:
- IoAllocateComplete
api_type:
- NA
---

# IoAllocateComplete rule


The **IoAllocateComplete** rule specifies that a driver should not call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) if the IRP was created with [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoAllocateComplete</strong> rule.</p>
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

[**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257)
[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
 

 





