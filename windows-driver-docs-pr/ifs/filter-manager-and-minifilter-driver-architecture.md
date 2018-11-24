---
title: Filter Manager and Minifilter Driver Architecture
description: Filter Manager and Minifilter Driver Architecture
ms.assetid: d3fde421-3475-4327-95cf-eaa520f5c132
keywords:
- file system minifilter drivers WDK , architecture
- minifilter drivers WDK , architecture
- filter manager WDK file system minifilter
- file system minifilter drivers WDK , filter manager
- minifilter drivers WDK , filter manager
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 


