---
title: Standard XPS Filters
description: Windows provides two (standard) XPS filters to support built-in conversion from XPS to PCL6 and PostScript level 3.
ms.assetid: 6404D215-8154-4604-A67B-19B20D1CF229
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standard XPS Filters


Windows provides two (standard) XPS filters to support built-in conversion from XPS to PCL6 and PostScript level 3.

The Windows-provided filters are available for both print class drivers and model-specific v4 print drivers. These XPS filters can be combined with IHV Feature Filters as well as IHV Post-processing filters, as needed in order to ensure compatibility with existing firmware implementations.

**Note**  These Windows-provided XPS filters are not re-distributable, and are not available to v3 print drivers.



## The Manifest file


To use the Windows-provided XPS filters, the v4 driver manifest file must use the RequiredFiles directive under the **DriverConfig** section to specify the filters. These are the names of the filters:

*MSxpsPCL6.dll*. Provides conversion from XPS to PCL6.
*MSxpsPS.dll*. Provides conversion from XPS to PostScript level 3.
No INF updates are required to utilize one of these filters, and redistribution is not supported.
## Print Filter Pipeline Configuration


To configure the print filter pipeline to use these filters, you must create configuration files as shown in the following examples.

Sample configuration file that specifies conversion to PCL6.

```xml
<?xml version="1.0" encoding="utf-8"?>
<Filters>
  <Filter dll="MSxpsPCL6.dll" clsid="{3821E518-33AF-4d17-92B3-28EB410D46B6}" name="Microsoft XPS to PCL6">
    <Input guid="{4d47a67c-66cc-4430-850e-daf466fe5bc4}" comment="IID_IPrintReadStream" />
    <Output guid="{65bb7f1b-371e-4571-8ac7-912f510c1a38}" comment="IID_IPrintWriteStream" />
  </Filter>  
</Filters>
```

Sample configuration file that specifies conversion to PostScript.

```xml
<?xml version="1.0" encoding="utf-8"?>
<Filters>
  <Filter dll="MSxpsPS.dll" clsid="{8636D90A-5E03-4d62-9269-E06493C57473}" name="Microsoft XPS to PS">
    <Input guid="{4d47a67c-66cc-4430-850e-daf466fe5bc4}" comment="IID_IPrintReadStream" />
    <Output guid="{65bb7f1b-371e-4571-8ac7-912f510c1a38}" comment="IID_IPrintWriteStream" />
  </Filter>  
</Filters>
```

## Supported Features


The standard XPS filters support many common features. All feature definitions use the GPD or PPD file for the driver. The *MSxpsPCL6.dll* filter requires the use of a GPD file for configuration, and the *MSxpsPS.dll* filter requires the use of a PPD file for configuration. Unless otherwise noted, if a custom PDL command is specified for a feature, it will be used.

If injection strings exist under any particular section (specified with the **\*Order** command), then in the case of GPD files, the filter will make a number of assumptions about the content of those strings, and will avoid sending default commands. This is because sending default commands in this case could cause command collisions. Therefore the creator of a GPD file must follow these guidelines:

-   JOB\_SETUP.\#
    o A PCL6 Binary Stream Header (for example: “)&lt;SP&gt;HP-PCL XL;1;&lt;CR&gt;&lt;LF&gt;”) must exist.
    o A BeginSession operator must exist, including all required attributes.
    o An OpenDataSource operator must exist, including all required attributes.
-   PAGE\_SETUP.\#
    o A BeginPage operator must exist, including all required attributes.
-   PAGE\_FINISH.\#
    o An EndPage operator must exist.
-   JOB\_FINISH.\#
    o A CloseDataSource operator must exist.
    o An EndSession operator must exist.
    o An EndPJLCommands operator must exist.

The XPS Standard Filters produce appropriate PDL data to set the origin of a page, based on the \*PrintableArea, \*PrintableOrigin or \*ImageableArea commands. And in order to avoid additional offset from the expected origin, GPD files should not specify any =SetPageOrigin commands in the \*Cmd string definition for their paper size.

For more information about the PrintTicket features supported by standard XPS filters, the see [Supported PrintTicket Features](supported-printticket-features.md).

## Retrieving PrintTicket in Post-processing Filters


In the v4 driver model that was released with Windows 8, when you added a post-processing filter after one of the MSxps filters, you sometimes also had to add a pre-processing filter. Adding the pre-processing filter was necessary to capture the job-level print ticket. But this approach essentially added an object model-based filter, before one of the stream-based MSxps filters, resulting in deserialization, and then serialization of the print data to simply extract a PrintTicket.

In Windows 8.1, the user default PrintTicket is merged with the Job-level PrintTicket in the MSxps filters, and the merged PrintTicket then is added to the Print Filter Pipeline’s property bag. The merged PrintTicket is added to Print Filter Pipeline’s property bag in the same manner as the User PrintTicket. The property is named as follows:

```cpp
#define XPS_FP_JOB_LEVEL_PRINTTICKET    "JobPrintTicket"
```

