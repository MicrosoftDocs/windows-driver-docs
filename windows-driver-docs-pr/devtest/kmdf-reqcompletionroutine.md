---
title: ReqCompletionRoutine rule (kmdf)
description: The ReqCompletionRoutine rule specifies that a completion routine must be set before a request is sent to an I/O target.
ms.assetid: 0ddf6980-0540-4224-9800-3cd534f03230
keywords: ["ReqCompletionRoutine rule (kmdf)"]
topic_type:
- apiref
api_name:
- ReqCompletionRoutine
api_type:
- NA
---

# ReqCompletionRoutine rule (kmdf)


The **ReqCompletionRoutine** rule specifies that a completion routine must be set before a request is sent to an I/O target.

If a request is not sent synchronously, or is not sent as send and forget, (specified by the **WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET** flag), the driver should set a completion routine so that the I/O target can notify the driver when the request is completed.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ReqCompletionRoutine</strong> rule.</p>
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

[**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027)
[**WdfRequestSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550030)
See also
--------

[Completing I/O Requests](https://msdn.microsoft.com/library/windows/hardware/ff540740)
[Synchronizing Cancel and Completion Code](https://msdn.microsoft.com/library/windows/hardware/ff544726)
[**WDF\_REQUEST\_SEND\_OPTIONS\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff552493)
[**WDF\_REQUEST\_SEND\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff552491)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20ReqCompletionRoutine%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




