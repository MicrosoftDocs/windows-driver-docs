---
title: OID_GEN_MEDIA_SUPPORTED
description: As a query, the OID_GEN_MEDIA_SUPPORTED OID specifies the media types that a NIC can support but not necessarily the media types that the NIC currently uses.
ms.assetid: e7b8d2b1-4e84-416f-aeb3-75591ed44b22
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MEDIA_SUPPORTED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MEDIA\_SUPPORTED


As a query, the OID\_GEN\_MEDIA\_SUPPORTED OID specifies the media types that a NIC can support but not necessarily the media types that the NIC currently uses.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Obsolete.

The following media types were added for NDIS 6.0 and later drivers:

-   **NdisMediumTunnel**

-   **NdisMediumLoopback**

-   **NdisMediumNative802\_11**

The following media types were added for NDIS 6.20 and later drivers:

-   **NdisMediumIP**

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory. See [OID\_GEN\_MEDIA\_SUPPORTED (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff560254).

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory. See [OID\_GEN\_MEDIA\_SUPPORTED (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff560254).

Remarks
-------

NDIS 6.0 and later miniport drivers do not receive this OID request. NDIS handles this OID with a cached value that miniport drivers supply during initialization.

These media types are listed as a proper subset of the following system-defined values:

<a href="" id="ndismedium802-3"></a>**NdisMedium802\_3**  
Ethernet (802.3).

**Note**  NDIS 5.*x* miniport drivers that conform to the 802.11 interface must use this media type. For more information about the 802.11 interface, see [802.11 Wireless LAN Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff543933).

 

<a href="" id="ndismedium802-5"></a>**NdisMedium802\_5**  
Token Ring (802.5). This media type is not supported for NDIS 6.0 and later drivers.

**Note**  Starting with Windows 8, the operating system will not support this media type for any miniport drivers.

 

<a href="" id="ndismediumfddi"></a>**NdisMediumFddi**  
FDDI. This media type is not supported on Windows Vista and later versions of Windows.

<a href="" id="ndismediumwan"></a>**NdisMediumWan**  
WAN

<a href="" id="ndismediumlocaltalk"></a>**NdisMediumLocalTalk**  
LocalTalk

<a href="" id="ndismediumdix"></a>**NdisMediumDix**  
DEC/Intel/Xerox (DIX) Ethernet

<a href="" id="ndismediumarcnetraw"></a>**NdisMediumArcnetRaw**  
ARCNET (raw). This media type is not supported on Windows Vista and later versions of Windows.

<a href="" id="ndismediumarcnet878-2"></a>**NdisMediumArcnet878\_2**  
ARCNET (878.2). This media type is not supported on Windows Vista and later versions of Windows.

<a href="" id="ndismediumatm"></a>**NdisMediumAtm**  
ATM. This media type is not supported for NDIS 6.0 and later drivers.

<a href="" id="ndismediumnative802-11"></a>**NdisMediumNative802\_11**  
Native 802.11. This media type is used by miniport drivers that conform to the Native 802.11 interface. For more information about this interface, see [Native 802.11 Wireless LAN Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff560648).

<a href="" id="ndismediumwirelesswan"></a>**NdisMediumWirelessWan**  
Various types of **NdisWireless***Xxx* media. This media type is not available for use beginning with Windows Vista and later versions of Windows.

<a href="" id="ndismediumirda"></a>**NdisMediumIrda**  
Infrared (IrDA).

<a href="" id="ndismediumcowan"></a>**NdisMediumCoWan**  
Connection-oriented WAN.

<a href="" id="ndismedium1394"></a>**NdisMedium1394**  
IEEE 1394 (firewire) bus. This media type is not supported on Windows Vista and later versions of Windows.

<a href="" id="ndismediumbpc"></a>**NdisMediumBpc**  
Broadcast PC network.

<a href="" id="ndismediuminfiniband"></a>**NdisMediumInfiniBand**  
InfiniBand network.

<a href="" id="ndismediumtunnel"></a>**NdisMediumTunnel**  
Tunnel network.

<a href="" id="ndismediumloopback"></a>**NdisMediumLoopback**  
NDIS loopback network.

<a href="" id="ndismediumip"></a>**NdisMediumIP**  
A generic medium that is capable of sending and receiving raw IP packets.

NDIS 5. *x* miniport drivers that support wireless LAN (WLAN) or wireless WAN (WWAN) packets appear to the operating system and to NDIS as Ethernet packets. These NDIS drivers must provide support for WWAN or WLAN networks as Ethernet networks. Such drivers declare their medium as **NdisMedium802\_3** and emulate Ethernet to higher-level NDIS drivers. Such drivers must also declare in [OID\_GEN\_PHYSICAL\_MEDIUM](oid-gen-physical-medium.md) the appropriate physical medium that they support..

For more information about NDIS 5.X WLAN miniport drivers, see [802.11 Wireless LAN Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff543933).

NDIS 6.0 and later miniport drivers that support the WLAN media transfer packets that appear to the operating system and to NDIS as IEEE 802.11 packets. These NDIS drivers must provide support for WLAN networks as Native 802.11 miniport drivers. Such drivers declare their medium as **NdisMediumNative802\_11**.

For more information about Native 802.11 miniport drivers, see [Native 802.11 Wireless LAN Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff560648).

If the underlying miniport driver returns **NULL** for this query, or if an experimental media type is used, the driver must indicate receive operations using the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function. Any protocol that is bound to such an underlying miniport driver receives all such indications, that is, the protocol driver cannot filter receive operations with [OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598)

[OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md)

[OID\_GEN\_PHYSICAL\_MEDIUM](oid-gen-physical-medium.md)

 

 




