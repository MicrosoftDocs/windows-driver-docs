---
title: IEEE 802.11e/WMM Support
description: IEEE 802.11e/WMM Support
ms.assetid: 5272d0c7-02a2-49ba-a68e-adae6cec6976
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IEEE 802.11e/WMM Support


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Windows operating system does not fully support Quality of Service (QoS) as specified through the IEEE 802.11e-2005 standard and IEEE Document 802.11-03-504r7. The operating system will:

-   Not insert the Wireless Multimedia (WMM) QoS Control field within the 802.11 media access control (MAC) header of packets sent through calls to the miniport driver's [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function.

-   Process the QoS Control field for received packets that are indicated through calls to the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function. In this situation, the Native 802.11 miniport driver must return the appropriate 802.1D priority value through the [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) structure that is associated with the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure used for the received packet.

For more information about the QoS Control field, refer to Clause 2.1 of IEEE Document 802.11-03-504r7.

Support for 802.11e QoS services is dependent upon the implementation of the 802.11 station and miniport driver. If the independent hardware vendor (IHV) supports 802.11e QoS, it must do the following:

-   Set the NDIS\_MAC\_OPTION\_8021P\_PRIORITY flags when [OID\_GEN\_MAC\_OPTIONS](https://msdn.microsoft.com/library/windows/hardware/ff569597) is queried.

-   Add the QoS Control field to the IEEE MAC header for packets sent through calls to the miniport driver's [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function. The driver sets the UP bits of the QoS Control field based on the IEEE 802.1D value. This value is returned through the [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) structure that is associated with the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure used for the sent packet.

-   Either retain or remove the QoS Control field from the IEEE MAC header for received packets prior to calling [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598). The driver must return the appropriate 802.1D priority value through the [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) structure that is associated with the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure used for the received packet.

In order to insert the QoS Control field into the IEEE MAC Header for packets sent through calls to [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440), the miniport driver must follow these guidelines.

-   When its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called, the miniport driver calls [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) and passes an [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure with the **DataBackFillSize** member set to the size of the QoS Control field.

-   For each [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure referenced through the *NetBufferLists* parameter of the [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function, the miniport driver adds the QoS Control field after the 802.11 MAC header, which is contained in the first [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure of the NET\_BUFFER\_LIST structure. To accomplish this, the miniport driver completes the following steps:
    1.  Retreats the start of the packet data to make room for the QoS Control field by calling [**NdisRetreatNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff564527) with the *DataOffsetDelta* parameter set to the length, in bytes, of the QoS Control field.
    2.  Queries the new data offset for the start of the packet data through the [**NET\_BUFFER\_DATA\_OFFSET**](https://msdn.microsoft.com/library/windows/hardware/ff568383) macro. The driver then copies the 802.11 MAC header to the packet data starting at the new data offset within the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.
    3.  Formats the QoS Control field immediately after the 802.11 MAC header, and then instructs the 802.11 station to send the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.
-   Before the miniport driver completes the packet send by calling [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668), the driver must restore the data offset of the first NET\_BUFFER structure to its original value by calling [**NdisAdvanceNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff560703) with the *DataOffsetDelta* parameter set to the length, in bytes, of the QoS Control field.

 

 





