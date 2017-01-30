---
title: NetAdapterWdmGetNdisHandle method
description: Retrieves the NDIS adapter handle for a specified net adapter.
ms.assetid: 509071be-6a29-478b-b9cc-db10e10a437d
keywords: ["NetAdapterWdmGetNdisHandle method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetAdapterWdmGetNdisHandle
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NetAdapterWdmGetNdisHandle method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the NDIS adapter handle for a specified net adapter.

Syntax
------

```ManagedCPlusPlus
NDIS_HANDLE NetAdapterWdmGetNdisHandle(
  _In_ NETADAPTER Adapter
);
```

Parameters
----------

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

Return value
------------

Retrieves the NDIS\_HANDLE for a specified net adapter.

Remarks
-------

Client drivers that bypass NetAdapterCx and call NDIS DDIs directly call this method to retrieve the NDIS handle required by these DDIs.

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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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
<td align="left">Netadapter.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>Any level</p></td>
</tr>
</tbody>
</table>

 

 





