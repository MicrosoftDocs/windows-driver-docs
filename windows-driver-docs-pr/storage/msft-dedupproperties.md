---
title: MSFT\_DedupProperties class
description: Volume deduplication properties.
ms.assetid: BE95BD75-F45E-494B-9091-558815543801
keywords:
- MSFT_DedupProperties class Windows Storage Management API
- MSFT_DedupProperties class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_DedupProperties
- MSFT_DedupProperties.UnoptimizedSize
- MSFT_DedupProperties.SavingsSize
- MSFT_DedupProperties.SavingsRate
- MSFT_DedupProperties.OptimizedFilesCount
- MSFT_DedupProperties.OptimizedFilesSize
- MSFT_DedupProperties.OptimizedFilesSavingsRate
- MSFT_DedupProperties.InPolicyFilesCount
- MSFT_DedupProperties.InPolicyFilesSize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DedupProperties class

Volume deduplication properties.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_DedupProperties
{
  UInt64 UnoptimizedSize;
  UInt64 SavingsSize;
  UInt32 SavingsRate;
  UInt64 OptimizedFilesCount;
  UInt64 OptimizedFilesSize;
  UInt32 OptimizedFilesSavingsRate;
  UInt64 InPolicyFilesCount;
  UInt64 InPolicyFilesSize;
};
```

## Members

The **MSFT\_DedupProperties** class has these types of members:

-   [Properties](#msft-dedupproperties-class)

### Properties

The **MSFT\_DedupProperties** class has these properties.

 

**InPolicyFilesCount**
   

Data type: **UInt64**
 

Access type: Read-only
 

The number of files that currently qualify for optimization.

 

**InPolicyFilesSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

The aggregate size of all files that currently qualify for optimization.

 

**OptimizedFilesCount**
   

Data type: **UInt64**
 

Access type: Read-only
 

The number of optimized files on the volume.

 

**OptimizedFilesSavingsRate**
   

Data type: **UInt32**
 

Access type: Read-only
 

The ratio of deduplication savings to the logical size of all optimized files on the volume, expressed as a percentage.

 

**OptimizedFilesSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

The total logical size of all optimized files on the volume, in bytes.

 

**SavingsRate**
   

Data type: **UInt32**
 

Access type: Read-only
 

The ratio of deduplication savings to the logical size of all of the files on the volume, expressed as a percentage.

 

**SavingsSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

The difference between the logical size of the optimized files and the logical size of the store (the deduplicated user data plus deduplication metadata).

 

**UnoptimizedSize**
   

Data type: **UInt64**
 

Access type: Read-only
 

The total logical size of all files on the volume, in bytes. This is an estimate of the volume's used space if the deduplication feature were disabled.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





