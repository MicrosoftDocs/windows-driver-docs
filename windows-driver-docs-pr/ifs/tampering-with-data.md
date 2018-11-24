---
title: Tampering with Data
description: Tampering with Data
ms.assetid: 277395b9-b770-45b4-8f4c-cad8b684ca44
keywords:
- threat models WDK file systems , data tampering
- security threat models WDK file systems , data tampering
- data tampering WDK file systems
- tampering with data WDK file systems
- buffers WDK file systems
- IOCTLs WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tampering with Data


## <span id="ddk_tampering_with_data_if"></span><span id="DDK_TAMPERING_WITH_DATA_IF"></span>


Data tampering is a threat for drivers, but a serious threat for file system and file system filter drivers. For all drivers, there is a potential threat that any control structure shared between user-mode and kernel-mode components may be modified by the user-mode component while it is in use by the kernel-mode component. File system and filter drivers are particularly vulnerable to this class of attack because they have a strong reliance on METHOD\_NEITHER data transfer types that directly access the user buffer through its virtual address. Fast I/O also directly accesses raw user-mode buffers. The risk here is that a driver might be using this data while the application is modifying the data. Typically, a driver attempts to protect against this by validating the data. However, data validation only works if the data cannot change after it has been validated.

For file system and file system filter drivers, there are numerous IOCTL and FSCTL operations that are used to transfer information between user-mode applications and the various kernel-mode drivers. Further, it is quite common for such drivers to have private IOCTL and FSCTL operations that also transfer control and data information between user-mode services and their kernel-mode drivers.

Inherent in this design model is an assumption that only the driver's service or application will take advantage of its interface. Such a design and implementation is at risk for the following reasons:

-   A malicious application could send a valid buffer to the driver, and then subsequently modify the data in an attempt to probe and find the weaknesses of the driver.

-   Failures within the control application could cause the data contents of a control buffer to become invalid. For example, a stack-based control region might become invalid if an exception were to change the flow of control and cause a reuse of the stack region.

Protecting against this category of problem requires constant vigilance in terms of the implementation. Buffers must be located in non-volatile memory (either kernel-only or read-only memory) prior to being validated. If the buffer contains references to any other buffers or control structures, they too must be located in non-volatile memory before they are validated.

Developers should also be aware that IOCTL using the **FastIoDeviceControl** dispatch will pass data in raw user buffers. So drivers implementing the fast I/O version for IOCTLs should take appropriate steps to prevent problems.

Note that validating the data by itself is not enough. For example, a successful call to [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) might indicate that a buffer is valid, but subsequent changes in the application address space could cause that state to change. The application could terminate, for example, prior to the driver actually using the buffer directly. Thus, the driver must protect against any change within the application's address space. Normally this is done using structured exception handling using **\_\_try** and **\_\_except** around any code that accesses a user buffer address directly.

 

 




