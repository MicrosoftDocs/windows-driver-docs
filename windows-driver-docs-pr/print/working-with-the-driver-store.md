---
title: Working with the Driver Store
author: windows-driver-content
description: V4 print drivers execute directly from the Driver Store, and enhanced Point and Print doesn't download the entire driver package to client machines, so it is important to be aware of the best practices in this section.
ms.assetid: 71199500-ECAD-46A8-8A9B-533DDB9783B4
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Working with the Driver Store


V4 print drivers execute directly from the Driver Store, and enhanced Point and Print doesn't download the entire driver package to client machines, so it is important to be aware of the best practices in this section.

-   Driver binaries should not try to open any other binary in the driver. Instead, driver binaries should use a driver property bag to encapsulate any common, proprietary data.

-   If you develop a printer extension that is installed separately from the driver (for example, with an MSI or setup.exe), then here are some recommended practices:

    o When your printer extension app registers with the print system, the app should specify command line switches in its AppPath entry, in order to inform the app of the PrinterDriverID for which the print system is launching the app. The command line switches also indicate the mode of operation for which the print system is launching the app.

    o If your printer extension app requires different switches for a user launch context, you can provide these options in a start menu shortcut, but this is not technically necessary.

-   If you develop a printer extension app that is installed with the driver, remember that this type of app will be installed to the Driver Store. And also be aware of the following:

    o These apps will be registered automatically by the print system, and will be registered with default command line switches.

    o Specifying additional command line switches is unsupported for such apps.

    o These apps will not be launched outside the print preferences or printer notifications events, so creating start menu shortcuts, or otherwise allowing users to launch these apps outside the context of one of the two events is unsupported.

## Related topics
[V4 Printer Driver Development Best Practices](v4-printer-driver-development-best-practices.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Working%20with%20the%20Driver%20Store%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


