---
title: TVOT\_EDITBOX
description: TVOT\_EDITBOX
ms.assetid: efbfe6ff-129d-4bf5-a0e3-3cae575dfcd7
keywords: ["TVOT_EDITBOX Print Devices"]
topic_type:
- apiref
api_name:
- TVOT_EDITBOX
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# TVOT\_EDITBOX


## <span id="ddk_tvot_editbox_gg"></span><span id="DDK_TVOT_EDITBOX_GG"></span>


The TVOT\_EDITBOX option type consists of an edit box inside a group box.

<span id="OPTITEM_Structure"></span><span id="optitem_structure"></span><span id="OPTITEM_STRUCTURE"></span>[**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) Structure  

<span id="Sel_pSel"></span><span id="sel_psel"></span><span id="SEL_PSEL"></span>**Sel/pSel**  
Application-supplied pointer to a NULL-terminated string containing the current contents of the edit box.

<span id="OPTPARAM_Structure_Array__pOptParam_member_of_OPTTYPE_"></span><span id="optparam_structure_array__poptparam_member_of_opttype_"></span><span id="OPTPARAM_STRUCTURE_ARRAY__POPTPARAM_MEMBER_OF_OPTTYPE_"></span>[**OPTPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff559660) Structure Array (**pOptParam** member of [**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670))  

<span id="pData"></span><span id="pdata"></span><span id="PDATA"></span>**pData**  
**pOptParam**\[0\]-&gt;**pData** points to a NULL-terminated text string to be displayed to the right of the editt box.

**pOptParam**\[1\]-&gt;**pData** points to a NULL-terminated text string to be displayed above the edit box.

<span id="IconID"></span><span id="iconid"></span><span id="ICONID"></span>**IconID**  
**pOptParam**\[0\]-&gt;**IconID** identifies an icon to be associated with the edit box.

**pOptParam**\[1\]-&gt;**IconID** is used for specifying the size, in bytes, of both the edit box and the buffer pointed to by **pSel** in the OPTITEM structure.

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>**lParam**  
Not used.

<span id="OPTTYPE_Structure"></span><span id="opttype_structure"></span><span id="OPTTYPE_STRUCTURE"></span>[**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670) Structure  

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>**Type**  
TVOT\_EDITBOX

<span id="Count"></span><span id="count"></span><span id="COUNT"></span>**Count**  
2

<span id="Style"></span><span id="style"></span><span id="STYLE"></span>**Style**  
Not used.

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
<td><p>Edit box</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+3</p></td>
<td><p>Edit box icon</p></td>
</tr>
<tr class="odd">
<td><p><strong>BegCtrlID</strong> contents+4</p></td>
<td><p>Text positioned to the right of the edit box</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+5</p></td>
<td><p>Text positioned above the edit box</p></td>
</tr>
<tr class="odd">
<td><p><strong>BegCtrlID</strong> contents+6</p></td>
<td><p>Extended check box or extended push button (optional)</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+7</p></td>
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

 

 




