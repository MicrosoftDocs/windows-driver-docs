---
title: MSFT\_ResiliencySetting class
description: Represents a storage pool's resiliency settings.
ms.assetid: 8F8981DB-50D7-424D-BD5B-C646FD8E434F
keywords:
- MSFT_ResiliencySetting class Windows Storage Management API
- MSFT_ResiliencySetting class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ResiliencySetting
- MSFT_ResiliencySetting.Name
- MSFT_ResiliencySetting.Description
- MSFT_ResiliencySetting.NumberOfDataCopiesMin
- MSFT_ResiliencySetting.NumberOfDataCopiesMax
- MSFT_ResiliencySetting.NumberOfDataCopiesDefault
- MSFT_ResiliencySetting.PhysicalDiskRedundancyMin
- MSFT_ResiliencySetting.PhysicalDiskRedundancyMax
- MSFT_ResiliencySetting.PhysicalDiskRedundancyDefault
- MSFT_ResiliencySetting.NumberOfColumnsMin
- MSFT_ResiliencySetting.NumberOfColumnsMax
- MSFT_ResiliencySetting.NumberOfColumnsDefault
- MSFT_ResiliencySetting.InterleaveMin
- MSFT_ResiliencySetting.InterleaveMax
- MSFT_ResiliencySetting.InterleaveDefault
- MSFT_ResiliencySetting.ParityLayout
- MSFT_ResiliencySetting.RequestNoSinglePointOfFailure
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_ResiliencySetting class

Represents a storage pool's resiliency settings.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_ResiliencySetting : MSFT_StorageObject
{
  String  Name;
  String  Description;
  UInt16  NumberOfDataCopiesMin;
  UInt16  NumberOfDataCopiesMax;
  UInt16  NumberOfDataCopiesDefault;
  UInt16  PhysicalDiskRedundancyMin;
  UInt16  PhysicalDiskRedundancyMax;
  UInt16  PhysicalDiskRedundancyDefault;
  UInt16  NumberOfColumnsMin;
  UInt16  NumberOfColumnsMax;
  UInt16  NumberOfColumnsDefault;
  UInt64  InterleaveMin;
  UInt64  InterleaveMax;
  UInt64  InterleaveDefault;
  UInt16  ParityLayout;
  Boolean RequestNoSinglePointOfFailure;
};
```

## Members

The **MSFT\_ResiliencySetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_ResiliencySetting** class has these methods.



| Method                                                    | Description                                                                                               |
|:----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**SetDefaults**](msft-resiliencysetting-setdefaults.md) | Allows a user to modify the default property values of the **MSFT\_ResiliencySetting** object. |



 

### Properties

The **MSFT\_ResiliencySetting** class has these properties.

 

**Description**
   

Data type: **String**
 

Access type: Read-only
 

A system-set description of the capabilities of the resiliency setting, including (but not limited to) when a setting should be used, its strengths and drawbacks, performance information, and any other information that the vendor feels is helpful to the user.

 

**InterleaveDefault**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: **Units** (Bytes)
 

The desired number of bytes that can form a strip in common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk. Thus, **Interleave** \* **NumberOfColumns** will yield the size of one stripe of user data.

 

**InterleaveMax**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: **Units** (Bytes)
 

The maximum number of bytes that can form a strip in common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk.

 

**InterleaveMin**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: **Units** (Bytes)
 

The minimum number of bytes that can form a strip in common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk.

 

**Name**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A system-set, user-friendly, display-oriented string that describes the resiliency setting.

 

**NumberOfColumnsDefault**
   

Data type: **UInt16**
 

Access type: Read-only
 

A user-settable preference for the maximum number of underlying physical disks across which data should be striped.

 

**NumberOfColumnsMax**
   

Data type: **UInt16**
 

Access type: Read-only
 

The maximum number of underlying physical disks across which data can be striped in the common striping-based resiliency settings.

 

**NumberOfColumnsMin**
   

Data type: **UInt16**
 

Access type: Read-only
 

The minimum number of underlying physical disks across which data can be striped in the common striping-based resiliency settings.

 

**NumberOfDataCopiesDefault**
   

Data type: **UInt16**
 

Access type: Read-only
 

A user-settable preference for the number of complete data copies to maintain. The value of this parameter must be within the range defined by *NumberofDataCopiesMin* and *NumberOfDataCopiesMax* (inclusive). For new concrete pools, the default should be inherited from the corresponding primordial pool's capability. In the case of the primordial pool, the initial value for this field is left to the Storage Management Provider software.

 

**NumberOfDataCopiesMax**
   

Data type: **UInt16**
 

Access type: Read-only
 

The maximum number of complete copies of data that can be maintained by the storage pool.

 

**NumberOfDataCopiesMin**
   

Data type: **UInt16**
 

Access type: Read-only
 

The minimum number of complete copies of data that can be maintained by the storage pool.

 

**ParityLayout**
   

Data type: **UInt16**
 

Access type: Read-only
 

Specifies whether a parity-based resiliency setting is using a rotated or non-rotated parity layout. If the resiliency setting is not parity based, this property must be set to NULL.



| Value                                                                                                                                                                                                                                                                   | Meaning                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
|  **Non-rotated Parity** 1  | The parity-based resiliency setting uses a non-rotated parity layout. |
|  **Rotated Parity** 2                  | The parity-based resiliency setting uses a rotated parity layout.     |



 

 

**PhysicalDiskRedundancyDefault**
   

Data type: **UInt16**
 

Access type: Read-only
 

A user-settable preference for how many physical disk failures a virtual disk should be able to withstand before data loss occurs.

 

**PhysicalDiskRedundancyMax**
   

Data type: **UInt16**
 

Access type: Read-only
 

The maximum number of tolerable physical disk failures that can occur before data loss would occur.

 

**PhysicalDiskRedundancyMin**
   

Data type: **UInt16**
 

Access type: Read-only
 

The minimum number of tolerable physical disk failures that can occur before data loss would occur.

 

**RequestNoSinglePointOfFailure**
   

Data type: **Boolean**
 

Access type: Read-only
 

Set to **TRUE** to request no single point of failure.

 

## Remarks

**MSFT\_ResiliencySetting** is a detailed description of the resiliency capabilities offered by a storage pool. A storage pool can have one or more of these settings. The **MSFT\_ResiliencySetting** object specifies a series of properties, each with a minimum, maximum, and default value. The minimum and maximum values may not reflect the current capabilities of the storage pool, but rather the ideal range of capabilities offered by the subsystem. The default values will be used when creating new virtual disks unless overridden.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

