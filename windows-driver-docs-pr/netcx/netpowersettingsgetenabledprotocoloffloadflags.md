---
title: NetPowerSettingsGetEnabledProtocolOffloadFlags method
topic_type:
- apiref
api_name:
- NetPowerSettingsGetEnabledProtocolOffloadFlags
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetPowerSettingsGetEnabledProtocolOffloadFlags method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves flags that specify currently enabled low power protocol offloads that a network adapter supports.

Syntax
------

```cpp
ULONG NetPowerSettingsGetEnabledProtocolOffloadFlags(
  _In_ NETPOWERSETTINGS NetPowerSettings
);
```

Parameters
----------

*NetPowerSettings* [in]  
A handle to the NETPOWERSETTINGS object associated with the NETADAPTER. To retrieve the handle, call [**NetAdapterGetPowerSettings**](netadaptergetpowersettings.md).

Return value
------------

A ULONG value that contains a bitwise **OR** of [**NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS**](net-adapter-protocol-offloads-flags.md)-typed flags that correspond to capabilities that the client driver reported in the **SupportedProtocolOffloads** member of the [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure. NDIS uses these flags to enable the low power protocol offload capabilities on a network adapter. For more information, see [**NDIS_PM_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759).

Remarks
-------

The client driver must only call **NetPowerSettingsGetEnabledProtocolOffloadFlags** during a power transition, typically from its [*EVT_WDF_DEVICE_ARM_WAKE_FROM_SX*](https://msdn.microsoft.com/library/windows/hardware/ff540844) or [*EVT_WDF_DEVICE_ARM_WAKE_FROM_S0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) callback function.  Otherwise, the call results in a system bugcheck.

In NetAdapterCx 1.0, this method was called **NetPowerSettingsGetEnabledProtocolOffloads**. It was renamed to **NetPowerSettingsGetEnabledProtocolOffloadFlags** in NetAdapterCx 1.1, which is included in Windows 10, version 1709 and later.

In NetAdapterCx 1.1, this method's required IRQL level was changed from DISPATCH_LEVEL to PASSIVE_LEVEL.

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
<td align="left"><p>1.1</p></td>
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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 






