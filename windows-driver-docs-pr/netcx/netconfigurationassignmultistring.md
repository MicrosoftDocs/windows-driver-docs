---
title: NetConfigurationAssignMultiString method
description: .
ms.assetid: b5081e10-7e91-4315-b0ff-fd926e79153e
keywords: ["NetConfigurationAssignMultiString method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetConfigurationAssignMultiString
api_location:
- netconfiguration.h
api_type:
- HeaderDef
---

# NetConfigurationAssignMultiString method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetConfigurationAssignMultiString** method assigns a set of strings to a specified value name in the registry. The strings are contained in a specified collection of framework string objects.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetConfigurationAssignMultiString(
  _In_ NETCONFIGURATION Configuration,
  _In_ PCUNICODE_STRING ValueName,
  _In_ WDFCOLLECTION    Collection
);
```

Parameters
----------

*Configuration* \[in\]  
Handle to a NETCONFIGURATION object that represents an opened registry key.

*ValueName* \[in\]  
A pointer to a **UNICODE_STRING** structure that contains a value name. 

*Collection* \[in\]  
A handle to a framework collection object that represents a collection of framework string objects. 

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-----
The client driver obtains a handle to a NETCONFIGURATION object by calling  [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or [**NetConfigurationOpenSubConfiguration**](netconfigurationopensubconfiguration.md).

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

 

 





