---
title: OID_WDI_TASK_DISCONNECT (dot11wificxintf.h)
description: The OID_WDI_TASK_DISCONNECT task command is used to terminate a connection with a peer.
ms.date: 07/30/2021
keywords:
 - OID_WDI_TASK_DISCONNECT Network Drivers Starting with Windows Vista
---

# OID\_WDI\_TASK\_DISCONNECT (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_TASK\_DISCONNECT is used to terminate a connection with a peer.

| Object | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------|---------------------------------------|---------------------------------|
| Port   | No            | 2                                     | 1                               |

 

This command is used to disconnect from an Access Point or a Wi-Fi Direct GO, and also to disconnect clients of the port. When the disconnect is received, the port must disassociate and deauthenticate from the peer and clear the state associated with that peer. However, it must not reset any of the connection parameters that are not specific to this peer. The task must be completed only after the disconnect activity has been completed.

## Task parameters


| TLV                                                                            | Multiple TLV instances allowed | Optional | Description                |
|--------------------------------------------------------------------------------|--------------------------------|----------|----------------------------|
| [**WDI\_TLV\_DISCONNECT\_PARAMETERS**](./wdi-tlv-disconnect-parameters.md) |                                |          | The disconnect parameters. |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_DISCONNECT\_COMPLETE](ndis-status-wdi-indication-disconnect-complete.md)
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION](ndis-status-wdi-indication-disassociation.md)

When the port gets disconnected from the network, it sends the disassociation indication to the OS. The disconnect may be triggered by a command from the OS, or may be triggered from the network. Network triggered disconnects may be explicit from received disassociation or deauthentication packets, or may be implicit when the port cannot detect the presence of the peer it is connected to.

Before the disassociation indication is sent, the port must clear the state associated with the peer. This includes any keys and 802.1x port authorization information associated with the peer. The port must not trigger a roam on its own.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

