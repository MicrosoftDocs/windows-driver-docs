---
title: NetConfigurationQueryMultiString method
description: Retrieves the strings that are currently assigned to the adapter configuration object, creates a WDFSTRING object for each string, and adds each string object to a specified collection object.
ms.assetid: 8015791d-ecbd-40e3-868c-f6b3bbbf9433
keywords: ["NetConfigurationQueryMultiString method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetConfigurationQueryMultiString
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetConfigurationQueryMultiString method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the strings that are currently assigned to the adapter configuration object, creates a WDFSTRING object for each string, and adds each string object to a specified collection object.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetConfigurationQueryMultiString(
  _In_     NETCONFIGURATION       Configuration,
  _In_     PCUNICODE_STRING       ValueName,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES StringsAttributes,
  _Inout_  WDFCOLLECTION          Collection
);
```

Parameters
----------

*Configuration* \[in\]  
Handle to a NETCONFIGURATION object that represents an opened registry key.

*ValueName* \[in\]  
A pointer to a **UNICODE\_STRING** structure that contains a value name.

*StringsAttributes* \[in, optional\]  
A pointer to a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure that contains driver-supplied attributes for the new WDFSTRING objects. This parameter is optional and can be WDF\_NO\_OBJECT\_ATTRIBUTES.

*Collection* \[in, out\]  
A handle to a driver-supplied collection object.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------
The client driver obtains a handle to a NETCONFIGURATION object by calling  [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or [**NetConfigurationOpenSubConfiguration**](netadapteropensubconfiguration.md).

By default, the strings are parented to the collection object. The client driver can change this by setting the **ParentObject** member of the [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure.

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

 

 





