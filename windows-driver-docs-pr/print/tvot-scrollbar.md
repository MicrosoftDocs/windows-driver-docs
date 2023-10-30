---
title: TVOT_SCROLLBAR
description: The TVOT_SCROLLBAR option type consists of a scroll bar inside a group box.
keywords: ["TVOT_SCROLLBAR Print Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- TVOT_SCROLLBAR
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 01/30/2023
---

# TVOT_SCROLLBAR

[!include[Print Support Apps](../includes/print-support-apps.md)]

The TVOT_SCROLLBAR option type consists of a scroll bar inside a group box.

## OPTITEM structure  

**Sel/pSel**  
Value representing the current scroll bar position.

## OPTPARAM structure array (pOptParam member of OPTTYPE)

**pData**  
**pOptParam**\[0\]->**pData** points to a NULL-terminated text string identifying the scroll bar units. **pOptParam**\[1\]->**pData** points to a NULL-terminated text string describing the low end of the scroll bar's range. **pOptParam**\[2\]->**pData** points to aNULL-terminated text string describing the high end of the scroll bar's range.

**IconID**  
**pOptParam**\[0\]->**IconID** identifies an icon to be associated with the scroll bar. **pOptParam**\[1\]->**IconID** specifies a 16-bit signed value representing the low end of the scroll bar's range. **pOptParam**\[2\]->**IconID** specifies the multiplication factor that is applied to the selected scroll position before its value is displayed. (Usually, this value is 1.)

**lParam**  
**pOptParam**\[0\]->**lParam** is not used. **pOptParam**\[1\]->**lParam** specifies a 16-bit signed value representing the high end of the scroll bar's range. **pOptParam**\[2\]->**lParam** specifies the scrolling increment value.

## OPTTYPE structure

**Type**  
TVOT_SCROLLBAR

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
| **BegCtrlID** contents+2 | Scroll bar |
| **BegCtrlID** contents+3 | Scroll bar icon |
| **BegCtrlID** contents+4 | Text describing the low end of the scroll bar range |
| **BegCtrlID** contents+5 | Text describing the high end of the scroll bar range |
| **BegCtrlID** contents+6 | Text describing the scroll bar units |
| **BegCtrlID** contents+7 | Extended check box or extended push button (optional) |
| **BegCtrlID** contents+8 | Extended check box or extended push button icon (optional) |

For additional information, see [Customizing CPSUI-Supported Window Controls](customizing-cpsui-supported-window-controls.md).

## Requirements

**Header:** compstui.h (include Compstui.h)

## See also

[**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem)

[**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam)

[**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype)
