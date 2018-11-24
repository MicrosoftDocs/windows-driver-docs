---
title: Property Value Requirements
description: Property Value Requirements
ms.assetid: 05512f3d-fe64-4de0-848c-c983d883fc60
keywords:
- device properties WDK device installations , property value requirements
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p>A fixed-length <a href="https://msdn.microsoft.com/library/windows/hardware/ff537793" data-raw-source="[&lt;strong&gt;base-data-type&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537793)"><strong>base-data-type</strong></a> value</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes in the base data type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>An array of a fixed-length base-data-type values</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes of an array of zero or more base-data-type values.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff543608" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_SECURITY_DESCRIPTOR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543608)"><strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR</strong></a> data type value</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes of a variable-length, self-relative SECURITY_DESCRIPTOR structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff543612" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543612)"><strong>DEVPROP_TYPE_STRING</strong></a> data type value, a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543609" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543609)"><strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING</strong></a> data type value, or a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543613" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_INDIRECT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543613)"><strong>DEVPROP_TYPE_STRING_INDIRECT</strong></a> data type value</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes of a Unicode <a href="https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types" data-raw-source="[REG_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types)">REG_SZ</a> string, including the NULL-terminator.</p></td>
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

 

 

 





