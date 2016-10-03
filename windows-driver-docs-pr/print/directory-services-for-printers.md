---
title: Directory Services for Printers
author: windows-driver-content
description: Directory Services for Printers
MS-HAID:
- 'prtinst\_d1f9365c-d5ef-4aff-88da-3587d6704375.xml'
- 'print.directory\_services\_for\_printers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4b368602-67d9-4d26-a82b-8d14d8da2625
keywords: ["Directory Services WDK printer", "printer Directory Services support WDK", "print queues WDK , Directory Services", "queues WDK printer , Directory Services"]
---

# Directory Services for Printers


## <a href="" id="ddk-directory-services-for-printers-gg"></a>


When a user installs a network-shared printer, the Windows 2000 and later print folder, by default, also publishes the printer to the Windows 2000 (or later) Directory Services. Publication is accomplished by calling the spooler's **SetPrinter** function with an input structure of PRINTER\_INFO\_7, as described in the Microsoft Windows SDK documentation.

Publishing a print queue makes it visible to users through the **Search** option on the task bar's **Start** menu.

The following topics provide more information about printer support for Directory Services:

[Print Spooler Support for Printer Directory Services](print-spooler-support-for-printer-directory-services.md)

[Printer Driver Support for Printer Directory Services](printer-driver-support-for-printer-directory-services.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Directory%20Services%20for%20Printers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


