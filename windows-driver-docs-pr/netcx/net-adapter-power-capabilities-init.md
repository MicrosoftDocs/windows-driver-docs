---
title: NET_ADAPTER_POWER_CAPABILITIES_INIT method
topic_type:
- apiref
api_name:
- NET_ADAPTER_POWER_CAPABILITIES_INIT
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_POWER\_CAPABILITIES\_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [**NET\_ADAPTER\_POWER\_CAPABILITIES**](net-adapter-power-capabilities.md) structure.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE VOID NET_ADAPTER_POWER_CAPABILITIES_INIT(
  _Out_ PNET_ADAPTER_POWER_CAPABILITIES PowerCapabilities
);
```

Parameters
----------

*PowerCapabilities* \[out\]  
A pointer to the driver-allocated [**NET\_ADAPTER\_POWER\_CAPABILITIES**](net-adapter-power-capabilities.md) structure.

Return value
------------

This method does not return a value.

Remarks
-----
The **NET_ADAPTER_POWER_CAPABILITIES_INIT** function zeros the specified **NET_ADAPTER_POWER_CAPABILITIES** structure and sets the structure's **Size** member. It also sets the structure's **ManageS0IdlePowerReferences** member to **WdfUseDefault**.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md)

 

 






