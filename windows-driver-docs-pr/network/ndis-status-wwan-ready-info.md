---
title: NDIS\_STATUS\_WWAN\_READY\_INFO
author: windows-driver-content
description: Miniport drivers use the NDIS\_STATUS\_WWAN\_READY\_INFO notification to inform the MB Service of device ready-state changes in response to OID\_WWAN\_READY\_INFO \ 160;query requests.
ms.assetid: 92ddf95f-8829-4259-b53a-c7ce56ee53f0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_WWAN_READY_INFO Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_READY\_INFO


Miniport drivers use the NDIS\_STATUS\_WWAN\_READY\_INFO notification to inform the MB Service of device ready-state changes in response to [OID\_WWAN\_READY\_INFO](oid-wwan-ready-info.md) query requests.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_READY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567916) structure.

Remarks
-------

Miniport drivers must report all device ready-state changes as an unsolicited event. When the miniport driver initializes the MB device, the miniport driver must set the WWAN\_READY\_INFO **ReadyState** member to **WwanReadyStateOff**. Thereafter, miniport drivers must report any device ready-state change to the MB Service through this notification. For example, miniport drivers must report a device ready-state change when the **ReadyState** member changes from **WwanReadyStateOff** to **WwanReadyStateDeviceLocked**, or **WwanReadyStateBadSim**, or **WwanReadyStateSimNotInserted**, or any other different device ready-state.

Most device ready-state changes happen when the device initializes the radio stack and the SIM card (if required). A change can also happen during the course of a session between the MB Service and the miniport driver, such as user changing the SIM card. The behavior of the MB Service shall change accordingly based on the new device ready-state.

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


[**NDIS\_WWAN\_READY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567916)

[OID\_WWAN\_READY\_INFO](oid-wwan-ready-info.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_READY_INFO%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


