---
title: NetConfigurationQueryUlong method
description: Retrieves the specified unsigned long word (REG\_DWORD) data from the adapter configuration object and copies the data to a specified location.
ms.assetid: 2a8975d5-459b-40f2-b8a6-aafec6c76c20
keywords: ["NetConfigurationQueryUlong method Network Drivers Starting with Windows Vista"]
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


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

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
A handle to an adapter configuration object opened in a prior call to [**NetAdapterOpenConfiguration**](netadapteropenconfiguration.md) or [**NetConfigurationOpenSubConfiguration**](netconfigurationopensubconfiguration.md).

*Flags* \[in\]  
A valid bitwise OR of [**NET\_CONFIGURATION\_QUERY\_ULONG\_FLAGS**](net-configuration-query-ulong-flags.md)-typed flags.

*ValueName* \[in\]  
A pointer to a **UNICODE\_STRING** structure that contains a name for the ULONG value.

*Value* \[out\]  
A pointer to a location that receives the data that is assigned to the value that *ValueName* specifies.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate [NTSTATUS](kernal-ntstatus_values) error code.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetConfigurationQueryUlong%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




