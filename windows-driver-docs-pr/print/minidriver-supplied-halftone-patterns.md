---
title: Minidriver-Supplied Halftone Patterns
author: windows-driver-content
description: Minidriver-Supplied Halftone Patterns
MS-HAID:
- 'nt5gpd\_8798c3d9-ca44-47b2-b349-a04e0e3c3157.xml'
- 'print.minidriver\_supplied\_halftone\_patterns'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: db2e1c5c-f337-4875-980d-a75a54a4cece
keywords: ["GDI-supplied halftoning WDK Unidrv", "minidriver-supplied halftoning WDK Unidrv"]
---

# Minidriver-Supplied Halftone Patterns


## <a href="" id="ddk-minidriver-supplied-halftone-patterns-gg"></a>


When GDI-supported halftone methods are being used, GDI allows specification of customized halftone patterns. To specify customized halftone patterns, use [option attributes for the halftone feature](option-attributes-for-the-halftone-feature.md) as follows:

-   The \*rcHTPatternID, \*HTPatternSize and \*HTNumPatterns attributes allow you to describe halftone patterns that are stored in a resource DLL. Halftone pattern resources are three-dimensional arrays of binary data, starting on a DWORD address boundary. They can be specified using the following format, which calculates the correct size and provides the required address alignment:

    ```
    BYTE HTPatternResource [HTNumPatterns][(HTPatternSize.y*HTPatternSize.x+3) & ~3];
    ```

    Within an .rc file used to create a resource DLL, the pattern might be specified as follows:

    ```
    1     RC_HTPATTERN LOADONCALL DISCARDABLE HALFTONE.BIN
    ```

    where halftone.bin is a file containing a halftone pattern.

-   The \*HTCallbackID attribute allows you to indicate that you are implementing the [**IPrintOemUni::HalftonePattern**](https://msdn.microsoft.com/library/windows/hardware/ff554258) method in a [rendering plug-in](rendering-plug-ins.md). A unique \***HTCallbackID** value must be provided for each pattern the **IPrintOemUni::HalftonePattern** method supports.

You can provide halftone pattern resources, an **IPrintOemUni::HalftonePattern** method, or both, as follows:

-   If you provide only halftone patterns, Unidrv obtains the patterns from the resource DLL and passes them to GDI. The patterns cannot be encrypted.

-   If you provide only an **IPrintOemUni::HalftonePattern** method, the method must generate and return halftone patterns to Unidrv, which passes them to GDI.

-   If you want to place encrypted halftone patterns in a resource DLL, then you must also provide an **IPrintOemUni::HalftonePattern** method to decode the patterns and return them to Unidrv, which in turn passes them to GDI.

For more information about halftoning, see [Customized Halftoning](customized-halftoning.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Minidriver-Supplied%20Halftone%20Patterns%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


