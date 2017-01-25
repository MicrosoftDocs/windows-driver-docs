---
title: NetConfigurationOpenSubConfiguration method
description: Opens a sub configuration of a specified adapter configuration object.
ms.assetid: ba79dd68-c5f2-4a23-a595-e17d0665dd91
keywords: ["NetConfigurationOpenSubConfiguration method Network Drivers Starting with Windows Vista"]
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

```ManagedCPlusPlus
NTSTATUS NetConfigurationOpenSubConfiguration(
  _In_     NETCONFIGURATION       Configuration,
  _In_     PCUNICODE_STRING       SubConfigurationName,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES SubConfigurationAttributes,
  _Out_    NETCONFIGURATION       *SubConfiguration
);
```

Parameters
----------

*Configuration* \[in\]  
A handle to an adapter configuration object opened in a prior call to [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or **NetConfigurationOpenSubConfiguration**.

*SubConfigurationName* \[in\]  
A pointer to a string specifying the name of the sub configuration to open.

*SubConfigurationAttributes* \[in, optional\]  
A pointer to a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure that contains driver-supplied attributes for the new configuration object. This parameter is optional and can be WDF\_NO\_OBJECT\_ATTRIBUTES.

*SubConfiguration* \[out\]  
A pointer to a location that receives a handle to the new sub configuration object.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

If the client provides a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400), it specifies **NULL** for **ParentObject**. By default, the sub configuration is parented to the existing adapter configuration object.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetConfigurationOpenSubConfiguration%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





