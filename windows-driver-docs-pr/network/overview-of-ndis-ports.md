---
title: Overview of NDIS Ports
description: Overview of NDIS Ports
ms.assetid: 324f06c9-d482-4acd-a7a6-050721197c89
keywords:
- ports WDK NDIS , about NDIS ports
- NDIS ports WDK , about NDIS ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of NDIS Ports





This section introduces NDIS ports, which are an NDIS 6.0 feature and which enable overlying networking layers to access subinterfaces. In NDIS, network interfaces are associated with miniport adapters, and subinterfaces of a miniport adapter are called *NDIS ports*.

The architecture of the driver stack is much simpler because every network interface is treated as a miniport adapter. For example, each miniport adapter has its own IP and MAC address. In most cases, the overlying drivers do not require information about the virtual or physical nature of the miniport adapter or information about the physical device at the bottom of the driver stack.

An NDIS miniport adapter can provide an interface for a physical device or a virtual device. NDIS intermediate drivers provide interfaces for virtual devices that are called *virtual miniports*. NDIS intermediate drivers can bind to underlying miniport adapters and expose virtual miniports that overlying protocol drivers bind to.

In many cases, there is no one-to-one relationship between the underlying physical devices and virtual miniports. For example, an intermediate driver that implements failover functionality can create one virtual miniport to support multiple physical devices, and a virtual LAN (VLAN) intermediate driver can create multiple virtual miniports that are associated with a single physical device. Also, a driver that combines both failover and VLAN functionality can create a set of virtual miniports (*N* number of VLANs) while the driver is bound to multiple physical devices (*M* number of physical devices). For more information about intermediate drivers and virtual miniports, see [NDIS 6.0 Intermediate Drivers](writing-ndis-intermediate-drivers.md).

In some applications, the ability to address the subinterfaces that are below virtual miniports is either required or simplifies the design. For example, the Extensible Authentication Protocol (EAP) protocol must specify the physical device that an EAP packet is sent or received on. If multiple physical devices are associated with a single virtual device, the EAP protocol is bound to the virtual device. In that case, the NDIS interfaces prior to NDIS 6.0 hide the subinterfaces, and the EAP protocol cannot choose which underlying physical device should carry the EAP packets. The EAP protocol then does not have any access to the underlying physical miniport adapters. Exposing the underlying physical miniport adapters as NDIS ports allows the EAP protocol to target a particular physical device.

The following topics further describe NDIS ports:

[Identifying an NDIS Port](identifying-an-ndis-port.md)

[Default NDIS Port](default-ndis-port.md)

[Types of NDIS Ports](types-of-ndis-ports.md)

[NDIS Port States](ndis-port-states.md)

 

 





