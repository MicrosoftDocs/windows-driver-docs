---
title: MarkPowerDown rule (wdm)
description: The MarkPowerDown rule specifies that an IRP\_MJ\_POWER with IRP\_MN\_SET\_POWER for SystemPowerState IRP going from s0 to \ S1...S5\ is pended.
ms.assetid: 5C35F607-1550-4B48-8325-8A01D522786F
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["MarkPowerDown rule (wdm)"]
topic_type:
- apiref
api_name:
- MarkPowerDown
api_type:
- NA
ms.localizationpriority: medium
---

# MarkPowerDown rule (wdm)


The **MarkPowerDown** rule specifies that an IRP\_MJ\_POWER with IRP\_MN\_SET\_POWER for **SystemPowerState** IRP going from s0 to \[S1...S5\] is pended.

This rule only applies to FDO and FIDO drivers.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>MarkPowerDown</strong> rule.</p>
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
[**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoGetDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff549186)
[**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422)
[**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526)
[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)
[**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 





