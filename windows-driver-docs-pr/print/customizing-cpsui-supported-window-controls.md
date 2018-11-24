---
title: Customizing CPSUI-Supported Window Controls
description: Customizing CPSUI-Supported Window Controls
ms.assetid: b9ced902-6368-4b3b-a974-81e7d38c0ced
keywords:
- Common Property Sheet User Interface WDK print , window controls
- CPSUI WDK print , window controls
- property sheet pages WDK print , window controls
- window controls WDK CPSUI
- customizing CPSUI-supported window controls WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customizing CPSUI-Supported Window Controls





If you are using [CPSUI-supported window controls](cpsui-supported-window-controls.md) in conjunction with [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md), CPSUI provides window control resources that describe the controls in a manner that allows them to fit together. Therefore, you do not need to provide resources for the controls.

On the other hand, if you are creating a property sheet page that does not use a CPSUI-supplied page or template, you must customize the CPSUI-supported window controls that you use. To do this, you need to provide window control resources for the [CPSUI option types](https://msdn.microsoft.com/library/windows/hardware/ff547142). You must specify identifiers for these resources using the **BegCtrlID** member of each option's [**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670) structure.

If you are customizing CPSUI-supported window controls, remember that CPSUI does not display an option if the OPTIF\_HIDE flag set in the [**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) structure. CPSUI moves the remaining controls to fill the space normally taken up by the hidden option. Therefore, if you are creating a page containing several simultaneously-displayed options, the following rules should be obeyed:

-   Each option should occupy the entire horizontal space of the property sheet page.

-   Option dialogs should not overlay each other.

-   For options represented by radio buttons that are arranged from left to right, buttons and icons should be aligned on the x axis. If the buttons are arranged from top to bottom, buttons and icons should be aligned on the y axis.

-   If several items share one group box, the group box must belong to the first [**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656), which is the topmost item in the group box. The group box must be large enough to contain all items associated with it.

Also, note that if radio buttons and icons are arranged top to bottom and some of these controls are hidden, CPSUI does not remove resulting white space in the y direction.

 

 




