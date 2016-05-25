---
title: Impersonation in a File System Filter Driver
author: windows-driver-content
description: Impersonation in a File System Filter Driver
ms.assetid: ee56cd54-01ac-46ad-8ee4-e76131b058f3
keywords: ["security WDK file systems , impersonation", "impersonation WDK file systems"]
---

# Impersonation in a File System Filter Driver


## <span id="ddk_impersonation_in_a_file_system_filter_driver_if"></span><span id="DDK_IMPERSONATION_IN_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


Another operation a file system filter driver might attempt to use is impersonation. While impersonation is a very powerful technique for handling security on behalf of other threads, it also requires appropriate care for use on behalf of any component. For a file system filter driver, it is important to identify the operations that need to be done using impersonation. Then, it is essential to ensure that other operations that are performed by the file system filter driver should not be done using impersonation. The risk with impersonation is typically that the caller has fewer privileges than the driver making the call. Thus, if a call is made with impersonation, it might fail, while it would succeed without impersonation.

Impersonation is needed for any operation that creates a new handle because the handle represents the reference to the object and is the point at which the security check has been performed. For example, impersonation is necessary when opening a file or other object (using [**ZwCreateSection**](https://msdn.microsoft.com/library/windows/hardware/ff566428), [**ZwCreateEvent**](https://msdn.microsoft.com/library/windows/hardware/ff566423), and [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), for example). In these calls, the filter driver calling them must ensure that the parameters being passed are valid because other operating system operations will assume that calls originating from kernel mode will have valid parameters. Thus, a filter driver cannot safely pass a user buffer address to any of these functions, even when impersonating.

In the case of [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), there is a corresponding I/O manager call, [**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418), that should be used with impersonation because it allows the filter driver to specify IO\_FORCE\_ACCESS\_CHECK. Absent this option, the I/O manager will not enforce proper user level access checks.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Impersonation%20in%20a%20File%20System%20Filter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


