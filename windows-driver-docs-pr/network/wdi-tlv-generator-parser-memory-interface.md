---
title: WDI TLV generator/parser memory interface
description: The parser and generator internally use C++ with new/delete.
ms.assetid: 318519FF-AF1F-4D86-96A9-ED0918D91310
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI TLV generator/parser memory interface


The parser and generator internally use C++ with new/delete. This simplifies several implementation details. This means that consumers of the library must provide overloaded operator implementations of these APIs when linking to the library. This is the only C++ dependency that your code must take.

All APIs that do any allocations take a parameter *Context* typed as PCTLV\_CONTEXT which has 2 fields: a ULONG\_PTR named **AllocationContext** and a ULONG named **PeerVersion**. The **AllocationContext** field is passed through to the overloaded `new` operator. This allows consumers of the APIs to customize the allocation in various ways. For more information about the TLV\_CONTEXT parameter, see [WDI TLV versioning](wdi-tlv-versioning.md).

**Warning**  Although you may be tempted to skip calling the library’s cleanup routines (such as FreeParsed, CleanupParsed, and FreeGenerated), do not skip calling them! It might work on some code paths, but will lead to hard-to-diagnose memory leaks.

 

Here is a sample overloaded operator.

```C++
/*++
Module Name:
    sample.cpp
Abstract:
    Contains sample code to override C++ new/delete for use with TLV parser/generator library
Environment:
    Kernel mode
--*/
#include "precomp.h"

#define TLV_POOL_TAG (ULONG) &#39;_VLT&#39;

void* __cdecl operator new(size_t Size, ULONG_PTR AllocationContext)
/*++
  Override C++ allocation operator.
--*/
{
    PVOID pData = ExAllocatePoolWithTag(NonPagedPoolNx, Size, TLV_POOL_TAG);
    UNREFERENCED_PARAMETER(AllocationContext);
    if (pData != NULL)
    {
        RtlZeroMemory( pData, Size);
    }
    return pData;
} 

void __cdecl operator delete(void* pData)
/*++
  Override C++ delete operator.
--*/
{
    if (pData != NULL)
    {
        ExFreePoolWithTag(pData, TLV_POOL_TAG);
    }
}
```

 

 





