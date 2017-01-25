---
title: NetPowerSettingsGetProtocolOffload method
description: Retrieves a structure that specifies parameters for a low power protocol offload to a network adapter.
ms.assetid: 4bcabb7b-a8eb-4675-81d4-eb3e10bfc06e
keywords: ["NetPowerSettingsGetProtocolOffload method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetPowerSettingsGetProtocolOffload
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetPowerSettingsGetProtocolOffload method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves a structure that specifies parameters for a low power protocol offload to a network adapter.

Syntax
------

```ManagedCPlusPlus
PNDIS_PM_PROTOCOL_OFFLOAD NetPowerSettingsGetProtocolOffload(
  _In_ NETPOWERSETTINGS NetPowerSettings,
  _In_ ULONG            Index
);
```

Parameters
----------

*NetPowerSettings* \[in\]  
A handle to the NETPOWERSETTINGS object associated with the net adapter. To retrieve the handle, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md).

*Index* \[in\]  
A zero-based value that is used as an index into the protocol offload structures associated with the NETPOWERSETTINGS object. This value must be less than the value returned by [**NetPowerSettingsGetProtocolOffloadCount**](netpowersettingsgetprotocoloffloadcount.md).

Return value
------------

Returns a pointer to the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure at the specified index, or **NULL** if the index value is invalid.

Remarks
-------

The client driver calls **NetPowerSettingsGetProtocolOffload** during a power transition, typically from its [*EVT\_WDF\_DEVICE\_ARM\_WAKE\_FROM\_SX*](https://msdn.microsoft.com/library/windows/hardware/ff540844) or [*EVT\_WDF\_DEVICE\_ARM\_WAKE\_FROM\_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) callback function, or from the [*EVT\_NET\_ADAPTER\_PREVIEW\_PROTOCOL\_OFFLOAD*](evt-net-adapter-preview-protocol-offload.md) callback function.

The client driver can use the pointer to examine the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure, but should not retain it. NetAdapterCx automatically releases the protocol offload structure during offload removal.

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
<td align="left">Netpowersettings.h (include Netadaptercx.h)</td>
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

## See also


[**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetPowerSettingsGetProtocolOffload%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





