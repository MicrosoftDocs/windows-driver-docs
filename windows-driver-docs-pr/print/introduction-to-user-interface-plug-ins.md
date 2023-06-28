---
title: Introduction to User Interface Plug-Ins
description: Introduction to User Interface Plug-Ins
keywords:
- user interface plug-ins WDK print , about user interface plug-ins
- UI plug-ins WDK print , about user interface plug-ins
ms.date: 06/22/2023
---

# Introduction to user interface plug-Ins

[!include[Print Support Apps](../includes/print-support-apps.md)]

> [!IMPORTANT]
> Some information contained in this article applies to obsolete Windows operating systems.

When you add support for a new printer device to either the [Microsoft Universal printer driver](microsoft-universal-printer-driver.md) (Unidrv) or the [Microsoft PostScript printer driver](microsoft-postscript-printer-driver.md) (Pscript), you can customize the driver's user interface by modifying the printer property sheet or the document property sheet for your printer.

You accomplish this customization by providing a user-mode DLL. This DLL is referred to as a *user interface plug-in*, or just *UI plug-in*.

A UI plug-in can modify the printer property sheet by adding, removing, or replacing options within the property sheet's **Device Settings** page. It can also add a new page. Likewise, the plug-in can modify the document property sheet by adding, removing, or replacing options within the property sheet's **Layout**, **Paper/Quality**, and **Advanced** pages, or it can add a new page.

If you are using Unidrv from Windows Vista, you can implement the [**IPrintOemUI2::HideStandardUI**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui2-hidestandardui) method in the plug-in to hide all of the printer configuration property pages that the standard driver provides. You can use this method if you want to provide a completely custom printer configuration user interface for your printer.

> [!IMPORTANT]
> Windows Help (WinHlp32.exe) is an application that enables users to view .hlp files. The Windows Help application is not included as a part of the Windows operating system. Software developers who develop applications that rely on .hlp files, should transition their files to an alternative Help format, such as .chm, .hxs, .html, or .xml files.

The [printer interface DLL](printer-interface-dll.md) calls UI plug-ins for Unidrv or Pscript, with a set of COM interfaces. Printer interface DLLs are implemented by using CPSUI, and a UI plug-in interacts indirectly with CPSUI through the driver's printer interface DLL. Therefore, you should read the [CPSUI](common-property-sheet-user-interface.md) section before you develop a UI plug-in.

In addition to modifying the printer driver's user interface, a UI plug-in can perform other operations, such as processing certain printer events and reporting supported capabilities. For more information, see [Customizing Other Printer Interface Operations](customizing-other-printer-interface-operations.md).
