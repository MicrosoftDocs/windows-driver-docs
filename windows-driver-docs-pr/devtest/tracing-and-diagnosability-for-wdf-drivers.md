---
title: Tracing and Diagnosability for WDF Drivers
description: This paper discusses how to implement event tracing using the Windows software trace preprocessor (WPP) in a Windows Driver Foundation (WDF) driver.
ms.assetid: C89A218F-3E73-4D3E-8F53-5D52E97711EF
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

## <span id="In_this_white_paper_"></span><span id="in_this_white_paper_"></span><span id="IN_THIS_WHITE_PAPER_"></span>In this white paper:


-   WPP software tracing basics
-   Trace message functions and macros
-   Supporting software tracing in a driver
-   Tools for software tracing
-   How to run a software trace session

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Tracing%20and%20Diagnosability%20for%20WDF%20Drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




