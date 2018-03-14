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

 

 




