---
title: IOleCvt Automation Interface
description: IOleCvt Automation Interface
MS-HAID:
- 'webfnc\_0ca4054a-768a-44b9-bb7e-84a5cb81349b.xml'
- 'print.iolecvt\_automation\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.date: 04/20/2017
---

# IOleCvt Automation Interface

The Automation interface for the **IOleCvt** object enables an ASP Web page to perform a variety of string conversions from one format to another. These include:

-   Conversion from Unicode to ANSI

-   Conversion from ANSI to Unicode

-   Conversion from Unicode to UTF-8 (UCS Transformation Format 8)

-   Conversion from Unicode using one code page to Unicode using another code page

Although most applications now use Unicode (UTF-16) encoding for character data, some Windows desktop applications use character sets based on Windows code pages. A code page assigns international characters to ANSI character codes greater than 127. For more information about code pages, see the Windows SDK documentation.

The **IOleCvt** interface is supported in Windows 2000 and later.

The programmatic identifier for the **IOleCvt** object is OlePrn.OleCvt.

For more information about how to access printers from ASP Web pages, see [Internet Printing](./internet-printing.md).

The "property get" operations in the **IOleCvt** interface are described in the following section:

[IOleCvt Property Get Operations](iolecvt-property-get-operations.md)
