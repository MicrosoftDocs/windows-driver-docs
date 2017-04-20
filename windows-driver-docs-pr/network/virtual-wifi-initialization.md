---
title: Virtual WiFi Initialization
description: Virtual WiFi Initialization
ms.assetid: f7ff1c74-1d5d-4987-bb66-10f1bf1d0ccd
keywords:
- Virtual WiFi in kernel mode WDK networking , initialization
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Virtual WiFi Initialization


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

To support Virtual WiFi, the 802.11 miniport driver must implement multiple instances of 802.11 MAC entities. Each MAC entity maintains the state related to one type of 802.11 connection. NDIS 6.20 and later support three types of MAC entities: Extensible Station, Extensible Access Point, and Virtual Station.

MAC entities are created and deleted dynamically by the miniport driver at the direction of the operating system, through calls to [Virtual WiFi OIDs](virtual-wifi-in-kernel-mode.md). The operating system treats each of the MAC entities as a separate virtual adapter, and it controls each MAC individually. The miniport driver is responsible for multiplexing and de-multiplexing the control and data traffic between the physical wireless interface and the different MAC entities.

The miniport driver exposes each MAC entity to the operating system as a separate NDIS port. By default, at initialization the driver creates the first MAC instance that is associated with the default NDIS port (port number 0) that is created by the operating system. For any subsequent MAC entities, the driver allocates and initializes a new NDIS port using the [**NdisMAllocatePort**](https://msdn.microsoft.com/library/windows/hardware/ff562779) function.

To map an operation to the appropriate MAC entity, the miniport driver uses the port number present in the NDIS OIDs and the NDIS Send calls. Similarly, for NDIS Receive and Status indications for a particular MAC entity, the miniport driver should fill in the corresponding NDIS port number. This port number exposes the MAC entity as a virtual adapter to the rest of the networking components.

The miniport driver should create ports as described in [Allocating an NDIS Port](allocating-an-ndis-port.md) and [OID\_DOT11\_CREATE\_MAC](https://msdn.microsoft.com/library/windows/hardware/ff569124).

 

 





