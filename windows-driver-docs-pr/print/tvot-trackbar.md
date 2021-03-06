---
title: TVOT\_TRACKBAR
description: TVOT\_TRACKBAR
keywords: ["TVOT_TRACKBAR Print Devices"]
topic_type:
- apiref
api_name:
- TVOT_TRACKBAR
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# TVOT\_TRACKBAR


## <span id="ddk_tvot_trackbar_gg"></span><span id="DDK_TVOT_TRACKBAR_GG"></span>


The TVOT\_TRACKBAR option type consists of a track bar inside a group box.

<span id="OPTITEM_Structure"></span><span id="optitem_structure"></span><span id="OPTITEM_STRUCTURE"></span>[**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem) Structure  

<span id="Sel_pSel"></span><span id="sel_psel"></span><span id="SEL_PSEL"></span>**Sel/pSel**  
Value representing the current track bar position.

<span id="OPTPARAM_Structure_Array__pOptParam_member_of_OPTTYPE_"></span><span id="optparam_structure_array__poptparam_member_of_opttype_"></span><span id="OPTPARAM_STRUCTURE_ARRAY__POPTPARAM_MEMBER_OF_OPTTYPE_"></span>[**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam) Structure Array (**pOptParam** member of [**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype))  

<span id="pData"></span><span id="pdata"></span><span id="PDATA"></span>**pData**  
**pOptParam**\[0\]-&gt;**pData** points to a NULL-terminated text string identifying the track bar units.

**pOptParam**\[1\]-&gt;**pData** points to a NULL-terminated text string describing the low end of the track bar's range.

**pOptParam**\[2\]-&gt;**pData** points to a NULL-terminated text string describing the high end of the track bar's range.

<span id="IconID"></span><span id="iconid"></span><span id="ICONID"></span>**IconID**  
**pOptParam**\[0\]-&gt;**IconID** identifies an icon to be associated with the track bar.

**pOptParam**\[1\]-&gt;**IconID** specifies a 16-bit signed value representing the low end of the track bar's range.

**pOptParam**\[2\]-&gt;**IconID** specifies the multiplication factor that is applied to the selected track position gefore its value is displayed. (Usually, this value is 1.)

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>**lParam**  
**pOptParam**\[0\]-&gt;**lParam** is not used.

**pOptParam**\[1\]-&gt;**lParam** specifies a 16-bit signed value representing the high end of the track bar's range.

**pOptParam**\[2\]-&gt;**lParam** specifies the tracking increment value.

<span id="OPTTYPE_Structure"></span><span id="opttype_structure"></span><span id="OPTTYPE_STRUCTURE"></span>[**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype) Structure  

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>**Type**  
TVOT\_TRACKBAR

<span id="Count"></span><span id="count"></span><span id="COUNT"></span>**Count**  
3

<span id="Style"></span><span id="style"></span><span id="STYLE"></span>**Style**  
Not used.

<span id="BegCtrlID"></span><span id="begctrlid"></span><span id="BEGCTRLID"></span>**BegCtrlID**  
If **pDlgPage** in [**COMPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_compropsheetui) identifies a CPSUI-supplied page, or if **DlgTemplateID** in [**DLGPAGE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_dlgpage) identifies a CPSUI-supplied template, **BegCtrlID** is not used.

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
<td><p>Track bar</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+3</p></td>
<td><p>Track bar icon</p></td>
</tr>
<tr class="odd">
<td><p><strong>BegCtrlID</strong> contents+4</p></td>
<td><p>Text describing the low end of the track bar range</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+5</p></td>
<td><p>Text describing the high end of the track bar range</p></td>
</tr>
<tr class="odd">
<td><p><strong>BegCtrlID</strong> contents+6</p></td>
<td><p>Text describing the track bar units</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+7</p></td>
<td><p>Extended check box or extended push button (optional)</p></td>
</tr>
<tr class="odd">
<td><p><strong>BegCtrlID</strong> contents+8</p></td>
<td><p>Extended check box or extended push button icon (optional)</p></td>
</tr>
</tbody>
</table>

 

For additional information, see [Customizing CPSUI-Supported Window Controls](./customizing-cpsui-supported-window-controls.md).

## Requirements

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

 

