---
title: DrvAckIoStop rule (kmdf)
description: The DrvAckIoStop rule verifies that the driver is aware of pending requests while its power-managed queue is getting powered-down and the driver acknowledges, completes, or cancels the pending requests accordingly.
ms.assetid: 4C6F8919-C3DF-4DE2-94EF-45475CE9E0C0
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["DrvAckIoStop rule (kmdf)"]
topic_type:
- apiref
api_name:
- DrvAckIoStop
api_type:
- NA
---

# DrvAckIoStop rule (kmdf)


The **DrvAckIoStop** rule verifies that the driver is aware of pending requests while its power-managed queue is getting powered-down and the driver acknowledges, completes, or cancels the pending requests accordingly. In the case of self-managed I/O requests, the driver should also correctly handle these requests from its [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907) function. A driver that fails to handle these requests during a power-down would cause [**Bug Check 0x9F: DRIVER\_POWER\_STATE\_FAILURE**](https://msdn.microsoft.com/library/windows/hardware/ff559329).

In some circumstances it might be appropriate to to suppress this warning. If the driver does not hold on to the requests, or does not forward them to other drivers, and if the driver completes the requests directly in the queue's handlers, you can use the **\_\_analysis\_assume** function to suppress the warning. For more information, see [Using the \_analysis\_assume Function to Suppress False Defects](https://msdn.microsoft.com/library/windows/hardware/ff556059) and [**How to: Specify Additional Code Information by Using \_\_analysis\_assume**](https://msdn.microsoft.com/library/windows/hardware/ms404702).

|              |      |
|--------------|------|
| Driver model | KMDF |

|                                   |                                                                                                          |
|-----------------------------------|----------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0x9F: DRIVER\_POWER\_STATE\_FAILURE**](https://msdn.microsoft.com/library/windows/hardware/ff559329) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DrvAckIoStop</strong> rule.</p>
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

[**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135)
[**WdfFdoInitSetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff547273)
[**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401)
 

 





