---
title: NonPnPDrvPowerPolicyOwnerAPI rule (kmdf)
description: The NonPnPDrvPowerPolicyOwnerAPI rule specifies that non-PnP drivers cannot call certain DDIs related to power management.
ms.assetid: d15211d2-cf53-4b60-bd26-a6c82d50bd42
keywords: ["NonPnPDrvPowerPolicyOwnerAPI rule (kmdf)"]
topic_type:
- apiref
api_name:
- NonPnPDrvPowerPolicyOwnerAPI
api_type:
- NA
---

# NonPnPDrvPowerPolicyOwnerAPI rule (kmdf)


The **NonPnPDrvPowerPolicyOwnerAPI** rule specifies that non-PnP drivers cannot call certain DDIs related to power management.

If the driver does not register the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function, the following DDIs cannot be called:

[**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903)
[**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546774)
[**WdfDeviceAssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545909)
[**WdfDeviceGetDevicePowerState**](https://msdn.microsoft.com/library/windows/hardware/ff545985)
[**WdfDeviceGetDevicePowerPolicyState**](https://msdn.microsoft.com/library/windows/hardware/ff545974)
[**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135)
[**WdfDeviceInitSetPowerPolicyOwnership**](https://msdn.microsoft.com/library/windows/hardware/ff546776)
[**WdfDeviceInitRegisterPowerStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546071)
[**WdfDeviceInitRegisterPowerPolicyStateChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546066)
[**WdfDeviceInitSetPowerNotPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546147)
[**WdfDeviceInitSetPowerPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546766)
[**WdfDeviceInitSetPowerInrush**](https://msdn.microsoft.com/library/windows/hardware/ff546142)
[**WdfDeviceSetPowerCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff546901)
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NonPnPDrvPowerPolicyOwnerAPI</strong> rule.</p>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20NonPnPDrvPowerPolicyOwnerAPI%20rule%20%28kmdf%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




