---
title: NetRxQueueQueryAllocatorCacheEnabled method
topic_type:
- apiref
api_name:
- NetRxQueueQueryAllocatorCacheEnabled
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetRxQueueQueryAllocatorCacheEnabled method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NetRxQueueQueryAllocatorCacheEnabled method queries whether DMA allocator cache is enabled.

Syntax
------

```cpp
NTSTATUS FORCEINLINE NetRxQueueQueryAllocatorCacheEnabled(
  _In_  NETRXQUEUE  RxQueue,
  _Out_ PBOOLEAN    CacheEnabled
);
```

Parameters
----------

*RxQueue* [in]  
The receive queue object that the client driver obtained from a previous call to [**NetRxQueueCreate**](netrxqueuecreate.md).

*CacheEnabled* [out]  
A pointer to a boolean value indicating whether DMA allocator cache is enabled or not.

Return value
------------

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

In NetAdapterCx 1.0, this method was called **NetRxQueueConfigureDmaAllocator**. It was renamed to **NetRxQueueQueryAllocatorCacheEnabled** in NetAdapterCx 1.1. DMA allocator configuration is now done by initializing a [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG](net-rxqueue-dma-allocator-config.md) structure with the [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT](net-rxqueue-dma-allocator-config-init.md) method.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.23</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">NetRxQueue.h (include NetAdapterCx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">NetAdapterCxStub.lib</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NET_RXQUEUE_CONFIG**](net-rxqueue-config.md)

 

 






