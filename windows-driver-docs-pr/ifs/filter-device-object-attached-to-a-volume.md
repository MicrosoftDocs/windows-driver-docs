---
title: Filter Device Object Attached to a Volume
description: Filter Device Object Attached to a Volume
ms.assetid: cf152065-fc03-4f5f-b65b-13a76e83d745
keywords:
- filter device objects WDK file system
- filter drivers WDK file system , device object I/O requests
- file system filter drivers WDK , device object I/O requests
- volumes WDK file system , device object I/O requests
- device object I/O requests WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Device Object Attached to a Volume


## <span id="ddk_a_filter_device_object_attached_to_a_volume_if"></span><span id="DDK_A_FILTER_DEVICE_OBJECT_ATTACHED_TO_A_VOLUME_IF"></span>


To filter a volume, a filter driver creates a filter device object and attaches it above the volume device object for the volume.

### <span id="types_of_i_o_requests_that_are_sent_to_a_volume"></span><span id="TYPES_OF_I_O_REQUESTS_THAT_ARE_SENT_TO_A_VOLUME"></span>Types of I/O Requests That Are Sent to a Volume

A filter device object that is attached above a volume can generally expect to receive the following types of I/O requests:

[**IRP\_MJ\_CLEANUP**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-cleanup)

[**IRP\_MJ\_CLOSE**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-close)

[**IRP\_MJ\_CREATE**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-create)

[**IRP\_MJ\_DEVICE\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-device-control)

[**IRP\_MJ\_DIRECTORY\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-directory-control)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-file-system-control)

[**IRP\_MJ\_FLUSH\_BUFFERS**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-flush-buffers)

[**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-internal-device-control)

[**IRP\_MJ\_LOCK\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-lock-control)

[**IRP\_MJ\_PNP**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-pnp)

[**IRP\_MJ\_QUERY\_EA**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-query-ea)

[**IRP\_MJ\_QUERY\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-query-information)

[**IRP\_MJ\_QUERY\_QUOTA**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-query-quota)

[**IRP\_MJ\_QUERY\_SECURITY**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-query-security)

[**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-query-volume-information)

[**IRP\_MJ\_READ**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-read)

[**IRP\_MJ\_SET\_EA**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-set-ea)

[**IRP\_MJ\_SET\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-set-information)

[**IRP\_MJ\_SET\_QUOTA**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-set-quota)

[**IRP\_MJ\_SET\_SECURITY**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-set-security)

[**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-set-volume-information)

[**IRP\_MJ\_SHUTDOWN**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-shutdown)

[**IRP\_MJ\_WRITE**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-write)

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

For more information, see the reference entry for [**FsRtlRegisterFileSystemFilterCallbacks**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks).

 

 

 




