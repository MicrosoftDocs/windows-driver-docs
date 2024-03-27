---
title: Pscript5 Keywords
description: Pscript5 Keywords
ms.date: 01/26/2024
---

# Pscript5 keywords

[!include[Print Support Apps](../includes/print-support-apps.md)]

Feature and option names that are passed to the helper interface from a Pscript5 plug-in are the string names of the features and options as they're defined in the PPD file. Certain reserved strings are defined for features that are implemented in the Pscript5 core driver that aren't represented in the PPD file.

All options listed in the following table can be determined at run-time by calling **EnumOptions**. For features that require numeric settings in ranges, the **EnumOptions** method returns a **NULL** value in its *pOptionList* parameter and a count of zero options in *pdwNumOptions.

| Feature name | Options | Description |
|--|--|--|
| %AddEuro | "True" "False" | Add the Euro symbol to device fonts. Printer-sticky. Requires PostScript Level 2. See note 1 following this table. |
| %CtrlDAfter | "True" "False" | Send CTRL+D after each job. Printer-sticky |
| %CtrlDBefore | "True" "False" | Send CTRL+D before each job. Printer-sticky. |
| %CustomPageSize | Custom page size options have a complex format. See note 2 following this table. | Read or specify a custom page size setting. Setting this feature also causes the dmPaperSize member of the public [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure to be reset to DMPAPER_CUSTOMSIZE (indicating a PS custom size), and sets the DM_PAPERSIZE bit flag. This feature can be read only if the public **DEVMODEW** structure indicates that a custom paper size is in use. Document-sticky. |
| %GraphicsAsTrueGray | "True" "False" | Convert gray graphics to PostScript gray. Printer-sticky. |
| %JobTimeout | Numeric (see note 3 following this table) "0" through "2147483647" | Specify the job timeout in seconds. Printer-sticky. |
| %MaxFontSizeAsBitmap | Numeric (see note 3) "0" through "32767" | Specify the maximum font size to download as a bitmap. Printer-sticky. |
| %MetafileSpooling | "True" "False" | Enable EMF spooling. Enabling this feature is equivalent to enabling the **Advanced Printing Features** UI option. This feature has constraints that interact with booklet printing, collating, and page ordering. This feature is given lowest precedence when resolving against any of those features. Document-sticky. |
| %MinFontAsOutline | Numeric (see note 3 following this table) "0" through "32,767" | Specify the minimum font size that should be downloaded as outline. Printer-sticky. |
| %Mirroring | "True" "False" | Mirror output by reversing the horizontal coordinates. Document-sticky. |
| %Negative | "True" "False" | Reverse the black and white regions on the printed page. Document-sticky. Requires a black and white printer, not color. |
| %Orientation | "Portrait" "Landscape" "RotatedLandscape" | Specify the output orientation. Configuring the orientation by using this technique changes both the private and public [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure values, when used with the **IPrintCoreHelperPS** interface. This warning doesn't apply to the **IPrintCoreUI2** interface. Document-sticky. |
| %OutputFormat | "Speed" "Portability" "EPS" "Archive" | Specify the PostScript output format. The behavior of output format is the same as defined for **IPrintCoreUI2**. Document-sticky. |
| %OutputProtocol | "ASCII" "BCP" "TBCP" "Binary" | Specify the protocol the printer uses to print jobs. The BCP and TBCP options are available only if supported. **EnumOptions** includes only the values that are supported. The output protocol can also be determined by checking the "Protocols" global attribute. Printer-sticky. |
| %OutputPSLevel | "1" "2" "3" | Specify which PostScript language level to generate for this print job. Available options are limited to values that are equal to or less than the language level of the device that is specified in the "LanguageLevel" global attribute. Document-sticky. Requires PostScript Level 2 or higher. See note 1 following this table. |
| %PageOrder | "FrontToBack" "BackToFront" | Specify the order in which to print the pages. If EMF spooling isn't available, this feature isn't listed when calling EnumFeatures, and attempts to read or write the setting for this feature returns E_FAIL. BackToFront is constrained if the %MetafileSpooling feature is set to False. Document-sticky. |
| %PagePerSheet | "1", "2", "4", "6", "9", "16", "Booklet" | Booklet printing is available only if duplexing is available. Setting the "Booklet" option causes duplexing to be turned on if it isn't on already. If duplex is turned off and booklet printing is selected, the option is forced to 2-up. If metafile spooling is disabled, it's represented as a constraint on booklet printing. If EMF spooling is unavailable because the print processor is being used, booklet printing is unavailable. In that situation, booklet printing isn't listed in **EnumOptions**, and **SetOptions** returns E_FAIL if the caller requests "%PagePerSheet" to be set to "Booklet". Document-sticky. |
| %PSErrorHandler | "True" "False" | Send PostScript error handler. Document-sticky. |
| %PSMemory | Numeric (see note 3 following this table). For PostScript Level 1 printers, range is "172" through "2097151". For Postscript Level 2 or 3 printers, range is "249" through "2097151". | Specifies the number of kilobytes of virtual memory that are available on the device. The values are indicated in kilobytes, and not bytes. Also, the valid ranges differ for level 1 and level 2 printers. Attempting to set values outside of these ranges fail with an HRESULT of E_FAIL. Printer-sticky. |
| %TextTrueGray | "True" "False" | Convert gray text to PostScript gray. Printer-sticky. |
| %TTDownloadFormat | "Automatic" "Outline" "Bitmap" "NativeTrueType" | Specify the TrueType font downloading format. NativeTrueType is available and listed in EnumOptions only if the "TTRasterizer" global attribute indicates support for "Type42". Document-sticky. |
| %WaitTimeout | Numeric (see note 3 following this table) "0" through "2147483647" | Specify the wait timeout value in seconds. Printer-sticky. |

**Note 1**
If the stated requirements aren't met for a feature, that feature isn't listed in **EnumFeatures**, and attempts to get or set that feature that causes E_FAIL to be returned. This note applies to %AddEuro, %Negative, and %OutputPSLevel.

**Note 2 (%CustomPageSize)**
Custom page size format is identical to that described in **IPrintCoreUI2**. **EnumOptions** returns an empty list of options.

**Note 3**
Numeric values are represented as ANSI strings that contain only digit characters. Sign symbols aren't allowed. For example, "300" is valid, but "-20", "20.5", and "+300" are all invalid. This note applies to %JobTimeout, %MaxFontSizeAsBitmap, %MinFontAsOutline, %PSMemory, and %WaitTimeout.
