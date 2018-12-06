---
title: TVOT\_LISTBOX
description: TVOT\_LISTBOX
ms.assetid: 2426ae5a-33e6-4f16-ad49-ff38ea19e392
keywords: ["TVOT_LISTBOX Print Devices"]
topic_type:
- apiref
api_name:
- TVOT_LISTBOX
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# TVOT\_LISTBOX


## <span id="ddk_tvot_listbox_gg"></span><span id="DDK_TVOT_LISTBOX_GG"></span>


The TVOT\_LISTBOX option type consists of a list box inside a group box.

<span id="OPTITEM_Structure"></span><span id="optitem_structure"></span><span id="OPTITEM_STRUCTURE"></span>[**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) Structure  

<span id="Sel_pSel"></span><span id="sel_psel"></span><span id="SEL_PSEL"></span>**Sel/pSel**  
Index into the [**OPTPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff559660) array that is pointed to by the **pOptParam** member of the option's [**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670) structure. This specifies the currently selected option parameter.

<span id="OPTPARAM_Structure_Array__pOptParam_member_of_OPTTYPE_"></span><span id="optparam_structure_array__poptparam_member_of_opttype_"></span><span id="OPTPARAM_STRUCTURE_ARRAY__POPTPARAM_MEMBER_OF_OPTTYPE_"></span>[**OPTPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff559660) Structure Array (**pOptParam** member of [**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670))  

<span id="pData"></span><span id="pdata"></span><span id="PDATA"></span>**pData**  
**pOptParam**\[0\]-&gt;**pData** points to the first text string to be displayed in the list box.

**pOptParam**\[1\]-&gt;**pData** points to the second text string to be displayed in the list box.

**pOptParam**\[*n*\]-&gt;**pData** points to the *n*th text string to be displayed in the list box.

<span id="IconID"></span><span id="iconid"></span><span id="ICONID"></span>**IconID**  
**pOptParam**\[0\]-&gt;**IconID** identifies an icon to be associated with the first text string.

**pOptParam**\[1\]-&gt;**IconID** identifies an icon to be associated with the second text string.

**pOptParam**\[*n*\]-&gt;**IconID** identifies an icon to be associated with the *n*th text string.

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>**lParam**  
Not used.

<span id="OPTTYPE_Structure"></span><span id="opttype_structure"></span><span id="OPTTYPE_STRUCTURE"></span>[**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670) Structure  

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>**Type**  
TVOT\_LISTBOX

<span id="Count"></span><span id="count"></span><span id="COUNT"></span>**Count**  
The number of OPTPARAM structures; that is, the number of text strings to be displayed in the list box.

<span id="Style"></span><span id="style"></span><span id="STYLE"></span>**Style**  
The following optional bit flags can be specified.

<span id="OTS_LBCB_INCL_ITEM_NONE"></span><span id="ots_lbcb_incl_item_none"></span>OTS\_LBCB\_INCL\_ITEM\_NONE  
If set, CPSUI includes a "None" string in the list box. If a user selects "None", the **Sel/pSel** union is set to negative one.

<span id="OTS_LBCB_NO_ICON16_IN_ITEM"></span><span id="ots_lbcb_no_icon16_in_item"></span>OTS\_LBCB\_NO\_ICON16\_IN\_ITEM  
If set, CPSUI does not draw each option parameter's icon (**IconID** in OPTPARAM) when displaying the parameter's value in the list box.

<span id="OTS_LBCB_PROPPAGE_LBUSECB"></span><span id="ots_lbcb_proppage_lbusecb"></span>OTS\_LBCB\_PROPPAGE\_LBUSECB  
When the option is displayed on a nontreeview property sheet page, it is displayed as a combo box instead of a list box.

<span id="OTS_LBCB_SORT"></span><span id="ots_lbcb_sort"></span>OTS\_LBCB\_SORT  
If set, CPSUI displays text strings in alphabetic order.

<span id="BegCtrlID"></span><span id="begctrlid"></span><span id="BEGCTRLID"></span>**BegCtrlID**  
If **pDlgPage** in [**COMPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff546211) identifies a CPSUI-supplied page, or if **DlgTemplateID** in [**DLGPAGE**](https://msdn.microsoft.com/library/windows/hardware/ff547607) identifies a CPSUI-supplied template, **BegCtrlID** is not used.

Otherwise, **BegCtrlID** must contain the first control identifier of a sequentially numbered set of control identifiers. Control identifiers must identify the following Windows controls:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Control Identifier</th>
<th>Windows Control</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>BegCtrlID</strong> contents</p></td>
<td><p>Group box</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+1</p></td>
<td><p>Title text</p></td>
</tr>
<tr class="odd">
<td><p><strong>BegCtrlID</strong> contents+2</p></td>
<td><p>List box</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+3</p></td>
<td><p>List box icon</p></td>
</tr>
<tr class="odd">
<td><p><strong>BegCtrlID</strong> contents+4</p></td>
<td><p>Extended check box or extended push button (optional)</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+5</p></td>
<td><p>Extended check box or extended push button icon (optional)</p></td>
</tr>
</tbody>
</table>

 

For additional information, see [Customizing CPSUI-Supported Window Controls](https://msdn.microsoft.com/library/windows/hardware/ff547296).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Compstui.h (include Compstui.h)</td>
</tr>
</tbody>
</table>

 

 




