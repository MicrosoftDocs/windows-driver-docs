---
title: NDIS_STATUS_WWAN_PACKET_SERVICE
description: Miniport drivers use the NDIS_STATUS_WWAN_PACKET_SERVICE notification to inform the MB Service when packet service availability changes, including to notify of a change to the type of packet data service currently used.
ms.assetid: 7a04b54e-e07b-43dc-ba76-086d7521ff60
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_PACKET_SERVICE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_PACKET\_SERVICE


Miniport drivers use the NDIS\_STATUS\_WWAN\_PACKET\_SERVICE notification to inform the MB Service when packet service availability changes, including to notify of a change to the type of packet data service currently used.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_PACKET\_SERVICE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567910) structure.

Remarks
-------

CDMA-based miniport drivers can automatically initiate packet-attach service if there is no resource allocation/release is possible and can send the event notification to the MB Service.

Miniport drivers should obey the following guidelines for event notifications:

-   Miniport drivers should set **AvailableDataClasses** is set to WWAN\_DATA\_CLASS\_NONE during miniport driver initialization. Thereafter, miniport drivers must notify the MB Service whenever there is any change to **AvailableDataClasses**.

-   Miniport drivers should set **CurrentDataClass** to WWAN\_DATA\_CLASS\_NONE during miniport driver initialization. Thereafter, miniport drivers must notify the MB Service whenever there is any change to **CurrentDataClass** . Miniport drivers should send an NDIS\_STATUS\_LINK\_STATE notification if the change to **CurrentDataClass** results in a change of the transmit or receive link speed.

-   Miniport drivers must notify the MB Service whenever there is any change in Packet Service attach state.

Miniport drivers should return *query* results according to the following rules:

-   Miniport drivers must return WWAN\_STATUS\_SUCCESS with **WwanPacketServiceStateAttaching** whenever the device attempts to packet-attach.

-   Miniport drivers should return WWAN\_STATUS\_SUCCESS with **WwanPacketServiceStateDetaching** whenever the device attempts to packet-detach.

-   When the device is in final state, miniport drivers should return WWAN\_STATUS\_SUCCESS along with the appropriate current state ( **WwanPacketServiceStateAttached** or **WwanPacketServiceStateDetached**)

-   Miniport drivers must list all the available data-classes; not just the highest data-class available. This applies to both *query* operations as well as event notifications.

Miniport drivers should return *set* results according to the following rules:

-   Return WWAN\_STATUS\_SUCCESS, if *set* request with **WwanPacketServiceActionAttach**, is issued by the Service and the device is already in the packet-attached state.

-   Return WWAN\_STATUS\_SUCCESS, if *set* request with **WwanPacketServiceActionDetach**, is issued by the Service and the device is already in the packet-detached state.

-   Never return transient states for the *set* request. Only the final states **WwanPacketServiceStateAttached** or **WwanPacketServiceStateDetached** must be returned after the successful completion of the packet service operation with WWAN\_STATUS\_SUCCESS

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_PACKET\_SERVICE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567910)

[OID\_WWAN\_PACKET\_SERVICE](oid-wwan-packet-service.md)

 

 




