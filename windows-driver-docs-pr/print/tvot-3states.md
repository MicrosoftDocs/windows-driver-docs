---
title: TVOT_3STATES
description: The TVOT_3STATES option type consists of three radio buttons inside a group box.
keywords: ["TVOT_3STATES Print Devices"]
topic_type:
- apiref
api_name:
- TVOT_3STATES
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 09/02/2021
---

# TVOT_3STATES

The TVOT_3STATES option type consists of three radio buttons inside a group box.

## OPTITEM structure  

**Sel/pSel**  
Index into the [**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam) array that is pointed to by the **pOptParam** member of the option's [**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype) structure. This specifies the currently selected option parameter.

## OPTPARAM structure array (pOptParam member of OPTTYPE)

**pData**  
**pOptParam**\[0\]->**pData** points to a text string describing state 1, used as a button label. **pOptParam**\[1\]->**pData** points to a text string describing state 2, used as a button label. **pOptParam**\[2\]->**pData** points to a text string describing state 3, used as a button label.

**IconID**  
**pOptParam**\[0\]->**IconID** identifies an icon to be associated with state 1. **pOptParam**\[1\]->**IconID** identifies an icon to be associated with state 2. **pOptParam**\[2\]->**IconID** identifies an icon to be associated with state 3.

**lParam**  
Not used.

## OPTTYPE structure  

**Type**  
TVOT_3STATES

**Count**  
3

**Style**  
Not used.

**BegCtrlID**  
If **pDlgPage** in [**COMPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_compropsheetui) identifies a CPSUI-supplied page, or if **DlgTemplateID** in [**DLGPAGE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_dlgpage) identifies a CPSUI-supplied template, **BegCtrlID** is not used. Otherwise, **BegCtrlID** must contain the first control identifier of a sequentially numbered set of control identifiers. Control identifiers must identify the following Windows controls:

| Control Identifier | Windows Control |
|--|--|
| **BegCtrlID** contents | Group box |
| **BegCtrlID** contents+1 | Title text |
| **BegCtrlID** contents+2 | State 1 radio button |
| **BegCtrlID** contents+3 | State 1 icon |
| **BegCtrlID** contents+4 | State 2 radio button |
| **BegCtrlID** contents+5 | State 2 icon |
| **BegCtrlID** contents+6 | State 3 radio button |
| **BegCtrlID** contents+7 | State 3 icon |
| **BegCtrlID** contents+8 | Extended check box or extended push button (optional) |
| **BegCtrlID** contents+9 | Extended check box or extended push button icon (optional) |

For additional information, see [Customizing CPSUI-Supported Window Controls](./customizing-cpsui-supported-window-controls.md).

## Requirements

**Header:** compstui.h (include Compstui.h)

## See also

[**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem)

[**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam)

[**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype)
