---
title: Reporting Wake Reason Status Indication Capabilities
description: Reporting Wake Reason Status Indication Capabilities
ms.assetid: A72D04F7-EB09-4B1B-9AF5-7FEBC2514CE9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Wake Reason Status Indication Capabilities


Starting with NDIS 6.30, the miniport driver must report whether it can issue an NDIS wake reason status indication ([**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808)) to report wake-up events caused by one of the following:

-   The network adapter received a packet that matched a wake-on-LAN (WOL) pattern. This includes the receipt of a packet that matches a receive filter specified through an object identifier (OID) set request of [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

    **Note**  For this type of wake reason status indication, the network adapter must be able to save the received packet. The driver must return the received packet within the status indication.

     

-   The network adapter detected a media-specific event, such as a disassociation from an 802.11 access point (AP) or the receipt of a mobile broadband (MB) Short Message Service (SMS) message.

-   The network adapter detected another enabled event that is not specific to a WOL pattern or media type (*media-independent event*). For example, the miniport driver issues the [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication if it enabled the network adapter to detect media connection or disconnection.

**Note**  Support for NDIS wake reason status indications is optional for Mobile Broadband (MB) miniport drivers.

 

When NDIS calls the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the miniport driver reports its wake reason status indication capabilities by following these steps:

1.  The miniport driver initializes an [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure with the power management capabilities of the underlying hardware.

    To enable the support for wake reason status indications, the miniport driver must set the members of the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure as follows:

    -   The miniport driver must specify NDIS\_PM\_CAPABILITIES\_REVISION\_2 and NDIS\_SIZEOF\_NDIS\_PM\_CAPABILITIES\_REVISION\_2 for the revision and length of the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure within the structure's **Header** member.
    -   If the network adapter can store the received packet that caused a system wake-up event, the miniport driver sets the NDIS\_PM\_WAKE\_PACKET\_INDICATION\_SUPPORTED flag within the **Flags** member of this structure.

        If this flag is set, the network adapter must be able to save the received packet that caused the adapter to generate a wake-up event. In addition, the miniport driver must be able to do the following with this packet after the network adapter transitions to a full-power state:

        -   The miniport driver must be able to indicate the packet by calling [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598).

        -   The miniport driver must be able to issue an [**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808) status indication and must pass the packet with indication.

    -   The miniport driver sets the **MaxWoLPacketSaveBuffer** member to the maximum size, in units of bytes, of the buffer that contains the WOL packet that caused a system wake-up event.

        The value of the **MaxWoLPacketSaveBuffer** member must be less than or equal to the size, in bytes, of the maximum transmission unit (MTU) and media access control (MAC) header for the network media. The driver reports the MTU size through OID query requests of [OID\_GEN\_MAXIMUM\_FRAME\_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569598).

    -   The miniport driver sets the **SupportedWakeUpEvents** to the media-independent wake-up events that the network adapter supports, such as generating a wake-up event when the adapter becomes connected to the networking interface.

    -   The miniport driver sets the **MediaSpecificWakeUpEvents** to the media-specific wake-up events that the network adapter supports. These events include generating a wake-up event when the 802.11 adapter becomes disassociated with the AP.

2.  The miniport driver initializes an [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure and sets the**PowerManagementCapabilitiesEx** member to the address of the initialized [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure.

3.  The miniport driver calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function to register its power management capabilities. When the miniport driver calls this function, it sets the *MiniportAttributes* parameter to the address of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure.

The method that is used by miniport drivers to report the wake reason status indication capabilities is based on the NDIS 6.20 method for reporting power management capabilities. For more information about this method, see [Reporting Power Management Capabilities](reporting-power-management-capabilities.md).

For more information about the adapter initialization process, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

For more information about how to report power management capabilities, see [Reporting Power Management Capabilities](reporting-power-management-capabilities.md).

 

 





