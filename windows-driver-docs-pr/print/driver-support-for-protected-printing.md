---
title: Driver Support for Protected Printing
author: windows-driver-content
description: Windows 8.1 includes support for protected printing, which allows users to specify a personal identification number (PIN) that is then used at the printer, prior to the job being printed out.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 43569030-224F-46C6-963F-FC3BE24A0FB3
---

# Driver Support for Protected Printing


Windows 8.1 includes support for protected printing, which allows users to specify a personal identification number (PIN) that is then used at the printer, prior to the job being printed out.

Windows 8.1 also allows administrators to specify a default PIN in order to reduce wasteful paper consumption related to content that is printed out but never retrieved by the user. This topic explains the changes that made it possible to provide support for protected printing and also outlines the steps required for adding this support to a v4 print driver.

## Print Schema Changes


Windows 8.1 has introduced new Print Schema keywords that you can use in PrintTicket and PrintCapabilities documents to specify protected printing. These keywords are defined in the new *printschemakeywordsv11* namespace. Here's the URI for this namespace:

*http://schemas.microsoft.com/windows/2013/05/printing/printschemakeywordsv11*

To see how to specify protected printing in a PrintTicket file, see [Sample PrintTicket File for PIN Printing](sample-printticket-file-for-pin-printing.md). And to see how to specify protected printing in a PrintCapabilities file, see [Sample PrintCapabilities File for PIN Printing](sample-printcapabilities-file-for-pin-printing.md).

Print Schema Specification v1.1 will be available in the near future. There is no date yet for its release.

## Driver Changes


If you're working with a v4 driver, you have to make changes to the generic printer description (GPD) or PostScript printer description (PPD) file, and other driver-related code files. The driver-related code files affected by the changes can be categorized as follows:

-   Driver configuration file (GPD or PPD)
-   XPS rendering filters
-   Printer extensions
-   Windows Store device apps

**Note**  You can use a v3 driver with the Print Schema keywords for protected printing, as long as you make the required changes in your PTProvider code. But the steps for making those changes are outside the scope of this topic.

 

The following sections give you more information about how to implement changes that will allow your v4 driver to support protected printing.

**Driver Configuration File**

You indicate support for protected printing in the DataFile for your v4 print driver. The DataFile is either the GPD or the PPD file - whichever one your driver uses. You must specify both the MinLength and MaxLength directives to enable protected printing. The following tables describe the relevant keywords that you must add to your driver's GPD or PPD file.

**What to add to a GPD file**. If your driver uses a GPD file, add the following new keywords using this syntax:

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyword</th>
<th>Description</th>
<th>Level</th>
<th>Allowed value</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>*JobPasscodeMinLength</strong></td>
<td><p>Minimum length of the supported PIN numeric string.</p>
<p>This value must be at least 4 and no greater than 15.</p></td>
<td>Root</td>
<td>Any [GPD numeric value](numeric-values.md)</td>
<td>*JobPasscodeMinLength: 4</td>
</tr>
<tr class="even">
<td><strong>*JobPasscodeMaxLength</strong></td>
<td><p>Maximum length of the supported PIN numeric string.</p>
<p>This value must be at least 4 and no greater than 15. It must be greater than or equal to the <strong>*JobPasscodeMinLength</strong> value.</p></td>
<td>Root</td>
<td>Any [GPD numeric value](numeric-values.md)</td>
<td>*JobPasscodeMaxLength: 9</td>
</tr>
</tbody>
</table>

 

