---
title: Driver features
description: Driver features
ms.date: 06/21/2023
---

# Driver features

[!include[Print Support Apps](../includes/print-support-apps.md)]

Driver features are non-PPD features that are synthesized by the driver (for example, the **%OutputFormat** feature). To avoid name conflicts with PPD feature keywords, all driver feature keyword names are preceded by a "%" character. Driver feature/option keywords are also case sensitive.

To obtain a list of all driver feature keywords that the driver supports, a plug-in can call EnumFeatures, which will return the feature keyword list containing both driver features and PPD features. The plug-in can then search for feature keyword names that begin with the "%" prefix to get the driver feature list.

The following table lists the currently supported driver features. Each row in the table lists a driver feature keyword, shows the supported options, states whether the feature's options can be enumerated in a call to EnumOptions, and provides a brief description.

| Driver feature | Supported options | Enum options | Description and comments |
|--|--|--|--|
| **%AddEuro** | "True"<br><br>"False" | Yes | Add the Euro symbol to device fonts.<br><br>This feature is supported only for Level 2+ printers. For Level 1 printers, **SetOptions** ignores this feature, and **GetOptions** always returns "False". |
| **%CtrlDAfter** | "True"<br><br>"False" | Yes | Send Ctrl-D after each job.<br><br>Printer-sticky |
| **%CtrlDBefore** | "True"<br><br>"False" | Yes | Send Ctrl-D before each job.<br><br>Printer-sticky |
| **%CustomPageSize** | See Note 1 below for more information. | No | Specify PostScript custom page size parameters.<br><br>Document-sticky |
| **%GraphicsTrueGray** | "True"<br><br>"False" | Yes | Convert gray graphics to PostScript gray.<br><br>Printer-sticky |
| **%JobTimeout** | A NULL-terminated ANSI string containing decimal digit characters that represents the unsigned integer number of seconds for the time-out, in the range 0 through 2,147,483,647.<br><br>For **SetOptions**, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol isn't allowed. | No | Specify the job time-out value.<br><br>Printer-sticky |
| **%MaxFontSizeAsBitmap** | A NULL-terminated ANSI string containing decimal digit characters that represents the unsigned integer number of pixels, in the range 0 through 32,767.<br><br>For **SetOptions**, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol isn't allowed. | No | Specify the maximum font size to download as a bitmap.<br><br>Printer-sticky |
| **%MetafileSpooling** | "True"<br><br>"False" | Yes | Enable/disable advanced printing features.<br><br>Document-sticky<br><br>See Note 2 below for more information. |
| **%MinFontSizeAsOutline** | A NULL-terminated ANSI string containing decimal digit characters that represents the unsigned integer number of pixels, in the range 0 through 32,767.<br><br>For **SetOptions**, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol isn't allowed. | No | Specify the minimum font size to download as outline.<br><br>Printer-sticky |
| **%Mirroring** | "True"<br><br>"False" | Yes | Mirror output by reversing the horizontal coordinates.<br><br>Document-sticky |
| **%Negative** | "True"<br><br>"False" | Yes | Produce negative output by reversing values for black and white. This feature is supported only for black and white printers. For color printers, **SetOptions** ignores this feature, and **GetOptions** always returns "False".<br><br>Document-sticky |
| **%Orientation** | "Portrait", "Landscape", "RotatedLandscape" | Yes | Specify the output orientation.<br><br>Document-sticky |
| **%OutputFormat** | "Speed", "Portability", "EPS", "Archive" | Yes | Specify the PostScript output format.<br><br>Document-sticky<br><br>See Note 5 below for more information. |
| **%OutputProtocol** | "ASCII", "BCP", "TBCP", "Binary" | Yes | Specify the protocol the printer will use for print jobs. PostScript printers are assumed to support "ASCII" and "Binary", so these options are always available. The "BCP" and "TBCP" options are available only if they're supported. To determine this, check the global attribute "Protocols".<br><br>Printer-sticky |
| **%OutputPSLevel** | "1", "2", "3" | No | Specify which PostScript language level to use for the print job. The setting will never be greater than the value specified in the "LanguageLevel" global attribute.<br><br>Document-sticky |
| **%PageOrder** | "FrontToBack"<br><br>"BackToFront" | Yes | Specify the order in which pages will be printed.<br><br>Document-sticky<br><br>See Note 3 below for more information. |
| **%PagePerSheet** | "1", "2", "4", "6",<br><br>"9", "16", "Booklet" | Yes | Specify the number of logical pages per physical sheet. This feature is also known as "N-up" printing.<br><br>Document-sticky<br><br>See Note 4 below for more information. |
| **%PSErrorHandler** | "True"<br><br>"False" | Yes | Send PostScript error handler.<br><br>Document-sticky |
| **%PSMemory** | A NULL-terminated ANSI string containing decimal digit characters that represents the unsigned integer number of kilobytes of PostScript memory, in the range 0 through 2,147,483,647.<br><br>For **SetOptions**, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol isn't allowed. | No | Specify the amount of available PostScript virtual memory.<br><br>The core driver requires a certain amount of available PostScript virtual memory for its processing. If **%PSMemory** is set below this minimum, the minimum value is used as the new value. Currently the minimum value is 172 KB for Level 1 printers and 249 KB for Level 2+ printers.<br><br>Printer-sticky |
| **%TextTrueGray** | "True"<br><br>"False" | Yes | Convert gray text to PostScript gray.<br><br>Printer-sticky |
| **%TTDownloadFormat** | "Automatic", "Outline", "Bitmap", "NativeTrueType" | Yes | Specify TrueType font downloading format. "NativeTrueType" is supported only when the "TTRasterizer" global attribute indicates support for "Type42".<br><br>Document-sticky |
| **%WaitTimeout** | A NULL-terminated ANSI string containing decimal digit characters that represents the unsigned integer number of seconds for the time-out, in the range 0 through 2,147,483,647.<br><br>For **SetOptions**, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol isn't allowed. | No | Specify wait time-out value.<br><br>Printer-sticky |

