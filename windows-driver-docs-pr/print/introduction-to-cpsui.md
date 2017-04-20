---
title: Introduction to CPSUI
author: windows-driver-content
description: Introduction to CPSUI
ms.assetid: 737c2dbf-1ce6-4f83-af94-265c948f3128
keywords:
- Common Property Sheet User Interface WDK print , about CPSUI
- CPSUI WDK print , about CPSUI
- property sheet pages WDK print , about CPSUI with printer drivers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to CPSUI


## <a href="" id="ddk-introduction-to-cpsui-gg"></a>


The Common Property Sheet User Interface (CPSUI) is a user-mode dynamic-link library that enables developers to create property sheet pages having a common, standard appearance. Most pages created with CPSUI consist of:

-   A treeview window, with each tree node representing a selectable, user-modifiable page option.

-   A context menu for each tree node, which is used for displaying and selecting parameter values associated with the node.

Context menu items are created using a predefined set of [CPSUI-supported window controls](cpsui-supported-window-controls.md). A user selects an option in the treeview window, then selects the desired value for that option using the context menu.

While CPSUI was designed to be used by any application, its primary use is by the NT-based operating system printing subsystem. Therefore, the Windows Driver Kit (WDK) documentation focuses on this use.

CPSUI provides predefined property sheet pages for printers and print documents. CPSUI-supplied pages consist of the **Device Settings** page for a printer, and the **Layout**, **Paper/Quality**, and **Advanced** pages for a document. These pages can be viewed from the print folder's **Printer** menu.

The print spooler, in conjunction with [printer interface DLLs](printer-interface-dll.md), use these predefined pages to create property sheets for printers and documents. For information about how the print spooler, printer interface DLLs, and CPSUI interact, see [Using CPSUI with Printer Drivers](using-cpsui-with-printer-drivers.md).

Customized user interface code created for Microsoft's [*Unidrv*](https://msdn.microsoft.com/library/windows/hardware/ff556343#wdkgloss-unidrv) and [*Pscript*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pscript) drivers can also use CPSUI. For more information, see [User Interface Plug-Ins](user-interface-plug-ins.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Introduction%20to%20CPSUI%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


