---
title: Filter Device Object Attached to a Volume
description: Filter Device Object Attached to a Volume
keywords:
- filter device objects WDK file system
- filter drivers WDK file system , device object I/O requests
- file system filter drivers WDK , device object I/O requests
- volumes WDK file system , device object I/O requests
- device object I/O requests WDK file system
ms.date: 04/20/2017
---

# Filter Device Object Attached to a Volume


## <span id="ddk_a_filter_device_object_attached_to_a_volume_if"></span><span id="DDK_A_FILTER_DEVICE_OBJECT_ATTACHED_TO_A_VOLUME_IF"></span>


To filter a volume, a filter driver creates a filter device object and attaches it above the volume device object for the volume.

### <span id="types_of_i_o_requests_that_are_sent_to_a_volume"></span><span id="TYPES_OF_I_O_REQUESTS_THAT_ARE_SENT_TO_A_VOLUME"></span>Types of I/O Requests That Are Sent to a Volume

A filter device object that is attached above a volume can generally expect to receive the following types of I/O requests:

[**IRP\_MJ\_CLEANUP**](./irp-mj-cleanup.md)

[**IRP\_MJ\_CLOSE**](./irp-mj-close.md)

[**IRP\_MJ\_CREATE**](./irp-mj-create.md)

[**IRP\_MJ\_DEVICE\_CONTROL**](./irp-mj-device-control.md)

[**IRP\_MJ\_DIRECTORY\_CONTROL**](./irp-mj-directory-control.md)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](./irp-mj-file-system-control.md)

[**IRP\_MJ\_FLUSH\_BUFFERS**](./irp-mj-flush-buffers.md)

[**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](./irp-mj-internal-device-control.md)

[**IRP\_MJ\_LOCK\_CONTROL**](./irp-mj-lock-control.md)

[**IRP\_MJ\_PNP**](./irp-mj-pnp.md)

[**IRP\_MJ\_QUERY\_EA**](./irp-mj-query-ea.md)

[**IRP\_MJ\_QUERY\_INFORMATION**](./irp-mj-query-information.md)

[**IRP\_MJ\_QUERY\_QUOTA**](./irp-mj-query-quota.md)

[**IRP\_MJ\_QUERY\_SECURITY**](./irp-mj-query-security.md)

[**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](./irp-mj-query-volume-information.md)

[**IRP\_MJ\_READ**](./irp-mj-read.md)

[**IRP\_MJ\_SET\_EA**](./irp-mj-set-ea.md)

[**IRP\_MJ\_SET\_INFORMATION**](./irp-mj-set-information.md)

[**IRP\_MJ\_SET\_QUOTA**](./irp-mj-set-quota.md)

[**IRP\_MJ\_SET\_SECURITY**](./irp-mj-set-security.md)

[**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](./irp-mj-set-volume-information.md)

[**IRP\_MJ\_SHUTDOWN**](./irp-mj-shutdown.md)

[**IRP\_MJ\_WRITE**](./irp-mj-write.md)

**FastIoCheckIfPossible**

**FastIoDetachDevice**

**FastIoDeviceControl**

**FastIoLock**

**FastIoQueryBasicInfo**

**FastIoQueryNetworkOpenInfo**

**FastIoQueryOpen**

**FastIoQueryStandardInfo**

**FastIoRead**

**FastIoReadCompressed**

**FastIoUnlockAll**

**FastIoUnlockAllByKey**

**FastIoUnlockSingle**

**FastIoWrite**

**FastIoWriteCompressed**

**MdlRead**

**MdlReadComplete**

**MdlReadCompleteCompressed**

**MdlWriteComplete**

**MdlWriteCompleteCompressed**

**PrepareMdlWrite**

File system filter device objects, attached to volumes, are required to pass all unrecognized or unwanted IRPs to the next-lower driver on the driver stack by default. In addition, they must implement **FastIoDetachDevice**.

**Note**   On Microsoft Windows XP and later, the following fast I/O callback routines are obsolete and should not be used by file system filter drivers:
**AcquireForCcFlush**

**AcquireFileForNtCreateSection**

**AcquireForModWrite**

**ReleaseForCcFlush**

**ReleaseFileForNtCreateSection**

**ReleaseForModWrite**

For more information, see the reference entry for [**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks).

 

 

