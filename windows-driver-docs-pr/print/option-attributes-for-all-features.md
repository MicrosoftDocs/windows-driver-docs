---
title: Option attributes for all features
description: Option attributes for all features
ms.date: 07/18/2023
---

# Option attributes for all features

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists, in alphabetic order, the [option attributes](option-attributes.md) available for all features and describes their parameters.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| \***Command** | A **CmdSelect** [option selection command](option-selection-command.md), specifying the command string that must be sent to the printer in order to select the option. | Required |
| \***DisabledFeatures** | LIST of feature name strings, identifying features that should be disabled if the option is selected.<br><br>Currently DUPLEX and COLLATE features are supported. This option attribute must be used in a feature that has FeatureType set to PRINTER_PROPERTY. | Optional.<br><br>Listed features cannot have *Installable? set to **TRUE**. For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md). |
| \***HelpIndex** | Numeric value representing an index into the help file specified by the \***HelpFile** [root-level-only attribute](root-level-only-attributes.md). | (Also a [feature attribute](feature-attributes.md).)<br><br>Index value cannot be zero or -1. |
| \***Installable?** | **TRUE** or **FALSE**, indicating whether the option is installable. (**FALSE** means always installed.)<br><br>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md). | Optional. If not specified, the default value is **FALSE**. (Also a [feature attribute](feature-attributes.md).) |
| \***InstallableFeatureName** | Text string that is displayed to ask the user whether an installable option is actually installed.<br><br>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md). | Required if \***Installable?** is **TRUE** and***rcInstallableFeatureNameID** is not specified. (Also a [feature attribute](feature-attributes.md).) |
| \***Name** | Text string used as the option's display name on the printer's property sheet. | Optional. If not specified, then ***rcNameID** must be specified. (Also a [feature attribute](feature-attributes.md).) |
| \***OptionID** | Numeric value representing a unique option identifier that Unidrv stores in the printer's [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure. For use only with the PaperSize, InputSlot, Halftoning, and MediaType features. Value is stored in the DEVMODE structure's **dmPaperSize**, **dmDefaultSource**, **dmDitherType**, or **dmMediaType** member, respectively. | Optional. If not specified, Unidrv assigns an identifier value (\>256). To avoid conflicts with Unidrv-assigned identifiers, the specified value must be greater than 512. |
| \***rcIconID** | Resource ID of an icon resource associated with the option. | Optional. If not specified, Unidrv does not display an icon for the option on the printer property sheet. (Also a [feature attribute](feature-attributes.md).) |
| \***rcInstallableFeatureNameID** | Resource ID of a text string that is displayed to ask the user whether an installable option is actually installed.<br><br>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md). | Required if \***Installable?** is **TRUE** and \***InstallableFeatureName** is not specified. (Also a [feature attribute](feature-attributes.md).) |
| \***rcNameID** | Resource ID of string resource representing the option name. | Optional. If not specified, then \***Name** must be specified. (Also a [feature attribute](feature-attributes.md).)<br><br>For [standard options](standard-options.md) of the PaperSize feature only, setting this attribute to RCID_DMPAPER_SYSTEM_NAME causes Unidrv to use a predefined option name string. |

For examples, see the [sample GPD files](sample-gpd-files.md).
