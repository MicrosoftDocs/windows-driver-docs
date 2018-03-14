---
title: IoAllocateFree rule
description: The IoAllocateFree rule specifies that a driver should use IoFreeIrp only on IRPs that were previously allocated with IoAllocateIrp.
ms.assetid: 902CC117-9B46-4F3E-A836-80F518E01281
keywords: ["IoAllocateFree rule"]
topic_type:
- apiref
api_name:
- IoAllocateFree
api_type:
- NA
---

# IoAllocateFree rule


The **IoAllocateFree** rule specifies that a driver should use [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113) only on IRPs that were previously allocated with [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoAllocateFree</strong> rule.</p>
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

[**ExInterlockedInsertHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff545397)
[**ExInterlockedInsertTailList**](https://msdn.microsoft.com/library/windows/hardware/ff545402)
[**ExInterlockedPushEntryList**](https://msdn.microsoft.com/library/windows/hardware/ff545418)
[**InsertHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff547820)
[**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257)
[**IoCsqInsertIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549066)
[**IoCsqInsertIrpEx**](https://msdn.microsoft.com/library/windows/hardware/ff549067)
[**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 





