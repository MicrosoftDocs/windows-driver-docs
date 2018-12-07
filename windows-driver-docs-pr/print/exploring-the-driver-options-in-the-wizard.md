---
title: Exploring the Driver Options in the Wizard
description: This topic explores the driver options in the first section of the Create a v4 Print Driver wizard.
ms.assetid: 48FF0A37-BBAF-49D1-9BDE-128AED00BEEF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Exploring the Driver Options in the Wizard


This topic explores the driver options in the first section of the Create a v4 Print Driver wizard.

The information is provided here in summarized form, to help you quickly find out about the various feature options. If you want more information about any feature, follow the provided links to related topics that provide more details.

## Driver rendering type


V4 print driver with custom rendering filters (accepts XPS only)

Choose this option, if you want to create a printer driver that only accepts the Microsoft XPS format as input. Note that this driver can produce output in XPS and/or OpenXPS format, depending on the choice that you make in the **Choose the driver XPS format** field.
V4 print driver with class driver rendering

When you choose this option, you create a printer driver that can accept input in either XPS or OpenXPS format. Additionally, when you choose this driver, you have to indicate on the next page of this Wizard the name of the print class driver that you would like to use for rendering.
Microsoft XPS to PCL6 render filter (accepts XPS only)

This option allows you to create a filter driver module that only accepts XPS format as input, and converts the input to PCL6. Note that this driver can produce output in XPS and/or OpenXPS format, depending on the choice that you make in the **Choose the driver XPS format** field.
Microsoft XPS to PostScript render filter (accepts XPS only)

This option allows you to create a filter driver module that only accepts XPS format as input, and converts the input to PostScript. Note that this driver can produce output in XPS and/or OpenXPS format, depending on the choice that you make in the **Choose the driver XPS format** field.
## Driver XPS format


XPS

This option configures the driver to produce output in XPS format only.
OpenXPS

This option configures the driver to produce output in OpenXPS format only.
XPS, OpenXPS

This option configures the driver to produce output in either XPS or OpenXPS format, with XPS set as default in the INF file.
OpenXPS, XPS

This option configures the driver to produce output in either OpenXPS or XPS format, with OpenXPS set as default in the INF file.
## Driver configuration type


GPD Driver

This option causes the Wizard to create a generic printer description (GPD) language file with the printer driver.
PPD Driver

This option causes the Wizard to create a PostScript printer description (PPD) language file with the printer driver.
## Protected printing


Enable protected printing

Select this option, if you want the ability to use a PIN to lock a print request that is sent to a printer. The end-user then has to provide the same PIN at the printer to release the locked print request for printing. For more information, see [Driver Support for Protected Printing](driver-support-for-protected-printing.md).
## Additional functionality


Driver property bag

This is an XML file that describes the contents of a driver property bag. The properties specified in this file, as well as the information provided in any data files added to the project’s ByteArray or IStream folders, will be compiled into a driver property bag. For more information, see [V4 Printer Driver Property Bags](v4-driver-property-bags.md).

And you can find the XML Schema for the driver property bag template in the Windows Driver Kit, in this folder: *\\Include\\um\\printdriverproperties.xml*.

Driver event file

This file is used to describe Bidi queries and the triggers that should cause a driver event to be raised. And it is important to note that driver events only support standard strings. For more information about driver events and standard strings, see [Driver Support for Customized UI](driver-support-for-customized-ui.md).
DevMode mapping file

This is an XML file that is used with PrintTicket &lt;-&gt; DEVMODE conversion in JavaScript code. When you provide this file, it must be specified in the [V4 Driver Manifest](v4-driver-manifest.md).
Queue property bag

This template allows you to provide per-queue configuration settings, including form-to-tray mappings and the configuration of printer properties like installable options. For more information, see [V4 Printer Driver Property Bags](v4-driver-property-bags.md).
Resource DLL

This template allows you to provide the descriptions for resources such as externally stored fonts, icons and other bitmaps, and localizable user interface text strings. For more information, see [Using Resource DLLs in a Minidriver](using-resource-dlls-in-a-minidriver.md), [V4 Driver Manifest](v4-driver-manifest.md) and [V4 Printer Driver Localization](v4-driver-localization.md).
Constraints JS

This template provides the method headers for all supported JavaScript constraint entry points. For more information, see [JavaScript Constraints](javascript-constraints.md).
Autoconfiguration GDL

This provides a basic auto-configuration file for a v4 print driver. For information about GDL syntax for auto-configuration, and to explore an example file, see the [Print Auto Configuration Sample](http://go.microsoft.com/fwlink/p/?LinkId=617938).
TCPMon Bidi extension XML

This provides a simple TCP/IP Bidi extension file. For more information about Bidi syntax for the standard TCP/IP port monitor, see [TCP/IP Schema Extensions](tcp-ip-schema-extensions.md).
WSDMon Bidi extension XML

This provides a simple WSD Bidi extension file. For more information about Bidi syntax for WSDMon, see [WSD Schema Extensions](wsd-schema-extensions.md).
USBMon Bidi extension XML + JS

This provides a simple USB Bidi extension file. It is dependent on the existence of a matched USB Bidi Extender JavaScript. For more information, see [USB Bidi Extender](usb-bidi-extender.md).
 

 