**What to add to a PPD file**. If your driver uses a PPD file, add the following new keywords using this syntax:

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyword</th>
<th>Description</th>
<th>Level</th>
<th>Allowed value</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>*MSJobPasscodeMinLength</strong></td>
<td><p>Minimum length of the supported PIN numeric string.</p>
<p>This value must be at least 4 and no greater than 15.</p></td>
<td>Root</td>
<td><p>”int” (QuotedValue)</p>
<p>In other words, the integer value must be expressed in quotation marks.</p></td>
<td>*MSJobPasscodeMinLength: ”4”</td>
</tr>
<tr class="even">
<td><strong>*MSJobPasscodeMaxLength</strong></td>
<td><p>Maximum length of the supported PIN numeric string.</p>
<p>This value must be at least 4 and no greater than 15. It must be greater than or equal to the <strong>*MSJobPasscodeMinLength</strong> value.</p></td>
<td>Root</td>
<td><p>”int” (QuotedValue)</p>
<p>In other words, the integer value must be expressed in quotation marks.</p></td>
<td>*MSJobPasscodeMaxLength: ”9”</td>
</tr>
</tbody>
</table>

 

**Specifying hardware constraints**. If you have a device that doesn't support PIN printing without installable hardware such as a hard drive, specify these constraints using either the GPD or PPD file. To do this, you must edit your GPD or PPD file to show the JobPasscode feature and both JobPasscode options (On and Off). The ON/OFF options must set either PrintSchemaKeywordMap or MSPrintSchemaKeywordMap to the appropriate values.

**Software constraints**. These are not supported.

The following table shows the valid values for the keywords that you must use if you want to specify support for protected printing and hardware constraints.

File type
Keyword
Valid values
GPD
\*Feature
JobPasscode
\*Option
-   OFF
-   ON

\*PrintSchemaKeywordMap
-   "Off"
-   "On"
-   "JobPasscode"

PPD
\*Feature
JobPasscode
\*Option
-   OFF
-   ON

\*MSPrintSchemaKeywordMap
-   "Off"
-   "On"
-   "JobPasscode"

 

**GPD and PPD file examples**

Here's an example of a GPD file specifying JobPasscode with an Installable Hardware Constraint.

```Text
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
    *Name: ”Job Passcode”
    *DefaultOption: OFF
    *ConcealFromUI: TRUE
    *PrintSchemaKeywordMap: “JobPasscode”

    *Option: OFF
    {
     *PrintSchemaKeywordMap: “Off”
        *Name: ”Off”
    }

    *Option: ON
    {
     *PrintSchemaKeywordMap: “On”
        *Name: ”On”
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

**Note**  You must use the \*ConcealFromUI keyword and set it to TRUE to prevent the protected printing option from being shown unintentionally. See the preceding GPD file example.

 

Here's an example of a PPD file specifying JobPasscode with an Installable Hardware Constraint.

```Text
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

**Note**  The Windows operating system automatically displays locale-specific strings for the protected printing feature and its associated options. You can't specify a new localized name for this feature or its options.

 

**XPS rendering filters**

Drivers for existing devices will need changes to their rendering code so that these drivers can convert the PrintTicket representation of the PIN value into a value that the device understands. In general, this will either require the addition of code to an existing XPS rendering filter, or the addition of a new XPS rendering filter to support protected printing. Drivers that use the standard XPS rendering filters for PCL6 and PostScript should develop a new stream filter for their filter pipeline. This new stream filter will inject an appropriate command into the pre-rendered PDL stream in their filter pipeline, after the stream passes through the standard filter.

The Microsoft recommendation is that, to minimize the rendering requirements on the client or server PC, any new devices that support XPS or OpenXPS should support the new keywords without using additional transforms.

**Printer extensions**

Printer extensions should be able to display a control for protected printing in their print preferences UI. This ensures that users of desktop apps can configure the protected printing feature when using the printer extension. Microsoft is making changes that will allow the [**IPrintSchemaTicket**](https://msdn.microsoft.com/library/windows/hardware/hh451398) family of APIs to support protected printing from printer extensions.

**Windows Store device apps**

Microsoft is also making changes to allow the [**IPrintSchemaTicket**](https://msdn.microsoft.com/library/windows/hardware/hh451398) family of APIs to work with Windows Store device apps to display a control for protected printing in their print preferences UI.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Driver%20Support%20for%20Protected%20Printing%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


