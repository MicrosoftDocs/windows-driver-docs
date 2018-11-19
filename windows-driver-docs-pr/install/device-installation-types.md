---
title: Device Installation Types
description: Windows uses INF files to install a driver package on a computer or device. All Windows platforms support universal INF files, while only Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) supports legacy INF files.
ms.assetid: 23b999de-7151-4b4a-b9fc-331909bb8c06
keywords:
- Device setup WDK device installations , types
- device installations WDK , types
- installing devices WDK , types
- server-side installations WDK device installations
- client-side installations WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Installation Types


Windows uses INF files to install a driver package on a computer or device. All Windows platforms support universal INF files, while only Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) supports legacy INF files.

## INF files for universal and mobile driver packages


If you are building a universal or mobile driver package, you must supply a universal INF file. Universal INFs contain only the subset of INF sections and directives that are required to install and configure a device. These directives can be performed on an offline system, without any runtime operations. For more information, see [Using a Universal INF File](using-a-universal-inf-file.md).

## INF files for desktop driver packages


If you are building a desktop-only driver package, your INF file can use legacy, non-universal INF syntax.

Windows 10 for desktop editions continues to support legacy INF behavior, such as co-installers and class installers.

 

 





