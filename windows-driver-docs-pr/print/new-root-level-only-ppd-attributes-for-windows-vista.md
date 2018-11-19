---
title: New Root-Level-Only PPD Attributes for Windows Vista
description: New Root-Level-Only PPD Attributes for Windows Vista
ms.assetid: 49cdfb2f-e119-4960-9e79-67e1025b753f
keywords:
- root-level-only attributes WDK Unidrv
- general printer attributes WDK Unidrv , root-level-only
- PPD attributes WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# New Root-Level-Only PPD Attributes for Windows Vista


The following list describes the PPD attributes that are new starting with Windows Vista. To maintain backwards compatibility with pre-Windows Vista versions of Windows, you should surround these attributes with the following code.

```cpp
*Ifdef: WINNT_60 ... *Endif: WINNT_60 blocks
```

### MSPrintSchemaKeywordMap

The **MSPrintSchemaKeywordMap** attribute defines the mapping from a PPD feature keyword to a public Print Schema feature keyword, or a mapping from a PPD option keyword of a PPD feature to a public Print Schema option keyword of a Print Schema feature.

**MSPrintSchemaKeywordMap** has two acceptable formats:

<a href="" id="format-1"></a>Format 1  
```cpp
*MSPrintSchemaKeywordMap: PrintSchema_feature_keyword *<PPD_feature_keyword>
```

<a href="" id="format-2"></a>Format 2  
```cpp
*MSPrintSchemaKeywordMap: PrintSchema_feature_keyword PrintSchema_option_keyword *<PPD_feature_keyword> <PPD_option_keyword>
```

The PPD feature keyword prefix (which is an asterisk \[\*\]) in both formats is required.

For format 1:

-   The PPD feature keyword must refer to a PPD feature that has already been defined in previous PPD file content.

-   Multiple definitions of \***MSPrintSchemaKeywordMap** for the same PPD feature are not allowed. If multiple definitions are found, only the first definition will be accepted, and other definitions will be ignored.

For format 2:

-   The \***MSPrintSchemaKeywordMap** definition for a PPD feature ( by using format 1) must be present before any \***MSPrintSchemaKeywordMap** definitions for the PPD feature's options can appear.

-   In the \***MSPrintSchemaKeywordMap** definition for a PPD option, the mapping of PPD feature keyword to the Print Schema feature keyword must be the same as what is defined in the previous \***MSPrintSchemaKeywordMap** definition for the PPD feature (by using format 1).

-   The PPD option keyword must refer to an option of the PPD feature that has already been defined in previous PPD file content.

-   Multiple definitions of \***MSPrintSchemaKeywordMap** for the same PPD option of a PPD feature are not allowed. If multiple definitions are found, only the first definition will be accepted, and other definitions will be ignored.

If an \***MSPrintSchemaKeywordMap** entry violates any of the preceding format rules, that entry will be ignored, and you will get a ppdchecker warning with detailed information.

**Important**  
\*MSPrintSchemaKeywordMap is not supported for use with the following standard PPD features:

\*Collate
\*Duplex
\*InputSlot
\*OutputBin
\*PageSize
\*Resolution
\*MediaType
It is also important to know that if you map a feature to a Print Schema keyword that is already being used in the PPD file, the corresponding PrintCapabilities document might list that feature more than once. Multiple occurrences might be confusing, so you should not map features to Print Schema keywords that are used in the PPD file.

 

**Note**  The PPD parser automatically generates the FORMSOURCE option for the InputBin feature and maps it to the AutoSelect keyword in the Print Schema. If your PPD file contains an InputBin option that uses the **MSPrintSchemaKeywordMap** attribute to map the option to a Print Schema keyword, the feature in the Print Schema will contain a FORMSOURCE option in the device namespace. AutoSelect will appear in the PrintCapabilities document and refer to the option that is specified in the **MSPrintSchemaKeywordMap** attribute of the PPD file.

 

