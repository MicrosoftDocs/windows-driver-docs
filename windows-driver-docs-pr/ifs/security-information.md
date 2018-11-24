---
title: SECURITY\_INFORMATION
description: SECURITY\_INFORMATION
ms.assetid: 28023f0f-62ae-407b-b81b-1c98499df9a2
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SECURITY\_INFORMATION


SECURITY\_INFORMATION

``` syntax
typedef ULONG SECURITY_INFORMATION, *PSECURITY_INFORMATION;
```




A value of type SECURITY\_INFORMATION is used to identify the object-related security information being set or queried. This security information includes:

-   The owner of an object

-   The primary group of an object

-   The discretionary access-control list (DACL) of an object

-   The system ACL (SACL) of an object

Each item of security information is designated by a bit flag. The following values specify the bits.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
<th align="left">Access</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DACL_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the object&#39;s DACL is being set or queried.</p>
<p>For the following items, the DACL is queried:</p>
<p>IRP_MJ_QUERY_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY</p>
<p>FltQuerySecurityObject</p>
<p>SeQuerySecurityDescriptorInfo</p>
<p>For the following items, the DACL is set:</p>
<p>IRP_MJ_SET_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_SET_SECURITY</p>
<p>FltSetSecurityObject</p>
<p>SeSetSecurityDescriptorInfo</p>
<p>SeSetSecurityDescriptorInfoEx</p></td>
<td align="left"><p>Requires READ_CONTROL access for:</p>
<p>IRP_MJ_QUERY_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY</p>
<p>FltQuerySecurityObject</p>
<p>SeQuerySecurityDescriptorInfo</p>
<p>Requires WRITE_DAC access for:</p>
<p>IRP_MJ_SET_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_SET_SECURITY</p>
<p>FltSetSecurityObject</p>
<p>SeSetSecurityDescriptorInfo</p>
<p>SeSetSecurityDescriptorInfoEx</p></td>
</tr>
<tr class="even">
<td align="left"><p>GROUP_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the primary group identifier of the object is being set or queried.</p>
<p>For the following items, the group identifier is queried:</p>
<p>IRP_MJ_QUERY_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY</p>
<p>FltQuerySecurityObject</p>
<p>SeQuerySecurityDescriptorInfo</p>
<p>IRP_MJ_SET_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_SET_SECURITY</p>
<p>For the following items, the group identifier is set:</p>
<p>FltSetSecurityObject</p>
<p>SeSetSecurityDescriptorInfo</p>
<p>SeSetSecurityDescriptorInfoEx</p></td>
<td align="left"><p>Requires READ_CONTROL access for:</p>
<p>IRP_MJ_QUERY_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY</p>
<p>FltQuerySecurityObject</p>
<p>SeQuerySecurityDescriptorInfo</p>
<p>Requires WRITE_OWNER access for:</p>
<p>IRP_MJ_SET_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_SET_SECURITY</p>
<p>FltSetSecurityObject</p>
<p>SeSetSecurityDescriptorInfo</p>
<p>SeSetSecurityDescriptorInfoEx</p></td>
</tr>
<tr class="odd">
<td align="left"><p>OWNER_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the owner identifier of the object is being set or queried.</p>
<p>For the following items, the owner identifier is queried:</p>
<p>IRP_MJ_QUERY_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY</p>
<p>FltQuerySecurityObject</p>
<p>SeQuerySecurityDescriptorInfo</p>
<p>IRP_MJ_SET_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_SET_SECURITY</p>
<p>For the following items, the owner identifier is set:</p>
<p>FltSetSecurityObject</p>
<p>SeSetSecurityDescriptorInfo</p>
<p>SeSetSecurityDescriptorInfoEx</p></td>
<td align="left"><p>Requires READ_CONTROL access for:</p>
<p>IRP_MJ_QUERY_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY</p>
<p>FltQuerySecurityObject</p>
<p>SeQuerySecurityDescriptorInfo</p>
<p>Requires WRITE_OWNER access for:</p>
<p>IRP_MJ_SET_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_SET_SECURITY</p>
<p>FltSetSecurityObject</p>
<p>SeSetSecurityDescriptorInfo</p>
<p>SeSetSecurityDescriptorInfoEx</p></td>
</tr>
<tr class="even">
<td align="left"><p>SACL_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the object&#39;s SACL is being set or queried.</p>
<p>For the following items, the SACL is queried:</p>
<p>IRP_MJ_QUERY_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY</p>
<p>FltQuerySecurityObject</p>
<p>SeQuerySecurityDescriptorInfo</p>
<p>IRP_MJ_SET_SECURITY</p>
<p>FLT_PARAMETERS for IRP_MJ_SET_SECURITY</p>
<p>For the following items, the SACL is set:</p>
<p>FltSetSecurityObject</p>
<p>SeSetSecurityDescriptorInfo</p>
<p>SeSetSecurityDescriptorInfoEx</p></td>
<td align="left"><p>Requires ACCESS_SYSTEM_SECURITY access in all cases.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PROCESS_TRUST_LABEL_SECURITY_INFORMATION</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

## Requirements


Wdm.h (include Wdm.h)

## Related topics


[**ACL**](https://msdn.microsoft.com/library/windows/hardware/ff538866)

[**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff556610)

[**SeQuerySecurityDescriptorInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556692)

[**SeSetSecurityDescriptorInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556709)

[**SeSetSecurityDescriptorInfoEx**](https://msdn.microsoft.com/library/windows/hardware/ff556712)

[**ZwQuerySecurityObject**](https://msdn.microsoft.com/library/windows/hardware/ff567066)

[**ZwSetSecurityObject**](https://msdn.microsoft.com/library/windows/hardware/ff567106)

 

 






