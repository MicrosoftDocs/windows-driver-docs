---
title: RequestForUrbXrb rule (kmdf)
ms.assetid: 8BFFB73D-106A-4CD0-93F2-D295D969729E
description: 
keywords: ["RequestForUrbXrb rule (kmdf)"]
topic_type:
- apiref
api_name:
- RequestForUrbXrb
api_type:
- NA
---

# RequestForUrbXrb rule (kmdf)


If the client driver calls [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428) and specifies the client contract version USBD\_CLIENT\_CONTRACT\_VERSION\_602 in the WDF\_USB\_DEVICE\_CREATE\_CONFIG structure (to use the new capabilities of the USB driver stack for Windows 8), DDIs that use a URB internally would only use *URB context* if any of the following preconditions apply:

-   Request parameter has the Wdf device in its parent object tree.
-   Request is represented via the I/O queue.
-   Request has another I/O queue represented request in its parent object tree.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>RequestForUrbXrb</strong> rule.</p>
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

[**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951)
[**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428)
[**WdfUsbTargetDeviceFormatRequestForControlTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff550082)
[**WdfUsbTargetDeviceFormatRequestForString**](https://msdn.microsoft.com/library/windows/hardware/ff550086)
[**WdfUsbTargetDeviceSendControlTransferSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550104)
[**WdfUsbTargetPipeAbortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551129)
[**WdfUsbTargetPipeFormatRequestForAbort**](https://msdn.microsoft.com/library/windows/hardware/ff551132)
[**WdfUsbTargetPipeFormatRequestForReset**](https://msdn.microsoft.com/library/windows/hardware/ff551138)
[**WdfUsbTargetPipeResetSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551156)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20RequestForUrbXrb%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




