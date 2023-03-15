---
title: MB Network Blacklist Operations
description: MB Network Blacklist Operations
ms.date: 04/20/2017
ms.custom: UpdateFrequency3
---

# MB Network Blacklist Operations

> [!IMPORTANT]
> ### Bias-free communication
>
> Microsoft supports a diverse and inclusive environment. This article contains references to terminology that the Microsoft [style guide for bias-free communication](/style-guide/bias-free-communication) recognizes as exclusionary. The word or phrase is used in this article for consistency because it currently appears in the software. When the software is updated to remove the language, this article will be updated to be in alignment.

A device could be required to not register to a network under various scenarios, such as when a specific SIM card is inserted or if a device does not want to register to a specific network. To address these situations, Windows 10, version 1703 is adding modem interfaces to enable the OS to configure blacklists for SIM cards and network providers.

At any time, the OS can configure the MCC/MNC pair in the modem to specify the SIM or network to which the device is not allowed to register.  The interface is flexible enough to allow two different lists, one for SIM providers, and another for network providers.  If the device did not attempt registration because a particular SIM or network provider was blacklisted, the modem must report the registration status as denied.

## MB Interface Update for Network Blacklist Operations

A new MBIM command has been created to enable the OS to query and set the MCC and MNC pair with which the modem should not attempt registration when a matching SIM cards or network provider is present on the device. For this command, a new MSFT proprietary CID has been defined as MBIM_CID_MS_NETWORK_BLACKLIST.

Service Name = **Basic Connect Extensions**

UUID = **UUID_BASIC_CONNECT_EXTENSIONS**

UUID Value = **3d01dcc5-fef5-4d05-0d3abef7058e9aaf**

| CID | Command Code | Minimum OS Version |
| --- | --- | --- |
| MBIM_CID_MS_NETWORK_BLACKLIST | 2 | Windows 10, version 1703 |

## MBIM_CID_MS_NETWORK_BLACKLIST

### Description

Enterprises, users or mobile operators may specify the SIM cards and networks on which they do not want the modem to register. This command is used for the OS to be able to query and set the blacklists on the modem. There are two blacklists:

1.	A SIM card blacklist – SIM cards whose provider is a member of the blacklist should not be allowed to register on any network.
2.	A network provider blacklist – networks on the blacklist should not be allowed to register regardless of what SIM card is present on the device.

The modem has to maintain both blacklists per modem and persist across SIM swaps and power cycles. Both blacklists can be accessed with Query or Set at all times, regardless of the SIM state.

For the Set command it is expected to overwrite the existing blacklists in the modem with the Set command’s payload.

#### Query

MBIM_MS_NETWORK_BLACKLIST_INFO is returned from completed Query and Set messages in the InformationBuffer. For Query, the InformationBuffer is NULL.

#### Set

For Set, the InformationBuffer contains an MBIM_MS_NETWORK_BLACKLIST_INFO. In the Set operation, a list of MNC/MCC combinations should be provided to the modem. When the SIM card’s IMSI matches the MNC and MCC value specified, the modem should deregister from the network and should not try to reregister until a new SIM card that does not match the MNC/MCC is inserted.

#### Unsolicited Event

An Unsolicited Event is expected if any of the blacklist states have changed from actuated to not actuated, or vice versa; for example, if a SIM is inserted whose provider matches the SIM provider blacklist.

### Parameters

| Operation | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | MBIM_MS_NETWORK_BLACKLIST_INFO | Not applicable | Not applicable |
| Response | MBIM_MS_NETWORK_BLACKLIST_INFO | MBIM_MS_NETWORK_BLACKLIST_INFO | MBIM_MS_NETWORK_BLACKLIST_INFO |

### Data Structures

#### Query

The InformationBuffer shall be NULL and InformationBufferLength shall be zero.

#### Set

The following MBIM_MS_NETWORK_BLACKLIST_INFO structure shall be used in the InformationBuffer.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | BlacklistState | MBIM_MS_NETWORK_BLACKLIST_STATE | Indicates whether any of the blacklist conditions are met that result in the modem not registering to the network. For more information, see the MBIM_MS_NETWORK_BLACKLIST_STATE table. |
| 4 | 4 | ElementCount (EC) | UINT32 | Count of MBIM_MS_NETWORK_BLACKLIST_PROVIDER structures that follow in the DataBuffer. |
| 8 | 8 * EC | BlacklistProviderRefList | OL_PAIR_LIST | The first element of the pair is a 4 byte offset, calculated from the beginning (offset 0) of this MBIM_MS_NETWORK_BLACKLIST_INFO structure, to a MBIM_MS_NETWORK_BLACKLIST_PROVIDER structure. For more information, see the MBIM_MS_NETWORK_BLACKLIST_PROVIDER table.  The second element of the pair is a 4-byte size of a pointer to the corresponding MBIM_MS_NETWORK_BLACKLIST_PROVIDER structure. |
| 8 + (8 * EC) |  | DataBuffer | DATABUFFER | Array of MBIM_MS_NETWORK_BLACKLIST_PROVIDER structures. |

The following data structures are used in the preceding table.

MBIM_MS_NETWORK_BLACKLIST_STATE describes the possible states of the two different blacklists.

| Type | Mask | Description |
| --- | --- | --- |
| MbimMsNetworkBlacklistStateNotActuated | 0h | Both blacklist conditions are not met. |
| MbimMsNetworkBlacklistSIMProviderActuated | 1h | Inserted SIM is blacklisted as its Provider ID matches the blacklist for SIM Provider ID. |
| MbimMsNetworkBlacklistNetworkProviderActuated | 2h | Available networks are blacklisted since their Provider IDs are all in the blacklist for network Provider ID. |

MBIM_MS_NETWORK_BLACKLIST_PROVIDER specifies the provider of the blacklist.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | MCC | UINT32 | As specified by 3GPP, MCC is part of IMSI and specifies the country of the provider. |
| 4 | 4 | MNC | UINT32 | As specified by 3GPP, MNC is part of IMSI and specifies the network of the provider. |
| 8 | 4 | NetworkBlacklistType | MBIM_MS_NETWORK_BLACKLIST_TYPE | Specifies for which type of blacklist the MCC/MNC pair is used. For more information, see the MBIM_MS_NETWORK_BLACKLIST_TYPE table. |

MBIM_MS_NETWORK_BLACKLIST_TYPE is used by the preceding data structure. It specifies which of the two blacklists will be used.

| Type | Value | Description |
| --- | --- | ---- |
| MbimMsNetworkBlacklistTypeSIM | 0 | The MCC/MNC pair are used for SIM provider blacklist. |
| MbimMsNetworkBlacklistTypeNetwork | 1 | The MCC/MNC pair are used for network provider blacklist. |

#### Response

For more information, see the MBIM_MS_NETWORK_BLACKLIST_INFO table.

### Status Codes

For Query and Set operations:

| Status Code | Description |
| --- | --- |
| MBIM_STATUS_READ_FAILURE | The operation failed because the device was unable to retrieve provisioned contexts. |
| MBIM_STATUS_NO_DEVICE_SUPPORT | The operation failed because the device does not support the operation. |

For Set operations only:

| Status Code | Description |
| --- | --- |
| MBIM_STATUS_INVALID_PARAMETERS | The operation failed because of invalid parameters. |
| MBIM_STATUS_WRITE_FAILURE | The operation failed because the update request was unsuccessful. |