The following code example shows an example of the **MSPrintSchemaKeywordMap** attribute in a partial PPD file.

```cpp
*OpenUI *IHVStapling:PickOne
*DefaultIHVStapling:Disabled
*IHVStapling Enabled:"..."
*IHVStapling Disabled:"..."
*CloseUI: *IHVStapling

*MSPrintSchemaKeywordMap: Staple*IHVStapling
*MSPrintSchemaKeywordMap: StapleOn*IHVStaplingEnabled
*MSPrintSchemaKeywordMap: StapleOff*IHVStaplingDisabled
```

### MSPrintSchemaPrivateNamespaceURI

The **MsPrintSchemaPrivateNamespaceURI** attribute defines the private namespace URI that the core driver should use for exposing private PPD features or options in PrintTicket or PrintCapabilities. This URI will be applied to any features or options that do not have explicit mapping (by using the \***MSPrintSchemaKeywordMap** definition) into public Print Schema.

**MSPrintSchemaPrivateNamespaceURI** uses the following format.

```cpp
*MSPPrintSchemaPrivateNamespaceURI: "<URI>"
```

&lt;URI&gt; represents a PPD QuotedValue. As defined by the PPD specification, QuotedValue allows both literal ASCII substrings and hexadecimal substrings.

A single printer model's PPD file (or files) should have only one definition of \***MSPrintSchemaPrivateNamespaceURI** . If multiple definitions are found, only the first definition will be accepted, and others will be ignored.

The following code example shows an example of the **MsPrintSchemaPrivateNamespaceURI** attribute in a partial PPD file.

```cpp
*MSPrivateNamespaceURI:  "http://www.ihv.com/schema/2004"
```

### MSIsXPSDriver

The **MSIsXPSDriver** attribute uses the following format.

```cpp
*MSIsXPSDriver:  True | False
```

You can use the Windows Vista PScript5 driver configuration module (Ps5ui.dll) for both Microsoft Win32 GDI drivers and the [new XPSDrv drivers](xpsdrv-printer-drivers.md). To use the PScript5 driver configuration module for XPSDrv drivers, the XPSDrv driver's PPD data file must specify **MSIsXPSDriver** and set its value to True.

The following code example shows an example of this attribute in a partial PPD file:

```cpp
*MSIsXPSDriver: True
```

To use the PScript5 driver configuration module for Win32 GDI drivers, you do not need to specify this PPD attribute.

### MSPrintProcDuplexOptions

The **MSPrintProcDuplexOptions** attribute uses the following format.

```cpp
*MSPrintProcDuplexOptions:  "int"
```

This attribute can have one of the following values:

1: Reverse pages for reverse duplex

2: Suppress generation of extra blank page if possible

3: Both of the above

0: None of the above

The following code example shows an example of **MSPrintProcDuplexOptions** in a partial PPD file.

```cpp
*MSPrintProcDuplexOptions:  "2" 
```

This attribute controls various duplexing options in the print processor.

If **MSPrintProcDuplexOptions** is 1, it controls whether the print processor should reverse pages on reverse duplex.

Assume that you have to print a four-page document with n-up = 1, and you want to use reverse printing and duplex printing. Because you want reverse printing, you want to print the last page before the first page. Because you want duplex printing, you want to print two pages on a single sheet of paper. The print processor can play back the pages in one of the following two formats (where each pair of numbers indicates the two pages that would print on the two sides of a single sheet of paper):

-   Format 1: (4,3),(2,1)

-   Format 2: (3,4),(1,2)

Before Windows Vista, a print processor would print the pages in format 2 \[(3,4),(1,2)\]. But in Windows Vistaand later, the default format is format 1 \[(4,3),(2,1)\]. This change occurred because many printers have incorrect output with format 2; that is, the pages that are printed are not ordered in the proper order.

If your printer works correctly with format 1, you will not need to change anything for Windows Vistaand later. However, if your printer works incorrectly with format 1 and you want to revert to format 2, add the **MSPrintProcDuplexOptions** attribute with value 1.

