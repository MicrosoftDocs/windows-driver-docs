---
title: Pscript User Interface
description: Pscript User Interface
ms.assetid: 88c1bb99-bc05-454f-ae36-722e9aa246c6
keywords:
- PostScript Printer Driver WDK print , user interface
- Pscript WDK print , user interface
- user interface WDK Pscript
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pscript User Interface





The Pscript user interface employs [CPSUI](common-property-sheet-user-interface.md) to create the following property sheet pages:

-   The **Device Settings** page for the printer property sheet, which is displayed when a user selects the **Properties** menu item from the printer folder or a printer window. The page lists printer-specific configuration settings.

-   The **Layout**, **Paper/Quality**, and **Advanced** pages for the document property sheet, which are displayed when a user selects **Printing Preferences** menu item from the printer folder or a printer window, or when an application calls the **PrinterProperties** or **DocumentProperties** functions (described in the Microsoft Windows SDK documentation). The pages list document-specific configuration settings.

These property sheet pages contain the printer features and printer options specified by a printer's Pscript minidriver. They also allow the user to modify option values.

The Pscript user interface is implemented as a user-mode [printer interface DLL](printer-interface-dll.md). Code within this DLL, in conjunction with CPSUI, specifies the contents of the property sheet pages. The DLL enforces constraints on which printer options can be combined, based on information in the minidriver. It also ensures that users do not select options not installed on the printer.

You can modify the Pscript-supplied property sheet pages by providing a [user interface plug-in](user-interface-plug-ins.md), which is described in the section entitled [Customizing Microsoft's Printer Drivers](customizing-microsoft-s-printer-drivers.md).

 

 




