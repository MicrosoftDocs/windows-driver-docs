---
title: Cleanup4CtlDeviceRegistered rule (kmdf)
description: The Cleanup4CtlDeviceRegistered rule specifies that if a Plug and Play (PnP) driver calls WdfDeviceCreate for the control device object, the driver must register one of the required event callback functions.
ms.assetid: f439ec36-f7af-46e5-8ddd-11e444bf36da
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Cleanup4CtlDeviceRegistered rule (kmdf)"]
topic_type:
- apiref
api_name:
- Cleanup4CtlDeviceRegistered
api_type:
- NA
---

# Cleanup4CtlDeviceRegistered rule (kmdf)


The **Cleanup4CtlDeviceRegistered** rule specifies that if a Plug and Play (PnP) driver calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) for the control device object, the driver must register one of the required event callback functions.

The event callback function can be one of the following:

[*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) or [*EvtDestroyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540841) in the [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure for the control device
-or-
[*EvtDeviceSelfManagedIoCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540898) in the [**WDF\_PNPPOWER\_EVENT\_CALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff552416) structure
|              |      |
|--------------|------|
| Driver model | KMDF |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Cleanup4CtlDeviceRegistered</strong> rule.</p>
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

 

 





