---
title: NetConfigurationAssignUlong method
description: .
ms.assetid: 861b862b-b833-45a8-bf18-132f98d73223
keywords: ["NetConfigurationAssignUlong method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetConfigurationAssignUlong
api_location:
- netconfiguration.h
api_type:
- HeaderDef
---

# NetConfigurationAssignUlong method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetConfigurationAssignUlong** method writes a caller-supplied unsigned long word value to a specified value name in the registry.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetConfigurationAssignUlong(
  _In_ NETCONFIGURATION Configuration,
  _In_ PCUNICODE_STRING ValueName,
  _In_ ULONG            Value
);
```

Parameters
----------

*Configuration* \[in\]  
Handle to the NETCONFIGURATION object that represents an opened registry key.

*ValueName* \[in\]  
A pointer to a **UNICODE_STRING** structure that contains a value name. 

*Value* \[in\]  
A ULONG value that will be assigned to the value name that *ValueName* specifies.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
---

The client driver obtains a handle to a NETCONFIGURATION object by calling  [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or [**NetConfigurationOpenSubConfiguration**](netadapteropensubconfiguration.md).

If an entry of the same name as *ValueName* already exists under the opened registry key, **NetConfigurationAssignUlong** replaces its current value with the caller-supplied value. Otherwise, **NetConfigurationAssignUlong** adds a new value entry with the given name and supplied value to the registry.


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

 
## See also


[**NdisWriteConfiguration **](https://msdn.microsoft.com/library/windows/hardware/ff564659)
 





