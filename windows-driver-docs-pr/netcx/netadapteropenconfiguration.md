---
title: NetAdapterOpenConfiguration method
topic_type:
- apiref
api_name:
- NetAdapterOpenConfiguration
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetAdapterOpenConfiguration method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Opens the adapter’s configuration database.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetAdapterOpenConfiguration(
  _In_     NETADAPTER             Adapter,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES ConfigurationAttributes,
  _Out_    NETCONFIGURATION       *Configuration
);
```

Parameters
----------

*Adapter* [in]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*ConfigurationAttributes* [in, optional]  
A pointer to a [**WDF_OBJECT_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure that contains driver-supplied attributes for the new configuration object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.

*Configuration* [out]  
A pointer to a location that receives a handle to the new adapter configuration object.

Return value
------------

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

The client is responsible for closing an opened configuration by calling [**NetConfigurationClose**](netconfigurationclose.md).

If the client provides a [**WDF_OBJECT_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400), it specifies **NULL** for **ParentObject**. The adapter configuration object is automatically parented to the adapter object.

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
<td align="left">Netadapter.h (include Netadaptercx.h)</td>
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


[**NetConfigurationClose**](netconfigurationclose.md)

 

 






