---
title: Device Installation Components
description: Device Installation Components
ms.date: 11/29/2021
ms.localizationpriority: High
---

# Device Installation Components


The following list describes the device installation components that are provided by the Windows operating system:

<a href="" id="plug-and-play--pnp--manager"></a>Plug and Play (PnP) Manager  
The Plug and Play (PnP) manager provides the following support for PnP functionality within Windows:

-   Device detection and enumeration while the system is booting
-   Processing addition or removal of devices while the system is running
-   Installing new devices with a matching [driver package](driver-packages.md)

For more information, see [PnP Manager](pnp-manager.md).

<a href="" id="driver-store"></a>Driver Store  
The driver store is a trusted collection of in-box and third-party [driver packages](driver-packages.md). The operating system maintains this collection in a secure location on the local hard disk. Only the driver packages in the driver store can be installed on a device.

For more information, see [Driver Store](driver-store.md).

<a href="" id="device-installation-apis"></a>Device Installation APIs  
With various device installation APIs, you can programatically add driver packages to the system and update the driver package installed on a device.

For more information, see [Functions that Simplify Driver Installation](functions-that-simplify-driver-installation.md).

<a href="" id="pnputil"></a>PnPUtil  
With PnPUtil, you can view and manage the devices and driver packages on a system. For example, you can view device status and update the driver package on a device.

For more information, see [PnPUtil](/windows-hardware/drivers/devtest/pnputil).

<a href="" id="device-manager"></a>Device Manager  
With Device Manager, you can view and manage the devices on a system. For example, you can view device status and update the driver package on a device.

For more information, see [Using Device Manager](using-device-manager.md). Also, see the Help documentation in Device Manager.

 

 





