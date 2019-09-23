---
title: FLT_PARAMETERS for IRP_MJ_QUERY_QUOTA union
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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FLT\_PARAMETERS for IRP\_MJ\_QUERY\_QUOTA union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md).

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
Pointer to a caller-supplied [**FILE\_QUOTA\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/ns-ntifs-_file_quota_information)-structured output buffer where the quota information is to be returned.

**MdlAddress**  
Address of a memory descriptor list (MDL) describing the buffer that **QuotaBuffer** points to. This member is optional and can be **NULL**.

Remarks
-------

The [**FLT\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md) operations contains the parameters for an IRP-based query-quota-information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

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


[**FILE\_QUOTA\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/ns-ntifs-_file_quota_information)

[**FLT\_CALLBACK\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT\_IS\_FASTIO\_OPERATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://docs.microsoft.com/previous-versions/ff544648(v=vs.85))

[**FLT\_IS\_IRP\_OPERATION**](https://docs.microsoft.com/previous-versions/ff544654(v=vs.85))

[**FLT\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_parameters)

[**IoCheckQuotaBufferValidity**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-iocheckquotabuffervalidity)

[**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md)

[**SID**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/ns-ntifs-_sid)

 

 






