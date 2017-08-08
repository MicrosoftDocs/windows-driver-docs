---
title: OID\_WWAN\_PIN\_LIST
author: windows-driver-content
description: OID\_WWAN\_PIN\_LIST returns a list of all the different types of Personal Identification Numbers (PINs) that are supported by the MB device and additional details for each PIN type, such as the length of the PIN (minimum and maximum lengths), PIN format, PIN-entry mode (enabled/disabled/not-available). This OID also specifies the current mode of each PIN supported by the device. Set requests are not supported. Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an NDIS\_STATUS\_WWAN\_PIN\_LIST status notification containing an NDIS\_WWAN\_PIN\_LIST structure to return a list of PINs with corresponding descriptions when completing query requests.
ms.assetid: 76a1181c-974e-472d-ad15-d9c6208aa2b4
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_PIN_LIST Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_PIN\_LIST


OID\_WWAN\_PIN\_LIST returns a list of all the different types of Personal Identification Numbers (PINs) that are supported by the MB device and additional details for each PIN type, such as the length of the PIN (minimum and maximum lengths), PIN format, PIN-entry mode (enabled/disabled/not-available). This OID also specifies the current mode of each PIN supported by the device.

Set requests are not supported.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_PIN\_LIST**](ndis-status-wwan-pin-list.md) status notification containing an [**NDIS\_WWAN\_PIN\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff567912) structure to return a list of PINs with corresponding descriptions when completing query requests.

Remarks
-------

For more information about using this OID, see [WWAN Pin Operations](https://msdn.microsoft.com/library/windows/hardware/ff559093).

Miniport drivers can access the Subscriber Identity Module (SIM card) when processing query operations, but should not access the provider network.

Miniport drivers must report all the PINs supported by their device. If the device does not support listing PINs, the miniport driver must report this list from a static (hard-coded) list maintained in the miniport driver itself for all the devices it supports.

Any PIN that provides device power-on verification or identification functionality should be reported as PIN1 and must be compliant to PIN1 guidelines.

Miniport drivers must return this information when the device ready-state changes to *WwanReadyStateInitialized* or when the device ready-state is *WwanReadyStateDeviceLocked* (PIN locked). Miniport drivers should also return this information in other device ready-states, wherever possible.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_PIN\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff567912)

[**NDIS\_STATUS\_WWAN\_PIN\_LIST**](ndis-status-wwan-pin-list.md)

[WWAN Pin Operations](https://msdn.microsoft.com/library/windows/hardware/ff559093)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_PIN_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


