---
title: Storage Management API Common Return Codes
description: Storage Management API Common Return Codes
ms.topic: article
ms.date: 12/18/2024
topic_type: 
- kbArticle
---

# SMP API common return codes

This article lists common return codes encountered when working with the Storage Management Provider (SMP) API.

For related information, see [Storage Management API Classes](storage-management-api-classes.md)

## Standard CIM Return Codes

| Error Value | Description |
| ----------- | ----------- |
| 0           | Success    |
| 1           | Not Supported |
| 2           | Unspecified Error |
| 3           | Timeout |
| 4           | Failed  |
| 5           | Invalid Parameter |
| 6           | In Use / Disk is in use |
| 7           | This command isn't supported on x86 running in x64 environment |
| 8           | Object Not Found |

## Extended CIM Return Codes

| Error Value | Description                             |
|-------------|-----------------------------------------|
| 4096        | Method Parameters Checked - Job Started |
| 4097        | Size not supported                      |
| 4098        | Timeout not supported                   |
| 4099        | The device is busy                      |

## Storage Management API Return Codes

### Common Errors 40000 - 40999

| Error Value | Description |
| ----------- | ----------- |
| 40000       | Not enough available capacity |
| 40001       | Access denied   |
| 40002       | There aren't enough resources to complete the operation. |
| 40003       | Cache out of date  |
| 40004       | An unexpected I/O error occurred  |
| 40005       | You must specify a size by using either the Size or the UseMaximumSize parameter. You can specify only one of these parameters at a time. |
| 40006       | The object or object type requested doesn't exist in cache.  |
| 40007       | The request failed due to a fatal device hardware error.  |
| 40018       | The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation. |

### Disk Errors 41000 - 41999

| Error Value | Description |
| ----------- | ----------- |
| 41000       | The disk hasn't been initialized.  |
| 41001       | The disk is already initialized.  |
| 41002       | The disk is read only. |
| 41003       | The disk is offline. |
| 41004       | The disk's partition limit has been reached. |
| 41005       | The specified partition alignment isn't valid. It must be a multiple of the disk's sector size. |
| 41006       | A parameter isn't valid for this type of partition.   |
| 41007       | Can't clear with OEM partitions present. To clear OEM partitions, use the RemoveOEM flag.       |
| 41008       | Can't clear with data partitions present. To clear data partitions, use the RemoveData flag.    |
| 41009       | Operation not supported on a critical disk.  |
| 41010       | The specified partition type isn't valid.  |
| 41011       | Only the first 2 TB are usable on MBR disks.  |
| 41012       | The specified offset isn't valid. |
| 41013       | Can't convert the style of a disk with data or other known partitions on it.  |
| 41014       | The disk isn't large enough to support a GPT partition style. |

### Partition Errors 42000 - 42999

| Error Value | Description |
| ----------- | ----------- |
| 42000       | The partition was deleted, although its access paths weren't.     |
| 42001       | The extended partition still contains other partitions.            |
| 42002       | The requested access path is already in use.                       |
| 42004       | Can't assign access paths to hidden partitions.                   |
| 42005       | Can't remove a volume GUID path.                                  |
| 42006       | Can't remove the drive letter of a boot or paging file partition. |
| 42007       | The access path isn't valid.                                      |
| 42008       | Can't shrink a partition containing a volume with errors.         |
| 42009       | Can't resize a partition containing an unknown file system.       |
| 42010       | The operation isn't allowed on a system or critical partition.    |
| 42011       | This operation is only supported on data partitions.               |
| 42012       | Can't assign multiple drive letters to a partition.               |
| 42013       | Can't assign drive letter to this type of partition.              |

### Volume Errors 43000 - 43999

| Error Value | Description |
| ----------- | ----------- |
| 43000       | The specified cluster size is invalid  |
| 43001       | The specified file system isn't supported   |
| 43002       | The volume can't be quick-formatted  |
| 43003       | The number of clusters exceeds 32 bits   |
| 43004       | The specified UDF version isn't supported  |
| 43005       | The cluster size must be a multiple of the disk's physical sector size |
| 43006       | Can't perform the requested operation when the drive is read only  |
| 43007       | The repair failed   |
| 43008       | The scan failed |
| 43009       | A snapshot error occurred while scanning this drive. You can try again, but if this problem persists, run an offline scan and fix. |
| 43010       | A scan is already running on this drive. Chkdsk can't run more than one scan on a drive at a time.   |
| 43011       | A snapshot error occurred while scanning this drive. You can try again, but if this problem persists, run an offline scan and fix. |
| 43012       | A snapshot error occurred while scanning this drive. Run an offline scan and fix.  |
| 43013       | Can't open drive for direct access  |
| 43014       | Can't determine the file system of the drive |
| 43015       | This setting can't be changed due to the group policy setting  |
| 43016       | This setting can't be changed due to the global registry setting  |