## Notes on Driver Feature Keywords

1. The **%CustomPageSize** driver feature has five option values: x, y, WidthOffset, HeightOffset, and FeedDirection. Please refer to section 5.16 of the *PostScript Printer Description File Format Specification, Version 4.3*, for a detailed explanation of these parameters.

    A **%CustomPageSize** entry contains the **%CustomPageSize** keyword, together with values for the x, y, WidthOffset, HeightOffset, and FeedDirection options. The first item is the %CustomPageSize keyword, followed by a NULL character. The values for x, y, WidthOffset, and HeightOffset follow this keyword, and appear as substrings of unsigned decimal digits, each representing the number of PostScript points for the corresponding option value. Each of these numeric values is followed by one or more space or tab characters. The final item in the string is the value for FeedDirection, which is terminated by a NULL character. The options for FeedDirection are "LongEdge", "ShortEdge" (corresponding to orientations 0 and 1), and "LongEdgeFlip", "ShortEdgeFlip" (corresponding to orientations 2 and 3). Check the **\*LeadingEdge** PPD feature keyword for supported feed directions.

    For **GetOptions**, the output buffer pointed to by *pmszFeatureOptionBuf* is as described in the previous paragraph. In the following example, the value for x is 612, the value for y is 792, the values for WidthOffset and HeightOffset are both 0, and the value for FeedDirection is "ShortEdge".

    ```PDD
    "%CustomPageSize\0612 792 0 0 ShortEdge\0"
    ```

    For **SetOptions**, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol isn't allowed. Otherwise, the input buffer pointed to by *pmszFeatureOptionBuf* should be constructed as described above.

1. The **%CustomPageSize** driver feature is supported only if all three of the following conditions are met:

    1. The PPD file contains the **\*CustomPageSize** feature.

    1. The **\*PPD-Adobe** keyword has a value greater than or equal to 4.3, or **\*UseHWMargin**: **False** is specified to indicate a roll-fed device.

    1. The **\*PageSize** PPD feature's currently selected option is CustomPageSize.

