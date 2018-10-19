---
title: General WIA Utility Functions
author: windows-driver-content
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
<td><p>[<strong>wiauGetDrvItemContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550166)</p></td>
<td><p>Gets the driver item context and, optionally, the driver item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauGetResourceString</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550169)</p></td>
<td><p>Gets a resource string, storing it as a <strong>BSTR</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauGetValidFormats</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550170)</p></td>
<td><p>Calls the [<strong>IWiaMiniDrv::drvGetWiaFormatInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543986) method and makes a list of valid formats, using a specified TYMED value.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauPropInPropSpec</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550171)</p></td>
<td><p>Determines whether a specified property specification identifier (ID) is contained in an array of such values. The function optionally gets the index where the property specification ID was found.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauPropsInPropSpec</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550173)</p></td>
<td><p>Determines whether any of a list of property specification IDs is contained within an array of such values.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauRegGetDword</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550176)</p></td>
<td><p>Gets a <strong>DWORD</strong> value from the <strong>DeviceData</strong> section of the registry.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauRegGetStr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550178)</p></td>
<td><p>Gets a string value from the <strong>DeviceData</strong> section of the registry.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauRegOpenData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550179)</p></td>
<td><p>Opens the <strong>DeviceData</strong> registry key.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauSetImageItemSize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550181)</p></td>
<td><p>Calculates the size and width, in bytes, for an image, based on the current WIA_IPA_FORMAT setting (defined in the Microsoft Windows SDK documentation), and writes the new values to the appropriate properties.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauStrC2C</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550183)</p></td>
<td><p>Copies an ANSI character string to another ANSI character string.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauStrC2W</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550186)</p></td>
<td><p>Converts an ANSI character string to a Unicode string.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>wiauStrW2C</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550187)</p></td>
<td><p>Converts a Unicode string to an ANSI character string.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>wiauStrW2W</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550189)</p></td>
<td><p>Copies a Unicode string to another Unicode string.</p></td>
</tr>
</tbody>
</table>

 

 

 




