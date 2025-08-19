---
title: MSIX Manifest Specification for Print Support Virtual Printer
description: Provides MSIX manifest guidance and examples for printer OEMs and IHVs that are implementing a Print Support Virtual Printer.
ms.date: 01/10/2025
ms.topic: concept-article
---

# MSIX Manifest Specification for Print Support Virtual Printer

This feature enables printing to a virtual printer without the need for legacy V3/V4 print drivers as Windows is planning to deprecate third-party V3/V4 print drivers. For more information, see [End of servicing plan for third-party printer drivers on Windows](../print/end-of-servicing-plan-for-third-party-printer-drivers-on-windows.md).

The Virtual Printer Architecture facilitates the implementation of software printers without third-party drivers. Through this architecture, ISVs (Independent Software Vendors) are able to implement a Software Printer as an application implementing the features currently supported by third-party V3/V4 drivers.

This article describes how an application can register itself as a Software Printer in the manifest.

For more information, see the following articles:

| Topic | Description |
|--|--|
| [Print Support App design guide](print-support-app-design-guide.md) | Provides guidance and examples for printer OEMs and IHVs that are implementing a print support app (PSA) for their device. |
| [Print Support App v3 API design guide](print-support-app-v3-design-guide.md) | Provides guidance and examples for printer OEMs and IHVs that are implementing a v3 Print Support App (PSA) for their device. |
| [Print Support App v4 API design guide](print-support-app-v4-design-guide.md) | Provides guidance and examples for printer OEMs and IHVs that are implementing a v4 Print Support App (PSA) for their device. |
| [Print support app association](print-support-app-association.md) | Provides guidance and examples for associating a print support app (PSA) with a printer. |

[Print Support App (PSA)](print-support-app-design-guide.md) is an architecture that was introduced to help IHVs add customization to IPP printers without the use of third-party drivers. To ease the transition to the Software Printer, all the APIs are part of the **PrintSupportApp** API namespace, and reuse some of the PSA contracts that are applicable to Virtual Printer Architecture.

The new manifest contract is similar to the **Windows.printSupportWorkflow** contract, but this contract needs more entries as it is used for installing a Virtual Printer.

The new Windows deployment extension handler (DEH) installs a virtual printer based on the manifest declaration and Windows Print Components invokes the app when user prints to the installed virtual printer.

## Manifest attributes

- **printSupport:Extension** - Extension entry for virtual printer

- **Category** - **Windows.printSupportVirtualPrinterWorkflow** new contract for app implementing Virtual Printer

- **PrintSupportVirtualPrinter** - Each entry specifies one Software Endpoint print queue to be installed along with the application. Each **PrintSupportVirtualPrinter** entry can have the following attributes:

  - **PreferredInputFormat** - This attribute indicates the preferred input PDL format for the Virtual Printer. Windows Print System generates this format before giving PDL data to the Virtual Printer for all printing paths. The field can only be one of the following values: application/oxps or application/postscript. Installation fails if other formats are specified in this field. If the field isn't specified, application/oxps is set as the preferred PDL format for the installed Virtual Printer.

  - **OutputFileTypes** - When this attribute is specified in the appx manifest, the Windows Print System creates a printer queue that is marked as a file printer and the Save As dialog is shown to the user when an application starts printing to the Virtual Printer. The values of this field should contain target file extensions such as pdf/pwgr/ps etc. These values are stored in driver data and is added to Save as Dialog as the allowed extensions. If a Virtual Printer doesn't want file print behavior (this includes Virtual Printers that store print data to the cloud or printers that send data to an application like OneNote), then this field shouldn't be added to the manifest.

  - **Supported Formats** - This element can be used Virtual Printer to specify all the PDL formats that it can process. This is used for passthrough printing applications like Microsoft Edge to identify the supported format like PDF and directly pass a PDF stream to the Virtual Printer without any changes being made in between by the Windows Print system. This field can have **SupportedFormat** as the child elements.

    - **SupportedFormat** - Element specifies a single passthrough PDL format and can have the following attributes.

      - **Type** - This attribute is used to specify the supported MIME type supported by Virtual Printer

      - **MaxVersion** - This attribute specifies the max version of that PDL format that Virtual Printer can receive. MaxVersion value must be in the format MajorVersion.MinorVersion. The Windows print system fails printer installation if it is in any other format. MajorVersion and MinorVersion can only be numbers. If any characters are present, the version field is invalidated and ignored.

