---
title: WDI_TLV_FTM_TARGET_BSS_ENTRY (dot11wificxtypes.hpp)
description: WDI_TLV_FTM_TARGET_BSS_ENTRY is a WiFiCx TLV that contains information for a BSS target with which Fine Timing Measurement (FTM) procedures should be completed.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_FTM_TARGET_BSS_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_FTM_TARGET_BSS_ENTRY (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_FTM_TARGET_BSS_ENTRY** is a TLV that contains information for a BSS target with which Fine Timing Measurement (FTM) procedures should be completed. 

This TLV is used in the task parameters for [OID_WDI_TASK_REQUEST_FTM](oid-wdi-task-request-ftm.md).

## TLV type

0x162

## Length

The sum (in bytes) of the sizes of all contained TLVs.

## Values

| TLV | Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- | --- |
| [WDI_TLV_BSSID](wdi-tlv-bssid.md) | [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) |   |   | The BSSID of the target BSS. |
| [WDI_TLV_PROBE_RESPONSE_FRAME](wdi-tlv-probe-response-frame.md) | TLV\<LIST\<UINT8>> |   | X | The probe response frame. If no probe response has been received, this field is empty. |
| [WDI_TLV_BEACON_FRAME](wdi-tlv-beacon-frame.md) | TLV\<LIST\<UINT8>> |   | X | The beacon frame. If no beacon has been received, this field is empty. |
| [WDI_TLV_BSS_ENTRY_SIGNAL_INFO](wdi-tlv-bss-entry-signal-info.md) | INT32 |   |   | The received signal strength indicator (RSSI) value of the beacon or probe response from the peer. This is in units of decibels referenced to 1.0 milliwatts (dBm). |
|  | UINT32 |   |   | The link quality value ranging from 0 through 100. A value of 100 specifies the highest link quality. |
| [WDI_TLV_BSS_ENTRY_CHANNEL_INFO](wdi-tlv-bss-entry-channel-info.md) | UINT32 |   |   | The logical channel number of the target BSS. |
|   | UINT32 |   |   | The Band ID of the target BSS. |
| [WDI_TLV_BSS_ENTRY_DEVICE_CONTEXT](wdi-tlv-bss-entry-device-context.md) | TLV\<LIST\<UINT8>> |  |  | IHV component-provided context data about this peer. This can be usd to store per-BSS entry state that the IHV component wants to maintain. To avoid lifetime management issues, the IHV component must not use pointers in this field. |
| [WDI_TLV_REQUEST_LCI_REPORT](wdi-tlv-request-lci-report.md) | UINT8 |   |   | Possible values: <ul><li>0: LCI report not needed.</li><li>1: LCI report should be requested.</li></ul> |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

