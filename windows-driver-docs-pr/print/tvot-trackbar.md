---
title: TVOT_TRACKBAR
description: The TVOT_TRACKBAR option type consists of a track bar inside a group box.
keywords: ["TVOT_TRACKBAR Print Devices"]
topic_type:
- apiref
api_name:
- TVOT_TRACKBAR
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 09/16/2021
---

# TVOT_TRACKBAR

The TVOT_TRACKBAR option type consists of a track bar inside a group box.

## OPTITEM structure

**Sel/pSel**  
Value representing the current track bar position.

## OPTPARAM structure array (pOptParam member of OPTTYPE)

**pData**  
**pOptParam**\[0\]->**pData** points to a NULL-terminated text string identifying the track bar units. **pOptParam**\[1\]->**pData** points to a NULL-terminated text string describing the low end of the track bar's range. **pOptParam**\[2\]->**pData** points to a NULL-terminated text string describing the high end of the track bar's range.

**IconID**  
**pOptParam**\[0\]->**IconID** identifies an icon to be associated with the track bar. **pOptParam**\[1\]->**IconID** specifies a 16-bit signed value representing the low end of the track bar's range. **pOptParam**\[2\]->**IconID** specifies the multiplication factor that is applied to the selected track position before its value is displayed. (Usually, this value is 1.)

**lParam**  
**pOptParam**\[0\]->**lParam** is not used. **pOptParam**\[1\]->**lParam** specifies a 16-bit signed value representing the high end of the track bar's range. **pOptParam**\[2\]->**lParam** specifies the tracking increment value.

## OPTTYPE structure

**Type**  
TVOT_TRACKBAR

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
| **BegCtrlID** contents+2 | Track bar |
| **BegCtrlID** contents+3 | Track bar icon |
| **BegCtrlID** contents+4 | Text describing the low end of the track bar range |
| **BegCtrlID** contents+5 | Text describing the high end of the track bar range |
| **BegCtrlID** contents+6 | Text describing the track bar units |
| **BegCtrlID** contents+7 | Extended check box or extended push button (optional) |
| **BegCtrlID** contents+8 | Extended check box or extended push button icon (optional) |

For additional information, see [Customizing CPSUI-Supported Window Controls](customizing-cpsui-supported-window-controls.md).

## Requirements

**Header:** compstui.h (include Compstui.h)

## See also

[**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem)

[**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam)

[**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype)
