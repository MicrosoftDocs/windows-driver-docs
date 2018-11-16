---
title: Unidrv User Interface
description: Unidrv User Interface
ms.assetid: b1f34ebf-8c8a-4b43-ba48-26bcf6352360
keywords:
- Unidrv, user interface
- user interface WDK Unidrv
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unidrv User Interface





The Unidrv user interface employs [CPSUI](common-property-sheet-user-interface.md) to create the following property sheet pages:

-   The **Device Settings** page for the printer property sheet, which is displayed when a user selects the **Properties** menu item from the printer folder or a printer window. The page lists printer-specific configuration settings.

-   The **Layout**, **Paper/Quality**, and **Advanced** pages for the document property sheet, which are displayed when a user selects the **Document Defaults** menu item from the printer folder or a printer window, or when an application calls the **PrinterProperties** or **DocumentProperties** functions (described in the Microsoft Windows SDK documentation). The pages list document-specific configuration settings.

These property sheet pages contain the [printer features](printer-features.md) and [printer options](printer-options.md) specified by a printer's Unidrv minidriver. They also allow the user to modify option values.

The Unidrv user interface is implemented as a user-mode [printer interface DLL](printer-interface-dll.md). Code within this DLL, in conjunction with CPSUI, specifies the contents of the property sheet pages. The DLL enforces constraints on which printer options can be combined, based on information in the minidriver. It also ensures that users do not select options not installed on the printer.

You can modify the Unidrv-supplied property sheet pages by providing a [user interface plug-in](user-interface-plug-ins.md).

 

 




