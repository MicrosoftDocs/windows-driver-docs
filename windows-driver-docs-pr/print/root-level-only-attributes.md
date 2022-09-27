---
title: Root-level-only attributes
description: Provides information about root-level-only attributes.
keywords:
- root-level-only attributes WDK Unidrv
- general printer attributes WDK Unidrv, root-level-only
ms.date: 09/16/2022
---

# Root-level-only attributes

Root-level-only attributes are [general attributes](general-attributes.md) that describe such driver-specific characteristics as the names of resource files, help files, or additional included GPD files, along with specifications for the driver's master units, version number, and character code page.

Additional root-level-only attributes specify such device-specific characteristics as the printer's name, type, maximum copy capacity, and number of font cartridge slots.

These attributes are called root-level-only attributes because they must always be placed in a GPD file at root level (that is, not inside braces).

The following table lists the root-level-only attributes.

| Attribute name | AttributeParameter | Comments |
|--|--|--|
| ***CodePage*** | Numeric-valued Windows code page identifier. | Optional. If not specified, Unicode is used. The code page is applied to all displayed strings. |
| **FontCartSlots** | Numeric value representing the number of font cartridge slots provided by the printer. | Optional. If not specified, the default value is zero. |
| ***GPDFileName*** | Quoted text string representing the GPD file name (without path). | Optional. |
| **GPDFileVersion** | Quoted text string representing the current GPD file version. Recommended format is *MajorVersion*.*MinorVersion*, such as "1.0". | Optional. If specified, this string is displayed in Unidrv's About dialog box. |
| ***GPDSpecVersion*** | Quoted text string representing the current GPD specification version. Required format is *MajorVersion*.*MinorVersion*, such as "1.0". | Required. Must be first entry in GPD file, before any comments.This value must be "1.0" for Windows 2000. |
| **HelpFile** | Quoted string containing the name of a customized help file, with a .hlp extension. | Optional. If included, it can add topics or overwrite existing topics in Unidrv's help file. Help file indexes are specified by *HelpIndex attributes for features and options. |
| **Include** | Quoted string containing the name of an additional GPD file. | Obsolete. This entry has been redefined as a [preprocessor directive](preprocessor-directives.md). |
| ***InstalledOptionName*** | Quoted string that is displayed to indicate an installable feature or option is installed. Typically, this string is "Installed", but any appropriate string can be specified. | Required if *Installable? is **TRUE** for any features or options (see [Feature attributes](feature-attributes.md)), and if **rcInstalledOptionNameID** is not specified. |
| **MasterUnits** | PAIR representing the printer's [master units](master-units.md). | Required. To reduce potential round-off errors, use the same values for resolution units in font metrics data that you specify for **MasterUnits**. (See Unidrv Font Metrics in [Customized font management](customized-font-management.md).) |
| **MaxCopies** | Numeric value representing the maximum number of copies the printer can support. | Optional. If not specified, the default value is 1. |
| ***ModelName*** | Quoted text string representing the printer model name. | Required if **rcModelNameID** is not specified. String must match name in setup.inf. |
| **NotInstalledOptionName** | Quoted string that is displayed to indicate an installable feature or option is not installed. Typically, this string is "Not installed", but any appropriate string can be specified. | Required if **Installable?** is **TRUE** for any features or options (see [Feature attributes](feature-attributes.md)), and if **rcNotInstalledOptionNameID** is not specified. |
| **Personality** | Quoted string representing the printer language used by the printer. | Optional. If specified, the string is displayed by Directory Services. Also see **rcPersonalityID** below in this table.|
| **PrinterType** | PAGE, SERIAL, or TTY | Required |
| **PrintRate** | Numeric value representing the monochrome print rate. Units are specified by **PrintRateUnit**. | Optional. If not specified, the default value is 0. |
| **PrintRatePPM** | Numeric value representing the printing speed, in pages per minute. | Optional. If not specified, the default value is 0. |
| ***PrintRateUnit*** | PPM - Pages/min<br><br>CPS - Characters/sec<br><br>LPM - Lines/min<br><br>IPM - Inches/min. (IPM is for plotters) | Required if **PrintRate** is specified. The specified unit should match the printer type. For example, PPM should be specified for page printers. |
| **rcInstalledOptionNameID** | Resource ID of a string resource that is displayed to indicate an installable feature or option is installed. Typically, this string is "Installed", but any appropriate string can be specified. | Required if **Installable?** is **TRUE** for any features or options (see [Feature attributes](feature-attributes.md)), and if **InstalledOptionName** is not specified. |
| **rcNotInstalledOptionNameID** | Resource ID of a string resource that is displayed to indicate an installable feature or option is not installed. Typically, this string is "Not installed", but any appropriate string can be specified. | Required if **Installable?** is **TRUE** for any features or options (see [Feature attributes](feature-attributes.md)), and if **NotInstalledOptionName** is not specified. |
| **rcPersonalityID** | Resource ID of a string resource representing the printer language used by the printer. | Optional. If specified, the string is displayed by Directory Services. Also see **Personality**. |
| **rcPrinterIconID** | Resource ID of an RC_ICON resource representing an icon associated with the printer. | Optional. If not specified, a default printer icon is displayed. It is recommended that all RC_ICON resource IDs be numbered contiguously starting with 1. |
| **ResourceDLL** | Quoted string containing the name, without path information, of a resource DLL. | Optional. See [Using resource DLLs in a minidriver](using-resource-dlls-in-a-minidriver.md). |

For examples, see the [Sample GPD files](sample-gpd-files.md).

For information about new root-level-only attributes for Windows Vista, see [New root-level-only GPD attributes for Windows Vista](new-root-level-only-gpd-attributes-for-windows-vista.md) and [New root-level-only PPD attributes for Windows Vista](new-root-level-only-ppd-attributes-for-windows-vista.md).
