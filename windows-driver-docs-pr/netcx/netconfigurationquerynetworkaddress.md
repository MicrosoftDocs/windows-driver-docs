---
title: NetConfigurationQueryNetworkAddress method
description: .
ms.assetid: 551f2c98-7daa-4dfc-a57d-81bf44e366f9
keywords: ["NetConfigurationQueryNetworkAddress method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetConfigurationQueryNetworkAddress
api_location:
- netconfiguration.h
api_type:
- HeaderDef
---

# NetConfigurationQueryNetworkAddress method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the software-configurable network address that was stored in the registry for a NIC.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetConfigurationQueryNetworkAddress(
  _In_  NETCONFIGURATION Configuration,
  _In_  ULONG            BufferLength,
  _Out_ PVOID            NetworkAddressBuffer,
  _Out_ PULONG           ResultLength
);
```

Parameters
----------

*Configuration* \[in\]  
Handle to a NETCONFIGURATION object that represents an opened registry key.

*BufferLength* \[in\]  
The length, in bytes, of the buffer that *NetworkAddressBuffer* points to.

*NetworkAddressBuffer* \[out\]  
A pointer to a caller-allocated buffer that receives the requested network address as a byte array. The pointer can be NULL if the *BufferLength* parameter is zero.

*ResultLength* \[out\]  
A caller-supplied location that, on return, contains the size, in bytes, of the information that the method stored in *NetworkAddressBuffer*. If the function's return value is STATUS_BUFFER_TOO_SMALL, this location receives the required buffer size.

Return value
------------
Returns one of the following status values:

|Return Code|Description|
|---|---|
|STATUS\_SUCCESS|The operation succeeded.|
|STATUS_BUFFER_TOO_SMALL|The supplied buffer is too small to receive the information.|

Remarks
-----
The client driver obtains a handle to a NETCONFIGURATION object by calling  [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or [**NetConfigurationOpenSubConfiguration**](netadapteropensubconfiguration.md).

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
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





