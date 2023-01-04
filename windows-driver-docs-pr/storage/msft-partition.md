---
title: MSFT\_Partition class
description: Represents a partition on a disk.
ms.assetid: d692d4f5-c912-48ec-98a6-9c72ac6e75f6
keywords:
- MSFT_Partition class Windows Storage Management API
- MSFT_Partition class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_Partition
- MSFT_Partition.DiskNumber
- MSFT_Partition.PartitionNumber
- MSFT_Partition.DriveLetter
- MSFT_Partition.AccessPaths
- MSFT_Partition.OperationalStatus
- MSFT_Partition.TransitionState
- MSFT_Partition.Size
- MSFT_Partition.MbrType
- MSFT_Partition.GptType
- MSFT_Partition.Guid
- MSFT_Partition.IsReadOnly
- MSFT_Partition.IsOffline
- MSFT_Partition.IsSystem
- MSFT_Partition.IsBoot
- MSFT_Partition.IsActive
- MSFT_Partition.IsHidden
- MSFT_Partition.IsShadowCopy
- MSFT_Partition.NoDefaultDriveLetter
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_Partition class

Represents a partition on a disk.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_Partition : MSFT_StorageObject
{
  UInt32  DiskNumber;
  UInt32  PartitionNumber;
  Char16  DriveLetter;
  String  AccessPaths[];
  UInt16  OperationalStatus;
  UInt16  TransitionState;
  UInt64  Size;
  UInt16  MbrType;
  String  GptType;
  String  Guid;
  Boolean IsReadOnly;
  Boolean IsOffline;
  Boolean IsSystem;
  Boolean IsBoot;
  Boolean IsActive;
  Boolean IsHidden;
  Boolean IsShadowCopy;
  Boolean NoDefaultDriveLetter;
};
```

## Members

The **MSFT\_Partition** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_Partition** class has these methods.



| Method                                                       | Description                                                                                                                                       |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddAccessPath**](addaccesspath-msft-partition.md)        | Adds a mount path or drive letter assignment to the partition.                                                                         |
| [**DeleteObject**](msft-partition-deleteobject.md)          | Deletes the partition and corresponding volume.                                                                                        |
| [**GetAccessPaths**](getaccesspaths-msft-partition.md)      | Retrieves all mount points and drive letters that can be used to access the partition.                                                 |
| [**GetSupportedSize**](msft-partition-getsupportedsizes.md) | Retrieves the minimum and maximum sizes that the partition can be resized to using the [**Resize**](msft-partition-resize.md) method. |
| [**Offline**](msft-partition-offline.md)                    | Takes the partition offline by dismounting the associated volume (if one exists).                                                      |
| [**Online**](msft-partition-online.md)                      | Brings the partition online by mounting the associated volume (if one exists).                                                         |
| [**RemoveAccessPath**](removeaccesspath-msft-partition.md)  | Remove an access path from the partition.                                                                                              |
| [**Resize**](msft-partition-resize.md)                      | Resizes the partition and any associated file system volume to the size specified by the *Size* parameter.                             |
| [**SetAttributes**](msft-partition-setattributes.md)        | Sets various attributes and properties of the partition.                                                                               |



 

### Properties

The **MSFT\_Partition** class has these properties.

 

**AccessPaths**
   

Data type: **String** array
 

Access type: Read-only
 

An array of strings containing the various mount points for the partition. This list includes drive letters, in addition to mounted folders.

 

**DiskNumber**
   

Data type: **UInt32**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**ModelCorrespondence {"MSFT\_Disk.Number"}**](/windows/win32/wmisdk/standard-qualifiers)
 

The operating system's number for the disk that contains this partition. Disk numbers may not necessarily remain the same across restarts.

 

**DriveLetter**
   

Data type: **Char16**
 

Access type: Read-only
 

The currently assigned drive letter for the partition. This property is **NULL** if no drive letter has been assigned.

 

**GptType**
   

Data type: **String**
 

Access type: Read-only
 

The partition's GPT type. This property is only valid when the disk's **PartitionStyle** property is **GPT** and will be **NULL** for all other partition styles.



| Value                                                                                                                                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **System Partition** c12a7328-f81f-11d2-ba4b-00a0c93ec93b          | An EFI system partition.                                                                                                                                                                                                                                                                                                                                                         |
|  **Microsoft Reserved** e3c9e316-0b5c-4db8-817d-f92df00215ae  | A Microsoft reserved partition.                                                                                                                                                                                                                                                                                                                                                  |
|  **Basic data** ebd0a0a2-b9e5-4433-87c0-68b6b72699c7                                  | A basic data partition. This is the data partition type that is created and recognized by Windows. Only partitions of this type can be assigned drive letters, receive volume GUID paths, host mounted folders (also called volume mount points) and be enumerated by calls to [**FindFirstVolume**](/windows/win32/api/fileapi/nf-fileapi-findfirstvolumew) and [**FindNextVolume**](/windows/win32/api/fileapi/nf-fileapi-findnextvolumew). |
|  **LDM Metadata** 5808c8aa-7e8f-42e0-85d2-e1e90434cfb3                          | A Logical Disk Manager (LDM) metadata partition on a dynamic disk.                                                                                                                                                                                                                                                                                                               |
|  **LDM Data** af9b60a0-1431-4f62-bc68-3311714a69ad                                          | The partition is an LDM data partition on a dynamic disk.                                                                                                                                                                                                                                                                                                                        |
|  **Microsoft Recovery** de94bba4-06d1-4d40-a16a-bfd50179d6ac  | A Microsoft recovery partition.                                                                                                                                                                                                                                                                                                                                                  |



 

 

**Guid**
   

Data type: **String**
 

Access type: Read-only
 

The partition's GPT GUID. This property is only valid when the disk's **PartitionStyle** property is **GPT** and will be **NULL** for all other partition styles.

 

**IsActive**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the partition is active and can be used to start the system. This property is only valid when the disk's **PartitionStyle** property is **MBR** and will be **NULL** for all other partition styles.

 

**IsBoot**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the partition is the current boot partition.

 

**IsHidden**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the partition is not detected by the mount manager. As a result, the partition does not receive a drive letter, does not receive a volume GUID path, does not host volume mount points, and is not enumerated by calls to [**FindFirstVolume**](/windows/win32/api/fileapi/nf-fileapi-findfirstvolumew) and [**FindNextVolume**](/windows/win32/api/fileapi/nf-fileapi-findnextvolumew). This ensures that applications such as Disk Defragmenter do not access the partition. The [Volume Shadow Copy Service (VSS)](/windows/win32/vss/volume-shadow-copy-service-portal) uses this attribute on its shadow copies.

 

**IsOffline**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, this partition is currently offline.

 

**IsReadOnly**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, this is a read-only partition.

 

**IsShadowCopy**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the partition is a shadow copy of another partition. This attribute is used by VSS. This attribute is an indication for file system filter driver-based software (such as antivirus programs) to avoid attaching to the volume. An application can use this attribute to differentiate a shadow copy partition from a production partition. For example, an application that performs a fast recovery will break a shadow copy virtual disk by clearing the read-only and hidden attributes and this attribute. This attribute is set when the shadow copy is created and cleared when the shadow copy is broken.

 

**IsSystem**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, this is a system partition.

 

**MbrType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The partition's MBR type. This property is only valid when the disk's **PartitionStyle** property is **MBR** and will be **NULL** for all other partition styles.

 

**FAT12** (1)
 

**FAT16** (4)
 

**Extended** (5)
 

**Huge** (6)
 

**IFS** (7)
 

**FAT32** (12)
 

 

**NoDefaultDriveLetter**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the operating system does not assign a drive letter automatically when the partition is discovered. This is only honored for GPT disks and is assumed to be **FALSE** for MBR disks. This attribute is useful in storage area network (SAN) environments.

 

**OperationalStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Values**](/windows/win32/wmisdk/standard-qualifiers) ( "Unknown", "Online", "No Media", "Failed", "Offline" ), [**ValueMap**](/windows/win32/wmisdk/standard-qualifiers) ( "0", "1", "3", "5", "4" )
 

The operational status of the partition.

 

**PartitionNumber**
   

Data type: **UInt32**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The operating system's number for the partition. Ordering is based on the partition's offset, relative to other partitions. This means that the value for this property may change based off of the partition configuration in the offset range preceding this partition.

 

**Size**
   

Data type: **UInt64**
 

Access type: Read-only
 

Total size of the partition, measured in bytes.

 

**TransitionState**
   

Data type: **UInt16**
 

Access type: Read-only
 

The transition state of the partition. One of the following values.



| Value                                                                        | Meaning                                                                                 |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
|  0  | This value is reserved for system use.                                       |
|  1  | The partition is stable. No configuration activity is currently in progress. |
|  2  | The partition is being extended.                                             |
|  3  | The partition is being shrunk.                                               |
|  4  | The partition is being automagically reconfigured.                           |
|  8  | The partition is being restriped.                                            |



 

 

## Remarks

**Starting in Windows 10:** **MSFT\_Partition** derives from [**MSFT\_StorageObject**](msft-storageobject.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

