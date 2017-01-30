---
title: NetConfigurationQueryBinary method
description: .
ms.assetid: 1940ed43-3f37-47b6-88df-13f0354408ae
keywords: ["NetConfigurationQueryBinary method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetConfigurationQueryBinary
api_location:
- netconfiguration.h
api_type:
- HeaderDef
---

# NetConfigurationQueryBinary method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetConfigurationQueryBinary(
  _In_  NETCONFIGURATION       Configuration,
  _In_  PCUNICODE_STRING       ValueName,
  _In_  POOL_TYPE              PoolType,
  _In_  PWDF_OBJECT_ATTRIBUTES MemoryAttributes,
  _Out_ WDFMEMORY*             Memory
);
```

Parameters
----------

*Configuration* \[in\]  

*ValueName* \[in\]  

*PoolType* \[in\]  

*MemoryAttributes* \[in\]  

*Memory* \[out\]  

Return value
------------

(NTSTATUS) The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

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
<td align="left">Netconfiguration.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





