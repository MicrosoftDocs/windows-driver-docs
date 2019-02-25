---
title: NDIS Miniport Drivers with a WDM Lower Edge
description: NDIS Miniport Drivers with a WDM Lower Edge
ms.assetid: b371a267-c57d-4d6d-81a1-53f4b51cacea
keywords:
- miniport drivers WDK networking , types
- NDIS miniport drivers WDK , types
- WDM lower edge WDK networking
- lower edge of NDIS miniport drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Miniport Drivers with a WDM Lower Edge





You can write an NDIS miniport driver that controls a device on a bus — for example, the Universal Serial Bus (USB) or the IEEE 1394 (firewire) bus. Such a miniport driver must expose a standard NDIS miniport driver interface at its upper edge and use the class interface for the particular bus at its lower edge. The miniport driver communicates with devices that are attached to the bus by sending I/O request packets (IRPs) to the bus through its Microsoft Windows Driver Model (WDM) lower interface.

A miniport driver with a WDM lower edge must be deserialized. For more information about deserialized drivers, see [Deserialized NDIS Miniport Drivers](deserialized-ndis-miniport-drivers.md).

For more information about miniport drivers with a WDM lower edge, see [Miniport Drivers with a WDM Lower Interface](miniport-drivers-with-a-wdm-lower-interface.md).

 

 