### Storage Provider Errors 46000 - 46999

| Error Value | Description |
| ----------- | ----------- |
| 46000       | The storage provider can't connect to the storage provider. |
| 46001       | The storage provider can't connect to the storage subsystem. |
| 46002       | The storage provider doesn't support a required profile. |
| 46003       | The storage provider doesn't support a required association. |
| 46004       | Can't register/unregister the storage subsystem on local host. |
| 46005       | The storage subsystem isn't registered.  |
| 46006       | This subsystem is already registered.  |
| 46007       | This subsystem is already registered with another user's credentials. Use the -Force flag to remove the existing registration and add a new one anyway. |
| 46008       | Failover clustering couldn't be enabled for this storage object. |

### Storage Subsystem Errors 47000 - 47999

| Error Value | Description |
| ----------- | ----------- |
| 47000       | No storage pools were found that can support this virtual disk configuration.                   |
| 47001       | This subsystem doesn't support creation of virtual disks with the specified provisioning type. |

### Partition Errors 48000 - 48999

| Error Value | Description |
| ----------- | ----------- |
| 48000       | This operation isn't supported on primordial storage pools.  |
| 48001       | The storage pool is reserved for special usage only.   |
| 48002       | The specified resiliency setting isn't supported by this storage pool.  |
| 48004       | There aren't enough physical disks in the storage pool to create the specified virtual disk configuration.  |
| 48005       | The specified storage pool couldn't be found. |
| 48006       | The storage pool couldn't complete the operation because its health or operational status doesn't permit it.  |
| 48007       | The storage pool couldn't complete the operation because its configuration is read-only.  |
| 48008       | The storage pool contains virtual disks.  |
| 48009       | The number of thin provisioning alert thresholds specified exceeds the limit for this storage pool.  |
| 48010       | You must specify the size info (either the Size or UseMaximumSize parameter) or the tier info (the StorageTiers and StorageTierSizes parameters), but not both size info and tier info. |
| 48011       | No autoallocation drives found in storage pool. |

### Resiliency Settings Errors 49000 - 49999

| Error Value | Description |
| ----------- | ----------- |
| 49000       | No resiliency setting with that name exists.                                      |
| 49001       | The value for NoSinglePointOfFailure isn't supported.                            |
| 49002       | The value for PhysicalDiskRedundancy is outside of the supported range of values. |
| 49003       | The value for NumberOfDataCopies is outside of the supported range of values.     |
| 49004       | The value for ParityLayout is outside of the supported range of values.           |
| 49005       | The value for Interleave is outside of the supported range of values.             |
| 49006       | The value for NumberOfColumns is outside of the supported range of values.        |

### Virtual Disk Errors 50000 - 50999

| Error Value | Description |
| ----------- | ----------- |
| 50000       | The specified virtual disk couldn't be found.  |
| 50001       | Couldn't repair the virtual disk because too many physical disks failed. Not enough information exists on the remaining physical disks to reconstruct the lost data. |
| 50002       | The virtual disk couldn't complete the operation because another computer controls its configuration.  |
| 50003       | The virtual disk couldn't complete the operation because its health or operational status doesn't permit it.  |
| 50004       | The virtual disk couldn't complete the operation because its Manual Attach status doesn't permit it.  |
| 50005       | The value for WriteCacheSize is outside of the supported range of values. |

### Physical Disk Errors 51000 - 51999

| Error Value | Description |
| ----------- | ----------- |
| 51000       | One of the physical disks specified isn't supported by this operation.                            |
| 51001       | Not enough physical disks were specified to successfully complete the operation.                   |
| 51002       | One of the physical disks specified is already in use.                                             |
| 51003       | One of the physical disks specified uses a sector size that isn't supported by this storage pool. |
| 51004       | One of the physical disks specified couldn't be removed because it's still in use.               |
| 51005       | One or more physical disks aren't connected to the nodes on which the pool is being created.      |

### Masking Set Errors 52000 - 52999

| Error Value | Description                                           |
|-------------|-------------------------------------------------------|
| 52000       | The device number specified isn't valid.             |
| 52001       | The HostType requested isn't supported.              |
| 52002       | DeviceAccess must be specified for each virtual disk. |

### Initiator ID Errors 53000 - 53999

| Error Value | Description |
| ----------- | ----------- |
| 53000       | The initiator address specified isn't valid |
| 53001       | Only one initiator address is acceptable for this operation. |

## Target Port Errors 54000 - 54999

| Error Value | Description                                     |
|-------------|-------------------------------------------------|
| 54000       | The target port address specified isn't valid. |
