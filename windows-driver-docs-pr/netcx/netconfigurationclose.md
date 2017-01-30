---
title: NetConfigurationClose method
description: Releases the handle to the registry key that is associated with an adapter configuration object and then deletes the adapter configuration object.
ms.assetid: 1e6ad52a-37d5-4142-bef2-f9dbb3d2caa3
keywords: ["NetConfigurationClose method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetConfigurationClose
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetConfigurationClose method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Releases the handle to the registry key that is associated with an adapter configuration object and then deletes the adapter configuration object.

Syntax
------

```ManagedCPlusPlus
void NetConfigurationClose(
  _In_ NETCONFIGURATION Configuration
);
```

Parameters
----------

*Configuration* \[in\]  
A handle to an adapter configuration object opened in a prior call to [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or [**NetConfigurationOpenSubConfiguration**](netconfigurationopensubconfiguration.md).

Return value
------------

This method does not return a value.

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
<td align="left">Netconfiguration.h (include Netadaptercx.h)</td>
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


[**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md)

[**NetConfigurationOpenSubConfiguration**](netconfigurationopensubconfiguration.md)

 

 






