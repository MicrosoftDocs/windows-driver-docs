---
title: TVOT\_PUSHBUTTON
description: TVOT\_PUSHBUTTON
ms.assetid: 47d51066-c1bc-4a84-bc9b-5091100b9f53
keywords: ["TVOT_PUSHBUTTON Print Devices"]
topic_type:
- apiref
api_name:
- TVOT_PUSHBUTTON
api_location:
- compstui.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# TVOT\_PUSHBUTTON


## <span id="ddk_tvot_pushbutton_gg"></span><span id="DDK_TVOT_PUSHBUTTON_GG"></span>


The TVOT\_PUSHBUTTON option type consists of a push button inside a group box.

<span id="OPTITEM_Structure"></span><span id="optitem_structure"></span><span id="OPTITEM_STRUCTURE"></span>[**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) Structure  

<span id="Sel_pSel"></span><span id="sel_psel"></span><span id="SEL_PSEL"></span>**Sel/pSel**  
Depends on the **Style** member of the OPTPARAM structure, as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Push Button Style</th>
<th>Sel/pSel Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PUSHBUTTON_TYPE_CALLBACK</p></td>
<td><p>Not used.</p></td>
</tr>
<tr class="even">
<td><p>PUSHBUTTON_TYPE_DLGPROC</p></td>
<td><p>CPSUI stores the return value of the dialog box procedure.</p></td>
</tr>
<tr class="odd">
<td><p>PUSHBUTTON_TYPE_HTCLRADJ</p></td>
<td><p>CPSUI stores the return value of the halftoning operation.</p></td>
</tr>
<tr class="even">
<td><p>PUSHBUTTON_TYPE_HTSETUP</p></td>
<td><p>CPSUI stores the return value of the halftoning operation.</p></td>
</tr>
</tbody>
</table>

 

<span id="OPTPARAM_Structure_Array__pOptParam_member_of_OPTTYPE_"></span><span id="optparam_structure_array__poptparam_member_of_opttype_"></span><span id="OPTPARAM_STRUCTURE_ARRAY__POPTPARAM_MEMBER_OF_OPTTYPE_"></span>[**OPTPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff559660) Structure Array (**pOptParam** member of [**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670))  

<span id="pData"></span><span id="pdata"></span><span id="PDATA"></span>**pData**  
Depends on the **Style** member, as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Push button style</th>
<th>pData usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PUSHBUTTON_TYPE_CALLBACK</p></td>
<td><p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564313" data-raw-source="[&lt;strong&gt;_CPSUICALLBACK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564313)"><strong>_CPSUICALLBACK</strong></a>-typed function.</p></td>
</tr>
<tr class="even">
<td><p>PUSHBUTTON_TYPE_DLGPROC</p></td>
<td><p>DLGPROC-typed pointer to a dialog box procedure (see the Microsoft Windows SDK documentation).</p></td>
</tr>
<tr class="odd">
<td><p>PUSHBUTTON_TYPE_HTCLRADJ</p></td>
<td><p>Pointer to COLORADJUSTMENT structure (described in the Windows SDK documentation).</p></td>
</tr>
<tr class="even">
<td><p>PUSHBUTTON_TYPE_HTSETUP</p></td>
<td><p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552832" data-raw-source="[&lt;strong&gt;DEVHTADJDATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552832)"><strong>DEVHTADJDATA</strong></a> structure.</p></td>
</tr>
</tbody>
</table>

 

<span id="IconID"></span><span id="iconid"></span><span id="ICONID"></span>**IconID**  
Identifies an icon to be associated with the push button.

