---
title: NetRequestQueueGetAdapter method
topic_type:
- apiref
api_name:
- NetRequestQueueGetAdapter
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NetRequestQueueGetAdapter method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the NETADAPTER object corresponding to the NETREQUESTQUEUE.

Syntax
------

```cpp
NETADAPTER NetRequestQueueGetAdapter(
  _In_ NETREQUESTQUEUE NetRequestQueue
);
```

Parameters
----------

*NetRequestQueue* [in]  
A handle to a net request queue object.

Return value
------------

Returns the NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

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
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Netrequestqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





