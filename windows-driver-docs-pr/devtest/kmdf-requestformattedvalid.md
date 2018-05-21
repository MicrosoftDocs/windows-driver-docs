---
title: RequestFormattedValid rule (kmdf)
description: The RequestFormattedValid rule specifies that the driver formats all requests, except for a WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET request, before it sends them to an I/O target.
ms.assetid: b7da37ed-3ca5-472e-a915-82674c9efee3
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["RequestFormattedValid rule (kmdf)"]
topic_type:
- apiref
api_name:
- RequestFormattedValid
api_type:
- NA
---

# RequestFormattedValid rule (kmdf)


The **RequestFormattedValid** rule specifies that the driver formats all requests, except for a WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET request, before it sends them to an I/O target.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>RequestFormattedValid</strong> rule.</p>
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

[**WdfIoTargetFormatRequestForInternalIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff548595)
[**WdfIoTargetFormatRequestForInternalIoctlOthers**](https://msdn.microsoft.com/library/windows/hardware/ff548599)
[**WdfIoTargetFormatRequestForIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff548604)
[**WdfIoTargetFormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff548612)
[**WdfIoTargetFormatRequestForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff548620)
[**WdfRequestFormatRequestUsingCurrentType**](https://msdn.microsoft.com/library/windows/hardware/ff549955)
[**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027)
[**WdfRequestWdmFormatUsingStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550036)
[**WdfUsbTargetDeviceFormatRequestForControlTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff550082)
[**WdfUsbTargetDeviceFormatRequestForCyclePort**](https://msdn.microsoft.com/library/windows/hardware/ff550084)
[**WdfUsbTargetDeviceFormatRequestForString**](https://msdn.microsoft.com/library/windows/hardware/ff550086)
[**WdfUsbTargetDeviceFormatRequestForUrb**](https://msdn.microsoft.com/library/windows/hardware/ff550088)
[**WdfUsbTargetPipeFormatRequestForAbort**](https://msdn.microsoft.com/library/windows/hardware/ff551132)
[**WdfUsbTargetPipeFormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff551136)
[**WdfUsbTargetPipeFormatRequestForReset**](https://msdn.microsoft.com/library/windows/hardware/ff551138)
[**WdfUsbTargetPipeFormatRequestForUrb**](https://msdn.microsoft.com/library/windows/hardware/ff551139)
[**WdfUsbTargetPipeFormatRequestForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff551141)
 

 