1. This feature is supported only when spooler EMF spooling is enabled.

    When supported, setting this feature's option to "False" causes changes to the following EMF-related features:

    1. If **%PagePerSheet** is "Booklet", it's changed to "1".

    1. If Collate is set to "True" (which can be set either directly in the public portion of the [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure or by calling **SetOptions** on the **\*Collate** PPD feature), but the Collate feature isn't currently available, Collate will be set to "False".

    1. If **%PageOrder** is the opposite of the printer's current output order setting, **%PageOrder** is reversed to the printer's value.

1. This feature is supported only when spooler EMF spooling is enabled.

    When it's supported, setting this feature can cause the following to occur:

    1. If the printer's PPD file includes the **\*OutputOrder** feature keyword, then its option selection is changed to match the output order of the new setting for the **%PageOrder** feature. This is done to prevent the spooler from performing unnecessary page order simulation.

    1. If the printer's PPD file doesn't include the **\*OutputOrder** feature, and the new setting for the **%PageOrder** driver feature is the opposite of the printer's current output order setting, and the **%MetafileSpooling** driver feature is "False", then **%MetafileSpooling** is reset to "True".

1. The "Booklet" option is supported only when spooler EMF spooling is enabled and the Duplex feature is available.

    When the "Booklet" option is supported, setting the **%PagePerSheet** driver feature to "Booklet" can cause the following changes:

    1. If the **%MetafileSpooling** driver feature is "False", it's reset to "True".

    1. If the **\*Duplex** PPD feature is set to None, the **\*Duplex** feature is reset to the first non-Simplex option defined in the PPD file.

1. Except for "EPS" (Encapsulated PostScript), the formats specified in the **%OutputFormat** driver feature are categorized according to the following two characteristics:

    1. Is the output PostScript code independent of page order?

    1. Does the output PostScript code contain device control commands (which usually use the **setpagedevice** operator)?

        | Category | Page Order Independent | setpagedevice |
        |--|--|--|
        | Archive | Yes | No |
        | Portability | Yes | Yes |
        | Speed | No | Yes |

When **GetOptions** is called on driver feature keywords, if a requested feature keyword isn't recognized, or if the feature keyword is recognized but not supported in the current *document-sticky* or *printer-sticky* mode (see [Replacing Driver-Supplied Property Sheet Pages](replacing-driver-supplied-property-sheet-pages.md)), the feature will simply be ignored and the output buffer won't contain its feature/option keyword pair.

For example, suppose the **GetOptions** method is called, and the *pmszFeaturesRequested* input buffer contains the following string (in MULTI\_SZ format):

```PDD
"Resolution\0%CustomPageSize\0Unknown_Name\0%Orientation\0\0"
```

After **GetOption** returns, the *pmszFeatureOptionBuf* output buffer could contain this string (also in MULTI\_SZ format):

```PDD
"Resolution\0300dpi\0%CustomPageSize\0612 792 0 0 ShortEdge\0%Orientation\0RotatedLandscape\0\0"
```

Notice that the Unknown_Name feature (which doesn't exist) listed in the first string doesn't appear in the second string, since it wasn't recognized by the Pscript driver. The other features, Resolution, **%CustomPageSize**, and **%Orientation**, appear in the output string, together with their current options, which are "300dpi", "612 792 0 0 ShortEdge", and "RotatedLandscape", respectively. See Driver Features for an explanation of the **%CustomPageSize** options.

When **SetOptions** is called on driver feature keywords, if a requested feature keyword or its option keyword in the input buffer pointed to by *pmszFeatureOptionBuf* is not recognized, or the feature is recognized but not supported in the current document-sticky or printer-sticky mode (see [Replacing Driver-Supplied Property Sheet Pages](replacing-driver-supplied-property-sheet-pages.md)), or both the feature keyword and its option keyword are recognized but the option keyword is invalid for that feature (for example, trying to set **%TTDownloadFormat** to "NativeTrueType" on a printer that does not support Type42 TTRasterizer), then that feature/option pair will be ignored and the current option for that feature will continue to be in effect.

The order of feature/option keyword pairs in the buffer pointed to by *pmszFeatureOptionBuf* can affect the result of the **SetOptions** call. For example, the following two different orders have different results.

| *pmszFeatureOptionBuf* | %PagePerSheet | %MetafileSpooling |
|--|--|--|
| "%MetafileSpooling\0False\0%PagePerSheet\0Booklet\0\0" | "Booklet" | "True" |
| "%PagePerSheet\0Booklet\0%MetafileSpooling\0False\0\0" | "1" | "False" |

For an explanation of why these results occur, see Note 3 on **%MetafileSpooling**, above.
