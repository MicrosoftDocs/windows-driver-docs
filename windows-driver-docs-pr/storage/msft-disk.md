---
title: MSFT\_Disk class
description: Represents a Windows disk.
ms.assetid: a3703b30-5e32-4bcf-9abd-fd3fb67fa6b6
keywords:
- MSFT_Disk class Windows Storage Management API
- MSFT_Disk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_Disk
- MSFT_Disk.Path
- MSFT_Disk.Location
- MSFT_Disk.FriendlyName
- MSFT_Disk.UniqueId
- MSFT_Disk.UniqueIdFormat
- MSFT_Disk.Number
- MSFT_Disk.SerialNumber
- MSFT_Disk.FirmwareVersion
- MSFT_Disk.Manufacturer
- MSFT_Disk.Model
- MSFT_Disk.Size
- MSFT_Disk.AllocatedSize
- MSFT_Disk.LogicalSectorSize
- MSFT_Disk.PhysicalSectorSize
- MSFT_Disk.LargestFreeExtent
- MSFT_Disk.NumberOfPartitions
- MSFT_Disk.ProvisioningType
- MSFT_Disk.OperationalStatus
- MSFT_Disk.HealthStatus
- MSFT_Disk.BusType
- MSFT_Disk.PartitionStyle
- MSFT_Disk.Signature
- MSFT_Disk.Guid
- MSFT_Disk.IsOffline
- MSFT_Disk.OfflineReason
- MSFT_Disk.IsReadOnly
- MSFT_Disk.IsSystem
- MSFT_Disk.IsClustered
- MSFT_Disk.IsBoot
- MSFT_Disk.BootFromDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_Disk class

Represents a Windows disk.

