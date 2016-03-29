---
title: XPSDrv Printer Drivers
description: XPSDrv Printer Drivers
ms.assetid: 9e61cb21-4e02-48dc-b291-576d37bb640d
keywords: ["XPSDrv printer drivers WDK , about XPS", "printer drivers WDK , XPSDrv", "XML Paper Specification WDK print", "XPS Documents WDK XPSDrv", "XPS spool files WDK XPSDrv", "spool files WDK print"]
---

# XPSDrv Printer Drivers


The XPSDrv printer driver extends Microsoft's GDI-based, version 3 printer driver architecture to support consuming XML Paper Specification (XPS) documents. With an XPSDrv printer driver, the XPS Document format is used as a spool file format and as a document file format.

### Overview of XPS

The XML Paper Specification (XPS) is the foundation for document and printing improvements in Windows Vista. This specification describes the appearance of fixed-format documents by using a structured, XML-based document format.

The XPS Document format consists of XML markup that defines the layout of a document and the visual appearance of each page along with rendering rules for displaying or printing the document.

### Introduction to XPS for Printing

The XPS Document format serves as a document format, a spool file format, and a page description language (PDL) for printers. If you consistently use XPS throughout a document cycle, you can greatly improve print predictability and reliability. Fidelity and performance improve when the document format is the same as the spool file format and the PDL. By using the XPS Document format throughout the print processing, you can eliminate the need for any document format conversions between an application and the printer, so you can deliver a "what you see is what you get" (WYSIWYG) experience.

The XPS spool file uses the XPS Document format. The XPS spool file is open and extensible, can be viewed by using platform services, and can be reintroduced into document workflows.

The markup in the XPS spool file to describe XPS Documents is compatible with the Extensible Application Markup Language (XAML) markup in Windows Presentation Foundation (WPF). Therefore, documents that are described in the XPS spool file can be rendered natively in WPF without data or fidelity loss because no conversion is necessary. The XAML tags in the XPS spool file are XAML representations for existing rendering classes in WPF. The XPS Document format is identical to the "print" format and effectively preserves application content and user intent.

This section includes:

[XPS Printing Features](xps-printing-features.md)

[Windows Vista Print Path Overview](windows-print-path-overview.md)

[XPS Support in Earlier Versions of Windows](xps-support-in-earlier-versions-of-windows.md)

For more detailed information about XPS printing for printer driver developers, see [XPSDrv Printer Driver](xpsdrv-printer-driver.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPSDrv%20Printer%20Drivers%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




