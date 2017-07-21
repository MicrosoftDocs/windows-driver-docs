---
title: WDI_TLV_P2P_PROVISION_SERVICE_ATTRIBUTES
author: windows-driver-content
description: WDI_TLV_P2P_PROVISION_SERVICE_ATTRIBUTES is a TLV that contains Wi-Fi Direct Provision Service attributes.
ms.assetid: CA318E91-660A-4F17-827B-F27E18643CC6
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_P2P_PROVISION_SERVICE_ATTRIBUTES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES


WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES is a TLV that contains Wi-Fi Direct Provision Service attributes.

## TLV Type


0xC6

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                        |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8                                             | Wi-Fi Direct Status Code, as defined by the Wi-Fi Direct specification.                                                                            |
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | Local MAC Address for future Wi-Fi Direct connection.                                                                                              |
| UINT8                                             | Connection Capability bitmask.                                                                                                                     |
| UINT32                                            | Feature Capability bitmask.                                                                                                                        |
| UINT32                                            | Advertisement ID for the Service Instance.                                                                                                         |
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | Service address for the Service instance.                                                                                                          |
| UINT32                                            | Session ID that uniquely identifies the Session to the Service.                                                                                    |
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | Session address that uniquely identifies the Session to the Service.                                                                               |
| UINT16                                            | GO Configuration Timeout in milliseconds.                                                                                                          |
| UINT16                                            | Client Configuration Timeout in milliseconds.                                                                                                      |
| UINT8                                             | A flag indicating if a Persistent Group will be used for the connection. The flag is set to 1 if a Persistent Group will be used.                  |
| UINT8                                             | A flag indicating if this frame is part of a follow-on provision discovery. The flag is set to 1 if it is part of a follow-on provision discovery. |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_P2P_PROVISION_SERVICE_ATTRIBUTES%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


