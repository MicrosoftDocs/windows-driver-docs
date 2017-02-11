---
title: NetConfigurationQueryBinary method
topic_type:
- apiref
api_name:
- NetConfigurationQueryBinary
api_location:
- netconfiguration.h
api_type:
- HeaderDef
---

# NetConfigurationQueryBinary method

Retrieves the data that is currently assigned to a specified registry value, stores the data in a framework-allocated buffer, and creates a framework memory object to represent the buffer.

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetConfigurationQueryBinary(
  _In_      NETCONFIGURATION       Configuration,
  _In_      PCUNICODE_STRING       ValueName,
  _In_      POOL_TYPE              PoolType,
  _In_opt_  PWDF_OBJECT_ATTRIBUTES MemoryAttributes,
  _Out_     WDFMEMORY*             Memory
);
```

Parameters
----------

*Configuration* \[in\]  
Handle to a NETCONFIGURATION object that represents an opened registry key.

*ValueName* \[in\]  
A pointer to a **UNICODE_STRING** structure that contains a value name. 

*PoolType* \[in\]  
A **POOL_TYPE**-typed value that specifies the type of memory to be allocated for the data buffer. 

*MemoryAttributes* \[in, optional\]  
A pointer to a [WDF_OBJECT_ATTRIBUTES](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure that contains object attributes for the new memory object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES. 

*Memory* \[out\]  
A pointer to a location that receives a handle to the new memory object. 

Return value
------------

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-----
The client driver obtains a handle to a NETCONFIGURATION object by calling  [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or [**NetConfigurationOpenSubConfiguration**](netconfigurationopensubconfiguration.md).

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

 

 





