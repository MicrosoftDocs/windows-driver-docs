---
title: Improved Spooling and Rendering
author: windows-driver-content
description: Improved Spooling and Rendering
ms.assetid: 0e385282-fbc8-4c4b-9070-19ee8290ddd6
keywords:
- XPSDrv printer drivers WDK , spooling
- XPSDrv printer drivers WDK , rendering
- XPS spool files WDK XPSDrv
- spool files WDK print
- rendering plug-ins WDK print , XPSDrv
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Improved Spooling and Rendering


The XPS print path improves spooler efficiency by spooling XPS Documents in the XPS spool file format when end users print to XPSDrv printer drivers. Because the XPS Document file format is the same as the XPS spool file format, the spooling process is simplified and eliminates the requirement to generate an intermediate spool file, such as an enhanced metafile (EMF) data file, before the document is spooled. Through smaller spool files sizes, the XPS print path can reduce network traffic and improve printing performance.

EMF is a closed format that represents application output as a series of GDI calls that then require calls into GDI for rendering services. Unlike EMF, the XPS spool format represents the actual visual output without requiring further interpretation when you target an XPSDrv driver. GDI-based print drivers require data and color space conversions while the XPSDrv print drivers can operate directly on the data in the spool file and avoid these conversions.

Spool file sizes are typically reduced when you use XPS Documents or target an XPSDrv driver. Files that rely on device fonts and files with large vector content may result in a larger spool file, but spool files are generally substantially smaller.

The size of spool files is reduced through several optimizations in the conversion process:

-   Font subsetting for all fonts. After the output is processed, it contains only the characters that are used for the fonts within the file. This optimization greatly reduces the size of spool files for documents, particularly documents that use East Asian font sets.

-   Identification of common resources, including logos and image files. The conversion process identifies whether an image is used multiple times within a document and, if so, creates a shared resource in the XPS spool file. This optimization can significantly reduce the size of spool files for graphics-intensive documents, such as Microsoft PowerPoint files that use the same logos and backgrounds on each slide.

-   ZIP compression. ZIP compression is implemented as part of the XPS spool file format (XPS Document format). This optimization reduces the spool file size.

These optimizations occur any time an XPS Document or XPS spool file is created.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Improved%20Spooling%20and%20Rendering%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


