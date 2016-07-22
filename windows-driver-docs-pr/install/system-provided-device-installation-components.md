---
title: System-Provided Device Installation Components
description: System-Provided Device Installation Components
ms.assetid: faf586b9-ab99-4fee-a0d1-923000000189
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20System-Provided%20Device%20Installation%20Components%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




