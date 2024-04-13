---
title: Driver Support for Protected Printing
description: Windows 8.1 includes support for protected printing, which allows users to specify a personal identification number (PIN) that is then used at the printer, prior to the job being printed out.
ms.date: 06/22/2023
---

# Driver Support for Protected Printing

[!include[Print Support Apps](../includes/print-support-apps.md)]

Windows 8.1 includes support for protected printing, which allows users to specify a personal identification number (PIN) that is then used at the printer, prior to the job being printed out.

Windows 8.1 also allows administrators to specify a default PIN in order to reduce wasteful paper consumption related to content that is printed out but never retrieved by the user. This topic explains the changes that made it possible to provide support for protected printing and also outlines the steps required for adding this support to a v4 print driver.

## Print Schema Changes

Windows 8.1 has introduced new Print Schema keywords that you can use in PrintTicket and PrintCapabilities documents to specify protected printing. These keywords are defined in the new *printschemakeywordsv11* namespace. Here is the URI for this namespace:

```xml
https://schemas.microsoft.com/windows/2013/05/printing/printschemakeywordsv11
```

To see how to specify protected printing in a PrintTicket file, see [Sample PrintTicket File for PIN Printing](sample-printticket-file-for-pin-printing.md). And to see how to specify protected printing in a PrintCapabilities file, see [Sample PrintCapabilities File for PIN Printing](sample-printcapabilities-file-for-pin-printing.md).

The specifications can be downloaded here:

