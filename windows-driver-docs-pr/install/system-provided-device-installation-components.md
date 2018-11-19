---
title: System-Provided Device Installation Components
description: System-Provided Device Installation Components
ms.assetid: faf586b9-ab99-4fee-a0d1-923000000189
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# System-Provided Device Installation Components


The following list describes the device installation components that are provided by the Windows operating system:

<a href="" id="plug-and-play--pnp--manager"></a>Plug and Play (PnP) Manager  
The Plug and Play (PnP) manager provides the following support for PnP functionality within Windows:

-   Device detection and enumeration while the system is booting
-   Adding or removing devices while the system is running

For more information, see [PnP Manager](pnp-manager.md).

<a href="" id="setupapi"></a>SetupAPI  
The Setup application programming interface (*SetupAPI*) includes the general setup functions (**Setup***Xxx*) and the device installation functions (**SetupDi***Xxx* and **Di***Xxx*). These functions perform many device installation tasks such as searching for INF files, building a potential list of drivers for a device, copying driver files, writing information to the registry, and registering device co-installers. Most of the other device installation components call these functions.

For more information, see [SetupAPI](setupapi.md).

<a href="" id="configuration-manager-api"></a>Configuration Manager API  
The PnP configuration manager API provides basic installation and configuration operations that are not provided by SetupAPI. The PnP configuration manager functions perform low-level tasks such as obtaining the status of a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) and managing resource descriptors. These functions are primarily called by SetupAPI but can also be called by other device installation components.

<a href="" id="driver-store"></a>Driver Store  
Starting with Windows Vista, the driver store is a trusted collection of in-box and third-party [driver packages](driver-packages.md). The operating system maintains this collection in a secure location on the local hard disk. Only the driver packages in the driver store can be installed for a device.

For more information, see [Driver Store](driver-store.md).

<a href="" id="device-manager"></a>Device Manager  
With Device Manager, you can view and manage the devices on a system. For example, you can view device status and set device properties.

For more information, see [Using Device Manager](using-device-manager.md). Also, see the Help documentation in Device Manager.

 

 





