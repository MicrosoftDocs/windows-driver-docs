---
title: NET_ADAPTER_DRIVER_TYPE enumeration
description: The NET\_ADAPTER\_DRIVER\_TYPE enumeration identifies the type of network adapter driver.
ms.assetid: 05a9d0b1-7764-41d6-bd2c-6f1f1224b9fe
keywords: ["NET_ADAPTER_DRIVER_TYPE enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_DRIVER_TYPE
api_location:
- netadapterdriver.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_DRIVER\_TYPE enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NET\_ADAPTER\_DRIVER\_TYPE** enumeration identifies the type of network adapter driver.

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_DRIVER_TYPE { 
  NET_ADAPTER_DRIVER_TYPE_INVALID   = 0,
  NET_ADAPTER_DRIVER_TYPE_MINIPORT  = 1
} NET_ADAPTER_DRIVER_TYPE;
```

Constants
---------

<a href="" id="net-adapter-driver-type-invalid"></a>**NET\_ADAPTER\_DRIVER\_TYPE\_INVALID**  

<a href="" id="net-adapter-driver-type-miniport"></a>**NET\_ADAPTER\_DRIVER\_TYPE\_MINIPORT**  

Remarks
-------

The **NET\_ADAPTER\_DRIVER\_TYPE** enumeration is used as a parameter to [**NetAdapterDriverWdmGetHandle**](netadapterdriverwdmgethandle.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapterdriver.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_ADAPTER_DRIVER_TYPE%20enumeration%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




