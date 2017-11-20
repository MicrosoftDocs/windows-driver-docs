---
title: TVOT\_UDARROW
description: TVOT\_UDARROW
MS-HAID:
- 'cpsuifnc\_2ba8e551-7619-45b1-acb0-59ef74fcbfd6.xml'
- 'print.tvot\_udarrow'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c1182cc5-5d82-4db5-8ef2-7d2601499e72
keywords: ["TVOT_UDARROW Print Devices"]
topic_type:
- apiref
api_name:
- TVOT_UDARROW
api_location:
- compstui.h
api_type:
- HeaderDef
---

# TVOT\_UDARROW


## <span id="ddk_tvot_udarrow_gg"></span><span id="DDK_TVOT_UDARROW_GG"></span>


The TVOT\_UDARROW option type consists of an up-down control and an edit control inside a group box.

<span id="OPTITEM_Structure"></span><span id="optitem_structure"></span><span id="OPTITEM_STRUCTURE"></span>[**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) Structure  

<span id="Sel_pSel"></span><span id="sel_psel"></span><span id="SEL_PSEL"></span>**Sel/pSel**  
Numeric value representing the edit control's current contents.

<span id="OPTPARAM_Structure_Array__pOptParam_member_of_OPTTYPE_"></span><span id="optparam_structure_array__poptparam_member_of_opttype_"></span><span id="OPTPARAM_STRUCTURE_ARRAY__POPTPARAM_MEMBER_OF_OPTTYPE_"></span>[**OPTPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff559660) Structure Array (**pOptParam** member of [**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670))  

<span id="pData"></span><span id="pdata"></span><span id="PDATA"></span>**pData**  
**pOptParam**\[0\]-&gt;**pData** points to a NULL-terminated text string identifying the control's units.

**pOptParam**\[1\]-&gt;**pData** points to a NULL-terminated text string describing the control. (If **NULL**, CPSUI displays the low end and high end of the control's range of values.)

<span id="IconID"></span><span id="iconid"></span><span id="ICONID"></span>**IconID**  
**pOptParam**\[0\]-&gt;**IconID** identifies an icon to be associated with the track bar.

**pOptParam**\[1\]-&gt;**IconID** specifies a 16-bit signed value representing the low end of the control's range.

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>**lParam**  
**pOptParam**\[0\]-&gt;**lParam** is not used.

**pOptParam**\[1\]-&gt;**lParam** specifies a 16-bit signed value representing the high end of the control's range.

<span id="OPTTYPE_Structure"></span><span id="opttype_structure"></span><span id="OPTTYPE_STRUCTURE"></span>[**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670) Structure  

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>**Type**  
TVOT\_UDARROW

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
<td><p>Icon</p></td>
</tr>
<tr class="odd">
<td><p><strong>BegCtrlID</strong> contents+4</p></td>
<td><p>Text describing value units</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+5</p></td>
<td><p>Text describing the control</p></td>
</tr>
<tr class="odd">
<td><p><strong>BegCtrlID</strong> contents+6</p></td>
<td><p>Up-down control</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20TVOT_UDARROW%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




