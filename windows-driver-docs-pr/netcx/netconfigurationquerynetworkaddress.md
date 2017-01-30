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
A pointer to a caller-allocated buffer that receives the requested network address as a byte array.

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

Typically, a **NetworkAddress** entry in the registry is stored as a string of hexadecimal digits. Optionally, an installer can store such an address as a string of paired digits, with each pair separated from the next by a hyphen. 

The **NetConfigurationQueryNetworkAddress** method searches the registry **Parameters** key for the keyword **NetworkAddress** and then converts the value of this string-type entry to a sequence of byte integers. **NetConfigurationQueryNetworkAddress** discards hyphens and converts each such pair into a single byte.

The buffer remains valid for the lifetime of the NETCONFIGURATION object.

Note that NDIS does not validate the network address. NDIS does not guarantee that this value is a valid address, that the value has the proper length, or even that the value is a network address. If the caller determines that the value is out of bounds, it should not use the value; instead, it should use the permanent medium access control (MAC) address or a default address.

To support software configurable network addressing, use MSFT_NetAdapter WMI classes instead.

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

 

 





