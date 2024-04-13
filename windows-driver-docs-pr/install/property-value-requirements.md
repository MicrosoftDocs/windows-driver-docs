---
title: Property Value Requirements
description: Property Value Requirements
keywords:
- device properties WDK device installations , property value requirements
ms.date: 04/20/2017
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
<td align="left"><p>A fixed-length <a href="/previous-versions/ff537793(v=vs.85)" data-raw-source="[&lt;strong&gt;base-data-type&lt;/strong&gt;](/previous-versions/ff537793(v=vs.85))"><strong>base-data-type</strong></a> value</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes in the base data type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>An array of a fixed-length base-data-type values</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes of an array of zero or more base-data-type values.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>A <a href="/windows-hardware/drivers/install/devprop-type-security-descriptor" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_SECURITY_DESCRIPTOR&lt;/strong&gt;](./devprop-type-security-descriptor.md)"><strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR</strong></a> data type value</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes of a variable-length, self-relative SECURITY_DESCRIPTOR structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>A <a href="/windows-hardware/drivers/install/devprop-type-string" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING&lt;/strong&gt;](./devprop-type-string.md)"><strong>DEVPROP_TYPE_STRING</strong></a> data type value, a <a href="/windows-hardware/drivers/install/devprop-type-security-descriptor-string" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING&lt;/strong&gt;](./devprop-type-security-descriptor-string.md)"><strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING</strong></a> data type value, or a <a href="/windows-hardware/drivers/install/devprop-type-string-indirect" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_INDIRECT&lt;/strong&gt;](./devprop-type-string-indirect.md)"><strong>DEVPROP_TYPE_STRING_INDIRECT</strong></a> data type value</p></td>
<td align="left"><p>The specified size of the supplied data must be the number of bytes of a Unicode <a href="/windows/desktop/SysInfo/registry-value-types" data-raw-source="[REG_SZ](/windows/desktop/SysInfo/registry-value-types)">REG_SZ</a> string, including the NULL-terminator.</p></td>
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

 

