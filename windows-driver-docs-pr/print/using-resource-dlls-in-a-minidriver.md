---
title: Using Resource DLLs in a Minidriver
description: Using Resource DLLs in a Minidriver
ms.assetid: b63c48bb-3321-45e0-b37c-a9612a95cc24
keywords:
- GPD files WDK Unidrv , resource DLLs
- resource DLLs WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Resource DLLs in a Minidriver





Typically, printer drivers require the use of such resources as externally stored fonts, icons and other bitmaps, and localizable user interface text strings. Descriptions of these items are placed in a resource DLL, as described in the Microsoft Windows SDK documentation.

To use resource DLLs in a Unidrv minidriver, you must identify the resources in either of the following manners:

-   If you are using more than one resource DLL, identify them using the RESDLL feature.

    An example usage of the RESDLL feature is as follows:

    ```cpp
    *Feature: RESDLL
    {
        *Option: FirstRes
        {*Name: "MyFirstRes.dll"}
        *Option: SecondRes
        {*Name: "MySecondRes.dll"}
        *Option: ThirdRes
        {*Name: "MyThirdRes.dll"}
    }
    ```

    To reference resources contained in one of these resource DLLs, use the following format:

    RESDLL.*ResourceOptionName*.*ResourceID*

-   If you are using only one resource DLL, you can identify it by assigning a value to the \*ResourceDLL attribute.

    To reference a resource contained in this resource DLL, simply specify the appropriate resource identifier, as illustrated in the following example:

    ```cpp
    *rcNameID: 288
    ```

All resource DLLs used with a minidriver must be specified in a printer INF file. See [Installing a Unidrv Minidriver](installing-a-unidrv-minidriver.md).

Within a [*GPD*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-) file, resource identifiers must be used when assigning values to any entry whose name begins with \*rc, such as \*rcIconID and \*rcCartridgeNameID, for example.

Additionally, if your printer contains hardware-resident fonts, you must provide [printer font descriptions](printer-font-descriptions.md) for these fonts in the form of .ufm or .ifi files, and you must identify these files in a resource DLL, using the RC\_UFM or RC\_FONT resource type, respectively.

Microsoft supplies one resource DLL, unires.dll, which contains string resources for the [standard features](standard-features.md) and [standard options](standard-options.md). The Microsoft-supplied GPD file, stdnames.gpd, assigns a macro symbol name to each resource identifier. This allows you to reference these resources by their macro name, as illustrated in the following example:

```cpp
*rcNameID: =LETTERSMALL_DISPLAY
```

 

 




