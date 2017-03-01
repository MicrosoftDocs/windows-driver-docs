---
title: NetConfigurationOpenSubConfiguration method
topic_type:
- apiref
api_name:
- NetConfigurationOpenSubConfiguration
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetConfigurationOpenSubConfiguration method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Opens a sub configuration of a specified adapter configuration object.

Syntax
------

```cpp
NTSTATUS NetConfigurationOpenSubConfiguration(
  _In_     NETCONFIGURATION       Configuration,
  _In_     PCUNICODE_STRING       SubConfigurationName,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES SubConfigurationAttributes,
  _Out_    NETCONFIGURATION       *SubConfiguration
);
```

Parameters
----------

*Configuration* [in]  
A handle to an adapter configuration object opened in a prior call to [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or **NetConfigurationOpenSubConfiguration**.

*SubConfigurationName* [in]  
A pointer to a string specifying the name of the sub configuration to open.

*SubConfigurationAttributes* [in, optional]  
A pointer to a [**WDF_OBJECT_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure that contains driver-supplied attributes for the new configuration object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.

*SubConfiguration* [out]  
A pointer to a location that receives a handle to the new sub configuration object.

Return value
------------

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

If the client provides a [**WDF_OBJECT_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400), it specifies **NULL** for **ParentObject**. By default, the sub configuration is parented to the existing adapter configuration object.

The client driver closes the sub configuration by calling [**NetConfigurationClose**](netconfigurationclose.md) with either the sub configuration object or the parent adapter configuration object.

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

## See also


[**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md)

[**NetConfigurationClose**](netconfigurationclose.md)

 

 






