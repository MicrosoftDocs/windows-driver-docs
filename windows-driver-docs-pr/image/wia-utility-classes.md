---
title: WIA Utility Classes
author: windows-driver-content
ms.assetid: cc20a088-6470-4648-b7d9-999dbd74baf1
description: 
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>CWiauDbgFn::CWiauDbgFn</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540348)</p></td>
<td><p>Class constructor.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauDbgFn::~CWiauDbgFn</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540356)</p></td>
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
<td><p>[<strong>CWiauFormatConverter::CWiauFormatConverter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540370)</p></td>
<td><p>Class constructor.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauFormatConverter::~CWiauFormatConverter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540385)</p></td>
<td><p>Class destructor.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauFormatConverter::ConvertToBmp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540369)</p></td>
<td><p>Converts an image to BMP format.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauFormatConverter::Init</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540374)</p></td>
<td><p>Initializes the class and GDI+ for converting images.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauFormatConverter::IsFormatSupported</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540379)</p></td>
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
<td><p>[<strong>CWiauPropertyList::CWiauPropertyList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540389)</p></td>
<td><p>Class constructor.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauPropertyList::~CWiauPropertyList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540472)</p></td>
<td><p>Class destructor.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauPropertyList::DefineProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540391)</p></td>
<td><p>Adds a property definition to the property list object.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauPropertyList::GetPropId</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540392)</p></td>
<td><p>Gets the property identifier (ID) for a property at a specified index.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauPropertyList::Init</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540396)</p></td>
<td><p>Initializes the property list object.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauPropertyList::LookupPropId</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540400)</p></td>
<td><p>Gets the property index for a property with a specified property ID.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauPropertyList::SendToWia</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540403)</p></td>
<td><p>Calls the WIA service to define all the properties currently contained in a property list object.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauPropertyList::SetAccessSubType</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540407)</p></td>
<td><p>Resets the access and subtype of a property.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauPropertyList::SetCurrentValue(BYTE*)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540412)</p></td>
<td><p>Sets the value of a property whose type is of <strong>BYTE</strong> array.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauPropertyList::SetCurrentValue(BSTR)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540410)</p></td>
<td><p>Sets the value of a property whose type is <strong>BSTR</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauPropertyList::SetCurrentValue(CLSID)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540416)</p></td>
<td><p>Sets the value of a property whose type is <strong>CLSID</strong>.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauPropertyList::SetCurrentValue(FLOAT)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540423)</p></td>
<td><p>Sets the value of a property whose type is <strong>FLOAT</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauPropertyList::SetCurrentValue(LONG)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540427)</p></td>
<td><p>Sets the value of a property whose type is <strong>LONG</strong>.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauPropertyList::SetCurrentValue(SYSTEMTIME)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540430)</p></td>
<td><p>Sets the value of a property whose type is <strong>SYSTEMTIME</strong> (described in the Microsoft Windows SDK documentation).</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauPropertyList::SetValidValues(BSTR, list)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540436)</p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>BSTR</strong> values.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauPropertyList::SetValidValues(CLSID, list)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540439)</p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>CLSID</strong> values.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauPropertyList::SetValidValues(flag)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540447)</p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a property whose values are determined by flag settings.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauPropertyList::SetValidValues(FLOAT, list)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540452)</p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>FLOAT</strong> values.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauPropertyList::SetValidValues(FLOAT, range)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540461)</p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a range of <strong>FLOAT</strong> values.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CWiauPropertyList::SetValidValues(LONG, list)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540462)</p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a list of <strong>LONG</strong> values.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CWiauPropertyList::SetValidValues(LONG, range)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540468)</p></td>
<td><p>Sets the type, as well as the default, current, and valid values of a range of <strong>LONG</strong> values.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Utility%20Classes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


