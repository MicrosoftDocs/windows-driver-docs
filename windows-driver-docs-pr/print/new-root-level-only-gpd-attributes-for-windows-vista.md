---
title: New Root-Level-Only GPD Attributes for Windows Vista
description: New Root-Level-Only GPD Attributes for Windows Vista
ms.assetid: 09f38459-6062-4d2a-9aee-929aa60193cf
keywords:
- root-level-only attributes WDK Unidrv
- general printer attributes WDK Unidrv , root-level-only
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# New Root-Level-Only GPD Attributes for Windows Vista


The following list describes the GPD attributes that are new starting with Windows Vista. To maintain backwards compatibility with pre-Windows Vista versions of Windows, you should surround these attributes with the following code.

```cpp
*Ifdef: WINNT_60 ... *Endif: WINNT_60 blocks
```

### PrintProcDuplexOptions

The **PrintProcDuplexOptions** attribute controls various duplexing options in a print processor. This attribute can have one of the following values:

1: Reverse pages for reverse duplex

2: Suppress generation of extra blank page if possible

3: Both of the above

0: None of the above

If **PrintProcDuplexOptions** is 1, it controls whether the print processor should reverse pages on reverse duplex.

Assume that you have to print a four-page document with n-up = 1, and you want to use reverse printing and duplex printing. Because you want reverse printing, you want to print the last page before the first page. Because you want duplex printing, you want to print two pages on a single sheet of paper. The print processor can play back the pages in one of the following two formats (where each pair of numbers indicates the two pages that would print on the two sides of a single sheet of paper):

-   Format 1: (4,3),(2,1)

-   Format 2: (3,4),(1,2)

Before Windows Vista, a print processor would print the order in format 2 \[(3,4),(1,2)\]. But in Windows Vista and later, the default format is format 1 \[(4,3),(2,1)\]. This change occurred because many printers have incorrect output with format 2; that is, the pages that are printed are not ordered in the proper order.

But if your printer works correctly with format 1, you will not need to change anything for Windows Vista and later. However, if your printer works incorrectly with format 1 and you want to revert to format 2, add the following code example to your GPD file.

```cpp
*Ifdef: WINNT_60
*PrintProcDuplexOptions: 1
*Endif: WINNT_60
```

Format 1 might work better in some orientations or some combination of input and output trays, and format 2 might work better in other combinations. As a result, you can put the **PrintProcDuplexOptions** attribute in a switch/case construct.

For a pre-Windows Vista Unidrv driver, if you have a pre-Windows Vista print processor, format 2 is the default, and you cannot change the format; otherwise, if you have a Windows Vista print processor, format 1 is the default, and you cannot change the format.

For the Windows Vista Unidrv driver, if you have a pre-Windows Vista print processor, format 2 is the default, and the GPD attribute will be ignored; otherwise, if you have a Windows Vista print processor, format 1 is the default, but you can change the format by using the **PrintProcDuplexOptions** attribute.

If **PrintProcDuplexOptions** is 2, it prevents the generation of blank pages in certain duplex scenarios.

This attribute controls whether you should send extra blank pages to the printer when you are performing duplex printing. For example, if the job is one-page job and duplex is on (assume n-up = 1), only one side of the sheet needs to be printed. Currently, printers will print one side and then generate an empty blank page on the reverse side. (Because the print job was started with duplex=on, the printer expects two pages before it ejects the sheet. If the second page does not print, some printers keep waiting.) The drawbacks of the current solution are that:

-   The generated page causes an inaccurate page count in accounting software and the page counter within printers.

-   When the page comes halfway out of the printer (in some Hewlett Packard DeskJet-style printers), the user might try to pull it out while the printer tries to pull it back in. This situation can cause hardware issues.

You can avoid the preceding problems by specifying \***PrintProcDuplexOptions**: 2 in the GPD file.

Note that even if this attribute is set, blank page optimization is performed only in the following limited cases:

1.  For reverse printing, blank page optimization is performed only when the whole job can fit on a single side of paper (for example, a one-page job with n-up=1 or a four-page job with n-up =4). If the job needs more than one sheet, the optimization is not performed (because the printer pages will be printed in an inaccurate order). For example, for a three-page job, the pages may be printed in the order 3,2,1,&lt;blank&gt; instead of 4,3,2,&lt;blank&gt;.

2.  Blank page optimization is not performed if the print processor has to simulate copies. The print processor simulates copies if the number of copies that are needed is more than the number of copies that the print processor can make.

    The following situation is an example of when simulations occurs and blank pages are generated (if required):

    -   Two copies for a printer that cannot make copies

    The following situations are examles of when simulation does not occur and you can suppress extra page generation:

    -   Single copy job for a printer that cannot make copies
    -   Five-copy job for a printer that can make more than one copys

**Usage of PrintProcDuplexOptions**

