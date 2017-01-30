---
title: NetAdapterGetPowerSettings method
description: Retrieves the NETPOWERSETTINGS that is associated with a net adapter.
ms.assetid: 4ca16de4-15ab-4592-bcac-92934c657228
keywords: ["NetAdapterGetPowerSettings method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetAdapterGetPowerSettings
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetAdapterGetPowerSettings method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the NETPOWERSETTINGS that is associated with a net adapter.

Syntax
------

```ManagedCPlusPlus
NETPOWERSETTINGS NetAdapterGetPowerSettings(
  _In_ NETADAPTER Adapter
);
```

Parameters
----------

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

Return value
------------

Returns the NETPOWERSETTINGS for the specified net adapter object.

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
<td align="left"><p>Library</p></td>
<td align="left">NetAdapterCxStub.lib</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





