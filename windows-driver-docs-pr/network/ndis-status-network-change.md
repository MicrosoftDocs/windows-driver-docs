---
title: NDIS_STATUS_NETWORK_CHANGE
description: The NDIS_STATUS_NETWORK_CHANGE status indicates a network change to allow overlying drivers to initiate renegotiation of network addresses.
ms.assetid: feb6bb71-7147-43dd-b09d-cb41404164eb
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_NETWORK_CHANGE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_NETWORK\_CHANGE


The NDIS\_STATUS\_NETWORK\_CHANGE status indicates a network change to allow overlying drivers to initiate renegotiation of network addresses.

Remarks
-------

NDIS miniport drivers can generate this status indication to request the overlying protocol drivers to renegotiate layer three addresses.

NDIS generates NDIS\_STATUS\_NETWORK\_CHANGE status indications for the older 802.1X wireless miniport drivers that emulate 802.3. These miniport drivers report a media type of **NdisMedium802\_3** and a physical media type of **NdisPhysicalMediumWirelessLan**. When such a miniport driver generates an [**NDIS\_STATUS\_MEDIA\_CONNECT**](ndis-status-media-connect.md) status indication and the associated miniport adapter is in a connected state, NDIS generates an NDIS\_STATUS\_NETWORK\_CHANGE status indication for the miniport adapter.

NDIS 6.0 and later miniport drivers should generate the NDIS\_STATUS\_NETWORK\_CHANGE status indication only after they are ready to handle network data. For example, in native 802.11, this status indication is generated after authentication is completed successfully and full layer two connectivity is achieved.

**Note**  Although the media-connected state is not precisely defined, this state can be loosely defined as - the state in which the miniport adapter is able to transmit and receive network data. Media-connected is not directly related to link authentication status. The native WiFi 802.3 interface is unable to send or receive packets until after the link is authenticated. In this case, the media-connected state is coincident with the link-authenticated state in native 802.11.

 

NDIS supplies one of the following NDIS\_NETWORK\_CHANGE\_TYPE values in the **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure:

<a href="" id="ndispossiblenetworkchange"></a>**NdisPossibleNetworkChange**  
The miniport driver detected that there might be a network change. In this case, the overlying protocols must detect the network change, if any, and renegotiate the addresses if necessary.

NDIS also uses this value when it generates NDIS\_STATUS\_NETWORK\_CHANGE status indications for older 802.1X wireless miniport drivers that emulate 802.3. However, NDIS uses **NdisNetworkChangeFromMediaConnect** instead of **NdisPossibleNetworkChange** when it translates the same event for Windows Management Instrumentation (WMI).

<a href="" id="ndisdefinitelynetworkchange"></a>**NdisDefinitelyNetworkChange**  
The miniport driver detected that there is a network change, so the overlying protocols must renegotiate the addresses.

<a href="" id="ndisnetworkchangefrommediaconnect"></a>**NdisNetworkChangeFromMediaConnect**  
An older 802.1X wireless miniport driver that emulates 802.3 generated an [**NDIS\_STATUS\_MEDIA\_CONNECT**](ndis-status-media-connect.md) status indication when it was in a connected state. This value is used in the WMI event notification for [GUID\_NDIS\_STATUS\_NETWORK\_CHANGE](https://msdn.microsoft.com/library/windows/hardware/ff553595). **NdisNetworkChangeFromMediaConnect** is not used in the NDIS\_STATUS\_NETWORK\_CHANGE status indication.

The **StatusBufferSize** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure is set to sizeof(NDIS\_NETWORK\_CHANGE\_TYPE).

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
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NDIS\_STATUS\_MEDIA\_CONNECT**](ndis-status-media-connect.md)

 

 




