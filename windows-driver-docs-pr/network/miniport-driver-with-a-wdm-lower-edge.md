---
title: Miniport Driver with a WDM Lower Edge
description: Miniport Driver with a WDM Lower Edge
keywords:
- NDIS-WDM miniport drivers WDK networking , about NDIS-WDM miniport drivers
- NDIS-WDM miniport drivers WDK networking , components
- lower edge of NDIS miniport drivers WDK networking
- WDM lower edge WDK networking
- lower edge of NDIS miniport drivers WDK networking , about WDM lower edge
- WDM lower edge WDK networking , about WDM lower edge
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Driver with a WDM Lower Edge





A miniport driver with a WDM lower edge (an NDIS-WDM miniport driver) follows the WDM rule that specifies that a WDM header file must be included in the driver's source files. An NDIS-WDM miniport driver requires a WDM header file to call kernel-mode routines on its lower edge. Typically, NDIS miniport drivers should just call functions that NDIS provides. This restriction is shown by the way NDIS wraps around NDIS miniport drivers in the figure in the [NDIS Drivers](ndis-drivers.md) section. Although typical NDIS miniport drivers are not called WDM drivers, they indirectly follow WDM rules because NDIS itself follows WDM rules.

The following diagram shows an NDIS-WDM miniport driver that interfaces with the USB driver stack by using a WDM lower edge.

![diagram illustrating an ndis-wdm miniport driver that interfaces with the usb driver stack by using a wdm lower edge.](images/nonndslo.png)

The following list describes the components that the preceding diagram shows:

<a href="" id="ipx-spx-compatible-and-tcp-ip"></a>IPX/SPX Compatible and TCP/IP  
[NDIS protocol drivers](./roadmap-for-developing-ndis-protocol-drivers.md) that transmit packets by using underlying miniport drivers.

<a href="" id="ndis"></a>NDIS  
The Ndis.sys driver that provides a standard interface between layered network drivers.

<a href="" id="ndis-wdm-miniport-driver-for-usb"></a>NDIS-WDM Miniport Driver for USB  
An NDIS-WDM miniport driver that interfaces with the USB driver stack.

<a href="" id="usb-client-drivers"></a>USB Client Drivers  
Other vendor-supplied USB client drivers.

<a href="" id="usb-class-interface"></a>USB Class Interface  
[USB Routines](/previous-versions/windows/hardware/drivers/ff540046(v=vs.85)) and [I/O requests](/previous-versions/ff537421(v=vs.85)) that USB client drivers can use to interface with the USB driver stack.

<a href="" id="usb-driver-stack"></a>USB Driver Stack  
Driver stack for USB devices. For more information, see [USB Driver Stack Architecture](../usbcon/usb-3-0-driver-stack-architecture.md).

