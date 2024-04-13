---
title: Working with the Driver Store
description: V4 print drivers execute directly from the Driver Store, and enhanced Point and Print doesn't download the entire driver package to client machines, so it is important to be aware of the best practices in this section.
ms.date: 01/25/2023
---

# Working with the Driver Store

[!include[Print Support Apps](../includes/print-support-apps.md)]

V4 print drivers execute directly from the Driver Store, and enhanced Point and Print doesn't download the entire driver package to client machines, so it is important to be aware of the best practices in this section.

- Driver binaries should not try to open any other binary in the driver. Instead, driver binaries should use a driver property bag to encapsulate any common, proprietary data.

- If you develop a printer extension that is installed separately from the driver (for example, with an MSI or setup.exe), then here are some recommended practices:

  - When your printer extension app registers with the print system, the app should specify command line switches in its AppPath entry, in order to inform the app of the PrinterDriverID for which the print system is launching the app. The command line switches also indicate the mode of operation for which the print system is launching the app.

  - If your printer extension app requires different switches for a user launch context, you can provide these options in a start menu shortcut, but this is not technically necessary.

- If you develop a printer extension app that is installed with the driver, remember that this type of app will be installed to the Driver Store. And also be aware of the following:

  - These apps will be registered automatically by the print system, and will be registered with default command line switches.

  - Specifying additional command line switches is unsupported for such apps.

  - These apps will not be launched outside the print preferences or printer notifications events, so creating start menu shortcuts, or otherwise allowing users to launch these apps outside the context of one of the two events is unsupported.

## Related topics

[V4 Printer Driver Development Best Practices](v4-printer-driver-development-best-practices.md)  
