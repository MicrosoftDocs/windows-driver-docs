---
title: Pscript User Interface
description: Provides information about the Pscript user interface.
keywords:
- PostScript Printer Driver WDK print, user interface
- Pscript WDK print, user interface
- user interface WDK Pscript
ms.date: 01/30/2023
---

# Pscript user interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The Pscript user interface employs [CPSUI](common-property-sheet-user-interface.md) to create the following property sheet pages:

- The **Device Settings** page for the printer property sheet, which is displayed when a user selects the **Properties** menu item from the printer folder or a printer window. The page lists printer-specific configuration settings.

- The **Layout**, **Paper/Quality**, and **Advanced** pages for the document property sheet, which are displayed when a user selects **Printing Preferences** menu item from the printer folder or a printer window, or when an application calls the [**PrinterProperties**](/windows/win32/printdocs/printerproperties) or [**DocumentProperties**](/windows/win32/printdocs/documentproperties) functions. The pages list document-specific configuration settings.

These property sheet pages contain the printer features and printer options specified by a printer's Pscript minidriver. They also allow the user to modify option values.

The Pscript user interface is implemented as a user-mode [printer interface DLL](printer-interface-dll.md). Code within this DLL, in conjunction with CPSUI, specifies the contents of the property sheet pages. The DLL enforces constraints on which printer options can be combined, based on information in the minidriver. It also ensures that users do not select options not installed on the printer.

You can modify the Pscript-supplied property sheet pages by providing a [user interface plug-in](user-interface-plug-ins.md), which is described in the section entitled [Customizing Microsoft's printer drivers](customizing-microsoft-s-printer-drivers.md).
