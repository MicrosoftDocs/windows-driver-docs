---
title: Updating Core Drivers Files for Non-Package-Aware Drivers
author: windows-driver-content
description: Updating Core Drivers Files for Non-Package-Aware Drivers
ms.assetid: ce5da376-edac-4cd1-8750-9981bb5b709d
---

# Updating Core Drivers Files for Non-Package-Aware Drivers


Core driver components for Windows operating systems earlier than Windows Vista, including Windows Server 2003, Windows XP, and Windows 2000, are available on the Microsoft [Connect](http://go.microsoft.com/fwlink/p/?linkid=133880) Web site as separate packages for the XPSDrv, UniDrv, and PostScript drivers. Each package has a different redistribution agreement. The files in the packages are, in fact, identical to their counterparts in Windows Vista. To unpack the driver files, follow the steps listed in [Get the Updated Core Driver Package](getting-the-updated-core-driver-package.md). Once you have expanded the core driver package, include the core driver files you need in your own driver package as if they were part of your driver. In other words, copy the driver binary files from the core package to the main directory of your driver package. This will break the integrity of the digitally signed core driver package, but it will enable Windows XP (and the other Windows operating systems earlier than Windows Vista) and drivers that are not package aware to take advantage of the core driver updates.

Note that the unaltered core driver package can still be stored in a separate subdirectory in your driver package to enable package-aware installation in Windows Vista. That is, you can release one driver package for both Windows Vista and Windows XP. The INF file in the package should choose the appropriate source for the core driver files based on the operating system on which you are installing the package. For Windows Vista, your INF file should install the unaltered core driver package from a subdirectory in your driver package. For Windows XP, the INF file should install the redistributable core driver file from your package's main directory.

For Windows Vista, avoid breaking up the core driver package and do not reference the core driver files directly as part of your driver package. Otherwise, the package might appear to install correctly in Windows Vista, but the result might be print system instability and regressions in functionality. To avoid such problems, test your driver update package extensively to verify that it installs correctly on both Windows Vista and Windows XP.

For more information, see [Creating a Single Driver Package for Windows XP and Windows Vista](creating-a-single-driver-package-for-windows-xp-and-windows-vista.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Updating%20Core%20Drivers%20Files%20for%20Non-Package-Aware%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


