---
title: FLT_PARAMETERS for IRP_MJ_SET_SECURITY union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_SET\_SECURITY.
ms.assetid: 9006ef50-bd2e-4c75-8c6b-8bb777122a75
keywords: ["FLT_PARAMETERS for IRP_MJ_SET_SECURITY union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FLT\_PARAMETERS for IRP\_MJ\_SET\_SECURITY union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_SET\_SECURITY**](irp-mj-set-security.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    SECURITY_INFORMATION SecurityInformation;
    PSECURITY_DESCRIPTOR SecurityDescriptor;
  } SetSecurity;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**SetSecurity**  
Structure containing the following members.

**SecurityInformation**  
Pointer to a [**SECURITY\_INFORMATION**](security-information.md) value that specifies which security information is to be set in the security descriptor. This value can be one of the following.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SecurityInformation Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DACL_SECURITY_INFORMATION</p></td>
<td align="left"><p>The discretionary access control list (DACL) of the object is being set. Requires WRITE_DAC access.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GROUP_SECURITY_INFORMATION</p></td>
<td align="left"><p>The primary group identifier of the object is being set. Requires WRITE_OWNER access.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>OWNER_SECURITY_INFORMATION</p></td>
<td align="left"><p>The owner identifier of the object is being set. Requires WRITE_OWNER access.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SACL_SECURITY_INFORMATION</p></td>
<td align="left"><p>The system ACL (SACL) of the object is being set. Requires ACCESS_SYSTEM_SECURITY access.</p></td>
</tr>
</tbody>
</table>

 

**SecurityDescriptor**  
Pointer to a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff556610) structure that contains the values of the security information to be assigned to the object.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for [**IRP\_MJ\_SET\_SECURITY**](irp-mj-set-security.md) operations contains the parameters for a set-security-information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_SET\_SECURITY is an IRP-based operation.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Fltkernel.h (include Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**IRP\_MJ\_SET\_SECURITY**](irp-mj-set-security.md)

[**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff556610)

[**SECURITY\_INFORMATION**](security-information.md)

 

 