<span id="___________lParam__________"></span><span id="___________lparam__________"></span><span id="___________LPARAM__________"></span> lParam   
Depends on the Style member, as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Push button style</th>
<th>lParam usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PUSHBUTTON_TYPE_CALLBACK</p></td>
<td><p>Not used.</p></td>
</tr>
<tr class="even">
<td><p>PUSHBUTTON_TYPE_DLGPROC</p></td>
<td><p>Resource identifier for a DIALOG resource, or handle to a DLGTEMPLATE structure (see the Windows SDK documentation). Depends on the DPF_USE_HDLGTEMPLATE flag in the OPTPARAM structure&#39;s <strong>Flags</strong> member.</p></td>
</tr>
<tr class="odd">
<td><p>PUSHBUTTON_TYPE_HTCLRADJ</p></td>
<td><p>Not used.</p></td>
</tr>
<tr class="even">
<td><p>PUSHBUTTON_TYPE_HTSETUP</p></td>
<td><p>Not used.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="___________Style__________"></span><span id="___________style__________"></span><span id="___________STYLE__________"></span> Style</p></td>
<td><p>Specifies the operation to be performed by CPSUI when a user clicks on the push button. Can be one of the following values:</p></td>
</tr>
<tr class="even">
<td><p><span id="PUSHBUTTON_TYPE_CALLBACK"></span><span id="pushbutton_type_callback"></span>PUSHBUTTON_TYPE_CALLBACK</p></td>
<td><p>CPSUI calls the application&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff564313" data-raw-source="[&lt;strong&gt;_CPSUICALLBACK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564313)"><strong>_CPSUICALLBACK</strong></a>-typed callback function to handle button events, with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547088" data-raw-source="[&lt;strong&gt;CPSUICBPARAM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547088)"><strong>CPSUICBPARAM</strong></a> structure&#39;s <strong>Reason</strong> member set to CPSUICB_REASON_PUSHBUTTON. (CPSUI ignores the callback function&#39;s return value.)</p></td>
</tr>
<tr class="odd">
<td><p><span id="PUSHBUTTON_TYPE_DLGPROC"></span><span id="pushbutton_type_dlgproc"></span>PUSHBUTTON_TYPE_DLGPROC</p></td>
<td><p>The application&#39;s dialog box procedure handles button events. (For more information, see the <strong>Remarks</strong> section for <a href="https://msdn.microsoft.com/library/windows/hardware/ff547607" data-raw-source="[&lt;strong&gt;DLGPAGE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547607)"><strong>DLGPAGE</strong></a>.)</p>
<p>When the function receives a WM_INITDIALOG message, its <em>lParam</em> argument points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547088" data-raw-source="[&lt;strong&gt;CPSUICBPARAM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547088)"><strong>CPSUICBPARAM</strong></a> structure with the <strong>Reason</strong> member set to CPSUICB_REASON_DLGPROC.</p></td>
</tr>
<tr class="even">
<td><p><span id="PUSHBUTTON_TYPE_HTCLRADJ"></span><span id="pushbutton_type_htclradj"></span>PUSHBUTTON_TYPE_HTCLRADJ</p></td>
<td><p>CPSUI displays a halftone color adjustment dialog box.</p></td>
</tr>
<tr class="odd">
<td><p><span id="PUSHBUTTON_TYPE_HTSETUP"></span><span id="pushbutton_type_htsetup"></span>PUSHBUTTON_TYPE_HTSETUP</p></td>
<td><p>CPSUI displays a device halftone setup dialog box.</p></td>
</tr>
</tbody>
</table>

 

<span id="OPTTYPE_Structure"></span><span id="opttype_structure"></span><span id="OPTTYPE_STRUCTURE"></span>[**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670) Structure  

<span id="___________Type__________"></span><span id="___________type__________"></span><span id="___________TYPE__________"></span> Type   
TVOT\_PUSHBUTTON

<span id="___________Count__________"></span><span id="___________count__________"></span><span id="___________COUNT__________"></span> Count   
1

<span id="___________Style__________"></span><span id="___________style__________"></span><span id="___________STYLE__________"></span> Style   
The following optional bit flags can be specified.

<span id="OTS_PUSH_ENABLE_ALWAYS"></span><span id="ots_push_enable_always"></span>OTS\_PUSH\_ENABLE\_ALWAYS  
If set, the push button is always enabled, even if the user cannot modify the property sheet page (that is, even if CPSUIF\_UPDATE\_PERMISSION is not set in a [**COMPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff546211) structure).

The push button's callback function must display its dialog, but it must not allow user modifications.

NOTE: You must also set this flag in the **Flags** member of the [**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670) structure.

<span id="OTS_PUSH_INCL_SETUP_TITLE"></span><span id="ots_push_incl_setup_title"></span>OTS\_PUSH\_INCL\_SETUP\_TITLE  
If set, CPSUI includes the word "Setup" after the button's name string (**pName** in OPTITEM).

<span id="OTS_PUSH_NO_DOT_DOT_DOT"></span><span id="ots_push_no_dot_dot_dot"></span>OTS\_PUSH\_NO\_DOT\_DOT\_DOT  
If set, CPSUI includes three dots (...) after the button's name string (**pName** in OPTITEM).

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
<td><p>Push button box</p></td>
</tr>
<tr class="even">
<td><p><strong>BegCtrlID</strong> contents+3</p></td>
<td><p>Push button icon</p></td>
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

 

 




