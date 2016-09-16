---
title: Best Practices for Client-Side Rendering
author: windows-driver-content
description: Best Practices for Client-Side Rendering
MS-HAID:
- 'splarch\_a9343eac-f353-45af-9248-0e08957e1214.xml'
- 'print.best\_practices\_for\_client\_side\_rendering'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d05086c1-4e0b-4767-bb1d-7b6d73b1b210
keywords: ["client-side rendering WDK print , best practices"]
---

# Best Practices for Client-Side Rendering


You should keep the following items in mind when writing your printer drivers so that they work properly with client-side rendering:

-   Printer drivers should be installed as driver packages.

-   Printer drivers should use the SetPrinterData or SetPrinterDataEx function to store printer configuration information. For more information about these functions, see the Microsoft Windows SDK documentation.

-   Printer drivers that use a custom print processor must include the processor in the driver package and make sure that Point and Print loads it onto the client computer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Best%20Practices%20for%20Client-Side%20Rendering%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


