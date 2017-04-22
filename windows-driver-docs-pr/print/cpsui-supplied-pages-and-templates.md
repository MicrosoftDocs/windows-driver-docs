---
title: CPSUI-Supplied Pages and Templates
author: windows-driver-content
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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CPSUI-Supplied Pages and Templates


## <a href="" id="ddk-cpsui-supplied-pages-and-templates-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20CPSUI-Supplied%20Pages%20and%20Templates%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


