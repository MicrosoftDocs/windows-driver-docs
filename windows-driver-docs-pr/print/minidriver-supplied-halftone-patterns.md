---
title: Minidriver-Supplied Halftone Patterns
description: Minidriver-Supplied Halftone Patterns
ms.assetid: db2e1c5c-f337-4875-980d-a75a54a4cece
keywords:
- GDI-supplied halftoning WDK Unidrv
- minidriver-supplied halftoning WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidriver-Supplied Halftone Patterns





When GDI-supported halftone methods are being used, GDI allows specification of customized halftone patterns. To specify customized halftone patterns, use [option attributes for the halftone feature](option-attributes-for-the-halftone-feature.md) as follows:

-   The \*rcHTPatternID, \*HTPatternSize and \*HTNumPatterns attributes allow you to describe halftone patterns that are stored in a resource DLL. Halftone pattern resources are three-dimensional arrays of binary data, starting on a DWORD address boundary. They can be specified using the following format, which calculates the correct size and provides the required address alignment:

    ```cpp
    BYTE HTPatternResource [HTNumPatterns][(HTPatternSize.y*HTPatternSize.x+3) & ~3];
    ```

    Within an .rc file used to create a resource DLL, the pattern might be specified as follows:

    ```cpp
    1     RC_HTPATTERN LOADONCALL DISCARDABLE HALFTONE.BIN
    ```

    where halftone.bin is a file containing a halftone pattern.

-   The \*HTCallbackID attribute allows you to indicate that you are implementing the [**IPrintOemUni::HalftonePattern**](https://msdn.microsoft.com/library/windows/hardware/ff554258) method in a [rendering plug-in](rendering-plug-ins.md). A unique \***HTCallbackID** value must be provided for each pattern the **IPrintOemUni::HalftonePattern** method supports.

You can provide halftone pattern resources, an **IPrintOemUni::HalftonePattern** method, or both, as follows:

-   If you provide only halftone patterns, Unidrv obtains the patterns from the resource DLL and passes them to GDI. The patterns cannot be encrypted.

-   If you provide only an **IPrintOemUni::HalftonePattern** method, the method must generate and return halftone patterns to Unidrv, which passes them to GDI.

-   If you want to place encrypted halftone patterns in a resource DLL, then you must also provide an **IPrintOemUni::HalftonePattern** method to decode the patterns and return them to Unidrv, which in turn passes them to GDI.

For more information about halftoning, see [Customized Halftoning](customized-halftoning.md).

 

 




