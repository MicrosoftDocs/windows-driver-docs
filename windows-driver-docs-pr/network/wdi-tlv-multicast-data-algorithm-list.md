---
title: WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST
description: WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST is a TLV that contains an array of multicast data algorithm pairs.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: BF07170E-CF4E-4E93-85E1-3276E414BDD9
keywords: ["WDI_TLV_MULTICAST_DATA_ALGORITHM_LIST Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WDI_TLV_MULTICAST_DATA_ALGORITHM_LIST
api_location:
- wditypes.hpp
api_type:
- HeaderDef
---

# WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST


WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST is a TLV that contains an array of multicast data algorithm pairs.

## TLV Type


0x14

## Length


The size (in bytes) of the array of WDI\_ALGO\_PAIRS elements. The array must contain 1 or more elements.

**Note**  WDI\_ALGO\_PAIRS is not a WDI structure. It is defined in the WDI TLV parser generator, and is used for documentation purposes only.

 

## Values


| Type                 | Description                                            |
|----------------------|--------------------------------------------------------|
| WDI\_ALGO\_PAIRS\[\] | An array of authentication and cipher algorithm pairs. |

 

WDI\_ALGO\_PAIRS consists of the following elements.

| Type  | Description                                                                                     |
|-------|-------------------------------------------------------------------------------------------------|
| UINT8 | Authentication algorithm as defined in [**WDI\_AUTH\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897792). |
| UINT8 | Cipher algorithm as defined in [**WDI\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897802).     |

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_MULTICAST_DATA_ALGORITHM_LIST%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




