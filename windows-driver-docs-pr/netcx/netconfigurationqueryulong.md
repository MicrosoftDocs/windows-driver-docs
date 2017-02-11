---
title: NetConfigurationQueryUlong method
topic_type:
- apiref
api_name:
- NetConfigurationQueryUlong
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetConfigurationQueryUlong method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the specified unsigned long word (REG\_DWORD) data from the adapter configuration object and copies the data to a specified location.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetConfigurationQueryUlong(
  _In_  NETCONFIGURATION                    Configuration,
  _In_  NET_CONFIGURATION_QUERY_ULONG_FLAGS Flags,
  _In_  PCUNICODE_STRING                    ValueName,
  _Out_ PULONG                              Value
);
```

Parameters
----------

*Configuration* \[in\]  
Handle to a NETCONFIGURATION object that represents an opened registry key.

*Flags* \[in\]  
A valid bitwise OR of [**NET\_CONFIGURATION\_QUERY\_ULONG\_FLAGS**](net-configuration-query-ulong-flags.md)-typed flags.

*ValueName* \[in\]  
A pointer to a **UNICODE\_STRING** structure that contains a name for the ULONG value.

*Value* \[out\]  
A pointer to a location that receives the data that is assigned to the value that *ValueName* specifies.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

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
<td align="left"><p>Library</p></td>
<td align="left">NetAdapterCxStub.lib</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





