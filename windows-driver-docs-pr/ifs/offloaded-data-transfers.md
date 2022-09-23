---
title: Windows Offloaded Data Transfers
description: Transferring data between computers or within the same computer is a frequent file system activity.
ms.date: 09/23/2022
keywords:
- offloaded data transfers
- Windows offloaded data transfers
- offloaded data transfers, file systems
- offloaded data transfers, filters
- offloaded data transfers, minifilters
ms.custom: contperf-fy22q1
---

# Windows Offloaded Data Transfers

Offloaded Data Transfer (ODX) is a feature that speeds up server copy and move operations. This feature is available starting in Windows Server 2012 and is supported on NTFS volumes. This page describes ODX from a file system and minifilter perspective. For information related to storage devices, see [Windows Storage Offloaded Data Transfers](../storage/offloaded-data-transfer.md).

Transferring data between computers or within the same computer is a frequent file system activity. Using the standard **ReadFile** and **WriteFile** functions work well from a functional point of view, but it involves heavy data movement through all levels of the system and potentially across a network. This can affect the availability of the systems involved in the transfer and the network connecting the systems. The advanced capabilities available with many storage subsystems provide a more efficient means of performing the ‘heavy lifting’ task of data movement.

Applications can take advantage of these capabilities to help offload the process of data movement to the storage subsystem. File system filters can typically monitor these actions by intercepting read and write requests to a volume. Additional actions are required for filters to be aware of offloaded data transfers.

## Typical Data Transfers

Moving data around in an application scenario today is quite simple. It involves reading the data into local memory, then writing it back out to a new location. The following diagram illustrates this scenario.

![typical data transfer.](images/odx-scenario-1.png)

This scenario involves copying a file between two locations on two different file servers, each with its own virtual disk exposed through an Intelligent Storage Array (ISA). The initiating system first needs to read the data from the source virtual disk into a local buffer. It then packages and transmits the data through some transport and protocol (like SMB over 1GbE) to the second system, which then receives the data and outputs it to a local buffer. Then, the target system writes the data to the destination virtual disk. This scenario describes a very typical Read/Write method of data transfer that is performed multiple times by many different applications every day.

While standard reads and writes work well in most scenarios, the data intending to be copied may be located on virtual disks managed by the same Intelligent Storage Array. This means that the data is moved out of the array, onto a server, across a network transport, onto another server, and back into the same array once again. The act of moving data within a server and across a network transport can significantly impact the availability of those systems; not to mention the fact that the throughput of the data movement is limited by the throughput and availability of the network.

## Offloaded Data Transfers (ODX)

### Offloading the Data Transfer

Two new FSCTLs were introduced in Windows 8 that facilitate a method of offloading the data transfer. This shifts the burden of bit movement away from servers to bit movement that occurs intelligently within the storage subsystems. The best way to visualize the command semantics is to think of them as analogous to an unbuffered read and an unbuffered write.

* [**FSCTL_OFFLOAD_READ**](./fsctl-offload-read.md)

  This control request takes an offset within the file to be read and a desired length in the [**FSCTL_OFFLOAD_READ_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_input) structure. If supported, the storage subsystem hosting the file receives the associated offload read storage command and generates a token, which is a logical representation of the data intended to be read at the time of the offload read command. This token string is returned to the caller in the [**FSCTL_OFFLOAD_READ_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_output) structure.

* [**FSCTL_OFFLOAD_WRITE**](./fsctl-offload-write.md)  

  This control request takes an offset within the file to be written to, the desired length of the write, and the token that is a logical representation of the data to be written. If supported, the storage subsystem hosting the file to be written receives the associated offload write storage command. It first attempts to recognize the given token, and then performs the write operation if possible. The write operation is completed underneath Windows, and therefore components on the file system and storage stacks will not see the data movement. Once the data movement is complete, the number of bytes written is returned to the caller.

Similar to the first diagram, the following diagram shows a simple file copy between two virtual disks on two different servers.

![offloaded data transfer.](images/odx-scenario-2.png)

However, instead of doing normal reads and writes, we offload the heavy lifting of bit movement to the storage array. The first system issues the offload read operation, requesting the array to generate a token representing a point-in-time view of the data to be read within the region of the first virtual disk. The first system then transmits the token to the second system, which in turn issues an offload write operation to the second virtual disk with the token. The array then interprets the token and attempts to perform the data movement between the virtual disks. You’ll notice that the actual data transfer occurs within the intelligent storage array, and not between the two hosts. This significantly improves availability of the two systems while virtually eliminating network traffic between the systems.

### Integration with the Copy Engine

The core copy engine in Windows is used by **CopyFile** and related functions. Starting with Windows 8, the copy engine transparently attempts to use offloaded data transfers before the traditional copy file code path. Since the copy APIs are used by most applications, utilities, and by the shell, these callers are able to use offloaded data transfer capabilities by default with little, if any, code modification or user intervention.

The following steps summarize how the copy engine attempts an offloaded data transfer:

