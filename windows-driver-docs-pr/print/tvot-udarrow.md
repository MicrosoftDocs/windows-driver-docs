---
title: TVOT_UDARROW
description: The TVOT_UDARROW option type consists of an up-down control and an edit control inside a group box.
keywords: ["TVOT_UDARROW Print Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- TVOT_UDARROW
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 01/30/2023
---

# TVOT_UDARROW

[!include[Print Support Apps](../includes/print-support-apps.md)]

The TVOT_UDARROW option type consists of an up-down control and an edit control inside a group box.

## OPTITEM structure

**Sel/pSel**  
Numeric value representing the edit control's current contents.

## OPTPARAM structure array (pOptParam member of OPTTYPE)

**pData**  
**pOptParam**\[0\]->**pData** points to a NULL-terminated text string identifying the control's units. **pOptParam**\[1\]->**pData** points to a NULL-terminated text string describing the control. (If **NULL**, CPSUI displays the low end and high end of the control's range of values.)

**IconID**  
**pOptParam**\[0\]->**IconID** identifies an icon to be associated with the track bar. **pOptParam**\[1\]->**IconID** specifies a 16-bit signed value representing the low end of the control's range.

**lParam**  
**pOptParam**\[0\]->**lParam** is not used. **pOptParam**\[1\]->**lParam** specifies a 16-bit signed value representing the high end of the control's range.

## OPTTYPE structure

**Type**  
TVOT_UDARROW

**Count**  
2

**Style**  
Not used.

**BegCtrlID**  
If **pDlgPage** in [**COMPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_compropsheetui) identifies a CPSUI-supplied page, or if **DlgTemplateID** in [**DLGPAGE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_dlgpage) identifies a CPSUI-supplied template, **BegCtrlID** is not used. Otherwise, **BegCtrlID** must contain the first control identifier of a sequentially numbered set of control identifiers. Control identifiers must identify the following Windows controls:

| Control Identifier | Windows Control |
|--|--|
| **BegCtrlID** contents | Group box |
| **BegCtrlID** contents+1 | Title text |
| **BegCtrlID** contents+2 | Edit box |
| **BegCtrlID** contents+3 | Icon |
| **BegCtrlID** contents+4 | Text describing value units |
| **BegCtrlID** contents+5 | Text describing the control |
| **BegCtrlID** contents+6 | Up-down control |
| **BegCtrlID** contents+7 | Extended check box or extended push button (optional) |
| **BegCtrlID** contents+8 | Extended check box or extended push button icon (optional) |

For additional information, see [Customizing CPSUI-Supported Window Controls](customizing-cpsui-supported-window-controls.md).

## Requirements

**Header:** compstui.h (include Compstui.h)

## See also

[**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem)

[**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam)

[**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype)
