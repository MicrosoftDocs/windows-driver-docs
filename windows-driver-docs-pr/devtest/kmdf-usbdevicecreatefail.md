---
title: UsbDeviceCreateFail rule (kmdf)
description: The UsbDeviceCreateFail rule specifies that the driver returns from the EvtDevicePrepareHardware event callback function with an error status if creation of a WDFUSBDEVICE object fails.
ms.assetid: f8a3b994-231f-44b4-995a-0da4eafa097e
keywords: ["UsbDeviceCreateFail rule (kmdf)"]
topic_type:
- apiref
api_name:
- UsbDeviceCreateFail
api_type:
- NA
---

# UsbDeviceCreateFail rule (kmdf)


The **UsbDeviceCreateFail** rule specifies that the driver returns from the [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) event callback function with an error status if creation of a WDFUSBDEVICE object fails.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>UsbDeviceCreateFail</strong> rule.</p>
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

[**WdfUsbTargetDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550077)
[**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428)
 

 





