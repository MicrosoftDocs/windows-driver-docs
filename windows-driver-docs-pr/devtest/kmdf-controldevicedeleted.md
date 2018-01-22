---
title: ControlDeviceDeleted rule (kmdf)
description: The ControDeviceDeleted rule specifies that if a PnP driver creates a control device object, the driver must delete the control device object in one of the cleanup callback functions before the driver unloads.
ms.assetid: 869f1c1c-8a9f-4e0b-bcbb-386e93663567
keywords: ["ControlDeviceDeleted rule (kmdf)"]
topic_type:
- apiref
api_name:
- ControlDeviceDeleted
api_type:
- NA
---

# ControlDeviceDeleted rule (kmdf)


The ControDeviceDeleted rule specifies that if a PnP driver creates a control device object, the driver must delete the control device object in one of the cleanup callback functions before the driver unloads.

If an FDO or filter driver calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) for the control device object, the driver must call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) for the control device object from the driver's cleanup callback function for the WDFDEVICE object, the destroy callback function for WDFDEVICE object, or the [*EvtDeviceSelfManagedIoCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540898) event callback function.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ControlDeviceDeleted</strong> rule.</p>
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

[**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926)
[**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20ControlDeviceDeleted%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




