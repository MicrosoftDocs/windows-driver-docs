---
title: Improved Color Printing
description: Improved Color Printing
ms.assetid: b0487ee0-9b4a-4083-9416-ad22b97ed94b
keywords:
- XPSDrv printer drivers WDK , color printing
- color printing WDK XPSDrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Improved Color Printing


New color management capabilities and the XPS print path in Windows Vista work together to provide a richer, more predictable color printing. Enhanced color support enables high-end printing by supporting printing with more than four colorants. (More than four colorants are required for customers with prepress applications.) The new XPS print architecture can communicate application-generated extended color information to wide-gamut color printers. Device drivers can access and control color information from within the print pipeline.

Windows Vista makes full use of the Windows Color System, which introduces significant innovations to color management to match color across different software applications, imaging devices, imaging media, and viewing conditions in a predictable, reliable, and consistent manner. The XPS Document is the conduit for sending application color information to the XPS Document-based devices. The XPS Document format applies this technology through native support for the following:

-   Higher precision, higher dynamic range, and larger gamut color spaces.

-   Use of CMYK and supporting n-ink systems (with greater than four colorants).

-   Support for named colors.

Through the XPS spool file, the XPS print path delivers this advanced color information directly to the device drivers. Optionally, the device drivers can provide the following improved color handling:

-   Automatic color configuration for devices with XPS print path drivers.

-   The ability to reuse content in the pipeline for a different print device.

-   The ability to reliably persist color data from the application to the driver because color profiles and processing instructions can be embedded directly in the spool file.

-   Improved communication of color capabilities and settings. Applications can control color processing by enabling or disabling system color management in the new print path. Drivers can more completely express color capabilities of their devices.

 

 