During InitializeFilter, the MTI Filters will add an implementation of [IPrintReadStreamFactory](https://msdn.microsoft.com/library/windows/hardware/ff554338) into the property bag. This interface’s one method, **GetStream**, will block until the PrintTicket stream is available. This provides a means of synchronizing access to the property.

**Important**  : If **GetStream** is called from InitializeFilter, it WILL cause a deadlock.



## Other Features


In the case of PrintTicket features that are not supported by the standard XPS filters, the filters will check all the PrintTicket members to see if they are referenced in the GPD/PPD, and then specify commands to be output. If so, the specified commands will be generated.

GPD features are mapped in the following order:

1. A PrintSchemaKeywordMap value is specified and matches the PrintTicket feature name.

2. The PrintSchemaPrivateNamespaceURI attribute is specified, and the GPD feature name matches the PrintTicket feature name. Matching feature names is not straightforward, and follows a number of rules:

a. If the **\*Order** section of the first option is PAGE\_SETUP or PAGE\_FINISH, and the GPD feature does not begin with “Page”, then “Page” is prepended to the GPD feature name before attempting to match.

b. If the **\*Order** section of the first option is DOC\_SETUP or DOC\_FINISH, and the GPD Feature does not begin with “Document”, then “Document” is prepended to the GPD feature name before attempting to match.

c. If the **\*Order** section of the first option is JOB\_SETUP or JOB\_FINISH, and the GPD Feature does not begin with “Job”, then “Job” is prepended to the GPD feature name before attempting to match.

d. Any character that is not \[A-Z\], \[a-z\], \[0-9\] or ‘\_’ is replaced with an ‘\_’ character before attempting to match. However, if the \*NoPunctuationCharSubstitute? attribute is set to TRUE, then the filter does not replace ‘.’ or ‘-‘ with an ‘\_’ character.

PPD Features are mapped in the following order:
1. A PrintSchemaKeywordMap value is specified and it matches the PrintTicket feature name.

2. The PrintSchemaPrivateNamespaceURI attribute is specified, and the PPD Feature name matches the PrintTicket feature name. Matching feature names is not straightforward, and follows a number of rules:

a. If the **OrderDependency** section is ExitServer, Prolog, or JCLSetup, and the PPD feature name does not begin with “Job”, then “Job” is prepended to the PPD feature name before attempting to match.

b. If the **OrderDependency** section is DocumentSetup, and the PPD feature name does not begin with “Document”, then “Document” is prepended to the PPD feature name before attempting to match.

c. If the **OrderDependency** section is AnySetup, then the filter performs two match checks:

i. If the PPD feature name does not begin with “Document”, then “Document” is prepended to the PPD feature name before attempting to match.

ii. If no match is found, or if the PPD feature name does not begin with “Job”, then “Job” is prepended to the PPD feature name before attempting to match.

d. If the **OrderDependency** section is PageSetup, and the PPD feature name does not begin with “Page”, then “Page” is prepended to the PPD feature name before attempting to match.

e. Any character that is not \[A-Z\], \[a-z\], \[0-9\] or ‘\_’ is replaced with an ‘\_’ character before attempting to match. However, if the \*MSNoPunctuationCharSubstitute? String is set to TRUE, the filter does not replace ‘.’ or ‘-‘ with an ‘\_’ character.

GPD and PPD Options are mapped in the following order:
1. A PrintSchemaKeywordMap value is specified and it matches the PrintTicket option name.

2. The PrintSchemaPrivateNamespaceURI attribute is specified, and the GPD/PPD option name matches the PrintTicket option name. Matching option names is not straightforward, and follows a number of rules:

a. If the GPD/PPD option name starts with \[0-9\] or ‘\_’, then an ‘\_’ character is prepended to the GPD/PPD option name before attempting to match. However, the following additional rules apply:

i. If this is a GPD option, and the \*NoPunctuationCharSubstitute? attribute is set to TRUE, then the filter does not prepend ‘\_’ with an ‘\_’ character.

ii. If this is a PPD option, and the \*MSNoPunctuationCharSubstitute? string is set to TRUE, then the filter does not prepend ‘\_’ with an ‘\_’ character.

b. Any character that is not \[A-Z\], \[a-z\], \[0-9\] or ‘\_‘ is replaced with an ‘\_‘ character before attempting to match. However, the following additional rules apply:

i. If this is a GPD option, and the \*NoPunctuationCharSubstitute? attribute is set to TRUE, then the filter does not replace ‘.’ or ‘-‘ with an ‘\_’ character.

ii. If this is a PPD option, and the \*MSNoPunctuationCharSubstitute? string is set to TRUE, then the filter does not replace ‘.’ or ‘-‘ with an ‘\_’ character.

## Form to Tray Mapping


The XPS to PCL6 and XPS to PS filters support the form-to-tray mapping table. If multiple trays support the selected media size (for example, letter), the filters break the tie as follows:

1. If the default tray (as specified in the GPD or PPD file) is configured to use the specified media size, then the default tray is used.

2. Otherwise, the filter chooses the first tray (top to bottom as they were specified in the GPD/PPD file) that is configured with the specified media size.

## Extra Backside Page suppression


By default, the XPS to PCL6 and XPS to PS filters handle duplex printing of documents that contain mixed media sizes, media types, input or output bins, by inserting an empty page. When the filters insert this empty page, it forces the device to print the next page on the front of a new piece of media. For devices that do not require a backside page to be output, this behavior can be suppressed by adding the following keywords to the driver’s GPD or PPD file.

| File type | Backside page suppression keyword    |
|-----------|--------------------------------------|
| GPD       | \*SuppressExtraBacksidePages?: TRUE  |
| PPD       | \*MSSuppressExtraBacksidePages: True |



## Optimizing SetPageDevice commands


The default behavior of a PostScript device that uses a driver with MSxpsPS.dll is that, a SetPageDevice command is issued for every page, and this command states the full set of options specified for the page. Note that some devices might not perform well with this technique.

However, if your device uses MSxpsPS.dll and the accompanying PPD file specifies **\*MSOptimizeSetPageDevice: True**, then the following is the PostScript device behavior: - For every page where there has been a change in any part of the SetPageDevice command since the previous page, a new SetPageDevice command is issued to indicate the set of options specified for the page. But if there has been no change in any part of the SetPageDevice command since the previous page, then a SetPageDevice command is not issued for the page.

## Related topics
[Supported PrintTicket Features](supported-printticket-features.md)  
[V4 Printer Driver Rendering](v4-driver-rendering.md)  



