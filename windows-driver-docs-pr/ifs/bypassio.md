---
title: BypassIO for filter drivers
description: About BypassIO
keywords:
- filter drivers WDK file system , BypassIO
ms.date: 12/08/2021
prerelease: false
ms.localizationpriority: medium
---

# BypassIO for filter drivers

## About BypassIO

Starting in Windows 11, BypassIO was added as an optimized I/O path for reading from files. The goal of this path is to reduce the CPU overhead of doing reads, which helps to meet the I/O demands of loading and running next-generation games on Windows. BypassIO is a part of the infrastructure to support DirectStorage on Windows.  

It is important that minifilters implement support for BypassIO, and that you keep BypassIO enabled as much as possible. Without filter support, game performance will be degraded, resulting in a poor gaming experience for end users.

There will be broader application uses beyond gaming in future Windows releases.

BypassIO is a per handle concept. When BypassIO is requested, it is requested for an explicit file handle. BypassIO has no impact on other handles for that file.

[**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) and an equivalent [**IOCTL_STORAGE_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_manage_bypass_io) were added as a part of this infrastructure. Minifilters process **FSCTL_MANAGE_BYPASS_IO**, while **IOCTL_STORAGE_MANAGE_BYPASS_IO** is sent by file systems to the volume/storage stacks. These control codes are designed to be diagnosable: they both return the identity of the driver that failed the BypassIO request, and the reason for vetoing it.

This page provides architectural details across the file system filter and storage stacks, as well as information on how to implement BypassIO in a minifilter driver. See [BypassIO for storage drivers](../storage/bypassio.md) for BypassIO information that is specific to storage drivers.

## Scope of BypassIO support

Starting in Windows 11, BypassIO is supported as follows:

* On Windows client systems only. Server system support will be added in a future release.

* On NVMe storage devices only. Support for other storage technologies will be added in a future release.

* On the NTFS file system only. Support for other file systems will be added in a future release.

* Only non-cached reads are supported. Support for non-cached writes will be added in a future release.

* Only supported on files (not supported on directory or volume handles).

## How BypassIO works

When [**NtReadFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile) is called on a BypassIO-enabled **FileHandle**, the operation does not flow through the traditional I/O stack, which traverses the entire file system stack, volume stack, and storage stack. Instead, no IRP is issued, and the operation flows directly from the I/O manager to the (NTFS) file system, then to the disk (classpnp) driver, and then to the StorNVMe driver. With a BypassIO-enabled **FileHandle**:

* All file system filters are skipped.
* All volume stack filters are skipped.
* All storage stack filters and drivers above the disk driver, and between the disk and StorNVMe drivers, are skipped.

:::image type="content" source="images/traditional-io-path.jpg" alt-text="Image that shows the traditional I O path for a read request.":::

:::image type="content" source="images/bypass-io-path.jpg" alt-text="Image that shows the Bypass I O path for a read request.":::

## DDIs changes and additions for BypassIO

The following DDIs relevant to filter drivers were added to provide BypassIO support:

* [**FltVetoBypassIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltvetobypassio) function
* [**FS_BPIO_INFLAGS**](/windows-hardware/drivers/ddi/ntifs/ne-ntifs-fs_bpio_inflags) enumerator
* [**FS_BPIO_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_info) structure
* [**FS_BPIO_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_input) structure
* [**FS_BPIO_OPERATIONS**](/windows-hardware/drivers/ddi/ntifs/ne-ntifs-fs_bpio_operations) enumerator
* [**FS_BPIO_OUTFLAGS**](/windows-hardware/drivers/ddi/ntifs/ne-ntifs-fs_bpio_outflags) enumerator
* [**FS_BPIO_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_output) structure
* [**FS_BPIO_RESULTS**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_results) structure
* [**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) control code
* [**FsRtlGetBypassIoOpenCount**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetbypassioopencount) function

Additionally, the following DDIs were changed to support BypassIO:

