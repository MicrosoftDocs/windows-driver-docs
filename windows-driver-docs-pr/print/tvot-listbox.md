---
title: TVOT_LISTBOX
description: The TVOT_LISTBOX option type consists of a list box inside a group box.
keywords: ["TVOT_LISTBOX Print Devices"]
topic_type:
- apiref
api_name:
- TVOT_LISTBOX
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 01/30/2023
---

# TVOT_LISTBOX

[!include[Print Support Apps](../includes/print-support-apps.md)]

The TVOT_LISTBOX option type consists of a list box inside a group box.

## OPTITEM structure  

**Sel/pSel**  
Index into the [**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam) array that is pointed to by the **pOptParam** member of the option's [**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype) structure. This specifies the currently selected option parameter.

## OPTPARAM structure array (pOptParam member of OPTTYPE)  

**pData**  
**pOptParam**\[0\]->**pData** points to the first text string to be displayed in the list box. **pOptParam**\[1\]->**pData** points to the second text string to be displayed in the list box. **pOptParam**\[*n*\]->**pData** points to the *n*th text string to be displayed in the list box.

**IconID**  
**pOptParam**\[0\]->**IconID** identifies an icon to be associated with the first text string. **pOptParam**\[1\]->**IconID** identifies an icon to be associated with the second text string. **pOptParam**\[*n*\]->**IconID** identifies an icon to be associated with the *n*th text string.

**lParam**  
Not used.

## OPTTYPE structure

**Type**  
TVOT_LISTBOX

**Count**  
The number of OPTPARAM structures; that is, the number of text strings to be displayed in the list box.

**Style**  
The following optional bit flags can be specified.

| Flag | Description |
|--|--|
| OTS_LBCB_INCL_ITEM_NONE | If set, CPSUI includes a "None" string in the list box. If a user selects "None", the **Sel/pSel** union is set to negative one. |
| OTS_LBCB_NO_ICON16_IN_ITEM | If set, CPSUI does not draw each option parameter's icon (**IconID** in OPTPARAM) when displaying the parameter's value in the list box. |
| OTS_LBCB_PROPPAGE_LBUSECB | When the option is displayed on a non-treeview property sheet page, it is displayed as a combo box instead of a list box. |
| OTS_LBCB_SORT | If set, CPSUI displays text strings in alphabetic order. |

**BegCtrlID**  
If **pDlgPage** in [**COMPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_compropsheetui) identifies a CPSUI-supplied page, or if **DlgTemplateID** in [**DLGPAGE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_dlgpage) identifies a CPSUI-supplied template, **BegCtrlID** is not used. Otherwise, **BegCtrlID** must contain the first control identifier of a sequentially numbered set of control identifiers. Control identifiers must identify the following Windows controls:

| Control Identifier | Windows Control |
|--|--|
| **BegCtrlID** contents | Group box |
| **BegCtrlID** contents+1 | Title text |
| **BegCtrlID** contents+2 | List box |
| **BegCtrlID** contents+3 | List box icon |
| **BegCtrlID** contents+4 | Extended check box or extended push button (optional) |
| **BegCtrlID** contents+5 | Extended check box or extended push button icon (optional) |

For additional information, see [Customizing CPSUI-Supported Window Controls](./customizing-cpsui-supported-window-controls.md).

## Requirements

**Header:** compstui.h (include Compstui.h)

## See also

[**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem)

[**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam)

[**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype)
