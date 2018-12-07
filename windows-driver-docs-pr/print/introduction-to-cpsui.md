---
title: Introduction to CPSUI
description: Introduction to CPSUI
ms.assetid: 737c2dbf-1ce6-4f83-af94-265c948f3128
keywords:
- Common Property Sheet User Interface WDK print , about CPSUI
- CPSUI WDK print , about CPSUI
- property sheet pages WDK print , about CPSUI with printer drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to CPSUI





The Common Property Sheet User Interface (CPSUI) is a user-mode dynamic-link library that enables developers to create property sheet pages having a common, standard appearance. Most pages created with CPSUI consist of:

-   A treeview window, with each tree node representing a selectable, user-modifiable page option.

-   A context menu for each tree node, which is used for displaying and selecting parameter values associated with the node.

Context menu items are created using a predefined set of [CPSUI-supported window controls](cpsui-supported-window-controls.md). A user selects an option in the treeview window, then selects the desired value for that option using the context menu.

While CPSUI was designed to be used by any application, its primary use is by the NT-based operating system printing subsystem. Therefore, the Windows Driver Kit (WDK) documentation focuses on this use.

CPSUI provides predefined property sheet pages for printers and print documents. CPSUI-supplied pages consist of the **Device Settings** page for a printer, and the **Layout**, **Paper/Quality**, and **Advanced** pages for a document. These pages can be viewed from the print folder's **Printer** menu.

The print spooler, in conjunction with [printer interface DLLs](printer-interface-dll.md), use these predefined pages to create property sheets for printers and documents. For information about how the print spooler, printer interface DLLs, and CPSUI interact, see [Using CPSUI with Printer Drivers](using-cpsui-with-printer-drivers.md).

Customized user interface code created for Microsoft's [*Unidrv*](https://msdn.microsoft.com/library/windows/hardware/ff556343#wdkgloss-unidrv) and [*Pscript*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pscript) drivers can also use CPSUI. For more information, see [User Interface Plug-Ins](user-interface-plug-ins.md).

 

 




