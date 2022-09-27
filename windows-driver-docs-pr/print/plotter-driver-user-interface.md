---
title: Plotter driver user interface
description: Provides information about the plotter driver user interface.
keywords:
- Plotter Driver WDK print, user interface
- MSPlot WDK print, user interface
- user interface WDK MSPlot
ms.date: 09/14/2022
---

# Plotter driver user interface

The plotter user interface employs [CPSUI](common-property-sheet-user-interface.md) to create the following two property sheet pages:

- The **Device Settings** page for the printer property sheet, which is displayed when a user selects the **Properties** menu item from the printer folder or a printer window. This page lists printer-specific configuration settings.

- The **Layout**, **Paper/Quality**, and **Advanced** pages for the document property sheet, which are displayed when a user selects the **Document Defaults** menu item from the printer folder or a printer window, or when an application calls the [**PrinterProperties**](/windows/win32/printdocs/printerproperties) or [**DocumentProperties**](/windows/win32/printdocs/documentproperties) functions. This page lists document-specific configuration settings.

These property sheets contain the plotter features and options specified by a plotter's minidriver. They also allow the user to modify option values.

The plotter's user interface is implemented as a user-mode [printer interface DLL](printer-interface-dll.md). Code within this DLL, in conjunction with CPSUI, specifies the contents of the property sheet pages. The DLL enforces constraints on which plotter options can be combined, based on information in the minidriver. It also ensures that users do not select options not installed on the plotter.
