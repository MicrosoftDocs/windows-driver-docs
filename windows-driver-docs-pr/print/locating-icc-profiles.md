---
title: Locating ICC Profiles
description: Locating ICC Profiles
ms.assetid: 828b53cd-452a-4c4d-bfbb-45ea674ef49a
keywords:
- color management WDK print , locating ICC profiles
- ICC profiles WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Locating ICC Profiles





When color management is enabled, GDI searches for an appropriate ICC profile, using the following steps:

1.  If the driver's [printer interface DLL](printer-interface-dll.md) provides a [**DrvQueryColorProfile**](https://msdn.microsoft.com/library/windows/hardware/ff548573) function, the GDI client calls the function to give the driver an opportunity to specify a profile. If the function returns a profile, it is used.

2.  If **DrvQueryColorProfile** does not exist or does not return a profile, GDI searches the color directory for profiles that have been installed for the specified printer type. GDI uses the first profile it finds that matches resolution, media type, and dithering settings in the DEVMODE structure.

3.  If the color directory does not contain any profiles for the specified printer type that match the specified DEVMODE contents, GDI uses the system's default sRGB profile.

For more information, see [Installing ICC Profiles](installing-icc-profiles.md). Additional information about ICC profiles can be found in the Microsoft Windows SDK documentation.

 

 




