---
title: Read ahead parameters
description: read-ahead parameters for  read-ahead granularity and pipelined read-ahead.
ms.assetid:
keywords: ["read-ahead parameters"]
topic_type:
- apiref
api_name:
- read_ahead_parame3ters
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.author:
ms.date: 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# READ_AHEAD_PARAMETERS structure

The **READ_AHEAD_PARAMETERS** structure contains publicly exposed read ahead parameters.

Syntax
------

```ManagedCPlusPlus
typedef struct _READ_AHEAD_PARAMETERS {

    CSHORT NodeByteSize;
    ULONG Granularity;
    ULONG PipelinedRequestSize;
    ULONG ReadAheadGrowthPercentage;

} READ_AHEAD_PARAMETERS, *PREAD_AHEAD_PARAMETERS;
```

Members
----------

*NodeByteSize* \[in\]  
Size of the node in bytes.

*Granularity* \[in\]  
Granularity of read aheads. This value must be an even power of 2 and greater than, or equal to PAGE_SIZE

*PipelinedRequestSize* \[in\]  
The request size in bytes, to be used when performing pipelined read-aheads. Each read ahead request that is pipelined is broken into smaller **PipelinedRequestSize** sized requests. This is typically used to increase the throughput by parallelizing multiple requets instead of one single big one.

> [!NOTE]
> Due to backward compatibility, If this value is zero, every read-ahead request will be broken into two.

*ReadAheadGrowthPercentage* \[in\]  
The growth of read ahead as a percentage of the data that has already been ready by the application so far. 
