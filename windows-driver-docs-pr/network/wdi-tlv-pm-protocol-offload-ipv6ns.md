---
title: WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv6NS
description: WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv6NS is a TLV that contains IPv6 NS protocol offload parameters.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0385449B-82C6-44B4-BBD3-A708ADE54AC4
keywords: ["WDI_TLV_PM_PROTOCOL_OFFLOAD_IPv6NS Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WDI_TLV_PM_PROTOCOL_OFFLOAD_IPv6NS
api_location:
- wditypes.hpp
api_type:
- HeaderDef
---

# WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv6NS


WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv6NS is a TLV that contains IPv6 NS protocol offload parameters.

## TLV Type


0x62

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32                                            | Specifies the protocol offload ID. This is an OS-provided value that identifies the offloaded protocol. Before the OS sends an Add request down or completes the request to the overlying driver, the OS sets ProtocolOffloadId to a value that is unique among the protocol offloads on a network adapter.                                                                                                    |
| UINT8\[16\]                                       | Specifies an optional IPv6 address to match with the Source Address field in the IPv6 header of the NS message. If the incoming NS message has a Source Address value that matches this IPv6 address, the network adapter sends a neighbor advertisement (NA) message when it is in a low power state. If this is set to zero, the network adapter should respond to NS messages from any remote IPv6 address. |
| UINT8\[16\]                                       | Specifies the solicited node IPv6 address.                                                                                                                                                                                                                                                                                                                                                                     |
| UINT8\[16\]                                       | Specifies one or two IPv6 addresses to match the Target Address field of an incoming NS message. If there is only one address, that address is stored in Target address 1, and Target address 2 is filled with zeros. If one of these addresses matches the Target Address field of an incoming NS message, the network adapter sends an NA message in response.                                               |
| UINT8\[16\]                                       | See description of Target address 1.                                                                                                                                                                                                                                                                                                                                                                           |
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | Specifies the MAC address that the network adapter must use for the target link-layer address (TLLA) field of the NA message that it generates. However, it should use the current MAC address of the network adapter as the source address in the MAC header.                                                                                                                                                 |

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_PM_PROTOCOL_OFFLOAD_IPv6NS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




