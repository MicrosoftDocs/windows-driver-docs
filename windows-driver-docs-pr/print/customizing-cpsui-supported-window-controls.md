---
title: Customizing CPSUI-Supported Window Controls
description: Customizing CPSUI-Supported Window Controls
keywords:
- Common Property Sheet User Interface WDK print , window controls
- CPSUI WDK print , window controls
- property sheet pages WDK print , window controls
- window controls WDK CPSUI
- customizing CPSUI-supported window controls WDK print
ms.date: 01/27/2023
---

# Customizing CPSUI-Supported Window Controls

[!include[Print Support Apps](../includes/print-support-apps.md)]

If you are using [CPSUI-supported window controls](cpsui-supported-window-controls.md) in conjunction with [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md), CPSUI provides window control resources that describe the controls in a manner that allows them to fit together. Therefore, you do not need to provide resources for the controls.

On the other hand, if you are creating a property sheet page that does not use a CPSUI-supplied page or template, you must customize the CPSUI-supported window controls that you use. To do this, you need to provide window control resources for the [CPSUI option types](./cpsui-option-types.md). You must specify identifiers for these resources using the **BegCtrlID** member of each option's [**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype) structure.

If you are customizing CPSUI-supported window controls, remember that CPSUI does not display an option if the OPTIF\_HIDE flag set in the [**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem) structure. CPSUI moves the remaining controls to fill the space normally taken up by the hidden option. Therefore, if you are creating a page containing several simultaneously-displayed options, the following rules should be obeyed:

- Each option should occupy the entire horizontal space of the property sheet page.

- Option dialogs should not overlay each other.

- For options represented by radio buttons that are arranged from left to right, buttons and icons should be aligned on the x axis. If the buttons are arranged from top to bottom, buttons and icons should be aligned on the y axis.

- If several items share one group box, the group box must belong to the first [**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem), which is the topmost item in the group box. The group box must be large enough to contain all items associated with it.

Also, note that if radio buttons and icons are arranged top to bottom and some of these controls are hidden, CPSUI does not remove resulting white space in the y direction.
