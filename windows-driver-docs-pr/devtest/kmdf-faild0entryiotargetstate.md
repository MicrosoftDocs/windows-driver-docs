---
title: FailD0EntryIoTargetState rule (kmdf)
description: The FailD0EntryIoTargetState rule specifies that an I/O target for a USB continuous reader started within the EvtDeviceD0Entry will get stopped appropriately from the same callback if the EvtDeviceD0Entry fails.
ms.assetid: 7FB616EB-2079-42AE-A724-990EFBF3F84D
keywords: ["FailD0EntryIoTargetState rule (kmdf)"]
topic_type:
- apiref
api_name:
- FailD0EntryIoTargetState
api_type:
- NA
---

# FailD0EntryIoTargetState rule (kmdf)


The **FailD0EntryIoTargetState** rule specifies that an I/O target for a USB continuous reader started within the [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) will get stopped appropriately from the same callback if the *EvtDeviceD0Entry* fails.

When [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function fails, the framework doesn’t execute the driver’s [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>FailD0EntryIoTargetState</strong> rule.</p>
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

[**WdfIoTargetStart**](https://msdn.microsoft.com/library/windows/hardware/ff548677)
[**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680)
[**WdfUsbTargetPipeConfigContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff551130)
[**WdfUsbTargetPipeGetIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff551146)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20FailD0EntryIoTargetState%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




