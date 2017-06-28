---
title: NetAdapterCreate method
topic_type:
- apiref
api_name:
- NetAdapterCreate
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetAdapterCreate method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Creates a net adapter object.

Syntax
------

```cpp
NTSTATUS NetAdapterCreate(
  _In_     WDFDEVICE              Device,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES AdapterAttributes,
  _In_     PNET_ADAPTER_CONFIG    Configuration,
  _Out_    NETADAPTER             *Adapter
);
```

Parameters
----------

*Device* [in]  
The WDFDEVICE object created by a prior call to [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

*AdapterAttributes* [in, optional]  
A pointer to a caller-allocated [**WDF_OBJECT_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure. The structure’s ParentObject must be NULL. The parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.

*Configuration* [in]  
A pointer to a caller-allocated [**NET_ADAPTER_CONFIG**](net-adapter-config.md) structure. For info, see [**NET_ADAPTER_CONFIG_INIT**](net-adapter-config-init.md).

*Adapter* [out]  
A pointer to a location that receives a handle to the new NETADAPTER object.

Return value
------------

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

After it has called [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926), the client typically calls **NetAdapterCreate** from within its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) routine.

The NETADAPTER object is a standard WDF object. The framework manages its deletion, which occurs when the parent WDFDEVICE is deleted.

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
<td align="left">Netadapter.h (include Netadaptercx.h)</td>
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


[**NET_ADAPTER_CONFIG_INIT**](net-adapter-config-init.md)

 

 






