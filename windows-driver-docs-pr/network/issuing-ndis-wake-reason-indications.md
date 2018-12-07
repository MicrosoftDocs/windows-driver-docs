---
title: Issuing NDIS Wake Reason Status Indications
description: Issuing NDIS Wake Reason Status Indications
ms.assetid: F3DBE0DB-9787-4C3D-8DE3-AD47E5778B21
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Issuing NDIS Wake Reason Status Indications


If a miniport driver supports NDIS wake reason status indications ([**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808)), it must generate this status indication immediately after the network adapter generates a wake-up event and the adapter resumes to a full-power state.

**Note**  Support for NDIS wake reason status indications is optional for Mobile Broadband (MB) miniport drivers.

The miniport driver is configured with power management (PM) parameters through an object identifier (OID) set request of [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768). This OID request specifies the PM parameters through an [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

The [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure specifies the parameters for the following types of wake-up events.

<a href="" id="received-packet-wake-up-events"></a>Received Packet Wake-up Events  
The network adapter generates a wake-up event if it receives a packet that matched a wake-on-LAN (WOL) pattern. WOL patterns include the following:

-   Media-independent WOL patterns, such as magic packets or TCP/IP data patterns within the packet payload. For example, the [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure could specify a WOL pattern for a TCP SYN frame.

-   Media-specific WOL patterns, such as an EAPOL request identifier packet or mobile broadband (MB) Short Message Service (SMS) message.

-   Wildcard patterns that match a receive filter specified through an OID set request of [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

**Note**  For this type of wake reason status indication, the network adapter must be able to save the received packet. The driver must return the received packet within the status indication.

WOL patterns are specified through the **EnabledWoLPacketPatterns** member of the [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

<a href="" id="media-specific-wake-up-events"></a>Media-Specific Wake-up Events  
The network adapter generates a wake-up event because of a media-specific reason, such as a disassociation from an 802.11 access point (AP) or the receipt of a mobile broadband (MB) Short Message Service (SMS) message.

Wake-up events of this type are specified through the **MediaSpecificWakeUpEvents** member of the [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

<a href="" id="media-independent-wake-up-events"></a>Media-Independent Wake-up Events  
The network adapter generates a wake-up event because of a media-independent reason, such as media connection or disconnection.

Wake-up events of this type are specified through the **WakeUpFlags** member of the [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

If the network adapter generated a wake-up signal, the miniport driver must issue an [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication. The driver does this while it is handling the OID set request of [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) for the transition of the adapter to a full-power state.

**Note**  The miniport driver must issue an [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication before it issues a status indication that is related to the wake-up event. For example, if the wake-up event was due to a change in the media connectivity state, the miniport driver must issue an [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391) status indication after it has issued the **NDIS\_STATUS\_PM\_WAKE\_REASON** status indication.

When the miniport driver issues the [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication, it must follow these steps:

1.  The miniport driver must allocate a buffer that is large enough to contain the following:

    -   An [**NDIS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh451605) structure.

    -   An [**NDIS\_PM\_WAKE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/hh451603) structure along with the received packet (*wake packet*) that caused the network adapter to generate the wake-up event.

        **Note**  The miniport driver does not need to allocate this buffer space if it indicates media-specific or media-independent wake-up events.

2.  The miniport driver initializes an [**NDIS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh451605) structure at the start of the buffer. The driver sets the **WakeReason** member to an [**NDIS\_PM\_WAKE\_REASON\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh451607) enumeration value that defines the type of the wake-up event.

    For example, if the miniport driver is indicating a received packet wake-up event, it must set the **WakeReason** member to **NdisWakeReasonPacket**. Otherwise, the driver sets the **WakeReason** member to the enumeration value that best describes the media-specific or media-independent wake-up event.

3.  If the miniportdriver is issuing an [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication for a received packet wake-up event, it must follow these steps:

    1.  The miniport driver sets the **InfoBufferOffset** member to the offset of an [**NDIS\_PM\_WAKE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/hh451603) structure that follows the [**NDIS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh451605) structure in the buffer.

        **Note**  The miniport driver must align the start of the [**NDIS\_PM\_WAKE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/hh451603) structure on a 64-bit boundary.

    2.  The miniport driver sets the **InfoBufferSize** member to the size of the [**NDIS\_PM\_WAKE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/hh451603) structure plus the size of the packet that caused the wake-up event.

    3.  The miniport driver initializes an [**NDIS\_PM\_WAKE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/hh451603) structure following the [**NDIS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh451605) structure in the buffer.

        The miniport driver sets the members of the [**NDIS\_PM\_WAKE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/hh451603) structure as follows:

        -   The **PatternId** member is set to the identifier of the WOL pattern that matches the wake packet. This identifier is specified by the **PatternId** member of the [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure that is passed to the driver during an OID set request of [OID\_PM\_ADD\_WOL\_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569764).

        -   The **PatternFriendlyName** member is set to the user-readable description of the wake pattern that is specified by the **PatternId** member. This value is specified by the **FriendlyName** member of the [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure.

            **Note**  The miniport driver does not need to initialize this member. NDIS sets the **PatternFriendlyName** member to the correct value before it passes the [**NDIS\_PM\_WAKE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/hh451603) structure to overlying drivers.

        -   The **OriginalPacketSize** member is set to the length of the packet as received by the network adapter.

        -   The **SavedPacketSize** member must be set to the length of the packet that is being reported through the [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication.

            **Note**  The value of this member must not be greater than the value that the miniport driver set in the **MaxWoLPacketSaveBuffer** member of the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure. The driver returns this structure when it reports its wake packet indication capabilities. For more information, see [Reporting Wake Reason Status Indication Capabilities](reporting-wake-reason-status-indication-capabilities.md).

        -   The **SavedPacketOffset** member must be set to the offset, in units of bytes, to the wake packet that follows the [**NDIS\_PM\_WAKE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/hh451603) structure.

            **Note**  The miniport driver must align the start of the wake packet on a 64-bit boundary in the buffer.

    4.  The miniport copies the wake packet into the buffer at the offset specified by the **SavedPacketOffset** member.

4.  If the miniport driver is issuing an [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication for a media-specific or media-independent wake-up event, it sets the **InfoBufferOffset** and **InfoBufferSize** members of the [**NDIS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh451605) structure to zero.

5.  The miniport driver initializes an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure. The driver sets the **StatusCode** member to NDIS\_STATUS\_PM\_WAKE\_REASON. The driver also sets the **StatusBuffer** member to point to the buffer, and sets the **StatusBufferLength** to the length, in bytes, of the buffer.

6.  The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) and passes a pointer to the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure in the *StatusIndication* parameter.

**Note**  After the miniport driver issues the [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication for a received packet wake-up event, it must indicate this received packet by calling [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598).