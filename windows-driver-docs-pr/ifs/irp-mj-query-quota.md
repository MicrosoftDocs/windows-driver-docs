---
title: IRP_MJ_QUERY_QUOTA (FS and Filter Drivers)
description: IRP_MJ_QUERY_QUOTA
keywords: ["IRP_MJ_QUERY_QUOTA Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_QUERY_QUOTA
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_QUERY_QUOTA (FS and filter drivers)

## When Sent

The I/O Manager sends the IRP_MJ_QUERY_QUOTA request. This request can be sent, for example, when a user-mode application has called a Win32 method such as [**IDiskQuotaControl::GetQuotaState**](/windows/win32/api/dskquota/nf-dskquota-idiskquotacontrol-getquotastate).

## Operation: File System Drivers

If the file system supports disk quotas, the file system driver should extract and decode the file object to determine whether it represents a user open of a file or directory. If it does, the driver should process the query and complete the IRP. Otherwise, the driver should complete the IRP as appropriate without processing the query.

## Operation: Legacy File System Filter Drivers

The filter driver should pass this IRP down to the next-lower driver on the stack, unless it needs to explicitly override quota behavior.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a query quota information request:

- **DeviceObject** is a pointer to the target device object.

- **DeviceObject->Flags**: The DO_BUFFERED_IO and DO_DIRECT_IO flags are used as follows to specify the method by which data is passed to the driver:

  |Flag Setting|I/O Method|
  |----|----|
  |~DO_BUFFERED_IO|~DO_DIRECT_IO|
  |METHOD_NEITHER|~DO_BUFFERED_IO|
  |DO_DIRECT_IO|METHOD_DIRECT|
  |DO_BUFFERED_IO|~DO_DIRECT_IO|
  |METHOD_BUFFERED|DO_BUFFERED_IO|
  |DO_DIRECT_IO|METHOD_BUFFERED|

- **Irp->AssociatedIrp.SystemBuffer** points to a system-supplied buffer to be used as an intermediate system buffer, if the DO_BUFFERED_IO flag is set in **DeviceObject->Flags**. Otherwise, this member is set to **NULL**.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **Irp->UserBuffer* points to a caller-supplied FILE_QUOTA_INFORMATION-structured output buffer that receives the quota information for the volume.

- **IrpSp->FileObject** points to the file object that is associated with **DeviceObject**.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_QUERY_QUOTA and shouldn't be used.

- **IrpSp->Flags** can be one or more of the following values:

| Flag | Meaning |
| ---- | ------- |
| SL_INDEX_SPECIFIED | Begin the scan at the entry in the quota list whose index is given by **IrpSp->Parameters.QueryQuota.StartSid** |
| SL_RESTART_SCAN | Begin the scan at the first entry in the list. If this flag isn't set, resume the scan from a previous IRP_MJ_QUERY_QUOTA request.|
| SL_RETURN_SINGLE_ENTRY | Return only the first entry that is found.|

- **IrpSp->MajorFunction** is set to IRP_MJ_QUERY_QUOTA.

- **IrpSp->Parameters.QueryQuota.Length** is the length, in bytes, of the buffer pointed to by **Irp->UserBuffer**.

- **IrpSp->Parameters.QueryQuota.SidList** is an optional pointer to a list of SIDs whose quota information is to be returned. Each entry in the list is a [**FILE_GET_QUOTA_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_get_quota_information) structure. This structure is defined as follows:

  ```cpp
  typedef struct _FILE_GET_QUOTA_INFORMATION {
      ULONG NextEntryOffset;
      ULONG SidLength;
      SID Sid;
  } FILE_GET_QUOTA_INFORMATION, *PFILE_GET_QUOTA_INFORMATION;
  ```

| Member | Meaning |
| ------ | ------- |
| NextEntryOffset | Byte offset of the next FILE_GET_QUOTA_INFORMATION entry, if multiple entries are present in a buffer. This member is zero if no other entries follow this one.|
| SidLength | Length, in bytes, of the **Sid** member.|
| Sid | Security identifier (SID)|

- **IrpSp->Parameters.QueryQuota.SidListLength** is the length, in bytes, of the list of SIDs, if one is specified.

- **IrpSp->Parameters.QueryQuota.StartSid** is an optional pointer to a SID that indicates that the returned information is to start with an entry other than the first. This parameter is ignored if a SID list is specified.

## See also

[**FILE_GET_QUOTA_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_get_quota_information)

[**FILE_QUOTA_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_quota_information)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCheckQuotaBufferValidity**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckquotabuffervalidity)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_SET_QUOTA**](irp-mj-set-quota.md)
