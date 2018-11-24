---
title: XPSDrv Printer Drivers
description: XPSDrv Printer Drivers
ms.assetid: 9e61cb21-4e02-48dc-b291-576d37bb640d
keywords:
- XPSDrv printer drivers WDK , about XPS
- printer drivers WDK , XPSDrv
- XML Paper Specification WDK print
- XPS Documents WDK XPSDrv
- XPS spool files WDK XPSDrv
- spool files WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
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

[Windows Print Path Overview](windows-print-path-overview.md)

[XPS Support in Earlier Versions of Windows](xps-support-in-earlier-versions-of-windows.md)

For more detailed information about XPS printing for printer driver developers, see [XPSDrv Printer Driver](xpsdrv-printer-driver.md).
