---
title: Device Installation Types
description: Windows uses INF files to install a driver package on a computer or device. All Windows platforms support Windows Drivers, while only Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) supports Windows Desktop Drivers.
keywords:
- Device setup WDK device installations , types
- device installations WDK , types
- installing devices WDK , types
- server-side installations WDK device installations
- client-side installations WDK device installations
ms.date: 12/01/2021
---

# Device Installation Types

Windows uses INF files to install a [driver package](driver-packages.md) on a device. All Windows platforms support [Windows Drivers](../develop/getting-started-with-windows-drivers.md), while only Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) support Windows Desktop Drivers.

## INF files for Windows Drivers

If you are building a [driver package](driver-packages.md) for a non-Desktop variant of Windows, you must supply a driver package that conforms to the Windows Driver requirements. INF files in Windows Driver driver packages contain only a subset of INF sections and directives. For more information, see [Windows Drivers](../develop/getting-started-with-windows-drivers.md).

## INF files for Windows Desktop Drivers

If you are building a desktop-only driver package, your INF file can use legacy, non-universal INF syntax. Windows 10 for desktop editions continues to support legacy INF behavior.

 

 





