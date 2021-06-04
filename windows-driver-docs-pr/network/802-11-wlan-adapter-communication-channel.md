---
title: 802.11 WLAN Adapter Communication Channel
description: 802.11 WLAN Adapter Communication Channel
keywords:
- adapters WDK 802.11 WLAN , communication channel
- WLAN adapters WDK , communication channel
- communication channels WDK networking
- pass-through communication channels WDK networking
- packets WDK networking , Native 802.11 IHV Extensions DLL
- indications WDK Native 802.11 IHV Extensions DLL
- send operations WDK Native 802.11 IHV Extensions DLL
- receive operations WDK Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# 802.11 WLAN Adapter Communication Channel




 

The operating system provides a pass-through communication channel between the IHV Extensions DLL and the Native 802.11 miniport driver. The IHV Extensions DLL accesses the communication channel for the following operations.

<a href="" id="--------sending-receiving-proprietary-configuration-data"></a> **Sending/Receiving Proprietary Configuration Data**  
The IHV Extensions DLL sends NDIS 6.0 or later object identifier (OID) method requests to the Native 802.11 miniport driver through calls to the [**Dot11ExtNicSpecificExtension**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_nic_specific_extension) function. Internally, this function issues a method request of [OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION](/previous-versions/windows/hardware/wireless/oid-dot11-nic-specific-extension) to the miniport driver. For more information about NDIS OID method requests, see [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request).

Typically, the IHV Extensions DLL calls **Dot11ExtNicSpecificExtension** to do the following:

-   Set proprietary configuration parameters for the miniport driver or WLAN adapter.

-   Query proprietary configuration parameters or status data from the miniport driver or WLAN adapter.

<a href="" id="receiving-notifications-indications"></a>**Receiving Notifications/Indications**  
The IHV Extensions DLL asynchronously receives notifications from the Native 802.11 miniport driver through calls to the [*Dot11ExtIhvReceiveIndication*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_receive_indication) IHV Handler function. The operating system calls this function whenever the miniport driver makes a media-specific indication through a call to [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex). For more information about this type of indication, see [**NDIS\_STATUS\_MEDIA\_SPECIFIC\_INDICATION**](./ndis-status-media-specific-indication.md).

<a href="" id="sending-802-11-packets"></a>**Sending 802.11 Packets**  
The IHV Extensions DLL sends 802.11 packets to the Native 802.11 miniport driver through calls to the [**Dot11ExtSendPacket**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_packet) function. The miniport driver queues the packet on the WLAN adapter for transmission. When the packet has been transmitted, the operating system calls the [*Dot11ExtIhvSendPacketCompletion*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_send_packet_completion) IHV Handler function. For more information about sending packets by the IHV Extensions DLL, see [Send Operations](send-operations.md).

Typically, the IHV Extensions DLL calls [**Dot11ExtSendPacket**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_packet) to send security packets during the post-association operation. The security packets are based on the authentication algorithm supported by the DLL and enabled on the WLAN adapter.

<a href="" id="receiving-802-11-packets"></a>**Receiving 802.11 Packets**  
The IHV Extensions DLL receives 802.11 packets from the Native 802.11 miniport driver through calls to the [*Dot11ExtIhvReceivePacket*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_receive_packet) function. The operating system calls this function for every received packet that has an IEEE EtherType that matches an entry in the list of EtherTypes registered by the DLL through a call to [**Dot11ExtSetEtherTypeHandling**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_ethertype_handling). For more information about receiving packets by the IHV Extensions DLL, see [Receive Operations](receive-operations.md).

The following points apply to the communication channel between the IHV Extensions DLL and the Native 802.11 miniport driver.

-   Configuration, notification, or indication data transferred over this channel has a format defined by the independent hardware vendor (IHV), which is opaque to the operating system.

-   All data received through this channel is serialized and delivered in the order the data was sent by the IHV Extensions DLL or Native 802.11 miniport driver.

 

 
