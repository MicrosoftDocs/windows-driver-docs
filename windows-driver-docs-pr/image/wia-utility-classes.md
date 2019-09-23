---
title: WIA Utility Classes
ms.assetid: cc20a088-6470-4648-b7d9-999dbd74baf1
description: 
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Utility Classes


This topic describes the three helper classes that are part of the WIA Utility Library:

-   [CWiauDbgFn Class](#cwiaudbgfn-class)
-   [CWiauFormatConverter Class](#cwiauformatconverter-class)
-   [CWiauPropertyList Class](#cwiaupropertylist-class)

## CWiauDbgFn Class


The [CWiauDbgFn Class](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540345(v=vs.85)) is a helper class for function or method entry/exit point tracing.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaudbgfn-cwiaudbgfn" data-raw-source="[&lt;strong&gt;CWiauDbgFn::CWiauDbgFn&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaudbgfn-cwiaudbgfn)"><strong>CWiauDbgFn::CWiauDbgFn</strong></a></p></td>
<td><p>Class constructor.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaudbgfn-~cwiaudbgfn" data-raw-source="[&lt;strong&gt;CWiauDbgFn::~CWiauDbgFn&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaudbgfn-~cwiaudbgfn)"><strong>CWiauDbgFn::~CWiauDbgFn</strong></a></p></td>
<td><p>Class destructor.</p></td>
</tr>
</tbody>
</table>

 

## CWiauFormatConverter Class


The [CWiauFormatConverter Class](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540363(v=vs.85)) is a helper class for converting images to BMP format.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiauformatconverter-cwiauformatconverter" data-raw-source="[&lt;strong&gt;CWiauFormatConverter::CWiauFormatConverter&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiauformatconverter-cwiauformatconverter)"><strong>CWiauFormatConverter::CWiauFormatConverter</strong></a></p></td>
<td><p>Class constructor.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiauformatconverter-~cwiauformatconverter" data-raw-source="[&lt;strong&gt;CWiauFormatConverter::~CWiauFormatConverter&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiauformatconverter-~cwiauformatconverter)"><strong>CWiauFormatConverter::~CWiauFormatConverter</strong></a></p></td>
<td><p>Class destructor.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiauformatconverter-converttobmp" data-raw-source="[&lt;strong&gt;CWiauFormatConverter::ConvertToBmp&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiauformatconverter-converttobmp)"><strong>CWiauFormatConverter::ConvertToBmp</strong></a></p></td>
<td><p>Converts an image to BMP format.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiauformatconverter-init" data-raw-source="[&lt;strong&gt;CWiauFormatConverter::Init&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiauformatconverter-init)"><strong>CWiauFormatConverter::Init</strong></a></p></td>
<td><p>Initializes the class and GDI+ for converting images.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiauformatconverter-isformatsupported" data-raw-source="[&lt;strong&gt;CWiauFormatConverter::IsFormatSupported&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiauformatconverter-isformatsupported)"><strong>CWiauFormatConverter::IsFormatSupported</strong></a></p></td>
<td><p>Verifies that GDI+ supports the image format to be converted.</p></td>
</tr>
</tbody>
</table>

 

## CWiauPropertyList Class


The [CWiauPropertyList Class](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540386(v=vs.85)) is a helper class for defining and initializing WIA property lists.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-cwiaupropertylist" data-raw-source="[&lt;strong&gt;CWiauPropertyList::CWiauPropertyList&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-cwiaupropertylist)"><strong>CWiauPropertyList::CWiauPropertyList</strong></a></p></td>
<td><p>Class constructor.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-~cwiaupropertylist" data-raw-source="[&lt;strong&gt;CWiauPropertyList::~CWiauPropertyList&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-~cwiaupropertylist)"><strong>CWiauPropertyList::~CWiauPropertyList</strong></a></p></td>
<td><p>Class destructor.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-defineproperty" data-raw-source="[&lt;strong&gt;CWiauPropertyList::DefineProperty&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-defineproperty)"><strong>CWiauPropertyList::DefineProperty</strong></a></p></td>
<td><p>Adds a property definition to the property list object.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-getpropid" data-raw-source="[&lt;strong&gt;CWiauPropertyList::GetPropId&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-getpropid)"><strong>CWiauPropertyList::GetPropId</strong></a></p></td>
<td><p>Gets the property identifier (ID) for a property at a specified index.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-init" data-raw-source="[&lt;strong&gt;CWiauPropertyList::Init&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-init)"><strong>CWiauPropertyList::Init</strong></a></p></td>
<td><p>Initializes the property list object.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-lookuppropid" data-raw-source="[&lt;strong&gt;CWiauPropertyList::LookupPropId&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-lookuppropid)"><strong>CWiauPropertyList::LookupPropId</strong></a></p></td>
<td><p>Gets the property index for a property with a specified property ID.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-sendtowia" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SendToWia&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-sendtowia)"><strong>CWiauPropertyList::SendToWia</strong></a></p></td>
<td><p>Calls the WIA service to define all the properties currently contained in a property list object.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-setaccesssubtype(int_ulong_ulong)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetAccessSubType&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wiautil/nf-wiautil-cwiaupropertylist-setaccesssubtype(int_ulong_ulong))"><strong>CWiauPropertyList::SetAccessSubType</strong></a></p></td>
<td><p>Resets the access and subtype of a property.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540412(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(BYTE*)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540412(v=vs.85))"><strong>CWiauPropertyList::SetCurrentValue(BYTE*)</strong></a></p></td>
<td><p>Sets the value of a property whose type is of <strong>BYTE</strong> array.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540410(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(BSTR)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540410(v=vs.85))"><strong>CWiauPropertyList::SetCurrentValue(BSTR)</strong></a></p></td>
<td><p>Sets the value of a property whose type is <strong>BSTR</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540416(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(CLSID)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540416(v=vs.85))"><strong>CWiauPropertyList::SetCurrentValue(CLSID)</strong></a></p></td>
<td><p>Sets the value of a property whose type is <strong>CLSID</strong>.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540423(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(FLOAT)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540423(v=vs.85))"><strong>CWiauPropertyList::SetCurrentValue(FLOAT)</strong></a></p></td>
<td><p>Sets the value of a property whose type is <strong>FLOAT</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540427(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(LONG)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540427(v=vs.85))"><strong>CWiauPropertyList::SetCurrentValue(LONG)</strong></a></p></td>
<td><p>Sets the value of a property whose type is <strong>LONG</strong>.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540430(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(SYSTEMTIME)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540430(v=vs.85))"><strong>CWiauPropertyList::SetCurrentValue(SYSTEMTIME)</strong></a></p></td>
<td><p>Sets the value of a property whose type is <strong>SYSTEMTIME</strong> (described in the Microsoft Windows SDK documentation).</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540436(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(BSTR, list)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540436(v=vs.85))"><strong>CWiauPropertyList::SetValidValues(BSTR, list)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>BSTR</strong> values.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540439(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(CLSID, list)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540439(v=vs.85))"><strong>CWiauPropertyList::SetValidValues(CLSID, list)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>CLSID</strong> values.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540447(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(flag)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540447(v=vs.85))"><strong>CWiauPropertyList::SetValidValues(flag)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a property whose values are determined by flag settings.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540452(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(FLOAT, list)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540452(v=vs.85))"><strong>CWiauPropertyList::SetValidValues(FLOAT, list)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>FLOAT</strong> values.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540461(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(FLOAT, range)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540461(v=vs.85))"><strong>CWiauPropertyList::SetValidValues(FLOAT, range)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a range of <strong>FLOAT</strong> values.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540462(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(LONG, list)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540462(v=vs.85))"><strong>CWiauPropertyList::SetValidValues(LONG, list)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>LONG</strong> values.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540468(v=vs.85)" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(LONG, range)&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff540468(v=vs.85))"><strong>CWiauPropertyList::SetValidValues(LONG, range)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a range of <strong>LONG</strong> values.</p></td>
</tr>
</tbody>
</table>

 

 

 




