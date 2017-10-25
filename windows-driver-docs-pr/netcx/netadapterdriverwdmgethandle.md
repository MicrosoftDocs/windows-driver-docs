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

A WDF client driver calls **NetAdapterDriverWdmGetHandle** to get a handle that can be used to call NDIS APIs.

Syntax
------

```cpp
NDIS_HANDLE NetAdapterDriverWdmGetHandle(
  _In_ WDFDRIVER               Driver
);
```

Parameters
----------

*Driver* [in]  
A handle to the driver's framework driver object, obtained from a previous call to [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175).

Return value
------------

**NetAdapterDriverWdmGetHandle** returns a WDM handle to the client driver. The framework's verifier reports an error if no corresponding WDM handle exists.

Remarks
-------

The driver must have previously called [**NetAdapterCreate**](netadaptercreate.md).

In NetAdapterCx version 1.1, the *Type* parameter from version 1.0 was removed.

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
<td align="left"><p>1.23</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.1</p></td>
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
<td align="left"><p>&lt;=DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





