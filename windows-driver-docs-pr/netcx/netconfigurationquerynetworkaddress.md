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

*BufferLength* \[in\]  

*NetworkAddressBuffer* \[out\]  

*ResultLength* \[out\]  

Return value
------------

(NTSTATUS) The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

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

 

 





