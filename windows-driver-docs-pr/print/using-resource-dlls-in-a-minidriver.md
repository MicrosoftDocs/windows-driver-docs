---
title: Using Resource DLLs in a Minidriver
description: Using Resource DLLs in a Minidriver
ms.assetid: b63c48bb-3321-45e0-b37c-a9612a95cc24
keywords: ["GPD files WDK Unidrv , resource DLLs", "resource DLLs WDK Unidrv"]
---

# Using Resource DLLs in a Minidriver


## <a href="" id="ddk-using-resource-dlls-in-a-minidriver-gg"></a>


Typically, printer drivers require the use of such resources as externally stored fonts, icons and other bitmaps, and localizable user interface text strings. Descriptions of these items are placed in a resource DLL, as described in the Microsoft Windows SDK documentation.

To use resource DLLs in a Unidrv minidriver, you must identify the resources in either of the following manners:

-   If you are using more than one resource DLL, identify them using the RESDLL feature.

    An example usage of the RESDLL feature is as follows:

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>*Feature: RESDLL
    {
        *Option: FirstRes
        {*Name: &quot;MyFirstRes.dll&quot;}
        *Option: SecondRes
        {*Name: &quot;MySecondRes.dll&quot;}
        *Option: ThirdRes
        {*Name: &quot;MyThirdRes.dll&quot;}
    }</code></pre></td>
    </tr>
    </tbody>
    </table>

    To reference resources contained in one of these resource DLLs, use the following format:

    RESDLL.*ResourceOptionName*.*ResourceID*

-   If you are using only one resource DLL, you can identify it by assigning a value to the \*ResourceDLL attribute.

    To reference a resource contained in this resource DLL, simply specify the appropriate resource identifier, as illustrated in the following example:

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>*rcNameID: 288</code></pre></td>
    </tr>
    </tbody>
    </table>

All resource DLLs used with a minidriver must be specified in a printer INF file. See [Installing a Unidrv Minidriver](installing-a-unidrv-minidriver.md).

Within a [*GPD*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-) file, resource identifiers must be used when assigning values to any entry whose name begins with \*rc, such as \*rcIconID and \*rcCartridgeNameID, for example.

Additionally, if your printer contains hardware-resident fonts, you must provide [printer font descriptions](printer-font-descriptions.md) for these fonts in the form of .ufm or .ifi files, and you must identify these files in a resource DLL, using the RC\_UFM or RC\_FONT resource type, respectively.

Microsoft supplies one resource DLL, unires.dll, which contains string resources for the [standard features](standard-features.md) and [standard options](standard-options.md). The Microsoft-supplied GPD file, stdnames.gpd, assigns a macro symbol name to each resource identifier. This allows you to reference these resources by their macro name, as illustrated in the following example:

```
*rcNameID: =LETTERSMALL_DISPLAY
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20Resource%20DLLs%20in%20a%20Minidriver%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




