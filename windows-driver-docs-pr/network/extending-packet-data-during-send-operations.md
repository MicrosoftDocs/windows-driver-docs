---
title: Extending Packet Data During Send Operations
description: Extending Packet Data During Send Operations
ms.assetid: fc45b9e7-f598-4082-8ab2-6f65a2c2bb9f
keywords:
- extending packet data during send WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extending Packet Data During Send Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If the miniport driver needs to add fields to the 802.11 media access control (MAC) header or payload data of a packet, the driver should use the data backfill area allocated within each [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

The miniport driver defines the maximum amount of data backfill area to reserve in each [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) through the **DataBackFillSize** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure. The miniport driver passes this structure in a call to the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function during driver initialization. For more information about driver initialization, see [Native 802.11 Miniport Driver Initialization](native-802-11-miniport-driver-initialization.md).

**Note**  Native 802.11 miniport drivers must not set the **DataBackFillSize** member to a value greater than 256.

 

The miniport driver sends packets when its [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function is called. Each packet is accessed through a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure, which is referenced through the *NetBufferLists* parameter. If the miniport driver specifies a nonzero value for the data backfill area, NDIS allocates additional space for the backfill area within a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) that is linked within a **NET\_BUFFER\_LIST** structure.

For Native 802.11 miniport drivers, the data backfill area precedes the MAC header or payload data within the buffer described in the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure. For the **NET\_BUFFER** structure within the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) in a send packet, the operating system formats the buffer in the following order:

-   Data backfill area, with as many bytes reserved as defined through the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure in the miniport driver's call to [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).

-   Standard 802.11 MAC header, as defined in Clause 8.2.3 of the IEEE 802.11-2012 standard.

-   IEEE LLC/SNAP header for packet payload encapsulation. For more information about packet payload encapsulation, see [802.11 Payload Encapsulation](802-11-payload-encapsulation.md).

For each [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure referenced through the *NetBufferLists* parameter of [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440), the miniport driver must follow these guidelines when inserting fields or headers within the 802.11 packet data:

-   The miniport driver must call [**NdisRetreatNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff564527) to move the start of the packet data, referenced through a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure, in which fields or headers are being added. The *DataOffsetDelta* parameter of **NdisRetreatNetBufferDataStart** defines the number of bytes to retreat the start of the packet data into the unused data backfill area of the NET\_BUFFER structure.

    For more information about retreating the start of packet data, see [Retreat Operations](retreat-operations.md).

-   The miniport driver determines the new start of the packet data within the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure through the [**NET\_BUFFER\_DATA\_OFFSET**](https://msdn.microsoft.com/library/windows/hardware/ff568383) macro. The miniport driver can then move data to align on the new offset when adding extensions to the packet data.

-   Before completing the send of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure through a call to [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668), the miniport driver must first restore the start of the packet data to its original value for each [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) modified by the driver. In this situation, the miniport driver calls [**NdisAdvanceNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff560703) and sets the *DataOffsetDelta* parameter to the number of bytes required to move the start of the packet data.

    For more information about advancing the start of packet data, see [Advance Operations](advance-operations.md).

    **Note**  When extending packet data, the miniport driver must use the same value for the *DataOffsetDelta* parameter when the driver calls [**NdisRetreatNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff564527) and [**NdisAdvanceNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff560703).

     

 

 





