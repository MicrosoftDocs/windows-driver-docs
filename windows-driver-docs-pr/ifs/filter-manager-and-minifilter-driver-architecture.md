---
title: Filter Manager and Minifilter Driver Architecture
author: windows-driver-content
description: Filter Manager and Minifilter Driver Architecture
ms.assetid: d3fde421-3475-4327-95cf-eaa520f5c132
keywords: ["file system minifilter drivers WDK , architecture", "minifilter drivers WDK , architecture", "filter manager WDK file system minifilter", "file system minifilter drivers WDK , filter manager", "minifilter drivers WDK , filter manager"]
---

# Filter Manager and Minifilter Driver Architecture


## <span id="ddk_writing_a_driverentry_routine_for_a_minifilter_driver_if"></span><span id="DDK_WRITING_A_DRIVERENTRY_ROUTINE_FOR_A_MINIFILTER_DRIVER_IF"></span>


The filter manager is a kernel-mode driver that conforms to the legacy file system filter model and exposes functionality commonly required in file system filter drivers. By taking advantage of this functionality, third-party developers can write minifilter drivers, which are simpler to develop than legacy file system filter drivers, thus shortening the development process while producing higher-quality, more robust drivers.

This section includes:

[Filter Manager Concepts](filter-manager-concepts.md)

[Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md)

[Filter Manager Support for Minifilter Drivers](filter-manager-support-for-minifilter-drivers.md)

[Controlling Filter Manager Operation](controlling-filter-manager-operation.md)

[Development and Testing Tools](development-and-testing-tools.md)

[Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Filter%20Manager%20and%20Minifilter%20Driver%20Architecture%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


