---
title: TVOT_CHKBOX
description: The TVOT_CHKBOX option type consists of a check box inside a group box.
keywords: ["TVOT_CHKBOX Print Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- TVOT_CHKBOX
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 01/30/2023
---

# TVOT_CHKBOX

[!include[Print Support Apps](../includes/print-support-apps.md)]

The TVOT_CHKBOX option type consists of a check box inside a group box.

## OPTITEM structure  

**Sel/pSel**  
Not used.

## OPTPARAM structure array (pOptParam member of OPTTYPE)  

**pData**  
Not used.

**IconID**  
Identifies an icon to be associated with the check box.

**lParam**  
Not used.

## OPTTYPE structure

**Type**  
TVOT_CHKBOX

**Count**  
1

**Style**
Not used.

**BegCtrlID**  
If **pDlgPage** in [**COMPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_compropsheetui) identifies a CPSUI-supplied page, or if **DlgTemplateID** in [**DLGPAGE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_dlgpage) identifies a CPSUI-supplied template, **BegCtrlID** is not used. Otherwise, **BegCtrlID** must contain the first control identifier of a sequentially numbered set of control identifiers. Control identifiers must identify the following Windows controls:

| Control Identifier | Windows Control |
|--|--|
| **BegCtrlID** contents | Group box |
| **BegCtrlID** contents+1 | Title text |
| **BegCtrlID** contents+2 | Check box |
| **BegCtrlID** contents+3 | Check box icon |
| **BegCtrlID** contents+4 | Extended check box or extended push button (optional) |
| **BegCtrlID** contents+5 | Extended check box or extended push button icon (optional) |

For additional information, see [Customizing CPSUI-Supported Window Controls](./customizing-cpsui-supported-window-controls.md).

## Requirements

**Header:** compstui.h (include Compstui.h)

## See also

[**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem)

[**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam)

[**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype)
