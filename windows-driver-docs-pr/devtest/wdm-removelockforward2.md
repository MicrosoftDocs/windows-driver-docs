---
title: RemoveLockForward2 rule (wdm)
description: The RemoveLockForward2 rule verifies that calls to IoAcquireRemoveLock and IoReleaseRemoveLock are used correctly when forwarding the IRP to another device.
ms.assetid: 1C04BCCF-5458-4524-88EF-AF5216588AC3
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["RemoveLockForward2 rule (wdm)"]
topic_type:
- apiref
api_name:
- RemoveLockForward2
api_type:
- NA
---

# RemoveLockForward2 rule (wdm)


The **RemoveLockForward2** rule verifies that calls to [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly when forwarding the IRP to another device.

Note this rule does not check IRP\_MN\_REMOVE\_DEVICE, IRP\_MN\_QUERY\_DEVICE or IRP\_MN\_SUPRISE\_REMOVAL IRPs.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>RemoveLockForward2</strong> rule.</p>
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
[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoCsqInsertIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549066)
[**IoCsqInsertIrpEx**](https://msdn.microsoft.com/library/windows/hardware/ff549067)
[**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 