1. The copy engine issues a [**FSCTL_OFFLOAD_READ**](./fsctl-offload-read.md) on the source file to get a read token.
2. If there was a failure in retrieving the read token, the copy engine falls back to traditional reads and writes (the traditional copy file code path). If the failure indicates that the source volume does not support offload, the copy engine also marks the volume in a per-process cache. The copy engine will not try offload any more for the volumes in the per-process cache.
3. If the token was successfully retrieved, the copy engine attempts to issue [**FSCTL_OFFLOAD_WRITE**](./fsctl-offload-write.md) commands on the target file in large chunks until all the data that is logically represented by the token has been offload written.
4. Any errors in performing the offload read or write results in the copy engine falling back to the traditional code path of reads and write, starting from where the offload code path ended off (where the read or write was truncated). If the failure indicates that the destination volume does not support offload, or the source volume cannot reach the destination volume, the copy engine updates the same per-process cache so it will not try offload on these volumes. This per-process cache will reset periodically.

The following functions support offloaded data transfers:

* **CopyFile**
* **CopyFileEx**
* **MoveFile**
* **MoveFileEx**
* **CopyFile2**

The following functions do not support offloaded data transfers:

* **CopyFileTransacted**
* **MoveFileTransacted**

### Supported Offload Data Transfer Scenarios

Support for the offload operations is provided in the Hyper-V storage stack and in the Windows SMB File Server. Where the backing physical storage supports ODX operations, callers can issue [**FSCTL_OFFLOAD_READ**](./fsctl-offload-read.md) and [**FSCTL_OFFLOAD_WRITE**](./fsctl-offload-write.md) to files residing on VHDs or on remote file shares, whether from within a virtual machine or on physical hardware. The following diagram illustrates the most basic supported source and destination targets for offloaded data transfers.

![offloaded data transfer scenarios.](images/odx-scenario-3.png)

## File System Filter Opt-In Model and Impact to Applications

Starting with Windows 8, Filter Manager allows a filter to specify offload capability as a supported feature. File system filters attached to a volume can collectively determine if a certain offloaded operation is supported or not; if it is not, the operation fails with an appropriate error code.

A filter must indicate that it supports [**FSCTL_OFFLOAD_READ**](./fsctl-offload-read.md) and [**FSCTL_OFFLOAD_WRITE**](./fsctl-offload-write.md) through a registry **DWORD** value named **SupportedFeatures**, located in the driver service definition in the registry at HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\*filter driver name*\\. This value contains bit fields where the bits determine which functionality is opted-in, and should be set during filter installation.

Currently, the defined bits are:

| Flag                                               | Meaning                               |
|----------------------------------------------------|---------------------------------------|
| SUPPORTED_FS_FEATURES_OFFLOAD_READ 0x00000001  | Filter supports FSCTL_OFFLOAD_READ  |
| SUPPORTED_FS_FEATURES_OFFLOAD_WRITE 0x00000002 | Filter supports FSCTL_OFFLOAD_WRITE |

The filter opt-in model can be enabled or disabled based on the value present in the HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\FileSystem\\FilterSupportedFeaturesMode registry key, which has the following values:

| FilterSupportedFeaturesMode Value | Meaning                                                                             |
|-----------------------------------|-------------------------------------------------------------------------------------|
| 0 (Default)                       | Do normal opt-in processing.                                                        |
| 1                                 | Never opt-in (equivalent to setting SupportedFeatures to 0 on all filters attached) |

### Testing

To check a filter's supported features of the stack, use the fltmc utility. Run **fltmc instances –v \[volume\]:** as an elevated user, and check the *SprtFtrs* column:

* If the *SprtFtrs* value is 0x00, it implies that the filter is blocking offload on this volume. If *SprtFtrs* is set to 0x03, both offload operations are supported.

### Checking Feature Support in IRP Processing

As part of IRP processing, the [**FsRtlGetSupportedFeatures**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetsupportedfeatures) routine retrieves the aggregated **SupportedFeatures** state for all filters attached to the given volume stack. Components such as I/O Manager and SRV (SMB) call this routine to validate the **SupportedFeatures** state for all the filters on the stack. Components that roll their own offload IRPs should call this function to validate opt-in support for that operation.

### Considerations for Filter Drivers

Offloaded data transfer is a new way to move data around in the data center. Due to the integration of offload logic in the core copy engine, many applications by default will have the ability to perform offloaded data movement without explicitly opting in. As a result, filter developers need to understand how these new operations impact filters. Not understanding these operations fully or not evaluating the new data flow can potentially result in scenarios where data can become inconsistent or corrupted. The following list summarizes a set of action items for filter developers to take note of with offload:

