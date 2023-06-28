---
title: Customized font management
description: Customized font management
keywords:
- Unidrv, fonts
- font management WDK Unidrv
- customized font management WDK Unidrv
- .ufm files
- UFM files
- .gtt files
- GTT files
- .uff files
- UFF files
- device fonts WDK Unidrv
- cartridge fonts WDK Unidrv
- downloadable PCL soft fonts WDK Unidrv
- PCL soft fonts WDK Unidrv
- Unidrv WDK print
ms.date: 06/16/2023
---

# Customized font management

[!include[Print Support Apps](../includes/print-support-apps.md)]

For *PCL* printers, Unidrv supports downloading soft fonts as bitmaps or TrueType outlines. For device fonts, Unidrv supports PCL, CAPSL, and PPDS printer command formats. For other formats, customized font management code must be provided in a rendering plug-in. The following set of IPrintOemUni methods can be implemented:

[**IPrintOemUni::DownloadFontHeader**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-downloadfontheader)  
Used to obtain a soft font's header information from Unidrv and then download the information to the printer.

[**IPrintOemUni::DownloadCharGlyph**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-downloadcharglyph)  
Used to download a soft font's character glyphs to the printer.

[**IPrintOemUni::OutputCharStr**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-outputcharstr)  
Used to control the printing of characters.

[**IPrintOemUni::SendFontCmd**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-sendfontcmd)  
Used to modify a printer's device font selection command, and if necessary, send it to the printer.

[**IPrintOemUni::TextOutAsBitmap**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-textoutasbitmap)  
Used to create a bitmap image of a text string.

[**IPrintOemUni::TTDownloadMethod**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-ttdownloadmethod)  
Used to specify the glyph format that the Unidrv should use when it sends a specified soft font to the printer.

Unidrv provides a callback function, [*UNIFONTOBJGetInfo*](/windows-hardware/drivers/ddi/printoem/nc-printoem-pfngetinfo), that rendering plug-ins can call to obtain font or glyph information.

For device fonts, font descriptions must be provided as explained in the **Unidrv font metrics files** section and the **Glyph translation table files** section.

For cartridge fonts, font descriptions can be provided in resource DLLs and specified using [font cartridges](font-cartridges.md) entries in a *GPD* file. Font descriptions can also be provided in the form of Unidrv font format files.

For downloadable PCL soft fonts, font descriptions must be provided as explained in the **Unidrv font format files** section.

## Unidrv Font Metrics files

Each device font that a printer supports represents a Unidrv Font Metrics (.ufm) file. A .ufm file is a binary file that is constructed using the structures described in [Unidrv Font Metrics Structures](/windows-hardware/drivers/ddi/_print/index). The first structure in a .ufm file is [**UNIFM_HDR**](/windows-hardware/drivers/ddi/prntfont/ns-prntfont-_unifm_hdr), which contains offsets to the file's other structures. The following figure shows the layout of an Unidrv Font Metrics file.

![diagram illustrating the layout of a unidrv font metrics file.](images/ufm.png)

Unidrv also supports .ifi files, the font metrics files created for Windows NT 4.0.

## Glyph Translation Table files

Each device font that a printer supports represents a Glyph Translation Table (.gtt) file. A .gtt file is a binary file that is constructed using the structures described in [Unidrv Glyph Translation Table Structures](/windows-hardware/drivers/ddi/_print/index). The first structure in a .gtt file is a [**UNI_GLYPHSETDATA**](/windows-hardware/drivers/ddi/prntfont/ns-prntfont-_uni_glyphsetdata) structure, which contains offsets to the file's other structures.

The following figure shows the layout of a glyph translation table file.

![diagram illustrating the layout of a glyph translation table file.](images/gtt.png)

