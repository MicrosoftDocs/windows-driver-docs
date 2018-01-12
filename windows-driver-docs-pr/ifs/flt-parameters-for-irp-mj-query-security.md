---
title: FLT\_PARAMETERS for IRP\_MJ\_QUERY\_SECURITY union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_QUERY\_SECURITY.
ms.assetid: 7707fec2-9fe8-40f6-9f34-f43403551440
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_SECURITY union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
---

# FLT\_PARAMETERS for IRP\_MJ\_QUERY\_SECURITY union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_QUERY\_SECURITY**](irp-mj-query-security.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    SECURITY_INFORMATION    SecurityInformation;
    ULONG POINTER_ALIGNMENT Length;
    PVOID                   SecurityBuffer;
    PDML                    MdlAddress;
  } QuerySecurity;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**QuerySecurity**  
Structure containing the following members.

**SecurityInformation**  
Pointer to a caller-supplied [**SECURITY\_INFORMATION**](security-information.md) value that specifies the security information to be queried. One of the following:

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
<td align="left"><p>OWNER_SECURITY_INFORMATION</p></td>
<td align="left"><p>The owner identifier of the object is being queried. Requires READ_CONTROL access.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GROUP_SECURITY_INFORMATION</p></td>
<td align="left"><p>The primary group identifier of the object is being queried. Requires READ_CONTROL access.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DACL_SECURITY_INFORMATION</p></td>
<td align="left"><p>The discretionary access control list (DACL) of the object is being queried. Requires READ_CONTROL access.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SACL_SECURITY_INFORMATION</p></td>
<td align="left"><p>The system ACL (SACL) of the object is being queried. Requires ACCESS_SYSTEM_SECURITY access.</p></td>
</tr>
</tbody>
</table>

 

**Length**  
Length, in bytes, of the buffer that **SecurityBuffer** points to.

**SecurityBuffer**  
Pointer to a caller-supplied output buffer that receives a copy of the security descriptor of the specified object. The calling process must have the right to view the specified aspects of the object's security status. The [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff556610) structure is returned in self-relative format.

**MdlAddress**  
Address of a memory descriptor list (MDL) that describes the buffer that **SecurityBuffer** points to. This member is optional and can be **NULL**.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for [**IRP\_MJ\_QUERY\_SECURITY**](irp-mj-query-security.md) operations contains the parameters for an IRP-based query-security-information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure.

On Windows XP and later, the object that the **TargetFileObject** member of the FLT\_IO\_PARAMETER\_BLOCK structure points to can represent a named data stream. For more information about named data streams, see [**FILE\_STREAM\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540364).

IRP\_MJ\_QUERY\_SECURITY is an IRP-based operation.

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


[**FILE\_STREAM\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540364)

[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**IRP\_MJ\_QUERY\_SECURITY**](irp-mj-query-security.md)

[**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff556610)

[**SECURITY\_INFORMATION**](security-information.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_QUERY_SECURITY%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





