---
title: TVOT_PUSHBUTTON
description: The TVOT_PUSHBUTTON option type consists of a push button inside a group box.
keywords: ["TVOT_PUSHBUTTON Print Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- TVOT_PUSHBUTTON
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 01/30/2023
---

# TVOT_PUSHBUTTON

[!include[Print Support Apps](../includes/print-support-apps.md)]

The TVOT_PUSHBUTTON option type consists of a push button inside a group box.

## OPTITEM structure  

**Sel/pSel**  
Depends on the **Style** member of the OPTPARAM structure, as follows.

| Push Button Style | Sel/pSel Usage |
|--|--|
| PUSHBUTTON_TYPE_CALLBACK | Not used. |
| PUSHBUTTON_TYPE_DLGPROC | CPSUI stores the return value of the dialog box procedure. |
| PUSHBUTTON_TYPE_HTCLRADJ | CPSUI stores the return value of the halftoning operation. |
| PUSHBUTTON_TYPE_HTSETUP | CPSUI stores the return value of the halftoning operation. |

## OPTPARAM structure array (pOptParam member of OPTTYPE)

**pData**  
Depends on the **Style** member, as follows.

| Push button style | pData usage |
|--|--|
| PUSHBUTTON_TYPE_CALLBACK | Pointer to a [**_CPSUICALLBACK**](/windows-hardware/drivers/ddi/compstui/nc-compstui-_cpsuicallback)-typed function. |
| PUSHBUTTON_TYPE_DLGPROC | DLGPROC-typed pointer to a dialog box procedure (see the Microsoft Windows SDK documentation). |
| PUSHBUTTON_TYPE_HTCLRADJ | Pointer to COLORADJUSTMENT structure (described in the Windows SDK documentation). |
| PUSHBUTTON_TYPE_HTSETUP | Pointer to a [**DEVHTADJDATA**](/windows/win32/api/winddi/ns-winddi-devhtadjdata) structure. |

**IconID**  
Identifies an icon to be associated with the push button.

**lParam**
Depends on the **Style** member, as follows.

| Push button style | lParam usage |
|--|--|
| PUSHBUTTON_TYPE_CALLBACK | Not used. |
| PUSHBUTTON_TYPE_DLGPROC | Resource identifier for a DIALOG resource, or handle to a DLGTEMPLATE structure (see the Windows SDK documentation). Depends on the DPF_USE_HDLGTEMPLATE flag in the OPTPARAM structure's **Flags** member. |
| PUSHBUTTON_TYPE_HTCLRADJ | Not used. |
| PUSHBUTTON_TYPE_HTSETUP | Not used. |

| Term | Description |
|--|--|
| Style | Specifies the operation to be performed by CPSUI when a user clicks on the push button. Can be one of the following values: |
| PUSHBUTTON_TYPE_CALLBACK | CPSUI calls the application's [**_CPSUICALLBACK**](/windows-hardware/drivers/ddi/compstui/nc-compstui-_cpsuicallback)-typed callback function to handle button events, with the [**CPSUICBPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_cpsuicbparam) structure's **Reason** member set to CPSUICB_REASON_PUSHBUTTON. (CPSUI ignores the callback function's return value.) |
| PUSHBUTTON_TYPE_DLGPROC | The application's dialog box procedure handles button events. (For more information, see the **Remarks** section for [**DLGPAGE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_dlgpage).) When the function receives a WM_INITDIALOG message, its *lParam* argument points to a [**CPSUICBPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_cpsuicbparam) structure with the **Reason** member set to CPSUICB_REASON_DLGPROC. |
| PUSHBUTTON_TYPE_HTCLRADJ | CPSUI displays a halftone color adjustment dialog box. |
| PUSHBUTTON_TYPE_HTSETUP | CPSUI displays a device halftone setup dialog box. |

## OPTTYPE structure

**Type**
TVOT_PUSHBUTTON

**Count**
1

**Style**
The following optional bit flags can be specified.

| Flag | Description |
|--|--|
| OTS_PUSH_ENABLE_ALWAYS | If set, the push button is always enabled, even if the user cannot modify the property sheet page (that is, even if CPSUIF_UPDATE_PERMISSION is not set in a [**COMPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_compropsheetui) structure).<br><br>The push button's callback function must display its dialog, but it must not allow user modifications.<br><br>Note that you must also set this flag in the **Flags** member of the [**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype) structure. |
| OTS_PUSH_INCL_SETUP_TITLE | If set, CPSUI includes the word "Setup" after the button's name string (**pName** in OPTITEM). |
| OTS_PUSH_NO_DOT_DOT_DOT | If set, CPSUI includes three dots (...) after the button's name string (**pName** in OPTITEM). |

**BegCtrlID**  
If **pDlgPage** in [**COMPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_compropsheetui) identifies a CPSUI-supplied page, or if **DlgTemplateID** in [**DLGPAGE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_dlgpage) identifies a CPSUI-supplied template, **BegCtrlID** is not used. Otherwise, **BegCtrlID** must contain the first control identifier of a sequentially numbered set of control identifiers. Control identifiers must identify the following Windows controls:

| Control Identifier | Windows Control |
|--|--|
| **BegCtrlID** contents | Group box |
| **BegCtrlID** contents+1 | Title text |
| **BegCtrlID** contents+2 | Push button box |
| **BegCtrlID** contents+3 | Push button icon |
| **BegCtrlID** contents+4 | Extended check box or extended push button (optional) |
| **BegCtrlID** contents+5 | Extended check box or extended push button icon (optional) |

For additional information, see [Customizing CPSUI-Supported Window Controls](customizing-cpsui-supported-window-controls.md).

## Requirements

**Header:** compstui.h (include Compstui.h)

## See also

[**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem)

[**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam)

[**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype)
