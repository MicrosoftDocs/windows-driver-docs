---
title: IrpCancelField rule (wdm)
description: The IrpCancelField rule specifies that the driver check the value of the Irp- Cancel member when setting a cancel routine on an IRP that it has pended.
ms.assetid: e9221436-21ca-47f0-9dc4-e8b1a7a44854
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrpCancelField rule (wdm)"]
topic_type:
- apiref
api_name:
- IrpCancelField
api_type:
- NA
ms.localizationpriority: medium
---

# IrpCancelField rule (wdm)


The **IrpCancelField** rule specifies that the driver check the value of the **Irp-&gt;Cancel** member when setting a cancel routine on an IRP that it has pended.

Static Driver Verifier applies this rule at the end of the driver's [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine and at the end of the driver's dispatch routine.

For information about how a driver should handle IRP cancellation, see [**Synchronizing IRP Cancellation**](https://msdn.microsoft.com/library/windows/hardware/ff564531).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrpCancelField</strong> rule.</p>
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

[**IoCsqInsertIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549066)
[**IoCsqInsertIrpEx**](https://msdn.microsoft.com/library/windows/hardware/ff549067)
[**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422)
[**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674)
See also
--------

[**Synchronizing IRP Cancellation**](https://msdn.microsoft.com/library/windows/hardware/ff564531)
 

 





