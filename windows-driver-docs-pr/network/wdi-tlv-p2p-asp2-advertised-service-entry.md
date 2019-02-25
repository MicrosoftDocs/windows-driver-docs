---
title: WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY
description: WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY is a TLV that contains an ASP2 Advertised Service Entry.
ms.assetid: CF7ED750-1987-4784-9E61-516EBBA22B9B
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




