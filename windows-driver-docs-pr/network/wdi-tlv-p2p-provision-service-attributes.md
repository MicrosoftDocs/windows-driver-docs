---
title: WDI_TLV_P2P_PROVISION_SERVICE_ATTRIBUTES
description: WDI_TLV_P2P_PROVISION_SERVICE_ATTRIBUTES is a TLV that contains Wi-Fi Direct Provision Service attributes.
ms.assetid: CA318E91-660A-4F17-827B-F27E18643CC6
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_PROVISION_SERVICE_ATTRIBUTES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




