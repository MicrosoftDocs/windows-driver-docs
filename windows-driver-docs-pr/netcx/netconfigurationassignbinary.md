---
title: NetConfigurationAssignBinary method
description: .
ms.assetid: 2657409d-c658-49bc-a128-f6e96bc9ae6f
keywords: ["NetConfigurationAssignBinary method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetConfigurationAssignBinary
api_location:
- netconfiguration.h
api_type:
- HeaderDef
---

# NetConfigurationAssignBinary method

The **NetConfigurationAssignBinary** method writes caller-supplied binary data to a specified value name in the registry.

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetConfigurationAssignBinary(
  _In_ NETCONFIGURATION Configuration,
  _In_ PCUNICODE_STRING ValueName,
  _In_ PVOID            Buffer,
  _In_ ULONG            BufferLength
);
```

Parameters
----------

*Configuration* \[in\]  
Handle to the NETCONFIGURATION object that represents an opened registry key.

*ValueName* \[in\]  
A pointer to a **UNICODE_STRING** structure that contains a value name. 

*Buffer* \[in\]  
A pointer to a buffer that contains driver-supplied data.

*BufferLength* \[in\]  
The length, in bytes, of the buffer that *Buffer* points to.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
---
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
<td align="left">Netconfiguration.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





