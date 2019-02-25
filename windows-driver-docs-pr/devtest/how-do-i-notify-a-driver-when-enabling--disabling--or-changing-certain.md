---
title: How do I notify a driver when enabling, disabling, or changing certain flags
description: How do I notify a driver when enabling, disabling, or changing certain flags
ms.assetid: 1bdf8047-8d3f-4cdf-883b-3544dea06705
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I notify a driver when enabling, disabling, or changing certain flags?


Some drivers need to do some additional work when trace flags are enabled, disabled, or changed. To notify a driver when such changes occur, use the following command:

```
#define WPP_PRIVATE_ENABLE_CALLBACK 
```

This symbolic constant must be defined before including the TMH file. The function signature that you will need to write is as follows:

```
typedef
VOID
(*PFN_WPP_PRIVATE_ENABLE_CALLBACK)(
__in LPCGUID Guid,
__in __int64 Logger,
__in BOOLEAN Enable,
__in ULONG Flags,
__in UCHAR Level);
```

The following is an example of how to notify a driver when certain flags are enabled:

```
#define WPP_PRIVATE_ENABLE_CALLBACK MyOwnCallback
#include "tracedrv.tmh" // this is the file that will be auto-generated 
VOID MyOwnCallback (
                 __in LPCGUID Guid,
                 __in __int64 Logger,
                 __in BOOLEAN Enable,
                 __in ULONG Flags,
                 __in UCHAR Level) 
{
//                
//                  This callback function will be called with the current values of : GUID, Logger, Enable, Flags, and Level
//                 

                  if (Enable) {
                        .
                        .
                   }
} 
```