- **PdcFile** - This attribute must point to a resource file within the application package. The file should contain contents in Print Device Capabilities XML format, which is to define printer capabilities and should be used to define any custom features/options or parameters. This is a mandatory field and printer installation fails if value isn't present or if the file contents aren't in valid PDC format.

- **PdrFile** - If provided, this attribute must point to a resource file within the application package. The file should contain Print Device Resources in an XML format. This field should be provided if the app wants to localize custom print preferences. This field is optional and resource localization for print preferences is handled by the print system if this field isn't present.

- **DisplayName** - Specifies the name of the Virtual Printer Queue which will be installed. Restrictions of this string are the same as restriction that you have for a windows printer name.

- **PrinterUri** - Specifies a unique URI that can be used by PSA applications to identify the printer. A single Virtual Printer app can specify multiple software endpoints which results in multiple printers to be installed.  The **PrinterUri** field can be used to differentiate between these printers. This URI output is given from [**IppPrintDevice::PrinterUri**](/uwp/api/windows.devices.printers.ippprintdevice.printeruri) API. If URI isn't specified, Windows assigns an arbitrary unique URI to the printer.

## Manifest sample

```xml
<Extensions> 
    <printsupport2:Extension Category="windows.printSupportVirtualPrinterWorkflow" EntryPoint="Tasks.PrintSupportWorkflowBackgroundTask">
        <PrintSupportVirtualPrinter DisplayName="ms-resource://PRINTER_NAME1" PrinterUri="contoso-psa:printer1" PreferredInputFormat="application/postscript" OutputFileTypes="ps;pdf" PdcFile="Config\PRINTER_PDC1.xml" PdrFile="Config\PRINTER_PDR1.xml">
            <SupportedFormats>
                <SupportedFormat Type="application/postscript" />
                <SupportedFormat Type="application/pdf" MaxVersion="1.7" />
            </SupportedFormats>
        </PrintSupportVirtualPrinter>
    </printsupport2:Extension>
    <printsupport2:Extension Category="windows.printSupportVirtualPrinterWorkflow" EntryPoint="Tasks.PrintSupportWorkflowBackgroundTask">
        <PrintSupportVirtualPrinter DisplayName="ms-resource://PRINTER_NAME2" PrinterUri ="contoso-psa:printer2" PreferredInputFormat="application/oxps" OutputFileTypes="pwgr;pdf" PdcFile="ms-appx:///PRINTER_PDC2.xml" PdrFile="ms-appx:///PRINTER_PDR2.xml">
            <SupportedFormats>
                <SupportedFormat Type="application/pdf" MaxVersion="1.7" />
            </SupportedFormats>
        </PrintSupportVirtualPrinter>
    </printsupport2:Extension>
    <printsupport:Extension Category="windows.printSupportExtension" EntryPoint="Tasks.PrintSupportExtensionBackGroundTask"/>
    <printsupport:Extension Category="windows.printSupportSettingsUI" EntryPoint="PrintSupportApp.App"/>
    <printsupport:Extension Category="windows.printSupportJobUI" EntryPoint="PrintSupportApp.App"/>
</Extensions>
```

## Related articles

[End of servicing plan for third-party printer drivers on Windows](../print/end-of-servicing-plan-for-third-party-printer-drivers-on-windows.md)

[**IppPrintDevice::PrinterUri**](/uwp/api/windows.devices.printers.ippprintdevice.printeruri)
