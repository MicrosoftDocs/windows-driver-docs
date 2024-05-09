---
title: WDI_TLV_RSN_KEY_INFO (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_RSN_KEY_INFO is a WiFiCx TLV that contains Rsn Eapol key parameters.
ms.date: 08/25/2023
---

# WDI_TLV_RSN_KEY_INFO (dot11wificxtypes.hpp)

WDI_TLV_RSN_KEY_INFO is a TLV that contains Rsn Eapol key parameters. This TLV is a value of the [WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY](wdi-tlv-pm-protocol-offload-80211rsn-rekey.md) TLV.

## TLV Type

0x148

## Length

The size (in bytes) of the following values.

## Values

| Type | Description |
| --- | --- |
| UINT32 | A UINT32 value that specifies the protocol offload ID. This is an OS-provided value that identifies the offloaded protocol. Before the OS sends an Add request down or completes the request to the overlying driver, the OS sets ProtocolOffloadId to a value that is unique among the protocol offloads on a network adapter. |
| UINT64 | A UINT64 value that specifies the replay counter. |
| UINT8\[16\] | A UINT8 array that specifies the IEEE 802.11 key confirmation key (KCK). |
| UINT8\[16\] | A UINT8 array that specifies the IEEE 802.11 key encryption key (KEK).  |
 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

