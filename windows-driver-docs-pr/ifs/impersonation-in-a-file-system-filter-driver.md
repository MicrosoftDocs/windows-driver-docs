---
title: Impersonation in a File System Filter Driver
description: Impersonation in a File System Filter Driver
ms.assetid: ee56cd54-01ac-46ad-8ee4-e76131b058f3
keywords:
- security WDK file systems , impersonation
- impersonation WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Impersonation in a File System Filter Driver


## <span id="ddk_impersonation_in_a_file_system_filter_driver_if"></span><span id="DDK_IMPERSONATION_IN_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


Another operation a file system filter driver might attempt to use is impersonation. While impersonation is a very powerful technique for handling security on behalf of other threads, it also requires appropriate care for use on behalf of any component. For a file system filter driver, it is important to identify the operations that need to be done using impersonation. Then, it is essential to ensure that other operations that are performed by the file system filter driver should not be done using impersonation. The risk with impersonation is typically that the caller has fewer privileges than the driver making the call. Thus, if a call is made with impersonation, it might fail, while it would succeed without impersonation.

Impersonation is needed for any operation that creates a new handle because the handle represents the reference to the object and is the point at which the security check has been performed. For example, impersonation is necessary when opening a file or other object (using [**ZwCreateSection**](https://msdn.microsoft.com/library/windows/hardware/ff566428), [**ZwCreateEvent**](https://msdn.microsoft.com/library/windows/hardware/ff566423), and [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), for example). In these calls, the filter driver calling them must ensure that the parameters being passed are valid because other operating system operations will assume that calls originating from kernel mode will have valid parameters. Thus, a filter driver cannot safely pass a user buffer address to any of these functions, even when impersonating.

In the case of [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), there is a corresponding I/O manager call, [**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418), that should be used with impersonation because it allows the filter driver to specify IO\_FORCE\_ACCESS\_CHECK. Absent this option, the I/O manager will not enforce proper user level access checks.

 

 




