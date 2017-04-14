---
title: Improved Color Printing
author: windows-driver-content
description: Improved Color Printing
ms.assetid: b0487ee0-9b4a-4083-9416-ad22b97ed94b
keywords: ["XPSDrv printer drivers WDK , color printing", "color printing WDK XPSDrv"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Improved%20Color%20Printing%20%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


