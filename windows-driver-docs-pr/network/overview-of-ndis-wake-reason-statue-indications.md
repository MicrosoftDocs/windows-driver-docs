---
title: Overview of NDIS Wake Reason Status Indications
description: Overview of NDIS Wake Reason Status Indications
ms.assetid: 94B54281-7A7E-4DBA-85AE-313EEF09E733
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of NDIS Wake Reason Status Indications


Starting with NDIS 6.30, miniport drivers issue an NDIS wake reason status indication ([**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808)) to notify NDIS and overlying drivers about the reason for a system wake-up event. If the network adapter generates a wake-up event, the miniport driver immediately issues an NDIS status indication of **NDIS\_STATUS\_PM\_WAKE\_REASON** when the network adapter resumes to a full-power state.

**Note**  Support for NDIS wake reason status indications is optional for Mobile Broadband (MB) miniport drivers.

 

The miniport driver is configured with power management (PM) parameters through an object identifier (OID) set request of [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768). This OID request specifies the PM parameters through an [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

The [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure specifies the parameters for the following types of wake-up events.

<a href="" id="received-packet-wake-up-events"></a>Received Packet Wake-up Events  
The network adapter generates a wake-up event if it receives a packet that matched a wake-on-LAN (WOL) pattern. WOL patterns include the following:

-   Media-independent WOL patterns, such as magic packets or TCP/IP data patterns within the packet payload. For example, the [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure could specify a WOL pattern for a TCP SYN frame.

-   Media-specific WOL patterns, such as an EAPOL request identifier packet or mobile broadband (MB) Short Message Service (SMS) message.

-   Wildcard patterns that match a receive filter specified through an OID set request of [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

**Note**  For this type of wake reason status indication, the network adapter must be able to save the received packet. The driver must return the received packet within the status indication.

 

WOL patterns are specified through the **EnabledWoLPacketPatterns** member of the [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

<a href="" id="media-specific-wake-up-events"></a>Media-Specific Wake-up Events  
The network adapter generates a wake-up event because of a media-specific reason, such as a disassociation from an 802.11 access point (AP) or the receipt of a mobile broadband (MB) Short Message Service (SMS) message.

Wake-up events of this type are specified through the **MediaSpecificWakeUpEvents** member of the [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

<a href="" id="media-independent-wake-up-events"></a>Media-Independent Wake-up Events  
The network adapter generates a wake-up event because of a media-independent reason, such as media connection or disconnection.

Wake-up events of this type are specified through the **WakeUpFlags** member of the [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

The miniport driver must follow these guidelines for NDIS wake reason status indications:

-   If the miniport driver supports the ability to issue wake packet indications, it must report this ability when NDIS calls the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function. For more information, see [Reporting Wake Reason Status Indication Capabilities](reporting-wake-reason-status-indication-capabilities.md).

    **Note**  The miniport driver does not have to report its ability to issue NDIS wake reason status indications for events that are not related to the receipt of a WOL packet.

     

-   When the miniport driver issues a wake packet indication for a WOL packet, it must include the packet that caused the wake-up event. For more information, see [Issuing NDIS Wake Reason Status Indications](issuing-ndis-wake-reason-indications.md).

-   If the network adapter generated a wake-up signal, the miniport driver must issue an [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication. The driver does this while it is handling the OID set request of [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) for the transition to a full-power state.

-   The miniport driver must issue an [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication before it issues a status indication that is related to the wake-up event. For example, if the wake-up event was due to a change in the media connectivity state, the miniport driver must issue an [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391) status indication after it has issued the **NDIS\_STATUS\_PM\_WAKE\_REASON** status indication.

-   The miniport driver must ssue an [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication only for power management events that were previously enabled through an OID set request of [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768).

-   The miniport driver must issue an [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication only for wake-up events that were generated by the underlying network adapter.

 

 





