---
title: CreatePartition method of the MSFT\_Disk class
description: Creates a partition on a disk.
ms.assetid: 4356352c-462e-4283-97e1-fcf7fe173b19
keywords:
- CreatePartition method Windows Storage Management API
- CreatePartition method Windows Storage Management API , MSFT_Disk class
- MSFT_Disk class Windows Storage Management API , CreatePartition method
topic_type:
- apiref
api_name:
- MSFT_Disk.CreatePartition
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreatePartition method of the MSFT\_Disk class

Creates a partition on a disk.

## Syntax


```mof
UInt32 CreatePartition(
  [in]  UInt64  Size,
  [in]  Boolean UseMaximumSize,
  [in]  UInt64  Offset,
  [in]  UInt32  Alignment,
  [in]  Char16  DriveLetter,
  [in]  Boolean AssignDriveLetter,
  [in]  UInt16  MbrType,
  [in]  String  GptType,
  [in]  Boolean IsHidden,
  [in]  Boolean IsActive,
  [out] String  CreatedPartition,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*Size* \[in\]
 

The desired size, in bytes, for the partition. This must be equal to or less than the size specified by the disk's **LargestFreeExtent** property. This parameter cannot be used with *UseMaximumSize*.

 

*UseMaximumSize* \[in\]
 

If **TRUE**, the partition will fill the largest free extent on the disk. This parameter cannot be used with the *Size* parameter.

 

*Offset* \[in\]
 

The partition offset, in bytes. If the offset is not aligned and the *Alignment* parameter is not specified, the offset is rounded up or down to the closest alignment boundary, depending on the size of the disk on which the partition is created.

 

*Alignment* \[in\]
 

The alignment of the partition, in bytes.

 

*DriveLetter* \[in\]
 

The drive letter to be assigned to the partition at the time of creation. This parameter cannot be used with *AssignDriveLetter*. If both parameters are specified, an Invalid Parameter error will be returned. If the drive letter is not available, the partition will be created, but error '42002' will be returned.

 

*AssignDriveLetter* \[in\]
 

If **TRUE**, the next available drive letter will be assigned to the created partition. If no more drive letters are available, the partition will be created with no drive letter. This parameter cannot be used with *DriveLetter*. If both parameters are specified, an Invalid Parameter error will be returned.

 

*MbrType* \[in\]
 

Specifies the MBR partition type. This parameter can only be set if the disk's **PartitionStyle** property is **MBR**, otherwise an error will be returned. The default value of this parameter is **Huge**.



| Value                                                                                                                                                                                                                           | Meaning                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **FAT12** 1                                      | A FAT12 file system partition.                                                                                                               |
|  **FAT16** 4                                      | A FAT16 file system partition.                                                                                                               |
|  **Extended** 5  | An extended partition.                                                                                                                       |
|  **Huge** 6                  | A huge partition. This value indicates that there is no Windows file system on the partition. Use this value when creating a logical volume. |
|  **IFS** 7                                            | An NTFS or ExFAT partition.                                                                                                                  |
|  **FAT32** 12                                     | A FAT32 partition.                                                                                                                           |



 

 

*GptType* \[in\]
 

The GPT type of the partition. This parameter is only valid if the disk's **PartitionStyle** property is **GPT**, otherwise an error will be returned. The default value for this parameter is **Basic data**.



| Value                                                                                                                                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **System Partition** c12a7328-f81f-11d2-ba4b-00a0c93ec93b          | An EFI system partition.                                                                                                                                                                                                                                                                                                                                                         |
|  **Microsoft Reserved** e3c9e316-0b5c-4db8-817d-f92df00215ae  | A Microsoft reserved partition.                                                                                                                                                                                                                                                                                                                                                  |
|  **Basic data** ebd0a0a2-b9e5-4433-87c0-68b6b72699c7                                  | A basic data partition. This is the data partition type that is created and recognized by Windows. Only partitions of this type can be assigned drive letters, receive volume GUID paths, host mounted folders (also called volume mount points) and be enumerated by calls to [**FindFirstVolume**](/windows/win32/api/fileapi/nf-fileapi-findfirstvolumew) and [**FindNextVolume**](/windows/win32/api/fileapi/nf-fileapi-findnextvolumew). |
|  **LDM Metadata** 5808c8aa-7e8f-42e0-85d2-e1e90434cfb3                          | A Logical Disk Manager (LDM) metadata partition on a dynamic disk.                                                                                                                                                                                                                                                                                                               |
|  **LDM Data** af9b60a0-1431-4f62-bc68-3311714a69ad                                          | The partition is an LDM data partition on a dynamic disk.                                                                                                                                                                                                                                                                                                                        |
|  **Microsoft Recovery** de94bba4-06d1-4d40-a16a-bfd50179d6ac  | A Microsoft recovery partition.                                                                                                                                                                                                                                                                                                                                                  |



 

 

*IsHidden* \[in\]
 

If **TRUE**, the partition will not be able to receive a drive letter assignment, nor will the mount manager assign a volume GUID name. The partition will not be enumerated by the [**FindFirstVolume**](/windows/win32/api/fileapi/nf-fileapi-findfirstvolumew) and [**FindNextVolume**](/windows/win32/api/fileapi/nf-fileapi-findnextvolumew) functions. The partition can be opened by its associated volume device name (for example, "\\\\?GLOBALROOT\\Device\\HarddiskVolumeX").

 

*IsActive* \[in\]
 

If **TRUE**, the partition's MBR active bit will be set, and the partition will become bootable. This parameter is only valid for MBR disks.

 

*CreatedPartition* \[out\]
 

A string that contains an embedded [**MSFT\_Partition**](msft-partition.md) object that represents the partition that was created.

 

*ExtendedStatus* \[out\]
 

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

 

## Return value

 

**Success** (0)
 

**Not Supported** (1)
 

**Unspecified Error** (2)
 

**Timeout** (3)
 

**Failed** (4)
 

**Invalid Parameter** (5)
 

**Disk is in use** (6)
 

**Size Not Supported** (4097)
 

**Not enough free space** (40000)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**You must specify a size by using either the Size or the UseMaximumSize parameter. You can specify only one of these parameters at a time.** (40005)
 

**The disk has not been initialized.** (41000)
 

**The disk is read only.** (41002)
 

**The disk is offline.** (41003)
 

**The disk's partition limit has been reached.** (41004)
 

**The specified partition alignment is not valid. It must be a multiple of the disk's sector size.** (41005)
 

**A parameter is not valid for this type of partition.** (41006)
 

**The specified partition type is not valid.** (41010)
 

**Only the first 2 TB are usable on MBR disks.** (41011)
 

**The specified offset is not valid.** (41012)
 

**There is no media in the device.** (41015)
 

**The specified offset is not valid.** (41016)
 

**The specified partition layout is invalid.** (41017)
 

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation.** (41018)
 

**The requested access path is already in use.** (42002)
 

**Cannot assign access paths to hidden partitions.** (42004)
 

**The access path is not valid.** (42007)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Disk**](msft-disk.md)
 

 

