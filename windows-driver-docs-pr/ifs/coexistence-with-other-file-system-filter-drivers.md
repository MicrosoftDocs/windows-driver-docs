---
title: Coexistence with other File System Filter Drivers
description: Coexistence with other File System Filter Drivers
ms.assetid: 595f9fa1-0ed7-4f99-a026-bf00bbf8bf33
keywords:
- security WDK file systems , coexistence
- coexistence WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Coexistence with other File System Filter Drivers


## <span id="ddk_coexistence_with_other_file_system_filter_drivers_if"></span><span id="DDK_COEXISTENCE_WITH_OTHER_FILE_SYSTEM_FILTER_DRIVERS_IF"></span>


One of the most insidious problems that must be properly handled by a file system filter driver is coexistence with other filter drivers. When building a file system filter driver to coexist with other file system filter drivers, it is best to consider the following issues:

-   Filter drivers must consider the presence of other filter drivers in their operations. Any operation performed by the filter driver should be robust enough to survive an additional filter driver using the same or different technique.

-   Filter drivers may impact the behavior of other filters by changing the base behavior of the system.

-   Increasing the number of filter drivers increases the consumption of scarce resources, notably stack space. File system filter drivers must strive to minimize their use of such scarce resources. Otherwise, malicious user applications can take advantage of such weaknesses to cause the system to fail. Developers should be particularly careful about completion paths and error paths.

-   Filter drivers should be conservative in what they send to the lower driver (filter driver or file system) and should be liberal in what they accept. Whenever possible, the filter driver should try to ensure the operations they send to the underlying driver are simple and not complicated (do not perform rename operations during create operations, for example).

-   Filter drivers must be cautious about locking. Locks must never be held across file system calls. Various components of the system make very precise and explicit assumptions about lock ordering and functions that can and cannot block. Disturbing this by adding another layer of locking can easily lead to deadlocks. I/O originating from Srv.sys exposes these problems particularly quickly, but they can be seen during normal stress testing as well.

It is imperative that any file system filter driver developer not only design and implement to coexist cleanly with other filter drivers, but also test the filter driver with other filter drivers to ensure that the driver does not introduce security problems within the system.

 

 