```cpp
*MSPrintProcDuplexOptions: "1"
```

For the pre-Windows Vista PScript driver, if you have a pre-Windows Vista print processor, format 2 is the default, and you cannot change the behavior; otherwise, if you have a Windows Vista print processor, format 1 is the default, and you cannot change the behavior.

For the Windows Vista PScript driver. if you have a pre-Windows Vista print processor, format 2 is the default, and the PPD attribute will be ignored; otherwise, if you have a Windows Vista print processor, format 1 is the default, but you can change the format by using the **MSPrintProcDuplexOptions** attribute.

If **MSPrintProcDuplexOptions** is 2, the print processor will suppress the generation of blank pages in certain duplex scenarios.

For example, if the job is a one-page job and duplex is on (assume n-up = 1), only one side of the sheet needs to be printed. Currently, printers will print one side and then generate an empty blank page on the reverse side. (Because the print job was started with duplex=on, the printer expects two pages before it ejects the sheet. If the second page does not print, some printers keep waiting.) The drawbacks of the current solution are:

-   The generated page causes inaccurate page count in accounting software and the page counter within printers.

-   When the page comes halfway out of the printer (in some Hewlett Packard DeskJet-style printers), the user might try to pull it out while the printer tries to pull it back in. This situation can cause hardware issues.

You can avoid the preceding problems by specifying \***MSPrintProcDuplexOptions**: "2" in the PPD file.

Note that even if this attribute is set, blank page optimization is performed only in the following limited cases:

1.  For reverse printing, blank page optimization is performed only when the whole job can fit on a single side of paper (for example, aone-page job with n-up=1 or a four-page job with n-up =4). If the job needs more than one sheet, the optimization is not performed (because the printer pages will be printed in an inaccurate order). For example, for a three-page job, the pages may be printed in the order 3,2,1,&lt;blank&gt; instead of 4,3,2,&lt;blank&gt;.

2.  Blank page optimization is not performedd if the print processor has to simulate copies. The print processor simulates copies if the number of copies that are needed is more than the number of copies that the print processor can make.

    The following situation is an example of when simulations occurs and blank pages are generated (if required):

    -   Two copies for a printer that cannot make copies

    The following situations are examles of when simulation does not occur and you can suppress extra page generation:

    -   Single copy job for a printer that cannot make copies
    -   Five-copy job for a printer that can make more than copies

For the pre-Windows Vista PScript driver, if you have a pre-Windows Vista print processor, a printer will print an extra blank page, if deemed necessary, and you cannot change the behavior; otherwise, if you have a Windows Vista print processor, a printer will print an extra blank page, if deemed necessary, and you cannot change the behavior.

For the Windows Vista PScript driver. if you have a pre-Windows Vista print processor, a printer will print an extra blank page, if deemed necessary, and the PPD attribute will be ignored; otherwise, if you have a Windows Vista print processor, and if an appropriate PPD attribute and the proper conditions are present (that is, the conditions that are described earlier about preventing blank page printing), a printer will not print blank pages.

### MSBidiQueryFile

The **MSBiDiQueryFile** attribute uses the following format.

```cpp
*MSBidiQueryFile: "filename"
```

Use **MSBiDiQueryFile** to specify the GPD or GDL file name that contains the printer driver's auto-config BidiQuery and BidiResponse data. The GPD or GDL file name should not specify any path.

The following code example shows an example of **MSBiDiQueryFile** in a partial PPD file.

```cpp
*MSBidiQueryFile: "ACnfgPS.GDL"
```

### MSXPSMaxCopies

The **MSXPSMaxCopies** attribute uses the following format.

```cpp
*MSXPSMaxCopies: "int"
```

Use **MSXPSMaxCopies** to specify the maximum number of copies that an XPSDrv printer driver can support.

The following code example shows an example of **MSXPSMaxCopies** in a partial PPD file.

```cpp
*MSXPSMaxCopies: "99"
```

 

 




