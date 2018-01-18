---
title: DrvAckIoStop rule (kmdf)
description: The DrvAckIoStop rule verifies that the driver is aware of pending requests while its power-managed queue is getting powered-down and the driver acknowledges, completes, or cancels the pending requests accordingly.
ms.assetid: 4C6F8919-C3DF-4DE2-94EF-45475CE9E0C0
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20DrvAckIoStop%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




