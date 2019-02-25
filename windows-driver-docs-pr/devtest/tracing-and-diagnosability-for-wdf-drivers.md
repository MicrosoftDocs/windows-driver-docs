---
title: Tracing and Diagnosability for WDF Drivers
description: This paper discusses how to implement event tracing using the Windows software trace preprocessor (WPP) in a Windows Driver Foundation (WDF) driver.
ms.assetid: C89A218F-3E73-4D3E-8F53-5D52E97711EF
ms.date: 07/09/2017
ms.localizationpriority: medium
---

# Tracing and Diagnosability for WDF Drivers


**Last updated:**

-   October 19, 2008

**Applies to:**

-   Windows Server 2008
-   Windows Vista
-   Windows Server 2003
-   Windows XP
-   Windows 2000

This paper discusses how to implement event tracing using the Windows software trace preprocessor (WPP) in a Windows Driver Foundation (WDF) driver.

File name: WPP\_intro.docx

169 KB

Microsoft Word file

[Get Office File Viewers](http://www.microsoft.com/download/office.aspx)

[![click here to download](./images/download.png)](http://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/WPP_intro.docx)

Software tracing for drivers is usually based on Event Tracing for Windows (ETW), a kernel-level facility that logs trace messages for both kernel-mode and user-mode processes. Because ETW can be somewhat complicated to use, most driver developers use the Windows software trace preprocessor (WPP), which simplifies and enhances the process of instrumenting a driver for ETW tracing.

## In this white paper:

-   WPP software tracing basics
-   Trace message functions and macros
-   Supporting software tracing in a driver
-   Tools for software tracing
-   How to run a software trace session

 

 