```cpp
*Ifdef: WINNT_60
*PrintProcDuplexOptions: 2
*Endif: WINNT_60 
```

In some cases, you might not mind extra page printing while in other cases you do. Therefore, you can put the **PrintProcDuplexOptions** attribute in a switch/case construct.

For a pre-Windows Vista Unidrv driver, if you have a pre-Windows Vista print processor, a printer will print an extra blank page, if deemed necessary, and you cannot change this behavior; otherwise, if you have a Windows Vista print processor, a printer will print an extra blank page, if deemed necessary, and you cannot change this behavior.

For the Windows Vista Unidrv driver, if you have a pre-Windows Vista print processor, a printer will print an extra Blank page, if deemed necessary, and the GPD attribute will be ignored; otherwise, if you have a Windows Vista print processor, and if the appropriate GPD attribute and the proper conditions are present (that is, the conditions that are described earlier about preventing blank page printing), a printer will not print blank pages.

### PreAnalysisOptions

The **PreAnalysisOptions** attribute can have one of the following values:

0: Disable all pre-analysis modes.

1: Default mode. Enable monochrome z-order text analysis and blank band optimization. This mode is enabled for devices with a downloadable font or device font support and high resolution (600 dpi or higher), 24 bpp render modes.

2: Enable 1 bpp optimization for 24 bpp ImageProcessing callback functions.

4: Enable device StretchBlt support.

8: Enable vendor pre-analysis mode.

16: Enable debug mode for 1 bpp where the band is converted to 24 bpp before calling the ImageProcessing callback function.

### UseBMPFontCompression?

The **UseBMPFontCompression?** attribute controls whether Unidrv should compress data when fonts are downloaded as a bitmap. The default value of **UseBMPFontCompression?** is **FALSE**, which means Unidrv will not do compression if this attribute is not present in the GPD file. This default value maintains compatibility with older versions of Unidrv that did not have the bitmap font compression feature. You should set this attribute to **TRUE** only if your printer supports bitmap font compressionThe compressed bitmap character data is in compressed run-length-with-line-repetition format.

### UseMode5Compression?

The **UseMode5Compression?** attribute controls whether UniDrv should use Mode 5 compression. Mode 5 (or Method 5) compression is adaptive compression that enables the combined use of multiple other compression methods (such as Unencoded, TIFF, or Delta-Row). The default value of **UseMode5Compression?** is **FALSE**, which means Unidrv will not perform adaptive compression if this attribute is not present in the GPD. This default value maintains compatibility with older versions of Unidrv that did not have the adaptive compression feature. You should set this attribute to **TRUE** only if your printer supports adaptive compression.

### UseHPGLPolylineEncoding?

The **UseHPGLPolylineEncoding?** attribute controls whether Unidrv should use polyline encoding. HP-GL/2 supports the Pen Up/Pen Down/Draw Absolute/Draw Relative commands for drawing vectors. The polyline encoded (PE) command is a more efficient way of representing vectors.

The default value for **UseHPGLPolylineEncoding?** is **FALSE**, which means Unidrv will not use the PE command if this attribute is not present in GPD. This default value maintains compatibility with older versions of Unidrv that did not have support for the PE command. You should you set this value to **TRUE** only if your printer supports polyline encoded.

### PrintSchemaPrivateNamespaceURI

The **PrintSchemaPrivateNamespaceURI** attribute defines the private namespace URI that the core driver should use for exposing private PPD features or options in PrintTicket or PrintCapabilities. The attribute must appear in the root of the GPD document and contains an ASCII representation of a URI that will be used to define a namespace in PrintTickets and PrintCapabilities documents. That URI will, in turn, be associated with all features and options that do not have an explicit mapping into the public schema, or that the core driver does not recognize.

### PrintSchemaKeywordMap

The **PrintSchemaKeywordMap** attribute appears under feature and option constructs in the GPD file. This attribute indicates what public print schema name you should use with the printer-defined features. You can rename any option that is specified in a GPD file, except Duplex and Collate, in the PrintTicket by using the **PrintSchemaKeywordMap** attribute.

**Note**   The GPD parser ignores this attribute for features that are explicitly recognized, including page size and color.

 

All values should be enclosed in quotation marks. They will be converted to Unicode by using the code page that is specified in the GPD, if any. Duplicate definitions of any attributes resolve in the same way as other GPD attributes: The last definition that is read is given precedence.

**Important**  If you map a feature to a Print Schema keyword that is already being used in the GPD file, the corresponding PrintCapabilities document might list that feature more than once. Multiple occurrences might be confusing, so you should not map features to Print Schema keywords that are used in the GPD file.

 

