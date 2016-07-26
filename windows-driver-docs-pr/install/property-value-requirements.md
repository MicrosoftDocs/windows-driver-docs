---
title: Property Value Requirements
description: Property Value Requirements
ms.assetid: 05512f3d-fe64-4de0-848c-c983d883fc60
keywords: ["device properties WDK device installations , property value requirements"]
---

# Property Value Requirements


Windows enforces the device property value size requirements that are listed in the following table. Windows only sets a device property value if the device property value complies with these value size requirements.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Property data type</th>
<th align="left">Property value size requirement</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>A fixed-length [<strong>base-data-type</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537793) value</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes in the base data type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>An array of a fixed-length base-data-type values</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes of an array of zero or more base-data-type values.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>A [<strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543608) data type value</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes of a variable-length, self-relative SECURITY_DESCRIPTOR structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>A [<strong>DEVPROP_TYPE_STRING</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543612) data type value, a [<strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543609) data type value, or a [<strong>DEVPROP_TYPE_STRING_INDIRECT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543613) data type value</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes of a Unicode REG_SZ string, including the NULL-terminator.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>A list of DEVPROP_TYPE_STRING-typed strings, a list of DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING-typed strings, or a DEVPROP_TYPE_STRING_LIST data type value</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes of a Unicode REG_MULTLI_SZ list of strings, including the final NULL-terminator that terminates the list of strings.</p></td>
</tr>
<tr class="even">
<td align="left"><p>All property values</p></td>
<td align="left"><p>In addition to the property value size requirements that are listed in the other rows of this table, the maximum size, in bytes, of a property value is UNICODE_STRING_MAX_BYTES.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Property%20Value%20Requirements%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




