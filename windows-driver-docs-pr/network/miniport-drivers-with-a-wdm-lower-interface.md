---
title: Miniport Drivers with a WDM Lower Interface
description: Miniport Drivers with a WDM Lower Interface
ms.assetid: defa955b-c1d2-4c78-a983-584aedc8a1a3
keywords:
- miniport drivers WDK networking , WDM lower interface
- NDIS miniport drivers WDK , WDM lower interface
- NDIS-WDM miniport drivers WDK networking
- WDM lower interface WDK NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Drivers with a WDM Lower Interface





A miniport driver with a Microsoft [Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698) (WDM) lower interface is also known as an *NDIS-WDM miniport driver*. This type of miniport driver:

-   Uses a WDM lower edge.

-   Can call both NDIS and non-NDIS functions. However, whenever possible, the miniport driver should call NDIS functions.

-   Can initialize a miniport instance that is used to control devices that are attached to a particular bus and that communicates with those devices over that bus.

For example, a miniport driver that controls devices on either Universal Serial Bus (USB) or IEEE 1394 (Firewire) buses must expose a standard NDIS miniport driver interface at its upper edge and use the class interface for the particular bus at its lower edge. Such a miniport driver communicates with devices that are attached to the bus by sending I/O request packets (IRPs) to the bus.

The following topics describe how to implement a miniport driver that uses a WDM lower edge:

[Miniport Driver with a WDM Lower Edge](miniport-driver-with-a-wdm-lower-edge.md)

[Registering Miniport Driver Functions for WDM Lower Edge](registering-miniport-driver-functions-for-wdm-lower-edge.md)

[Initializing a Miniport Driver with a WDM Lower Edge](initializing-a-miniport-driver-with-a-wdm-lower-edge.md)

[Issuing Commands to Communicate with Devices](issuing-commands-to-communicate-with-devices.md)

[Implementation Tips and Requirements for WDM Lower Edge](implementation-tips-and-requirements-for-wdm-lower-edge.md)

[Compile Flags for WDM Lower Edge](compile-flags-for-wdm-lower-edge.md)

[Power Management for WDM Lower Edge](power-management-for-wdm-lower-edge.md)

[Installing NDIS-WDM Miniport Drivers](installing-ndis-wdm-miniport-drivers.md)

 

 





