---
title: General WIA Utility Functions
description: General WIA Utility Functions
ms.assetid: 235c07a1-4903-4df6-b29f-0ecc342782b4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General WIA Utility Functions





You can use the following functions to retrieve the driver item context, retrieve information from the system registry, and copy a string.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550166" data-raw-source="[&lt;strong&gt;wiauGetDrvItemContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550166)"><strong>wiauGetDrvItemContext</strong></a></p></td>
<td><p>Gets the driver item context and, optionally, the driver item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550169" data-raw-source="[&lt;strong&gt;wiauGetResourceString&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550169)"><strong>wiauGetResourceString</strong></a></p></td>
<td><p>Gets a resource string, storing it as a <strong>BSTR</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550170" data-raw-source="[&lt;strong&gt;wiauGetValidFormats&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550170)"><strong>wiauGetValidFormats</strong></a></p></td>
<td><p>Calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543986" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvGetWiaFormatInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543986)"><strong>IWiaMiniDrv::drvGetWiaFormatInfo</strong></a> method and makes a list of valid formats, using a specified TYMED value.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550171" data-raw-source="[&lt;strong&gt;wiauPropInPropSpec&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550171)"><strong>wiauPropInPropSpec</strong></a></p></td>
<td><p>Determines whether a specified property specification identifier (ID) is contained in an array of such values. The function optionally gets the index where the property specification ID was found.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550173" data-raw-source="[&lt;strong&gt;wiauPropsInPropSpec&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550173)"><strong>wiauPropsInPropSpec</strong></a></p></td>
<td><p>Determines whether any of a list of property specification IDs is contained within an array of such values.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550176" data-raw-source="[&lt;strong&gt;wiauRegGetDword&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550176)"><strong>wiauRegGetDword</strong></a></p></td>
<td><p>Gets a <strong>DWORD</strong> value from the <strong>DeviceData</strong> section of the registry.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550178" data-raw-source="[&lt;strong&gt;wiauRegGetStr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550178)"><strong>wiauRegGetStr</strong></a></p></td>
<td><p>Gets a string value from the <strong>DeviceData</strong> section of the registry.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550179" data-raw-source="[&lt;strong&gt;wiauRegOpenData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550179)"><strong>wiauRegOpenData</strong></a></p></td>
<td><p>Opens the <strong>DeviceData</strong> registry key.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550181" data-raw-source="[&lt;strong&gt;wiauSetImageItemSize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550181)"><strong>wiauSetImageItemSize</strong></a></p></td>
<td><p>Calculates the size and width, in bytes, for an image, based on the current WIA_IPA_FORMAT setting (defined in the Microsoft Windows SDK documentation), and writes the new values to the appropriate properties.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550183" data-raw-source="[&lt;strong&gt;wiauStrC2C&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550183)"><strong>wiauStrC2C</strong></a></p></td>
<td><p>Copies an ANSI character string to another ANSI character string.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550186" data-raw-source="[&lt;strong&gt;wiauStrC2W&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550186)"><strong>wiauStrC2W</strong></a></p></td>
<td><p>Converts an ANSI character string to a Unicode string.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550187" data-raw-source="[&lt;strong&gt;wiauStrW2C&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550187)"><strong>wiauStrW2C</strong></a></p></td>
<td><p>Converts a Unicode string to an ANSI character string.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550189" data-raw-source="[&lt;strong&gt;wiauStrW2W&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550189)"><strong>wiauStrW2W</strong></a></p></td>
<td><p>Copies a Unicode string to another Unicode string.</p></td>
</tr>
</tbody>
</table>

 

 

 




