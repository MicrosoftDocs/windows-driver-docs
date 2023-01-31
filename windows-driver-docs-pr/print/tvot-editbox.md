---
title: TVOT_EDITBOX
description: The TVOT_EDITBOX option type consists of an edit box inside a group box.
keywords: ["TVOT_EDITBOX Print Devices"]
topic_type:
- apiref
api_name:
- TVOT_EDITBOX
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 01/30/2023
---

# TVOT_EDITBOX

[!include[Print Support Apps](../includes/print-support-apps.md)]

The TVOT_EDITBOX option type consists of an edit box inside a group box.

## OPTITEM structure

**Sel/pSel**  
Application-supplied pointer to a NULL-terminated string containing the current contents of the edit box.

## OPTPARAM structure array (pOptParam member of OPTTYPE)  

**pData**  
**pOptParam**\[0\]->**pData** points to a NULL-terminated text string to be displayed to the right of the edit box. **pOptParam**\[1\]->**pData** points to a NULL-terminated text string to be displayed above the edit box.

**IconID**  
**pOptParam**\[0\]->**IconID** identifies an icon to be associated with the edit box. **pOptParam**\[1\]->**IconID** is used for specifying the size, in bytes, of both the edit box and the buffer pointed to by **pSel** in the OPTITEM structure.

**lParam**  
Not used.

## OPTTYPE structure

**Type**  
TVOT_EDITBOX

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
| **BegCtrlID** contents+3 | Edit box icon |
| **BegCtrlID** contents+4 | Text positioned to the right of the edit box |
| **BegCtrlID** contents+5 | Text positioned above the edit box |
| **BegCtrlID** contents+6 | Extended check box or extended push button (optional) |
| **BegCtrlID** contents+7 | Extended check box or extended push button icon (optional) |

For additional information, see [Customizing CPSUI-Supported Window Controls](./customizing-cpsui-supported-window-controls.md).

## Requirements

**Header:** compstui.h (include Compstui.h)

## See also

[**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem)

[**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam)

[**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype)
