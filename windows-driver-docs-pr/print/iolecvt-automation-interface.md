---
title: IOleCvt Automation Interface
description: IOleCvt Automation Interface
MS-HAID:
- 'webfnc\_0ca4054a-768a-44b9-bb7e-84a5cb81349b.xml'
- 'print.iolecvt\_automation\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 286ab231-c215-45cc-b0da-97ec8adf2de1
---

# IOleCvt Automation Interface


## <span id="ddk_iolecvt_automation_interface_gg"></span><span id="DDK_IOLECVT_AUTOMATION_INTERFACE_GG"></span>


The Automation interface for the **IOleCvt** object enables an ASP Web page to perform a variety of string conversions from one format to another. These include:

-   Conversion from Unicode to ANSI

-   Conversion from ANSI to Unicode

-   Conversion from Unicode to UTF-8 (UCS Transformation Format 8)

-   Conversion from Unicode using one code page to Unicode using another code page

Although most applications now use Unicode (UTF-16) encoding for character data, some Windows desktop applications use character sets based on Windows code pages. A code page assigns international characters to ANSI character codes greater than 127. For more information about code pages, see the Windows SDK documentation.

The **IOleCvt** interface is supported in Windows 2000 and later.

The programmatic identifier for the **IOleCvt** object is OlePrn.OleCvt.

For more information about how to access printers from ASP Web pages, see [Internet Printing](https://msdn.microsoft.com/library/windows/hardware/ff551735).

The "property get" operations in the **IOleCvt** interface are described in the following section:

[IOleCvt Property Get Operations](iolecvt-property-get-operations.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IOleCvt%20Automation%20Interface%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




