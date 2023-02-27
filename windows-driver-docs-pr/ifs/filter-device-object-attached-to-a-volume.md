---
title: Filter Device Object Attached to a Volume
description: Filter Device Object Attached to a Volume
keywords:
- filter device objects WDK file system
- filter drivers WDK file system , device object I/O requests
- file system filter drivers WDK , device object I/O requests
- volumes WDK file system , device object I/O requests
- device object I/O requests WDK file system
ms.date: 02/23/2023
---

# Filter Device Object Attached to a Volume

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

To filter a volume, a filter driver creates a filter device object and attaches it above the volume device object for the volume.

## Types of I/O Requests That Are Sent to a Volume

A filter device object that is attached above a volume can generally expect to receive the following types of I/O requests:

* [**IRP_MJ_CLEANUP**](./irp-mj-cleanup.md)
* [**IRP_MJ_CLOSE**](./irp-mj-close.md)
* [**IRP_MJ_CREATE**](./irp-mj-create.md)
* [**IRP_MJ_DEVICE_CONTROL**](./irp-mj-device-control.md)
* [**IRP_MJ_DIRECTORY_CONTROL**](./irp-mj-directory-control.md)
* [**IRP_MJ_FILE_SYSTEM_CONTROL**](./irp-mj-file-system-control.md)
* [**IRP_MJ_FLUSH_BUFFERS**](./irp-mj-flush-buffers.md)
* [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](./irp-mj-internal-device-control.md)
* [**IRP_MJ_LOCK_CONTROL**](./irp-mj-lock-control.md)
* [**IRP_MJ_PNP**](./irp-mj-pnp.md)
* [**IRP_MJ_QUERY_EA**](./irp-mj-query-ea.md)
* [**IRP_MJ_QUERY_INFORMATION**](./irp-mj-query-information.md)
* [**IRP_MJ_QUERY_QUOTA**](./irp-mj-query-quota.md)
* [**IRP_MJ_QUERY_SECURITY**](./irp-mj-query-security.md)
* [**IRP_MJ_QUERY_VOLUME_INFORMATION**](./irp-mj-query-volume-information.md)
* [**IRP_MJ_READ**](./irp-mj-read.md)
* [**IRP_MJ_SET_EA**](./irp-mj-set-ea.md)
* [**IRP_MJ_SET_INFORMATION**](./irp-mj-set-information.md)
* [**IRP_MJ_SET_QUOTA**](./irp-mj-set-quota.md)
* [**IRP_MJ_SET_SECURITY**](./irp-mj-set-security.md)
* [**IRP_MJ_SET_VOLUME_INFORMATION**](./irp-mj-set-volume-information.md)
* [**IRP_MJ_SHUTDOWN**](./irp-mj-shutdown.md)
* [**IRP_MJ_WRITE**](./irp-mj-write.md)
* Any of the following [FAST_IO_DISPATCH](/windows-hardware/drivers/ddi/wdm/ns-wdm-_fast_io_dispatch) callback routines:
  * **FastIoCheckIfPossible**
  * **FastIoRead**
  * **FastIoWrite**
  * **FastIoQueryBasicInfo**
  * **FastIoQueryStandardInfo**
  * **FastIoLock**
  * **FastIoUnlockSingle**
  * **FastIoUnlockAll**
  * **FastIoUnlockAllByKey**
  * **FastIoDeviceControl**
  * **FastIoDetachDevice**
  * **FastIoQueryNetworkOpenInfo**
  * **MdlRead**
  * **MdlReadComplete**
  * **PrepareMdlWrite**
  * **MdlWriteComplete**
  * **FastIoReadCompressed**
  * **FastIoWriteCompressed**
  * **MdlReadCompleteCompressed**
  * **MdlWriteCompleteCompressed**
  * **FastIoQueryOpen**

File system filter device objects attached to volumes must pass all unrecognized or unwanted IRPs to the next-lower driver on the driver stack by default. In addition, they must implement **FastIoDetachDevice**.

On Windows XP and later, file system filter drivers shouldn't use any of the following fast I/O callback routines because they're obsolete.

* **AcquireForCcFlush**
* **AcquireFileForNtCreateSection**
* **AcquireForModWrite**
* **ReleaseForCcFlush**
* **ReleaseFileForNtCreateSection**
* **ReleaseForModWrite**

For more information, see the reference entry for [**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks).
