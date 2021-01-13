---
title: Filter Initialization
description: Filter Initialization
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Initialization


The crash dump drivers are initialized in the early stages of the system crash or hibernation processes. However, the filter drivers are initialized as soon as they are loaded. This gives the filter drivers an opportunity to do any necessary initialization that cannot be done during the crash initialization time, such as allocating memory.

In the crash dump driver stack, filter drivers are initialized during the system boot time. You can disable and re-enable crash dump at any time when the system is running, so crash dump filter drivers should not make any assumptions about the driver load and unload time. For hibernation, the filter driver is loaded and initialized when hibernation is started.

After the filter driver is loaded into memory, the crash dump driver calls the filter driver's DriverEntry function to initialize the filter driver. The standard DriverEntry function takes two arguments (DriverObject and RegistryPath). When the filter driver is called, DriverObject points to a [**FILTER\_EXTENSION**](/windows-hardware/drivers/ddi/ntdddump/ns-ntdddump-_filter_extension) structure, and RegistryPath points to a [**FILTER\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/ntdddump/ns-ntdddump-_filter_initialization_data) structure.

To complete the initialization process, the filter driver should initialize the [**FILTER\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/ntdddump/ns-ntdddump-_filter_initialization_data) structure and return it to the crash dump driver.

 

