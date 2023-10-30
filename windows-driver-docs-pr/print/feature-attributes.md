---
title: Feature attributes
description: Feature attributes
keywords:
- printer attributes WDK Unidrv , features
- feature attributes WDK Unidrv
- printer features WDK Unidrv , attributes
ms.date: 06/22/2023
---

# Feature attributes

[!include[Print Support Apps](../includes/print-support-apps.md)]

When specifying a printer feature, you use attributes to provide Unidrv with the following information:

- A text string representing the feature's display name.

- The set of printer options associated with the feature.

- A Boolean value indicating whether the feature is always present or is installable.

- The feature type and priority, if the feature is customized, indicating on which property sheet the feature is displayed and its relative priority.

The following table lists the feature attributes in alphabetic order and describes their parameters.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| **\*ConcealFromUI?** | **TRUE** or **FALSE**, indicating whether the feature should be displayed in the user interface. | Optional. If not specified the default value is **FALSE**, which means the feature is displayed.<br><br>Should be **TRUE** only if a feature has only one option (for example, one resolution) and is thus not user-modifiable, or, if the feature's option selection is controlled by setting another feature's options.<br><br>If the **\*ConcealFromUI** attribute is set to **TRUE**, then Unidrv or PrintConfig will add the psk:DisplayUI element to the Feature element for this item in the PrintCapabilities XML. |
| **\*ConflictPriority** | Numeric value representing the feature's priority, where 1 is the highest priority. | Optional. See [Feature Conflict Priority](feature-conflict-priority.md). |
| **\*DefaultOption** | Name of one of the feature's options. | Optional. If not specified, the first option listed in a \*Feature entry is the default. For the PaperSize feature, the default options for Unidrv are A4 for metric locales and Letter elsewhere. If the default PaperSize does not exist, Unidrv uses the PaperSize option that is specified by the ***DefaultOption** keyword. |
| **\*FeatureType** | DOC_PROPERTY<br><br>JOB_PROPERTY<br><br>PRINTER_PROPERTY<br><br>If DOC_PROPERTY or JOB_PROPERTY, the feature is assigned to the document property sheet. If PRINTER_PROPERTY, the feature is assigned to the printer property sheet. | Required for customized features. Optional for standard features. If not specified, the default value for standard features is DOC_PROPERTY unless otherwise noted.<br><br>If PRINTER_PROPERTY, the feature's option value is saved in the registry. If DOC_PROPERTY or JOB_PROPERTY, the feature's option value is saved with the document. |
| **\*HelpIndex** | Numeric value representing an index into the help file specified by the **\*HelpFile** [root-level-only attribute](root-level-only-attributes.md). | (Also an [option attribute](option-attributes.md).) |
| **\*Installable?** | **TRUE** or **FALSE**, indicating whether the feature is installable. (**FALSE** means always installed.)<br><br>For more information, see "[Handling Installable Features and Options](handling-installable-features-and-options.md). | Optional. If not specified, the default value is **FALSE**. If **TRUE**, all the feature's options are also installable, except for the first one specified. If **FALSE**, at least one of the feature's options must also always be installed. (Also an [option attribute](option-attributes.md).) |
| **\*InstallableFeatureName** | Text string that is displayed to ask the user whether an installable feature is actually installed.<br><br>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md). | Required if **\*Installable?** is **TRUE** and **\*rcInstallableFeatureNameID** is not specified. (Also an [option attribute](option-attributes.md).) |
| **\*Name** | Text string used as the feature's display name on the printer's property sheet. | Optional. If not specified, then **\*rcNameID** must be specified. (Also an [option attribute](option-attributes.md).) |
| **\*Option** | Option parameters, as described in [Option Entry Format](option-entry-format.md). | Required. Use an **\*Option** entry for each option associated with the feature. |
| **\*rcIconID** | Resource ID of an icon resource associated with the feature. | Optional. If not specified, Unidrv does not display an icon for the feature on the printer property sheet. (Also an [option attribute](option-attributes.md).) |
| **\*rcInstallableFeatureNameID** | Resource ID of a text string that is displayed to ask the user whether an installable feature is actually installed.<br><br>For more information, see [Handling Installable Features and Options](handling-installable-features-and-options.md). | Required if **\*Installable?** is **TRUE** and **\*InstallableFeatureName** is not specified. (Also an [option attribute](option-attributes.md).) |
| **\*rcNameID** | Resource ID of string resource representing the feature name. (Zero is not a valid resource ID.) | Optional. If not specified, then **\*Name** must be specified. (Also an [option attribute](option-attributes.md).) |
| **\*UpdateQualityMacro?** | **TRUE** or **FALSE**, indicating whether the feature is included in a conditional statement that specifies quality settings (see [Controlling Image Quality](controlling-image-quality.md)). | Optional. If not specified, the default value is **FALSE**. (The value is forced to **TRUE** if the feature is included in a conditional statement that specifies quality settings.) |

For examples, see the [sample GPD files](sample-gpd-files.md).
