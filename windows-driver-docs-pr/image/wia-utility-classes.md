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


The [CWiauDbgFn Class](https://msdn.microsoft.com/library/windows/hardware/ff540345) is a helper class for function or method entry/exit point tracing.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540348" data-raw-source="[&lt;strong&gt;CWiauDbgFn::CWiauDbgFn&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540348)"><strong>CWiauDbgFn::CWiauDbgFn</strong></a></p></td>
<td><p>Class constructor.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540356" data-raw-source="[&lt;strong&gt;CWiauDbgFn::~CWiauDbgFn&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540356)"><strong>CWiauDbgFn::~CWiauDbgFn</strong></a></p></td>
<td><p>Class destructor.</p></td>
</tr>
</tbody>
</table>

 

## CWiauFormatConverter Class


The [CWiauFormatConverter Class](https://msdn.microsoft.com/library/windows/hardware/ff540363) is a helper class for converting images to BMP format.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540370" data-raw-source="[&lt;strong&gt;CWiauFormatConverter::CWiauFormatConverter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540370)"><strong>CWiauFormatConverter::CWiauFormatConverter</strong></a></p></td>
<td><p>Class constructor.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540385" data-raw-source="[&lt;strong&gt;CWiauFormatConverter::~CWiauFormatConverter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540385)"><strong>CWiauFormatConverter::~CWiauFormatConverter</strong></a></p></td>
<td><p>Class destructor.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540369" data-raw-source="[&lt;strong&gt;CWiauFormatConverter::ConvertToBmp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540369)"><strong>CWiauFormatConverter::ConvertToBmp</strong></a></p></td>
<td><p>Converts an image to BMP format.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540374" data-raw-source="[&lt;strong&gt;CWiauFormatConverter::Init&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540374)"><strong>CWiauFormatConverter::Init</strong></a></p></td>
<td><p>Initializes the class and GDI+ for converting images.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540379" data-raw-source="[&lt;strong&gt;CWiauFormatConverter::IsFormatSupported&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540379)"><strong>CWiauFormatConverter::IsFormatSupported</strong></a></p></td>
<td><p>Verifies that GDI+ supports the image format to be converted.</p></td>
</tr>
</tbody>
</table>

 

## CWiauPropertyList Class


The [CWiauPropertyList Class](https://msdn.microsoft.com/library/windows/hardware/ff540386) is a helper class for defining and initializing WIA property lists.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540389" data-raw-source="[&lt;strong&gt;CWiauPropertyList::CWiauPropertyList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540389)"><strong>CWiauPropertyList::CWiauPropertyList</strong></a></p></td>
<td><p>Class constructor.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540472" data-raw-source="[&lt;strong&gt;CWiauPropertyList::~CWiauPropertyList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540472)"><strong>CWiauPropertyList::~CWiauPropertyList</strong></a></p></td>
<td><p>Class destructor.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540391" data-raw-source="[&lt;strong&gt;CWiauPropertyList::DefineProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540391)"><strong>CWiauPropertyList::DefineProperty</strong></a></p></td>
<td><p>Adds a property definition to the property list object.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540392" data-raw-source="[&lt;strong&gt;CWiauPropertyList::GetPropId&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540392)"><strong>CWiauPropertyList::GetPropId</strong></a></p></td>
<td><p>Gets the property identifier (ID) for a property at a specified index.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540396" data-raw-source="[&lt;strong&gt;CWiauPropertyList::Init&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540396)"><strong>CWiauPropertyList::Init</strong></a></p></td>
<td><p>Initializes the property list object.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540400" data-raw-source="[&lt;strong&gt;CWiauPropertyList::LookupPropId&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540400)"><strong>CWiauPropertyList::LookupPropId</strong></a></p></td>
<td><p>Gets the property index for a property with a specified property ID.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540403" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SendToWia&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540403)"><strong>CWiauPropertyList::SendToWia</strong></a></p></td>
<td><p>Calls the WIA service to define all the properties currently contained in a property list object.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540407" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetAccessSubType&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540407)"><strong>CWiauPropertyList::SetAccessSubType</strong></a></p></td>
<td><p>Resets the access and subtype of a property.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540412" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(BYTE*)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540412)"><strong>CWiauPropertyList::SetCurrentValue(BYTE*)</strong></a></p></td>
<td><p>Sets the value of a property whose type is of <strong>BYTE</strong> array.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540410" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(BSTR)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540410)"><strong>CWiauPropertyList::SetCurrentValue(BSTR)</strong></a></p></td>
<td><p>Sets the value of a property whose type is <strong>BSTR</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540416" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(CLSID)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540416)"><strong>CWiauPropertyList::SetCurrentValue(CLSID)</strong></a></p></td>
<td><p>Sets the value of a property whose type is <strong>CLSID</strong>.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540423" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(FLOAT)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540423)"><strong>CWiauPropertyList::SetCurrentValue(FLOAT)</strong></a></p></td>
<td><p>Sets the value of a property whose type is <strong>FLOAT</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540427" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(LONG)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540427)"><strong>CWiauPropertyList::SetCurrentValue(LONG)</strong></a></p></td>
<td><p>Sets the value of a property whose type is <strong>LONG</strong>.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540430" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetCurrentValue(SYSTEMTIME)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540430)"><strong>CWiauPropertyList::SetCurrentValue(SYSTEMTIME)</strong></a></p></td>
<td><p>Sets the value of a property whose type is <strong>SYSTEMTIME</strong> (described in the Microsoft Windows SDK documentation).</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540436" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(BSTR, list)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540436)"><strong>CWiauPropertyList::SetValidValues(BSTR, list)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>BSTR</strong> values.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540439" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(CLSID, list)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540439)"><strong>CWiauPropertyList::SetValidValues(CLSID, list)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>CLSID</strong> values.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540447" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(flag)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540447)"><strong>CWiauPropertyList::SetValidValues(flag)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a property whose values are determined by flag settings.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540452" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(FLOAT, list)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540452)"><strong>CWiauPropertyList::SetValidValues(FLOAT, list)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>FLOAT</strong> values.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540461" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(FLOAT, range)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540461)"><strong>CWiauPropertyList::SetValidValues(FLOAT, range)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a range of <strong>FLOAT</strong> values.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540462" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(LONG, list)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540462)"><strong>CWiauPropertyList::SetValidValues(LONG, list)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>LONG</strong> values.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540468" data-raw-source="[&lt;strong&gt;CWiauPropertyList::SetValidValues(LONG, range)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540468)"><strong>CWiauPropertyList::SetValidValues(LONG, range)</strong></a></p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a range of <strong>LONG</strong> values.</p></td>
</tr>
</tbody>
</table>

 

 

 




