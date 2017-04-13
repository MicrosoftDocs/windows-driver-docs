---
title: General WIA Utility Functions
author: windows-driver-content
description: General WIA Utility Functions
ms.assetid: 235c07a1-4903-4df6-b29f-0ecc342782b4
---

# General WIA Utility Functions


## <a href="" id="ddk-general-wia-utility-functions-si"></a>


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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20General%20WIA%20Utility%20Functions%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


