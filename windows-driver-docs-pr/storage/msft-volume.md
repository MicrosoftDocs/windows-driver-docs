---
title: MSFT\_Volume class
description: Represents a volume on a computer.
ms.assetid: 007dd46a-4812-4273-beaa-74fbe9520c7d
keywords:
- MSFT_Volume class Windows Storage Management API
- MSFT_Volume class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Volume
- MSFT_Volume.DriveLetter
- MSFT_Volume.Path
- MSFT_Volume.HealthStatus
- MSFT_Volume.FileSystem
- MSFT_Volume.FileSystemLabel
- MSFT_Volume.FileSystemType
- MSFT_Volume.Size
- MSFT_Volume.SizeRemaining
- MSFT_Volume.DriveType
- MSFT_Volume.DedupMode
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_Volume class

Represents a volume on a computer.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_Volume : MSFT_StorageObject
{
  Char16 DriveLetter;
  String Path;
  UInt16 HealthStatus;
  String FileSystem;
  String FileSystemLabel;
  UInt16 FileSystemType;
  UInt64 Size;
  UInt64 SizeRemaining;
  UInt32 DriveType;
  UInt32 DedupMode;
};
```

## Members

The **MSFT\_Volume** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_Volume** class has these methods.



| Method                                                                   | Description                                                                       |
|:-------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**DeleteObject**](msft-volume-deleteobject.md)                         | Deletes the volume.                                                    |
| [**Diagnose**](msft-volume-diagnose.md)                                 | Performs a diagnostic on the volume, returning any actionable results. |
| [**Flush**](msft-volume-flush.md)                                       | Flushes the cached data in the volume's file system to disk.           |
| [**Format**](format-msft-volume.md)                                     | Formats the volume.                                                    |
| [**GetAttributes**](msft-volume-getattributes.md)                       | Retrieves the volume attributes.                                       |
| [**GetCorruptionCount**](msft-volume-getcorruptioncount.md)             | Retrieves the corruption count for the volume.                         |
| [**GetDedupProperties**](msft-volume-getdeduplicationstatistics.md)     | Gets deduplication properties of the volume.                           |
| [**GetSupportedClusterSizes**](msft-volume-getsupportedclustersizes.md) | Retrieves the supported cluster sizes for the volume.                  |
| [**GetSupportedFileSystems**](msft-volume-getsupportedfilesystems.md)   | Retrieves the names of file systems that are supported on the volume.  |
| [**Optimize**](optimize-msft-volume.md)                                 | Optimizes the volume.                                                  |
| [**Repair**](repair-msft-volume.md)                                     | Repairs the volume.                                                    |
| [**Resize**](msft-volume-resize.md)                                     | Resizes the volume.                                                    |
| [**SetAttributes**](msft-volume-setattributes.md)                       | Sets or changes the volume attributes.                                 |
| [**SetDedupMode**](msft-volume-setdeduplication.md)                     | Enables or disables deduplication on the volume.                       |
| [**SetFileSystemLabel**](msft-volume-setfilesystemlabel.md)             | Sets the file system label for the volume.                             |



 

### Properties

The **MSFT\_Volume** class has these properties.

 

**DedupMode**
   

Data type: **UInt32**
 

Access type: Read-only
 

**Starting in Windows 10:** Indicates whether deduplication is available, disabled, or the deduplication mode of the volume.

 

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
 

<span id="GeneralPurpose"></span><span id="generalpurpose"></span><span id="GENERALPURPOSE"></span>**GeneralPurpose** (1)
 

<span id="HyperV"></span><span id="hyperv"></span><span id="HYPERV"></span>**HyperV** (2)
 

<span id="Backup"></span><span id="backup"></span><span id="BACKUP"></span>**Backup** (3)
 

<span id="NotAvailable"></span><span id="notavailable"></span><span id="NOTAVAILABLE"></span>**NotAvailable** (4)
 

 

**DriveLetter**
   

Data type: **Char16**
 

Access type: Read-only
 

The volume drive letter.

 

**DriveType**
   

Data type: **UInt32**
 

Access type: Read-only
 

The type of the volume.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Invalid_Root_Path"></span><span id="invalid_root_path"></span><span id="INVALID_ROOT_PATH"></span>**Invalid Root Path** (1)
 

<span id="Removable"></span><span id="removable"></span><span id="REMOVABLE"></span>**Removable** (2)
 

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>**Fixed** (3)
 

<span id="Remote"></span><span id="remote"></span><span id="REMOTE"></span>**Remote** (4)
 

<span id="CD-ROM"></span><span id="cd-rom"></span>**CD-ROM** (5)
 

<span id="RAM_Disk"></span><span id="ram_disk"></span><span id="RAM_DISK"></span>**RAM Disk** (6)
 

 

**FileSystem**
   

Data type: **String**
 

Access type: Read-only
 

The volume's file system. One of the following:

-   "NTFS"
-   "ReFS"
-   "FAT32"
-   "CSVFS"

 

**FileSystemLabel**
   

Data type: **String**
 

Access type: Read-only
 

The volume's file system label.

 

**FileSystemType**
   

Data type: **UInt16**
 

Access type: Read-only
 

**Starting in Windows 10:** The underlying file system on the volume. It can have one of the following values:

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

 (Threshold)
 

<span id="UFS"></span><span id="ufs"></span>**UFS** (2)
 

<span id="HFS"></span><span id="hfs"></span>**HFS** (3)
 

<span id="FAT"></span><span id="fat"></span>**FAT** (4)
 

<span id="FAT16"></span><span id="fat16"></span>**FAT16** (5)
 

<span id="FAT32"></span><span id="fat32"></span>**FAT32** (6)
 

<span id="NTFS4"></span><span id="ntfs4"></span>**NTFS4** (7)
 

<span id="NTFS5"></span><span id="ntfs5"></span>**NTFS5** (8)
 

<span id="XFS"></span><span id="xfs"></span>**XFS** (9)
 

<span id="AFS"></span><span id="afs"></span>**AFS** (10)
 

<span id="EXT2"></span><span id="ext2"></span>**EXT2** (11)
 

<span id="EXT3"></span><span id="ext3"></span>**EXT3** (12)
 

<span id="ReiserFS"></span><span id="reiserfs"></span><span id="REISERFS"></span>**ReiserFS** (13)
 

<span id="NTFS"></span><span id="ntfs"></span>**NTFS** (14)
 

<span id="ReFS"></span><span id="refs"></span><span id="REFS"></span>**ReFS** (15)
 

<span id="CSVFS_NTFS"></span><span id="csvfs_ntfs"></span>**CSVFS\_NTFS** (0x8000)
 

<span id="CSVFS_ReFS"></span><span id="csvfs_refs"></span><span id="CSVFS_REFS"></span>**CSVFS\_ReFS** (0x8001)
 

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

The health status of the volume.

 

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>**Healthy** (0)
 

<span id="Scan_Needed"></span><span id="scan_needed"></span><span id="SCAN_NEEDED"></span>**Scan Needed** (1)
 

<span id="Spot_Fix_Needed"></span><span id="spot_fix_needed"></span><span id="SPOT_FIX_NEEDED"></span>**Spot Fix Needed** (2)
 

<span id="Full_Repair_Needed"></span><span id="full_repair_needed"></span><span id="FULL_REPAIR_NEEDED"></span>**Full Repair Needed** (3 )
 

 

**Path**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The volume path.

 

**Size**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

Total size, in bytes, of the volume.

 

**SizeRemaining**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("Bytes")
 

The total space, in bytes, that is currently free on the volume.

 

## Remarks

**Starting in Windows 10:** **MSFT\_Volume** derives from [**MSFT\_StorageObject**](msft-storageobject.md). It now inherits the property *ObjectId*, which was formerly a property of **MSFT\_Volume**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