A **MSFT\_Disk** object models the Windows operating system's concept of a disk device. The disk may be directly attached to the computer system, or it may be a virtual disk exposed to the system through the use of a Storage Management Provider.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_Disk : MSFT_StorageObject
{
  String  Path;
  String  Location;
  String  FriendlyName;
  String  UniqueId;
  UInt16  UniqueIdFormat;
  UInt32  Number;
  String  SerialNumber;
  String  FirmwareVersion;
  String  Manufacturer;
  String  Model;
  UInt64  Size;
  UInt64  AllocatedSize;
  UInt32  LogicalSectorSize;
  UInt32  PhysicalSectorSize;
  UInt64  LargestFreeExtent;
  UInt32  NumberOfPartitions;
  UInt16  ProvisioningType;
  UInt16  OperationalStatus;
  UInt16  HealthStatus;
  UInt16  BusType;
  UInt16  PartitionStyle;
  UInt32  Signature;
  String  Guid;
  Boolean IsOffline;
  UInt16  OfflineReason;
  Boolean IsReadOnly;
  Boolean IsSystem;
  Boolean IsClustered;
  Boolean IsBoot;
  Boolean BootFromDisk;
};
```

## Members

The **MSFT\_Disk** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_Disk** class has these methods.



| Method                                               | Description                                                                                     |
|:-----------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**Clear**](clear-msft-disk.md)                     | Removes partition information and uninitializes a disk, returning it to a RAW state. |
| [**ConvertStyle**](msft-disk-convertstyle.md)       | Converts the partition style of an already initialized disk.                         |
| [**CreatePartition**](createpartition-msft-disk.md) | Creates a partition on a disk.                                                       |
| [**Initialize**](initialize-msft-disk.md)           | Initializes a RAW disk with a particular partition style.                            |
| [**Offline**](msft-disk-offline.md)                 | Takes the disk offline.                                                              |
| [**Online**](msft-disk-online.md)                   | Brings the disk online.                                                              |
| [**Refresh**](msft-disk-refresh.md)                 | Refreshes the cached disk layout information.                                        |
| [**SetAttributes**](msft-disk-setattributes.md)     | Sets the disk's attributes and properties.                                           |



 

### Properties

The **MSFT\_Disk** class has these properties.

 

**AllocatedSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**Units**](/windows/win32/wmisdk/standard-qualifiers) (Bytes)
 

The amount of space, in bytes, that is currently used on the disk.

 

**BootFromDisk**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if the computer is configured to start from this disk. On computers with BIOS firmware, this is the first disk that the firmware detects during startup. On computers that use EFI firmware, this is the disk that contains the EFI System Partition (ESP). If there are no disks, or if there are multiple disks with an ESP partition, this property is not set for any disk.

 

**BusType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The I/O bus type used by the disk.



| Value                                                                                                                                                                                                                                                                             | Meaning                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
|  **Unknown** 0                                                        | The bus type is unknown.               |
|  **SCSI** 1                                                                                           | SCSI                                   |
|  **ATAPI** 2                                                                                        | ATAPI                                  |
|  **ATA** 3                                                                                              | ATA                                    |
|  **1394** 4                                                                                                                  | IEEE 1394                              |
|  **SSA** 5                                                                                              | SSA                                    |
|  **Fibre Channel** 6                                | Fibre Channel                          |
|  **USB** 7                                                                                              | USB                                    |
|  **RAID** 8                                                                                           | RAID                                   |
|  **iSCSI** 9                                                                | iSCSI                                  |
|  **SAS** 10                                                                                             | Serial Attached SCSI (SAS)             |
|  **SATA** 11                                                                                          | Serial ATA (SATA)                      |
|  **SD** 12                                                                                                | Secure Digital (SD)                    |
|  **MMC** 13                                                                                             | Multimedia Card (MMC)                  |
|  **Virtual** 14                                                       | This value is reserved for system use. |
|  **File Backed Virtual**  15   | File-Backed Virtual                    |
|  **Storage Spaces**  16                       | Storage spaces                         |
|  **NVMe** 17                                                                   | NVMe                                   |



 

 

**FirmwareVersion**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the disk's firmware version.

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-friendly, display-oriented string to identify the disk.

 

**Guid**
   

Data type: **String**
 

Access type: Read-only
 

If the **PartitionStyle** is GPT, this property contains the GUID for the disk. This property will be NULL for all other disk types.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

The health status of the disk device.



| Value                                                                                                                                                                                                                               | Meaning                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|  **Healthy** 0          | The disk is functioning normally.                                                                                     |
|  **Warning** 1          | The disk is still functioning, but has detected errors or issues that require administrator intervention.             |
|  **Unhealthy** 2  | The volume is not functioning, due to errors or failures. The volume needs immediate attention from an administrator. |



 

 

**IsBoot**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if the disk contains the boot partition.

 

**IsClustered**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if the disk is used in a clustered environment, or **FALSE** otherwise.

 

**IsOffline**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if the disk is offline, or **FALSE** otherwise.

 

**IsReadOnly**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if the disk is read-only, or **FALSE** if it is read/write.

 

**IsSystem**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if this disk contains the system partition, or **FALSE** otherwise.

 

**LargestFreeExtent**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) (Bytes)
 

The largest contiguous block of free space on the disk. This is also the largest size of a partition that can be created on the disk.

 

**Location**
   

Data type: **String**
 

Access type: Read-only
 

A string that contains the PnP location path of the disk. The format of this string depends on the bus type. If the bus type is SCSI, SAS, or PCI RAID, the format is *AdapterPnpLocationPath*\#*BusType*(P*PathId*T*TargetId*L*LunId*). If the bus type is IDE, ATA, PATA, or SATA, the format is *AdapterPnpLocationPath*\#*BusType*(C*PathId*T*TargetId*L*LunId*). See the following Remarks section for a table that lists the parts of this string.

> [!Note]  
> For Hyper-V and VHD images, this property is **NULL**, because the virtual controller does not return the location path.

 

For more information about this property, see the following Remarks section.

 

**LogicalSectorSize**
   

Data type: **UInt32**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) (Bytes)
 

The logical sector size of the disk, in bytes. For example, a 4K native disk will report 4096, while a 512 emulated disk will report 512.

 

**Manufacturer**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the disk's hardware manufacturer.

 

**Model**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the disk's model number.

 

**Number**
   

Data type: **UInt32**
 

Access type: Read-only
 

The operating system's number for the disk. Disk 0 is typically the boot device. Disk numbers may not necessarily remain the same across restarts.

 

**NumberOfPartitions**
   

Data type: **UInt32**
 

Access type: Read-only
 

The number of partitions that have been created on the disk.

 

**OfflineReason**
   

Data type: **UInt16**
 

Access type: Read-only
 

If **IsOffline** is **TRUE**, this property contains the reason for the disk being offline.

One of the following values.



| Value                                                                                                                                                                                                                                                                                                           | Meaning                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
|  **Policy** 1                                                                                          | The user requested the disk to be offline.                       |
|  **Redundant Path** 2                                                          | The disk is used for multi-path I/O.                             |
|  **Snapshot** 3                                                                                  | The disk is a snapshot disk.                                     |
|  **Collision** 4                                                                              | There was a signature or identifier collision with another disk. |
|  **Resource Exhaustion** 5                                      | There were insufficient resources to bring the disk online.      |
|  **Critical Write Failures** 6                      | There were critical write failures on the disk.                  |
|  **Data Integrity Scan Required** 7  | A data integrity scan is required.                               |



 

 

**OperationalStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

The operational status of the disk device.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0                                                                               | The operational status is unknown.                                                                                                                                         |
|  **Other** 1                                                                                       | A vendor-specific *OperationalStatus* has been specified by setting the *OtherOperationalStatusDescription* property.                                                      |
|  **OK** 2                                                                                                                        | The disk is responding to commands and is in a normal operating state.                                                                                                     |
|  **Degraded** 3                                                                           | The disk is responding to commands, but is not running in an optimal operating state.                                                                                      |
|  **Stressed** 4                                                                           | The disk is functioning, but needs attention. For example, the disk might be overloaded or overheated.                                                                     |
|  **Predictive Failure** 5                                   | The disk is functioning, but a failure is likely to occur in the near future.                                                                                              |
|  **Error** 6                                                                                       | An error has occurred.                                                                                                                                                     |
|  **Non-Recoverable Error** 7                       | A non-recoverable error has occurred.                                                                                                                                      |
|  **Starting** 8                                                                           | The disk is in the process of starting.                                                                                                                                    |
|  **Stopping** 9                                                                           | The disk is in the process of stopping.                                                                                                                                    |
|  **Stopped** 10                                                                              | The disk was stopped or shut down in a clean and orderly fashion.                                                                                                          |
|  **In Service** 11                                                                  | The disk is being configured, maintained, cleaned, or otherwise administered.                                                                                              |
|  **No Contact** 12                                                                  | The storage provider has knowledge of the disk, but has never been able to establish communication with it.                                                                |
|  **Lost Communication** 13                                  | The storage provider has knowledge of the disk and has contacted it successfully in the past, but the disk is currently unreachable.                                       |
|  **Aborted** 14                                                                              | Similar to **Stopped**, except that the disk stopped abruptly and may require configuration or maintenance.                                                                |
|  **Dormant** 15                                                                              | The disk is reachable, but it is inactive.                                                                                                                                 |
|  **Supporting Entity in Error** 16  | This status value does not necessarily indicate trouble with the disk, but it does indicate that another device or connection that the disk depends on may need attention. |
|  **Completed** 17                                                                      | The disk has completed an operation. This status value should be combined with OK, Error, or Degraded, depending on the outcome of the operation.                          |
|  **Online** 0xD010                                                                              | In Windows-based storage subsystems, this indicates that the object is online.                                                                                             |
|  **Not Ready** 0xD011                                                                  | In Windows-based storage subsystems, this indicates that the object is not ready.                                                                                          |
|  **No Media** 0xD012                                                                      | In Windows-based storage subsystems, this indicates that the object has no media present.                                                                                  |
|  **Offline** 0xD013                                                                          | In Windows-based storage subsystems, this indicates that the object is offline.                                                                                            |
|  **Failed** 0xD014                                                                              | In Windows-based storage subsystems, this indicates that the object is in a failed state.                                                                                  |



 

 

**PartitionStyle**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The partition style used by the disk.



| Value                                                                                                                                                                                                                       | Meaning                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
|  **Unknown** 0  | The partition style is unknown. |
|  **MBR** 1                                        | Master Boot Record (MBR)        |
|  **GPT**  2                                     | GUID Partition Table (GPT)      |



 

 

**Path**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A path that can be used to open an operating system handle to the disk device.

 

**PhysicalSectorSize**
   

Data type: **UInt32**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) (Bytes)
 

The physical sector size of the disk, in bytes. For example, both 4K native disks and 512 emulated disks will report 4096.

 

**ProvisioningType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The provisioning type of the disk device.



| Value                                                                                                                                                                                                                       | Meaning                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
|  **Unknown** 0  | The provisioning scheme is unspecified.            |
|  **Thin** 1              | The storage for the disk is allocated on-demand.   |
|  **Fixed** 2          | The storage is allocated when the disk is created. |



 

 

**SerialNumber**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the disk's serial number.

 

**Signature**
   

Data type: **UInt32**
 

Access type: Read-only
 

If the **PartitionStyle** is MBR, this property contains the MBR partition signature. This property will be NULL for all other disk types.

 

**Size**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**Units**](/windows/win32/wmisdk/standard-qualifiers) (Bytes)
 

Total size of the disk, in bytes.

 

**UniqueId**
   

Data type: **String**
 

Access type: Read-only
 

The disk identifier. This contains the VPD Page 0x83 information that uniquely identifies this disk. The following types are accepted (in order of precedence):

-   8 (SCSI Name String)
-   3 (FCPH Name)
-   2 (EUI64)
-   1 (Vendor Id)
-   0 (Vendor Specific)

If the disk is an exposed virtual disk, the **UniqueId** is used to map the association between the two objects.

 

**UniqueIdFormat**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Values**](/windows/win32/wmisdk/standard-qualifiers) ( "Vendor Specific", "Vendor Id", "EUI64", "FCPH Name", "SCSI Name String" ), [**ValueMap**](/windows/win32/wmisdk/standard-qualifiers) ("0", "1", "2", "3", "8")
 

The format of the disk identifier. This property contains the VPD Page 0x83 descriptor type that was used to set the **UniqueId** property.

 

## Remarks

The following table lists the parts of the location path string used in the **Location** property.

| Location path part | Description |
|:------------------ |:----------- |
| **AdapterPnpLocationPath** | The adapter's PnP location path. This is retrieved by calling the [SetupDiGetDeviceProperty](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) function, passing &amp;DEVPKEY_Device_LocationPaths for the **PropertyKey** parameter. |
| **BusType** | The bus type: ATA, RAID, SAS, or SCSI. Note: If the bus type is IDE, PATA, or SATA, it appears as ATA in the location path string. If it is PCI RAID, it appears as RAID. |
| **PathId** | The number of the bus. This is the value of the **PathId** member of the [SCSI_ADDRESS](/windows-hardware/drivers/ddi/ntddscsi/ns-ntddscsi-_scsi_address) structure that is returned by the [IOCTL_SCSI_GET_ADDRESS](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_get_address) control code. |
| **TargetId** | The number of the target device. This is the value of the **TargetId** member of the [SCSI_ADDRESS](/windows-hardware/drivers/ddi/ntddscsi/ns-ntddscsi-_scsi_address) structure that is returned by the [IOCTL_SCSI_GET_ADDRESS](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_get_address) control code. |
| **LunId** | The number of the LUN. This is the value of the **Lun** member of the [SCSI_ADDRESS](/windows-hardware/drivers/ddi/ntddscsi/ns-ntddscsi-_scsi_address) structure that is returned by the [IOCTL_SCSI_GET_ADDRESS](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_get_address) control code. |



 

The following table contains examples of location paths.



| Bus type | Example location path                                        |
|----------|--------------------------------------------------------------|
| ATA      | PCIROOT(0)\#PCI(0100)\#ATA(C01T03L00)                        |
| RAID     | PCIROOT(0)\#PCI(0200)\#PCI(0003)\#PCI(0100)\#RAID(P02T00L00) |
| SAS      | PCIROOT(1)\#PCI(0300)\#SAS(P00T03L00)                        |
| SCSI     | PCIROOT(0)\#PCI(1C00)\#PCI(0000)\#SCSI(P00T01L01)            |



 

**Starting in Windows 10:** **MSFT\_Disk** derives from [**MSFT\_StorageObject**](msft-storageobject.md). It now inherits the property *ObjectId*, which was formerly a property of **MSFT\_Disk**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

