---
title: NET_ADAPTER_DRIVER_TYPE enumeration
topic_type:
- apiref
api_name:
- NET_ADAPTER_DRIVER_TYPE
api_location:
- netadapterdriver.h
api_type:
- HeaderDef
---

# NET_ADAPTER_DRIVER_TYPE enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Identifies the type of network adapter driver.

Syntax
------

```cpp
typedef enum _NET_ADAPTER_DRIVER_TYPE { 
  NET_ADAPTER_DRIVER_TYPE_INVALID   = 0,
  NET_ADAPTER_DRIVER_TYPE_MINIPORT  = 1
} NET_ADAPTER_DRIVER_TYPE;
```

Constants
---------

**NET_ADAPTER_DRIVER_TYPE_INVALID**  
Not currently supported.

**NET_ADAPTER_DRIVER_TYPE_MINIPORT**  
In NetAdapterCx version 1.0, this is the only supported value.

Remarks
-------

The **NET_ADAPTER_DRIVER_TYPE** enumeration is used to specify adapter type in the [**NET_ADAPTER_CONFIG**](net-adapter-config.md) structure.

An initialized **NET_ADAPTER_CONFIG** structure is an input parameter to [**NetAdapterCreate**](netadaptercreate.md).

The **NET_ADAPTER_DRIVER_TYPE** enumeration is also used as input to [**NetAdapterDriverWdmGetHandle**](netadapterdriverwdmgethandle.md).

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

 

 





