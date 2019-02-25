---
title: CPSUI-Supplied Pages and Templates
description: CPSUI-Supplied Pages and Templates
ms.assetid: de33cb29-3941-4232-bd61-d36fb04d69d3
keywords:
- Common Property Sheet User Interface WDK print , templates
- CPSUI WDK print , templates
- property sheet pages WDK print , templates
- Common Property Sheet User Interface WDK print , predefined pages
- CPSUI WDK print , predefined pages
- property sheet pages WDK print , predefined pages
- predefined property sheet pages WDK CPSUI
- templates WDK CPSUI
- treeview pages WDK CPSUI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CPSUI-Supplied Pages and Templates





CPSUI supplies a set of predefined property sheet pages, along with three page templates. Predefined property sheet pages include the following:

-   A set of three pages, with tab titles of **Layout**, **Paper/Quality**, and **Advanced**. These pages are meant to contain document properties for printers, and can be used for creating a property sheet from within a printer interface DLL's [**DrvDocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548548) function.

-   A single page, with a tab title of **Advanced**. Again, the page is meant to contain document properties for printers, and can be used for creating a property sheet from within a printer interface DLL's [**DrvDocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548548) function.

-   A single page, with a tab title of **Device Settings**. This page is meant to contain printer properties, and can be used for creating a property sheet from within a printer interface DLL's [**DrvDevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548542) function.

-   A single, generic treeview page with no predefined title. Any CPSUI application can use this page.

To use a predefined page, an application must identify it using the **pDlgPage** member of a [**COMPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff546211) structure.

CPSUI also supplies three predefined page templates. CPSUI uses these templates for creating its predefined pages. Applications can also use them. The templates consist of the following:

-   A treeview page template, which CPSUI uses to create the predefined **Advanced** and **Device Settings** pages. This template consists of a treeview control that contains a node for each [property sheet option](property-sheet-options.md). A context menu is associated with each node of the tree. Each node's context menu provides the means by which a user can modify the option's value. CPSUI supplies a dialog box procedure for this template, which handles Windows messages for all the [CPSUI-supported window controls](cpsui-supported-window-controls.md).

-   Two multiple control templates, which CPSUI uses to create the predefined **Layout** and **Paper/Quality** pages. CPSUI supplies a dialog box procedure for this template, which handles Windows messages for all the CPSUI-supported window controls.

To use a predefined page template, an application must identify it using the **DlgTemplateID** member of a [**DLGPAGE**](https://msdn.microsoft.com/library/windows/hardware/ff547607) structure.

 

 




