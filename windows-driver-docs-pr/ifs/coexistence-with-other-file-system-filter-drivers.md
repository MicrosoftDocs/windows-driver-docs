---
title: Coexistence with other File System Filter Drivers
author: windows-driver-content
description: Coexistence with other File System Filter Drivers
ms.assetid: 595f9fa1-0ed7-4f99-a026-bf00bbf8bf33
keywords: ["security WDK file systems , coexistence", "coexistence WDK file systems"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Coexistence%20with%20other%20File%20System%20Filter%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


