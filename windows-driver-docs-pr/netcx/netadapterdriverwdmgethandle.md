---
title: NetAdapterDriverWdmGetHandle method
topic_type:
- apiref
api_name:
- NetAdapterDriverWdmGetHandle
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetAdapterDriverWdmGetHandle method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

An NDIS-WDF miniport client driver calls **NetAdapterDriverWdmGetHandle** returns a Windows Driver Model (WDM) handle to the client driver.

Syntax
------

```ManagedCPlusPlus
NDIS_HANDLE NetAdapterDriverWdmGetHandle(
  _In_ WDFDRIVER               Driver,
  _In_ NET_ADAPTER_DRIVER_TYPE Type
);
```

Parameters
----------

*Driver* \[in\]  
A handle to the driver's framework driver object, obtained from a previous call to [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175).

*Type* \[in\]  
A [**NET_ADAPTER_DRIVER_TYPE**](net-adapter-driver-type.md) enumeration value that specifies the type of network adapter driver.

Return value
------------

**NetAdapterDriverWdmGetHandle** returns a WDM handle to the client driver. The framework's verifier reports an error if no corresponding WDM handle exists.

Remarks
-------

The driver must have previously called [**NetAdapterCreate**](netadaptercreate.md).

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
<td align="left"><p>&lt;= DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





