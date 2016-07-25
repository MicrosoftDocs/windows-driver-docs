---
title: Device Installation Types
description: Windows uses INF files to install a driver package on a computer or device. All Windows platforms support universal INF files, while only Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) supports legacy INF files.
ms.assetid: 23b999de-7151-4b4a-b9fc-331909bb8c06
keywords: ["Device setup WDK device installations , types", "device installations WDK , types", "installing devices WDK , types", "server-side installations WDK device installations", "client-side installations WDK device installations"]
---

# Device Installation Types


Windows uses INF files to install a driver package on a computer or device. All Windows platforms support universal INF files, while only Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) supports legacy INF files.

## INF files for universal and mobile driver packages


If you are building a universal or mobile driver package, you must supply a universal INF file. Universal INFs contain only the subset of INF sections and directives that are required to install and configure a device. These directives can be performed on an offline system, without any runtime operations. For more information, see [Using a Universal INF File](using-a-configurable-inf-file.md).

## INF files for desktop driver packages


If you are building a desktop-only driver package, your INF file can use legacy, non-universal INF syntax.

Windows 10 for desktop editions continues to support legacy INF behavior, such as co-installers and class installers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Installation%20Types%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




