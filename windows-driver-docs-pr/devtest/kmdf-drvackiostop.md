---
title: DrvAckIoStop rule (kmdf)
description: The DrvAckIoStop rule verifies that the driver is aware of pending requests while its power-managed queue is getting powered-down and the driver acknowledges, completes, or cancels the pending requests accordingly.
ms.assetid: 4C6F8919-C3DF-4DE2-94EF-45475CE9E0C0
ms.date: 05/21/2018
keywords: ["DrvAckIoStop rule (kmdf)"]
topic_type:
- apiref
api_name:
- DrvAckIoStop
api_type:
- NA
ms.localizationpriority: medium
---

# DrvAckIoStop rule (kmdf)


The **DrvAckIoStop** rule verifies that the driver is aware of pending requests while its power-managed queue is getting powered-down and the driver acknowledges, completes, or cancels the pending requests accordingly. In the case of self-managed I/O requests, the driver should also correctly handle these requests from its [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907) function. A driver that fails to handle these requests during a power-down would cause [**Bug Check 0x9F: DRIVER\_POWER\_STATE\_FAILURE**](https://msdn.microsoft.com/library/windows/hardware/ff559329).

In some circumstances it might be appropriate to suppress this warning. If the driver does not hold on to the requests, or does not forward them to other drivers, and if the driver completes the requests directly in the queue's handlers, you can use the **\_\_analysis\_assume** function to suppress the warning. For more information, see [Using the \_analysis\_assume Function to Suppress False Defects](https://msdn.microsoft.com/library/windows/hardware/ff556059) and [**How to: Specify Additional Code Information by Using \_\_analysis\_assume**](https://msdn.microsoft.com/library/windows/hardware/ms404702).

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>DrvAckIoStop</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135)
[**WdfFdoInitSetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff547273)
[**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401)
 

 





