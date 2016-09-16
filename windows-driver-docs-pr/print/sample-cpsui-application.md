---
title: Sample CPSUI Application
author: windows-driver-content
description: Sample CPSUI Application
MS-HAID:
- 'cpsui\_e6eb3e37-5f79-4f0b-8872-d91312220a82.xml'
- 'print.sample\_cpsui\_application'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 895afbfe-c18a-4bcc-b815-8cb323bbac80
keywords: ["Common Property Sheet User Interface WDK print , samples", "CPSUI WDK print , samples", "property sheet pages WDK print , samples"]
---

# Sample CPSUI Application


## <a href="" id="ddk-sample-cpsui-application-gg"></a>


Source code for CPSUISAM, a sample CPSUI application, is included in the \\src\\print directory of the WDK. The application causes CPSUI to call into the print spooler to create property sheet pages for the system's default printer. The application then creates an additional property sheet page, in order to illustrate some of the techniques that can be employed when using CPSUI to create a new page.

**Note**  Printer interface DLLs should not call into the print spooler. CPSUISAM illustrates some of the capabilities of CPSUI but does not represent techniques that should be used by printer interface DLLs. Instead, these DLLs should follow the steps described in [Using CPSUI with Printer Drivers](using-cpsui-with-printer-drivers.md).

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Sample%20CPSUI%20Application%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