* Understand this data flow, the impact to the filter, and the ability of the filter to support these offloaded operations.
* Update your filter installer to add a REG_DWORD value for **SupportedFeatures** to the HKLM\\System\\CurrentControlSet\\Services\\\[filter\] subkey. Initialize it to specify offload functionality.
* For filters that want to act upon offload operations, update the registration to **IRP_MJ_FILE_SYSTEM_CONTROL** to handle [**FSCTL_OFFLOAD_READ**](./fsctl-offload-read.md) and [**FSCTL_OFFLOAD_WRITE**](./fsctl-offload-write.md).
* For filters that need to block offloaded operations, return the status code STATUS_NOT_SUPPORTED from within the filter. Do not rely upon the registry value to enforce blocking offload operations since it can be changed by end users. A filter should explicitly allow or disallow offload operations.

## Copy Tokens

With offloaded operations, the file data is not seen by the I/O stack. Instead it is seen as a 512-byte token that is the logical proxy for the data. This token is either an opaque and unique string of a vendor-specific format generated by the storage subsystem, or can be of a well-known type to represent a pattern of data (such as a data range that is logically equivalent to zero). Modifications to the data that the token is a proxy for will either result in invalidating the token, or for the storage subsystem to persist the original data by some vendor-specific means (such as through a snapshot mechanism). Subsequent offload read requests to a specified range in a file results in unique tokens.

There are classes of tokens that represent a pattern of data that is well defined. The most common well known token is the Zero Token which is equivalent to zero. When a token is defined as a Well Known Token, the **TokenType** member in the **STORAGE_OFFLOAD_TOKEN** structure will be set to STORAGE_OFFLOAD_TOKEN_TYPE_WELL_KNOWN. When this field is set, the **WellKnownPattern** member determines which pattern of data the token is.

* When the **WellKnownPattern** field is set to STORAGE_OFFLOAD_PATTERN_ZERO or STORAGE_OFFLOAD_PATTERN_ZERO_WITH_PROTECTION_INFORMATION, it indicates the Zero Token. When this token is returned by a [**FSCTL_OFFLOAD_READ**](./fsctl-offload-read.md) operation, it indicates that the data contained within the desired file range is logically equivalent to zero. When this token is provided to a [**FSCTL_OFFLOAD_WRITE**](./fsctl-offload-write.md) operation, it indicates that the desired range of the file to be written to should be logically zeroed.
* Other than the Zero Token, there are no other Well Known Token patterns currently defined. It is not recommended that users define their own Well Known Token patterns.

## Truncation

The underlying storage subsystem that Windows communicates with can process less data that was desired in an offload operation. This is called truncation. With offload read, this means that the returned token represents a range of the data less than that which was requested. This is indicated by the **TransferLength** member in the [**FSCTL_OFFLOAD_READ_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_output) structure, which is a byte count from the beginning of the range of the file to be read. For offload write, a truncation indicates that less data was written than was desired. This is indicated by the **LengthWritten** member in the [**FSCTL_OFFLOAD_WRITE_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_write_output) structure, which is a byte count from the beginning of the range of the file to be written. Errors in command processing, or limitations within the stack for large ranges, result in truncation.

There are two scenarios in which NTFS truncates the range to be offload read or written:

1. The copy range will be truncated to Valid Data Length (VDL) if VDL is before the End of the File (EOF). This assumes that VDL is aligned to a logical sector boundary, otherwise see scenario.

   ![vdl occurring before eof.](images/odx-vdl-1.png)

   During a [**FSCTL_OFFLOAD_READ**](./fsctl-offload-read.md) operation, the flag OFFLOAD_READ_FLAG_ALL_ZERO_BEYOND_CURRENT_RANGE is set in the [**FSCTL_OFFLOAD_READ_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_output) structure indicating that the rest of the file contains zeros, and the **TransferLength** member is truncated to VDL.

2. Similar to Scenario 1, but when VDL is not aligned to a logical sector boundary, the desired range is truncated by NTFS to the next logical sector boundary.

   ![vdl misaligned with sector boundary.](images/odx-vdl-2.png)

## Limitations

* Offload operations are supported only on NTFS volumes.
* Offload operations are supported through remote file servers if the remote share is a NTFS volume and if the server is running Windows Server 2012 or later versions (assuming the remote stack also supports offload operations).
* NTFS does not support offload FSCTLs performed on files encrypted with Bitlocker or NTFS encryption (EFS), de-duplicated files, compressed files, resident files, sparse files, or files participating in TxF transactions.
* NTFS does not support offload FSCTLs performed on files within a volsnap snapshot.
* NTFS will fail the offload FSCTL if the desired file range is unaligned to the logical sector size on the source device or if the desired file range is unaligned to the logical sector size on the destination device. This follows the same semantics as non-cached IO.
* The destination file must be pre-allocated (**SetEndOfFile** and not **SetAllocation**) before [**FSCTL_OFFLOAD_WRITE**](./fsctl-offload-write.md).
* In processing offload read and offload write, NTFS first calls [**CcCoherencyFlushAndPurgeCache**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-cccoherencyflushandpurgecache) to commit any modified data in the system cache. This is the same semantic as non-cached IO.
