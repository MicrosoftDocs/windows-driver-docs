---
title: NetAdapterCreate method
description: Creates a net adapter object.
ms.assetid: 9e36d6f9-c0ca-4e18-83f8-5d1cb74ab1e1
keywords: ["NetAdapterCreate method Network Drivers Starting with Windows Vista"]
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

```ManagedCPlusPlus
NTSTATUS NetAdapterCreate(
  _In_     WDFDEVICE              Device,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES AdapterAttributes,
  _In_     PNET_ADAPTER_CONFIG    Configuration,
  _Out_    NETADAPTER             *Adapter
);
```

Parameters
----------

*Device* \[in\]  
The WDFDEVICE object created by a prior call to [**WdfDeviceCreate**](wdf-wdfdevicecreate)

*AdapterAttributes* \[in, optional\]  
A pointer to a caller-allocated [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure. The structure’s ParentObject must be NULL. The parameter is optional and can be WDF\_NO\_OBJECT\_ATTRIBUTES.

*Configuration* \[in\]  
A pointer to a caller-allocated [**NET\_ADAPTER\_CONFIG**](net-adapter-config.md) structure. For info, see [**NET\_ADAPTER\_CONFIG\_INIT**](net-adapter-config-init.md).

*Adapter* \[out\]  
A pointer to a location that receives a handle to the new NET adapter object.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

After it has called [**WdfDeviceCreate**](wdf-wdfdevicecreate), the client typically calls **NetAdapterCreate** from within its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) routine.

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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NET\_ADAPTER\_CONFIG\_INIT**](net-adapter-config-init.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetAdapterCreate%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





