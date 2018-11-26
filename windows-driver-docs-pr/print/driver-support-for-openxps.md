---
title: Driver Support for OpenXPS
description: OpenXPS is the Open XML Paper Specification format for documents, and it’s based on the Ecma International standard specification.
ms.assetid: 9BC9787E-A54D-4A11-B256-57BE5D206404
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Support for OpenXPS


OpenXPS is the Open XML Paper Specification format for documents, and it’s based on the Ecma International standard specification.

For the most up to date information about this specification, see [Open XML Paper Specification](http://www.ecma-international.org/publications/standards/Ecma-388.htm).

Windows 8 provides full support for OpenXPS, side-by-side with continued support for the existing Microsoft XPS format. This topic focuses on support for OpenXPS via the v4 driver model. For OpenXPS support that is relevant to Windows application developers, see [App Support for OpenXPS Printing](https://msdn.microsoft.com/library/windows/desktop/dn495653.aspx).

## Supported OpenXPS Scenarios


The Windows print path has been developed to ensure that the submitted XPS format matches a supported format of the targeted print driver, and will convert formats as needed. Windows also provides APIs to query the print driver, so that the application can provide compatible elements and avoid any additional conversion within the print system.

A print driver can use its manifest to indicate whether it supports Microsoft XPS, Open XPS, or both formats. Either Microsoft XPS or OpenXPS can be presented to the filters in the print filter pipeline, using the existing stream and object model (OM) interfaces – no new interfaces are required by drivers to support OpenXPS. The format that is presented to the filters, depends on the format that is supported by the driver, or the format that is provided by the application.

The Microsoft XPS Document Writer (MXDW) has been updated to allow MXDW to output either Microsoft XPS or OpenXPS from any Windows desktop application. Likewise, the Microsoft XPS Viewer and the Reader app in Windows 8 can open both XPS formats. If needed, users can print from the XPS Viewer to MXDW in order to convert formats.

## Unsupported OpenXPS Scenarios


Some legacy functionality is either not supported, or provides a downgraded experience when used with OpenXPS.

*Unsupported*: Sending OpenXPS files directly to the spooler (bypassing the XPS Print API) is an unsupported scenario. Doing this, will produce the following functionality issues:

-   XPS spool files sent directly to the spooler will be treated as MSXPS and handled accordingly.
-   The results of sending an OpenXPS file directly to the spooler are undefined and will likely cause the print job to fail.

**Note**  There are no plans to provide support for this scenario.

 

*Not recommended*: Sending an OpenXPS stream from an application directly to the XPS Print API is not a recommended technique. For example, do not send an OpenXPS stream directly to the StartXPSPrintJob method. If you do this, the resulting conversion from one flavor of XPS to another as a stream can be very expensive for performance.

Instead, you should use IPrintDocumentPackageTarget to submit the print job as an XPS OM to avoid performance degradation.

*Not recommended*: Sending an XPS spool file directly to the spooler. If you do this, the print system will not find the required metadata added by the print path APIs, assume that the format is MSXPS, and will attempt to convert it to OpenXPS. If the spool file that was sent directly to the spooler was an OpenXPS-formatted file, the attempt by the print filter pipeline to ‘convert’ it to OpenXPS will have undefined results. If the file that was sent to the spooler was an MSXPS-formatted file and the driver is an OpenXPS-only driver, then the conversion by the print filter pipeline to OpenXPS will be successful. But this late stage conversion will result in a significant loss in print system performance.

## Impact on App Developers


For information about the impact on app developers regarding the Windows 8 support for OpenXPS, see [App Support for OpenXPS Printing](https://msdn.microsoft.com/library/windows/desktop/dn495653.aspx).

## Impact on Driver Developers


The following are the basic steps for enabling OpenXPS in a v4 print driver:

-   Driver manifest: Add “OpenXPS” to the Driver Render section.
-   Driver manifest: Add “oxps” to the FileSave section, if applicable.
-   Filter pipeline: Update print filters to handle OpenXPS elements.

For a given stream, and with the appropriate object interfaces, a client can use the OpenXPS format to transfer data to the filters in the print filter pipeline. To transfer a data stream, the client uses the IID\_IPrintReadStream and IID\_IPrintWriteStream interfaces. To transfer data to an OM component, the client uses the IID\_IXpsDocumentProvider and IID\_IXpsDocumentConsumer interfaces. Drivers that declare support for OpenXPS will have to ensure that the print filters provided can correctly handle the OpenXPS format when this format is received from the pipeline manager.

**Driver Manifest: DriverRender section**. During driver installation, the setup process checks the DriverRender section of the manifest to see if the XpsFormat entry includes OpenXPS. The XpsFormat entry can include both XPS (for Microsoft XPS) and OpenXPS, to indicate dual support. The order in which the two formats are listed in the XpsFormat entry determines the preferred format for the driver.

Here are some examples of how to update the DriverRender section.

Indicating support for OpenXPS only:

```Manifest
[DriverRender]
XpsFormat = OpenXPS
```

Indicating support for MSXPS only:

```Manifest
[DriverRender]
XpsFormat = XPS
```

Indicating support for both formats, with a preference for OpenXPS:

```Manifest
[DriverRender]
XpsFormat = OpenXPS,XPS
```

Indicating support for both formats, with a preference for MSXPS:

```Manifest
[DriverRender]
XpsFormat = XPS,OpenXPS
```

The driver developer determines the preferred format for their V4 print driver, and this decision is based on the functionality that the driver was designed to provide. For example, a print driver could be developed to provide JPEG XR support for high-fidelity images.

The print system makes various decisions based on the DriverRender information in the manifest. Here are some examples of those decisions:

-   GDI-based print jobs sent to v4 drivers

    The Microsoft XPS Document Converter (MXDC) takes GDI print job input and converts the job to an XPS spool file. The format of that spool file will match the preferred XPS format denoted in the DriverRender section of the manifest.

-   XPS Print API format conversion

    The XPS Print API will query supported XPS formats for the target driver. If the driver supports both formats, the XPS Print API will pass the XPS Print Job to the spooler AS SUBMITTED by the application. No conversion will be performed.

    If the target driver only supports one or the other format, then the job will be converted to the correct format before spooling.

    If no XpsFormat is provided in the manifest, the behavior will default to MSXPS only. OpenXPS input will be converted to MSXPS. This behavior provides the strongest backward compatibility for drivers.

-   XPS files sent directly to spooler

    XPS files sent directly to the spooler are, by default, MSXPS. Submitting OpenXPS direct to the spooler is not supported. However, .NET prior to 4.5+ serialized its own MSXPS and submitted the job directly to the spooler. This behavior was implemented prior to the introduction of the XPS Print API (xpsprint.dll).

    To provide backward compatibility for these .NET applications, the print filter pipeline manager will check the spool file to determine if it was received direct-to-spooler. If so, it will be assumed to be MSXPS. The print filter pipeline manager will query the driver’s XPS formats at that point. If the driver supports MSXPS, no conversion will be performed. If the driver only supports OpenXPS, the print filter pipeline manager will perform a conversion of the file. Conversion at this point in the job is performance expensive; however, it ensures that legacy .NET apps will be able to print to new v4 OpenXPS drivers.

**Driver Manifest: FileSave section**. The FileSave section of the v4 print driver manifest provides extensions for the **File Save** dialog used by the PORTPROMPT: port. (PORTPROMPT: should be used in lieu of FILE: in Windows 8.1, because PORTPROMPT: will allow users to access all file locations to which they have rights, even when the application is running in low-rights mode.) The entries in the FileSave section are associated with the entries in the DriverRender section by index.

Example:

```Manifest
[FileSave]
xps=0
oxps=0

[DriverRender]
XpsFormat=XPS,OpenXPS
```

This will ensure that when the user sends a print job to this driver, and the port is set to PORTPROMPT:, the **File Save** dialog will display XPS and OpenXPS as file type options in the dialog, and apply .xps or .oxps respectively, as the file extension.

For additional information about other options for the File Save section of the manifest, see [V4 Driver Manifest](v4-driver-manifest.md).

## Related topics

[App Support for OpenXPS Printing](https://docs.microsoft.com/windows/desktop/printdocs/app-support-for-openxps-printing)  

[Open XML Paper Specification](http://www.ecma-international.org/publications/standards/Ecma-388.htm) 

[V4 Driver Manifest](v4-driver-manifest.md)  
