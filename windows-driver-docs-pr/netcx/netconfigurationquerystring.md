---
title: NetConfigurationQueryString method
description: Retrieves the specified string value from the adapter configuration object and assigns the string to a specified framework string object.
ms.assetid: fdb68710-d3c4-44c5-a95e-036cfb38f4b6
keywords: ["NetConfigurationQueryString method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetConfigurationQueryString
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetConfigurationQueryString method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the specified string value from the adapter configuration object and assigns the string to a specified framework string object.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetConfigurationQueryString(
  _In_     NETCONFIGURATION       Configuration,
  _In_     PCUNICODE_STRING       ValueName,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES StringAttributes,
  _Out_    WDFSTRING              *WdfString
);
```

Parameters
----------

*Configuration* \[in\]  
A handle to an adapter configuration object opened in a prior call to [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or [**NetConfigurationOpenSubConfiguration**](netconfigurationopensubconfiguration.md).

*ValueName* \[in\]  
A pointer to a **UNICODE\_STRING** structure that contains a name for string value.

*StringAttributes* \[in, optional\]  
A pointer to a [**WDF\_OBJECT\_ATTRIBUTES**](wdf-wdf_object_attributes) structure that contains driver-supplied attributes for the new WDFSTRING object. This parameter is optional and can be WDF\_NO\_OBJECT\_ATTRIBUTES.

*WdfString* \[out\]  
A handle to a framework string object. NetAdapterCx will assign the registry value's string data to this object.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

By default, the framework string object is parented to the collection object. The client driver can change this by setting the **ParentObject** member of the [**WDF\_OBJECT\_ATTRIBUTES**](wdf-wdf_object_attributes) structure.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetConfigurationQueryString%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




