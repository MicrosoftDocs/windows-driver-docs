---
title: Security Considerations for File System Filter Drivers
description: Security Considerations for File System Filter Drivers
ms.assetid: 59b5fa88-fd7e-4d1c-8e2e-2b2ec4c9a250
---

# Security Considerations for File System Filter Drivers


## <span id="ddk_security_considerations_for_file_system_filter_drivers_if"></span><span id="DDK_SECURITY_CONSIDERATIONS_FOR_FILE_SYSTEM_FILTER_DRIVERS_IF"></span>


File system filter drivers have a distinct set of security issues in addition to those that apply to all drivers and to file system specific issues. This section discusses key issues that need to be addressed by file system filter driver writers, although it does not provide a complete list of all possible security issues.

This section includes the following topics:

[Proxy Operations in File System Filter Drivers](proxy-operations-in-file-system-filter-drivers.md)

[Impersonation in a File System Filter Driver](impersonation-in-a-file-system-filter-driver.md)

[Coexistence with other File System Filter Drivers](coexistence-with-other-file-system-filter-drivers.md)

[Memory Mapped Files in a File System Filter Driver](memory-mapped-files-in-a-file-system-filter-driver.md)

[Reparse Points in a File System Filter Driver](reparse-points-in-a-file-system-filter-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Security%20Considerations%20for%20File%20System%20Filter%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




