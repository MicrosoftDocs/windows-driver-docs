---
title: WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY
author: windows-driver-content
description: WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY is a TLV that contains an ASP2 Advertised Service Entry.
ms.assetid: CF7ED750-1987-4784-9E61-516EBBA22B9B
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_ASP2\_ADVERTISED\_SERVICE\_ENTRY


WDI\_TLV\_P2P\_ASP2\_ADVERTISED\_SERVICE\_ENTRY is a TLV that contains an ASP2 Advertised Service Entry.

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x12E

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                           | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SERVICE\_TYPE**](wdi-tlv-p2p-service-type.md)               |                                |          | Service Type of the service (UTF-8), up to 21 bytes.                                                                                                                                                                                                                                     |
| [**WDI\_TLV\_P2P\_SERVICE\_TYPE\_HASH**](wdi-tlv-p2p-service-type-hash.md)    |                                |          | Hash of Service Type.                                                                                                                                                                                                                                                                    |
| [**WDI\_TLV\_P2P\_INSTANCE\_NAME**](wdi-tlv-p2p-instance-name.md)             |                                |          | Instance Type of the service (UTF-8), up to 63 bytes.                                                                                                                                                                                                                                    |
| [**WDI\_TLV\_P2P\_INSTANCE\_NAME\_HASH**](wdi-tlv-p2p-instance-name-hash.md)  |                                |          | Hash of "Instance Name, Service Type".                                                                                                                                                                                                                                                   |
| [**WDI\_TLV\_P2P\_SERVICE\_INFORMATION**](wdi-tlv-p2p-service-information.md) |                                | X        | Service Information for the service.                                                                                                                                                                                                                                                     |
| [**WDI\_TLV\_P2P\_SERVICE\_STATUS**](wdi-tlv-p2p-service-status.md)           |                                |          | Service Status of the service.                                                                                                                                                                                                                                                           |
| [**WDI\_TLV\_P2P\_ADVERTISEMENT\_ID**](wdi-tlv-p2p-advertisement-id.md)       |                                |          | An ID that uniquely identifies the service instance.                                                                                                                                                                                                                                     |
| [**WDI\_TLV\_P2P\_CONFIG\_METHODS**](wdi-tlv-p2p-config-methods.md)           |                                |          | Configuration methods as defined in [**WDI\_WPS\_CONFIGURATION\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/dn898198). Only **WDI\_WPS\_CONFIGURATION\_METHOD\_DISPLAY**, **WDI\_WPS\_CONFIGURATION\_METHOD\_KEYPAD**, and **WDI\_WPS\_CONFIGURATION\_METHOD\_WFDS\_DEFAULT** are applicable. |

 

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


