---
title: Creating Property Sheet Pages
author: windows-driver-content
description: Creating Property Sheet Pages
ms.assetid: 90b1743c-b530-408a-aa30-9ab774166306
keywords:
- Common Property Sheet User Interface WDK print , creating property sheet pages
- CPSUI WDK print , creating property sheet pages
- property sheet pages WDK print , creating
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating Property Sheet Pages


## <a href="" id="ddk-creating-property-sheet-pages-gg"></a>


Property sheet pages created using CPSUI are made up of [property sheet options](property-sheet-options.md), where each option represents a user-modifiable value. Dialogs for property sheet options are created using a set of [CPSUI-supported window controls](cpsui-supported-window-controls.md) that let a user modify an option's value.

CPSUI-supplied window controls can be displayed within [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md), or they can be used with customized pages. There are several [methods for specifying pages](methods-for-specifying-pages.md), all of which involve calling CPSUI's [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207) function.

Creating property sheet pages for printers and print documents involves [using CPSUI with printer drivers](using-cpsui-with-printer-drivers.md) and requires interaction between an application, the print spooler, a printer interface DLL, and CPSUI.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Creating%20Property%20Sheet%20Pages%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


