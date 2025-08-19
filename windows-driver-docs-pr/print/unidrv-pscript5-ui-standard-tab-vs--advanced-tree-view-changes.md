---
title: Unidrv/PScript5 UI Standard Tab vs. Advanced Tree View Changes
description: Unidrv/PScript5 UI Standard Tab vs Advanced Tree View Changes
ms.date: 06/11/2024
ms.topic: concept-article
---

# Unidrv/PScript5 UI Standard Tab vs. Advanced Tree View Changes

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following public Print Schema features use the UniDrive/PScript5 user interface (UI):

JobPageOrder

PageOrientation (PS only)

PageDeviceFontSubstitution

PageOutputQuality

JobNUpAllDocumentsContiguously or DocumentNUp

If there are custom GPD or PPD features or options that are mapped to the preceding Print Schema features and their standard Print Schema options by using GPD's **PrintSchemaKeywordMap** keyword or PPD's **MSPrintSchemaKeywordMap** keyword, the Unidrv/PScript5 driver UI shows the features in the standard tabs in the same way that they appear for Unidrv or PScript5 drivers that are running in non-XPSDrv mode, unless the feature in the GPD file has "\*ConcealFromUI?" set to "TRUE".

When these Print Schema features (which are mapped from GPD or PPD custom features) are shown in Unidrv/Pscript5 driver UI standard tabs rather than in the generic "Printer Features" group in the **Advanced** tree view UI, the standard display names and icons for COMPSTUI are displayed. Any display name or icon that is specified in the GPD or PPD files for these features are ignored.

To present a consistent Unidrv/PScript5 driver UI for these standard printing features, the Unidrv/PScript5 driver that is running in XPSDrv mode has the following behavior.

| Print Schema mapped feature | XPSDrv Behavior |
|--|--|
| JobPageOrder | If the GPD or PPD file defines a feature with the "JobPageOrder" Print Schema keyword. And the feature has exactly two options with the "Standard" and "Reverse" Print Schema keywords, the feature is shown in the Page Order area in the standard Layout tab. Otherwise, the GPD or PPD feature is shown in the generic "Printer Features" group in the Advanced tree view UI.<br><br>When the feature is shown in the Page Order area in the standard Layout tab, then the following scenario is true:<br><br>If the driver's GPD file doesn't specify "OutputOrderReversed?: TRUE" or its PPD file doesn't specify "DefaultOutputOrder: Reverse", then the GPD/PPD "Standard" option is shown as the Front to Back UI option, and the GPD/PPD "Reverse" option is shown as the Back to Front UI option.<br><br>If the driver's GPD file does specify "OutputOrderReversed?: TRUE" or its PPD file does specify "DefaultOutputOrder: Reverse", then the GPD/PPD "Standard" option is shown as the Back to Front UI option, and the GPD/PPD "Reverse" option is shown as the Front to Back UI option.<br><br>The following screenshot shows the Page Order area on the Printing Preferences dialog box.<br><br>![page order area on the printing preferences dialog box](images/xpsdrv-printingpreferences1.png) |
| PageOrientation<br>(PS only) | If PPD defines a feature with the "PageOrientation" Print Schema keyword and the feature has either exactly three options with the "Portrait", "Landscape", and "ReversePortrait" Print Schema keywords or exactly two options with the "Portrait" and "Landscape" Print Schema keywords, that feature is shown in the Orientation area in the standard Layout tab.<br><br>Otherwise, the PPD feature is shown in the generic "Printer Features" group in the Advanced tree view UI.<br><br>The following screenshot shows the Orientation area on the Printing Preferences dialog box.<br><br>![orientation area on the printing preferences dialog box](images/xpsdrv-printingpreferences2.png)<br><br>The following screenshot illustrates the Orientation area (without the Rotated Landscape option) on the Printing Preferences dialog box.<br><br>![orientation area without the rotated landscape option on the printing preferences dialog box](images/xpsdrv-printingpreferences3.png) |
| PageDeviceFont-Substitution | If GPD or PPD defines a feature with the "PageDeviceFontSubstitution" Print Schema keyword and the feature has exactly two options with the "On" and "Off" Print Schema keywords that feature is shown in the TrueType Font list in the Advanced tab's "Graphic" group. The "On" option is shown as Substitute with Device Font, and the "Off" option is shown as Download as Softfont.<br><br>Otherwise, the GPD or PPD feature is shown in the generic "Printer Features" group in the Advanced tree view UI.<br><br>The following screenshot of the Advanced Options dialog box shows the Substitute with Device font option selected.<br><br>![advanced options dialog box with substitute with device font selected](images/xpsdrv-printingpreferences4.png) |
| PageOutput-Quality | If GPD or PPD defines a feature with the "PageOutputQuality" Print Schema keyword and the feature has exactly three options with the "Draft", "Normal", and "High" Print Schema keywords, that feature is shown in the Quality Settings area in the standard Paper/Quality tab. The "Draft" option is shown as the Draft option, the "Normal" option is shown as the Better option, and the "High" option is shown as the Best option.<br><br>Otherwise, the GPD or PPD feature is shown in the generic "Printer Features" group in the Advanced tree view UI.<br><br>The following screenshot of the Printing Preferences dialog box illustrates the Quality Settings area.<br><br>![quality settings area on the printing preferences dialog box](images/xpsdrv-printingpreferences5.png) |
| JobNUpAllDocumentsContiguously or DocumentNUp | If GPD or PPD defines a feature with the "JobNUpAllDocumentsContiguously" or "DocumentNUp" Print Schema keyword (the "DocumentNUp" feature is used only if no "JobNUpAllDocumentsContiguously" feature exists) and the feature has exactly six options whose GPD or PPD keyword names are numeric strings (that is, "1", "2", "4", "6", "9", and "16"), the feature is shown in the Pages Per Sheet list in the standard Layout tab.<br><br>Otherwise, the GPD or PPD feature is shown in the generic "Printer Features" group in the Advanced tree view UI.<br><br>![pages per sheet option on the printing preferences dialog box](images/xpsdrv-printingpreferences6.png) |

For any other custom GPD or PPD features, no matter if they're mapped to public Print Schema features or not, they show in the generic "Printer Features" group in the **Advanced tree view** UI.