**Note**  The GPD parser automatically generates the FORMSOURCE option for the InputBin feature and maps it to the AutoSelect keyword in the Print Schema. If your GPD file contains an InputBin option that uses the **PrintSchemaKeywordMap** attribute to map the option to a Print Schema keyword, the feature in the Print Schema will contain a FORMSOURCE option in the device namespace. AutoSelect will appear in the PrintCapabilities document and refer to the option that is specified in the **PrintSchemaKeywordMap** attribute of the GPD file.

 

The following code example shows a partial GPD file to show the layout.

```cpp
*Feature: HPSTAPLER
{
    *Name: "Staple"
    *DefaultOption: Off
    * PrintSchemaKeywordMap: "Staple"

    *Option: Off
    {
        *Name: "Off"
        * PrintSchemaKeywordMap: "Off"
    }
 
    *Option: On
    {
        *Name: "On"
        * PrintSchemaKeywordMap: "On"
    }
}
```

### IsXPSDriver

The **IsXPSDriver** attribute uses the following GPD syntax.

```cpp
*IsXPSDriver?: TRUE | FALSE
```

You can use the Windows Vista Unidrv configuration module (Unidrvui.dll) for both Microsoft Win32 GDI drivers and the new [XPSDrv drivers](xpsdrv-printer-drivers.md). To use the Unidrv configuration module for XPSDrv drivers, the XPSDrv driver's GPD data file must specify the **IsXPSDriver** attribute and set its value to **TRUE**.

For example, if you have an XPS driver, use the following code.

```cpp
*IsXPSDriver?: TRUE
```

To use the Unidrv configuration module for Win32 GDI drivers, you do not need to specify this attribute.

### UseImageForHatchBrush?

The **UseImageForHatchBrush?** attribute uses the following GPD syntax.

```cpp
*Ifdef: WINNT_60
*UseImageForHatchBrush?: TRUE
*Endif: WINNT_60 
```

In Microsoft Windows Server 2003 or Windows XP, when Unidrv prints in HP-GL/2 mode, if a hatch brush is received in the [**DrvRealizeBrush**](https://msdn.microsoft.com/library/windows/hardware/ff556273) function, Unidrv sends a command so that the printer selects the appropriate hatch brush. Unidrv does not control how the hatch brush is rendered. For example, spacing between the lines is usually controlled by the resolution. On higher resolution, the spacing gets small, while on lower resolution, spacing would be greater. Therefore, a document might print differently if different resolution is used.

In Windows Vista, if the GPD specifies the **UseImageForHatchBrush?** attribute, Unidrv renders the hatch brush onto a bitmap surface and then sends that bitmap to the device. Unidrv, therefore, has some control on how the hatch brush is rendered.

### ReverseBandOrder?

The **ReverseBandOrder?** attribute uses the following GPD syntax.

```cpp
*Ifdef: WINNT_60
*ReverseBandOrder?: TRUE
*Endif: WINNT_60 
```

The value of **ReverseBandOrder?** is **TRUE** or **FALSE** to indicate whether reverse banding is enabled. This attribute causes banding to take place in reverse order. For example, for a portrait page, banding occurs from bottom to top instead of top to bottom.

This attribute is essentially the same as ReverseBandOrderForEvenPages?, except that **ReverseBandOrder?** is considered even if duplex is not active (**ReverseBandOrderForEvenPages?** works only if duplex is ON), and it works for all pages (**ReverseBandOrderForEvenPages?** works only on even pages). For details about how to use **ReverseBandOrder?** and other related information, see \***ReverseBandOrderForEvenPages?**. Especially note that plug-ins must reverse the scan lines and the bits in the scan line.

You can use a combination of \*ReverseBandOrderForEvenPages? and \***ReverseBandOrder?**.

When only **ReverseBandOrder?** is set to **TRUE**, banding will be reversed for all pages.

When only **ReverseBandOrderForEvenPages?** is set to **TRUE**, banding will be reversed for even pagesonly if the printer is printing duplex. If duplex is not set, the **ReverseBandOrderForEvenPages?** setting is ignored.

When both **ReverseBandOrder?** and **ReverseBandOrderForEvenPages?** are set, the following occurs:

-   If duplex is ON, reverse banding is performed for odd pages (that is, 1, 3, 5, 7, and so on).

-   If duplex is OFF, reverse banding is performed for all pages.

### BidiQueryFile

The **BidiQueryFile** attribute uses the following GPD syntax.

```cpp
*BidiQueryFile: <GPD or GDL file name>
```

Use **BidiQueryFile** to specify the GPD or GDL file name that contains the printer driver's auto-config **BidiQuery** or **BidiResponse** data. The GPD or GDL file name should not specify any path. If the auto-config data is contained within the driver's DataFile GPD file, you can also specify that GPD file as the value of the **BidiQueryFile** attribute.

The following code example shows an example of this attribute in a partial GPD file.

```cpp
*Ifdef: WINNT_60
*BidiQueryFile: "ACnfgUni.GDL"
*Endif: WINNT_60
```

 

 