In the preceding figure, the UNI_GLYPHSETDATA structure contains the offsets from the beginning of the file to the first [**GLYPHRUN**](/windows-hardware/drivers/ddi/prntfont/ns-prntfont-_glyphrun) structure, to the first [**UNI_CODEPAGEINFO**](/windows-hardware/drivers/ddi/prntfont/ns-prntfont-_uni_codepageinfo) structure, and to the [**MAPTABLE**](/windows-hardware/drivers/ddi/prntfont/ns-prntfont-_maptable) structure.

Unidrv also supports glyph translation files created for Windows NT 4.0, which use run-length encoding (RLE) compression and have an .rle extension.

## Unidrv Font Format files

For cartridge fonts that aren't specified using [font cartridges](font-cartridges.md) entries in a GPD file, the fonts must be described in a Unidrv Font Format (.uff) file. Additionally, downloadable *PCL* soft fonts must be specified using a .uff file.

A .uff file is a binary file that is constructed using the following sets of structures:

- [Unidrv font format structures](/windows-hardware/drivers/ddi/_print/index), which define the contents and structure of a .uff file.

- [Unidrv font metrics structures](/windows-hardware/drivers/ddi/_print/index), which define the metrics for each font.

- [Unidrv glyph translation table structures](/windows-hardware/drivers/ddi/_print/index), which define the glyph sets used by the fonts.

The following figure shows the layout of a Unidrv Font Format file.

![diagram illustrating the layout of a unidrv font format file.](images/uff.png)

A Unidrv Font Format file consists of a [**UFF_FILEHEADER**](/windows-hardware/drivers/ddi/prntfont/ns-prntfont-_uff_fileheader) structure, and one or more [**UFF_FONTDIRECTORY**](/windows-hardware/drivers/ddi/prntfont/ns-prntfont-_uff_fontdirectory) and [**DATA_HEADER**](/windows-hardware/drivers/ddi/prntfont/ns-prntfont-_data_header) structure pairs. Each **DATA_HEADER** structure is associated with a block of font data. The UFF_FILEHEADER structure contains the offset from the beginning of the file to the first **UFF_FONTDIRECTORY** structure. Each **UFF_FONTDRECTORY** structure contains the offset from the beginning of the file to a DATA_HEADER structure that contains font data.

Additionally, for downloadable *PCL* soft fonts, the binary data to be downloaded is stored in a .uff file.

.uff files creation is the responsibility of vendor-supplied font installation software. Unidrv reads a printer's .uff files to obtain font and glyph information. The font installer should modify .uff file contents when fonts are added or deleted. For more information about creating a font installer, see [Customized Font Installers for Unidrv](customized-font-installers-for-unidrv.md).

All .uff files must be stored in the %SystemRoot%\\System32\\Spool\\Drivers\\Unifont directory. To associate individual .uff files with specific printers, installation software must call the SetPrinterData function (described in the Windows SDK documentation) to create registry values under each printer's registry key. The following table lists the registry value names that must be used, and indicates the maintainer of each value.

| Registry value name and type | Value definition | Maintainer |
|--|--|--|
| "ExternalFontFile"<br><br>REG_SZ | Filename of a .uff file that specifies the current installed fonts. Fonts can be downloadable or contained in a cartridge. | Font Installer |
| "ExtFontCartFile"<br><br>REG_SZ | Filename of a .uff file that specifies all the fonts contained in all the font cartridges listed for "ExtFontCartNames". | Font Installer |
| "ExtFontCartNames"<br><br>REG_MULTI_SZ | Names of all the font cartridges that could possibly be installed on the printer. | Font Installer |
| "FontCart"<br><br>REG_MULTI_SZ | Names of all the font cartridges currently installed for the printer. | Unidrv user interface |

After you add a font cartridge to a printer, the system administrator must run the font installer, which is responsible to copy font descriptions from the .uff file specified by "ExtFontCartFile" into the .uff file specified by "ExternalFontFile". Likewise, the font installer must remove font descriptions from the .uff file specified by "ExtFontCartFile" when a cartridge is removed.
