---
title: Filter Initialization
description: Filter Initialization
ms.assetid: c39dc5a6-f529-40a2-87d4-bac325b4fa1a
---

# Filter Initialization


The crash dump drivers are initialized in the early stages of the system crash or hibernation processes. However, the filter drivers are initialized as soon as they are loaded. This gives the filter drivers an opportunity to do any necessary initialization that cannot be done during the crash initialization time, such as allocating memory.

In the crash dump driver stack, filter drivers are initialized during the system boot time. You can disable and re-enable crash dump at any time when the system is running, so crash dump filter drivers should not make any assumptions about the driver load and unload time. For hibernation, the filter driver is loaded and initialized when hibernation is started.

After the filter driver is loaded into memory, the crash dump driver calls the filter driver's DriverEntry function to initialize the filter driver. The standard DriverEntry function takes two arguments (DriverObject and RegistryPath). When the filter driver is called, DriverObject points to a [**FILTER\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff553862) structure, and RegistryPath points to a [**FILTER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff553865) structure.

To complete the initialization process, the filter driver should initialize the [**FILTER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff553865) structure and return it to the crash dump driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Filter%20Initialization%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




