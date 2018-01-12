---
title: FLT\_PARAMETERS for IRP\_MJ\_QUERY\_QUOTA union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_QUERY\_QUOTA.
ms.assetid: b87b008d-f1ce-4dab-9afa-df67aa3dc596
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_QUOTA union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
---

# FLT\_PARAMETERS for IRP\_MJ\_QUERY\_QUOTA union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                       Length;
    PSID                        StartSid;
    PFILE_GET_QUOTA_INFORMATION SidList;
    ULONG                       SidListLength;
    PVOID                       QuotaBuffer;
    PMLD                        MdlAddress;
  } QueryQuota;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**QueryQuota**  
Structure containing the following members.

**Length**  
Length, in bytes, of the buffer that **QuotaBuffer** points to.

**StartSid**  
Optional pointer to the security identifier (SID) of the entry at which to begin scanning the quota list. This parameter is ignored if the SL\_INDEX\_SPECIFIED flag is not set in the FLT\_IO\_PARAMETER\_BLOCK structure for the operation or if **SidList** points to a nonempty list.

**SidList**  
Pointer to a caller-supplied FILE\_GET\_QUOTA\_INFORMATION-structured input buffer specifying the SIDs whose quota information is to be queried.

**SidListLength**  
Length, in bytes, of the buffer that **SidList** points to.

**QuotaBuffer**  
Pointer to a caller-supplied [**FILE\_QUOTA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540342)-structured output buffer where the quota information is to be returned.

**MdlAddress**  
Address of a memory descriptor list (MDL) describing the buffer that **QuotaBuffer** points to. This member is optional and can be **NULL**.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for [**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md) operations contains the parameters for an IRP-based query-quota-information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_QUERY\_QUOTA is an IRP-based operation.

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


[**FILE\_QUOTA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540342)

[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**IoCheckQuotaBufferValidity**](https://msdn.microsoft.com/library/windows/hardware/ff548279)

[**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md)

[**SID**](https://msdn.microsoft.com/library/windows/hardware/ff556740)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_QUERY_QUOTA%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