[Print Schema Specification 1.1](https://download.microsoft.com/download/1/6/a/16acc601-1b7a-42ad-8d4e-4f0aa156ec3e/print-schema-spec-1-1.zip)

[Print Schema Specification 2.0](https://download.microsoft.com/download/d/e/c/deca6e6b-3e81-48e7-b7ef-6d92a547d03c/print-schema-spec-2-0.zip)

## Driver Changes

If you're working with a v4 driver, you have to make changes to the generic printer description (GPD) or PostScript printer description (PPD) file, and other driver-related code files. The driver-related code files affected by the changes can be categorized as follows:

- Driver configuration file (GPD or PPD)
- XPS rendering filters
- Printer extensions
- UWP device apps

ou can use a v3 driver with the Print Schema keywords for protected printing, as long as you make the required changes in your PTProvider code. But the steps for making those changes are outside the scope of this topic.

The following sections give you more information about how to implement changes that will allow your v4 driver to support protected printing.

### Driver Configuration File

You indicate support for protected printing in the DataFile for your v4 print driver. The DataFile is either the GPD or the PPD file - whichever one your driver uses. You must specify both the MinLength and MaxLength directives to enable protected printing. The following tables describe the relevant keywords that you must add to your driver's GPD or PPD file.

### What to add to a GPD file

If your driver uses a GPD file, add the following new keywords using this syntax:

| Keyword | Description | Level | Allowed value | Example |
|--|--|--|--|--|
| **\*JobPasscodeMinLength** | Minimum length of the supported PIN numeric string.<br><br>This value must be at least 4 and no greater than 15. | Root | Any [GPD numeric value](numeric-values.md) | \*JobPasscodeMinLength: 4 |
| **\*JobPasscodeMaxLength** | Maximum length of the supported PIN numeric string.<br><br>This value must be at least 4 and no greater than 15. It must be greater than or equal to the **\*JobPasscodeMinLength** value. | Root | Any [GPD numeric value](numeric-values.md) | \*JobPasscodeMaxLength: 9 |

## What to add to a PPD file

If your driver uses a PPD file, add the following new keywords using this syntax:

| Keyword | Description | Level | Allowed value | Example |
|--|--|--|--|--|
| **MSJobPasscodeMinLength** | Minimum length of the supported PIN numeric string.<br><br>This value must be at least 4 and no greater than 15. | Root | "int" (QuotedValue)<br><br>In other words, the integer value must be expressed in quotation marks. | \*MSJobPasscodeMinLength: "4" |
| **MSJobPasscodeMaxLength** | Maximum length of the supported PIN numeric string.<br><br>This value must be at least 4 and no greater than 15. It must be greater than or equal to the **\*MSJobPasscodeMinLength** value. | Root | "int" (QuotedValue)<br><br>In other words, the integer value must be expressed in quotation marks. | \*MSJobPasscodeMaxLength: "9" |

### Specifying hardware constraints

If you have a device that doesn't support PIN printing without installable hardware such as a hard drive, specify these constraints using either the GPD or PPD file. To do this, you must edit your GPD or PPD file to show the JobPasscode feature and both JobPasscode options (On and Off). The ON/OFF options must set either PrintSchemaKeywordMap or MSPrintSchemaKeywordMap to the appropriate values.

### Software constraints

These are not supported.

### Hardware constraints

The following table shows the valid values for the keywords that you must use if you want to specify support for protected printing and hardware constraints.

File type
Keyword
Valid values
GPD
\*Feature
JobPasscode
\*Option
- OFF
- ON

\*PrintSchemaKeywordMap
- "Off"
- "On"
- "JobPasscode"

PPD
\*Feature
JobPasscode
\*Option
- OFF
- ON

\*MSPrintSchemaKeywordMap
- "Off"
- "On"
- "JobPasscode"

### GPD and PPD file examples

Here is an example of a GPD file specifying JobPasscode with an Installable Hardware Constraint.

```GDP
*%
*GPDSpecVersion: "1.0"
*GPDFileVersion: "1.0"

*Include:        "StdNames.gpd"
*Include:        "MSxpsinc.gpd"
*ResourceDLL:    "unires.dll"

*GPDFileName:    "FAsmpl.gpd"
*ModelName:      "Fabrikam JobPasscode Sample"
*MasterUnits:    PAIR(1200, 1200)
*PrinterType:    PAGE
*MaxCopies:      999

*JobPasscodeMinLength: 4
*JobPasscodeMaxLength: 15

*%******************************************************************************
*%                             JobPasscode
*%******************************************************************************
*Feature: JobPasscode
{
    *Name: "Job Passcode"
    *DefaultOption: OFF
    *ConcealFromUI: TRUE
    *PrintSchemaKeywordMap: "JobPasscode"

    *Option: OFF
    {
     *PrintSchemaKeywordMap: "Off"
        *Name: "Off"
    }

    *Option: ON
    {
     *PrintSchemaKeywordMap: "On"
        *Name: "On"
    }
}

*Feature:PrinterHardDisk
{
    *rcNameID: RESDLL.PCL5ERES.430
    *FeatureType: PRINTER_PROPERTY
    *DefaultOption: FALSE
    *Option: FALSE
    {
     *DisabledFeatures: LIST(JobPasscode)
        *rcNameID: RESDLL.PCL5ERES.444
    }
    *Option: TRUE
    {
        *rcNameID: RESDLL.PCL5ERES.443
    }
}
```

You must use the \*ConcealFromUI keyword and set it to TRUE to prevent the protected printing option from being shown unintentionally. See the preceding GPD file example.

Here's an example of a PPD file specifying JobPasscode with an Installable Hardware Constraint.

```PPD
*MSJobPasscodeMinLength: "4"
*MSJobPasscodeMaxLength: "15"

*OpenGroup: InstallableOptions/Installable Options

*% ===== Optional Hard Disk =====
*OpenUI *HardDisk/Printer Hard Disk: Boolean
*DefaultHardDisk:  False
*HardDisk False/Not Installed: ""
*HardDisk True/Installed: ""
*CloseUI: *HardDisk

*CloseGroup: InstallableOptions

*% ===== JobPasscode Feature =====
*OpenUI *JobPasscode: PickOne
*DefaultJobPasscode: On
*JobPasscode On: ""
*CloseUI: *JobPasscode

*MSPrintSchemaKeywordMap: JobPasscode  *JobPasscode
*MSPrintSchemaKeywordMap: JobPasscode  On *JobPasscode On

*UIConstraints: *HardDisk False *JobPasscode
```

As you can see in the preceding PPD file example, the \*UIConstraints keyword indicates the hardware constraint.

The Windows operating system automatically displays locale-specific strings for the protected printing feature and its associated options. You can't specify a new localized name for this feature or its options.

### XPS rendering filters

Drivers for existing devices will need changes to their rendering code so that these drivers can convert the PrintTicket representation of the PIN value into a value that the device understands. In general, this will either require the addition of code to an existing XPS rendering filter, or the addition of a new XPS rendering filter to support protected printing. Drivers that use the standard XPS rendering filters for PCL6 and PostScript should develop a new stream filter for their filter pipeline. This new stream filter will inject an appropriate command into the pre-rendered PDL stream in their filter pipeline, after the stream passes through the standard filter.

Microsoft recommends that to minimize the rendering requirements on the client or server PC, any new devices that support XPS or OpenXPS should support the new keywords without using additional transforms.

### Printer extensions

Printer extensions should be able to display a control for protected printing in their print preferences UI. This ensures that users of desktop apps can configure the protected printing feature when using the printer extension. Microsoft is making changes that will allow the [**IPrintSchemaTicket**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschematicket) family of APIs to support protected printing from printer extensions.

### UWP device apps

Microsoft is also making changes to allow the [**IPrintSchemaTicket**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschematicket) family of APIs to work with UWP device apps to display a control for protected printing in their print preferences UI.