* A **BypassIoOpenCount** field was added to the [**FSRTL_ADVANCED_FCB_HEADER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsrtl_advanced_fcb_header) structure. The file system uses this field to maintain a count of unique FileObjects on a stream that currently have BypassIO enabled. The addition of this field increases the structure size. The structure version to use starting in Windows 11 is **FSRTL_FCB_HEADER_V4**.

## Impact of other operations on BypassIO-enabled handles

Enabling BypassIO on a handle doesn't impact other handles. However, other operations on a BypassIO-enabled handle do impact the use of BypassIO, such as the following:

* If you have Handle A open to a file on which BypassIO is enabled and functioning, and someone (for example, another thread or process) opens Handle B to perform cached or memory mapped IO, then BypassIO will temporarily be suspended on Handle A, until Handle B is closed. The system will instead use the traditional I/O path to guarantee that stale data does not occur. The system will continue to use the traditional I/O path on that handle until all data sections and cache maps are torn down, so filters must close the handle’s file in order for BypassIO to resume.

* If a BypassIO-enabled file is marked sparse, all BypassIO operations start using the traditional I/O path.

* Defragging a BypassIO-enabled file causes all BypassIO operations to use the traditional I/O path. Once the defragging is completed, the system will switch back to the BypassIO path on that handle.

## Implementing BypassIO support in minifilters

### Update your INF or MANIFEST files

Starting in Windows 11, filter developers should add **SUPPORTED_FS_FEATURES_BYPASS_IO** to **SupportedFeatures** in your driver's .INF or MANIFEST files. (You can type ```fltmc instances``` in an elevated command prompt to see "SprtFtrs" values for all active filters.)

> [!NOTE]
> A filter that can never support BypassIO should still add **SUPPORTED_FS_FEATURES_BYPASS_IO** to its **SupportedFeatures** state, and then veto appropriately inside the filter, specifying the reason.
>
> Minifilters are encouraged to minimize vetoing BypassIO as much as possible.

If a minifilter attaches to a volume on which BypassIO is enabled, but that minifilter has not updated its **SupportedFeatures** setting to include **SUPPORTED_FS_FEATURES_BYPASS_IO**, all BypassIO operations on that volume are immediately blocked, falling back to the traditional I/O path, resulting in degraded game performance.

Minifilters that do not filter IRP_MJ_READ or IRP_MJ_WRITE are automatically opted in to BypassIO support, as if they had added **SUPPORTED_FS_FEATURES_BYPASS_IO** in **SupportedFeatures**.

The **FS_BPIO_OP_ENABLE** and **FS_BPIO_OP_QUERY** operations will fail on a stack if there is an attached minifilter that has not opted in.

### Implement support for BypassIO requests

Minifilters should add support for BypassIO requests, which are sent through the [**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) control code. See [Supporting BypassIO operations](bypassio-operations.md) for details.

## Determining whether BypassIO is working

An *fsutil* command has been added that issues an **FSCTL_MANAGE_BYPASS_IO** specifying the **FS_BPIO_OP_QUERY** operation. The displayed results identify the first driver that is preventing BypassIO and the reason why.

``` Command
> fsutil bypassIo state <path>
```

Where *\<path>* can be a volume, a directory, or a specific filename.

For example, say the WOF minifilter has not opted in to BypassIO. Executing the command ```fsutil bypassIo state c:\``` results in the following output:

``` output
BypassIo on "c:\" is not currently supported.
Status: 506 (At least one minifilter does not support bypass IO)
Driver: wof.sys
Reason: The specified minifilter does not support bypass IO.
```

## NTFS-specific behavior

BypassIO can be enabled on an NTFS resident file; however, the file will take the traditional I/O path as long as it is resident. If a write occurs to the file such that it goes non-resident, the system will switch to use the BypassIO path.

NTFS compression cannot be enabled on a BypassIO active file.

NTFS encryption can be enabled on a BypassIO active file. BypassIO will be paused.

BypassIO has no impact on offload read/write operations.
