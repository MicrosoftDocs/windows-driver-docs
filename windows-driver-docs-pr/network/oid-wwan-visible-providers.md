---
title: OID\_WWAN\_VISIBLE\_PROVIDERS
author: windows-driver-content
description: OID\_WWAN\_VISIBLE\_PROVIDERS returns a list of network providers currently visible within the MB device's range.
ms.assetid: 4dfd4477-6332-4163-8b3e-a1604b11d175
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_WWAN_VISIBLE_PROVIDERS Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_VISIBLE\_PROVIDERS


OID\_WWAN\_VISIBLE\_PROVIDERS returns a list of network providers currently visible within the MB device's range.

Set requests are not supported.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_VISIBLE\_PROVIDERS**](ndis-status-wwan-visible-providers.md) status notification containing an [**NDIS\_WWAN\_VISIBLE\_PROVIDERS**](ndis-wwan-visible-providers.md) structure to provide information about visible network providers when completing query requests.

*Query* requests specify NDIS\_WWAN\_GET\_VISIBLE\_PROVIDERS structure as input. When the **Action** member in WWAN\_GET\_VISIBLE\_PROVIDERS is set to WWAN\_GET\_VISIBLE\_PROVIDERS\_ALL the miniport should return all visible providers. When the **Action** member in WWAN\_GET\_VISIBLE\_PROVIDERS is set to WWAN\_GET\_VISIBLE\_PROVIDERS\_MULTICARRIER the miniport should only return visible multi-carrier providers that can be set as the home provider.

The visible provider list returned by the device should have the provider state set correctly for each of the providers. For example, the multicarrier preferred providers should be tagged as WWAN\_PROVIDER\_STATE\_PREFERRED\_MULTICARRIER, the current home provider if any should be tagged as WWAN\_PROVIDER\_STATE\_HOME, The current registered provider if any should be tagged as WWAN\_PROVIDER\_STATE\_REGISTERED.

The **Rssi** and **ErrorRate** members of WWAN\_PROVIDER2 structure should be set if available.

Remarks
-------

For more information about using this OID, see [WWAN Provider Operations](https://msdn.microsoft.com/library/windows/hardware/ff559101).

Miniport drivers can access the Subscriber Identity Module (SIM card) when processing query operations, but should not access the provider network.

Miniport drivers should set the **VisibleListHeader.ElementType** member to *WwanStructProvider*.

For CDMA-based networks, miniport driver should return only the home provider, if any of the networks in the Preferred Roaming List (PRL) is currently visible. For GSM-based networks, more than one provider may be present in the visible provider list.

Devices that do not support scanning for visible providers while connected should return the WWAN\_STATUS\_BUSY error value in the **uStatus** member of the NDIS\_WWAN\_VISIBLE\_PROVIDERS structure.

Both GSM-based and CDMA-based devices must support scanning for visible providers while in registered mode. However, miniport drivers are not required to support scanning for visible provider while a Packet Data Protocol (PDP) context is active (for example, the device is connected to the provider's network).

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


[**NDIS\_WWAN\_VISIBLE\_PROVIDERS**](ndis-wwan-visible-providers.md)

[**NDIS\_STATUS\_WWAN\_VISIBLE\_PROVIDERS**](ndis-status-wwan-visible-providers.md)

[WWAN Provider Operations](https://msdn.microsoft.com/library/windows/hardware/ff559101)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_VISIBLE_PROVIDERS%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


