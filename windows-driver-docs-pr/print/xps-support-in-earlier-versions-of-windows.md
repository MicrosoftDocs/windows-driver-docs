---
title: XPS Support in Earlier Versions of Windows
description: XPS Support in Earlier Versions of Windows
ms.assetid: e13b43f5-e926-404d-9f76-c2dfef6e0637
keywords:
- XPSDrv printer drivers WDK , earlier Windows versions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XPS Support in Earlier Versions of Windows


In addition to Windows Vista, XPS-based technologies are supported on Microsoft Windows Server 2003 and Windows XP through the Microsoft WinFX Runtime Component 3.0. XPS printing will work in Point and Print scenarios with these operating systems.

Support for Windows Server 2003 and Windows XP is provided in the following manner:

-   Transparent conversion of output for Win32 and Windows Presentation Foundation (WPF) applications. Although rendering output differs significantly between Win32 and Windows Presentation Foundation (WPF) applications, the XPSDrv driver model enables both application types to print to a single driver. Output for printing is converted appropriately between the application types and the driver types, enabling a full support matrix between Win32 and WPF applications that print to GDI-based and XPS-based printers. The XPSDrv infrastructure is also available for use in Windows Server 2003 and Windows XP.

-   Consistent filter pipeline model. The filter pipelines on Windows Vista, Windows Server 2003, and Windows XP support the same interfaces for filters, plug-in models, pipeline configuration files, and event logging. There are a few differences, including the reduced support for notifications in earlier versions of Windows. For Windows Vista, the rendering filter has complete control of notifications and can send notifications about any type of "part" that the filter is processing (that is, a document, page, font, image, and so on). For scalable consumers in earlier versions of Windows, notifications happen only at page boundaries.

-   XPS-based print processor. For Windows Server 2003 and Windows XP, there is an XPS-based print processor that enables XPSDrv. The XPS-based print processor hosts XPSDrv drivers and communicates with the existing spooler on these operating systems. Certain XPS print path features are available only on Windows Vista, so the XPSDrv driver must be able to degrade gracefully on earlier versions of Windows.

For more information about XPS, download the [XML Paper Specification Overview](http://download.microsoft.com/download/1/6/a/16acc601-1b7a-42ad-8d4e-4f0aa156ec3e/XPS_1_0.exe).
