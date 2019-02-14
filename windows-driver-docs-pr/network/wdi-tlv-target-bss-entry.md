---
title: WDI_TLV_TARGET_BSS_ENTRY
description: WDI_TLV_TARGET_BSS_ENTRY is a TLV that contains information for a BSS target with which Fine Timing Measurement (FTM) procedures should be completed.
ms.assetid: 04C996C7-8207-4363-A990-5CF39B0333F8
ms.date: 02/13/2019
keywords:
 - WDI_TLV_TARGET_BSS_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_TARGET_BSS_ENTRY

**WDI_TLV_TARGET_BSS_ENTRY** is a TLV that contains information for a BSS target with which Fine Timing Measurement (FTM) procedures should be completed. This TLV is used in the task parameters for [OID_WDI_TASK_REQUEST_FTM](oid-wdi-task-request-ftm.md).

## TLV type

0x162

## Length

The sum (in bytes) of the sizes of all contained TLVs.

## Values

| Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| WDI_MAC_ADDRESS |   |   | The BSSID of the target BSS. |
| TLV\<LIST\<UINT8>> |   | X | X | The probe response frame. If no probe response has been received, this field is empty. |
| TLV\<LIST\<UINT8>> |   | X | X | The beacon frame. If no beacon has been received, this field is empty. |
| INT32 |   |   |   | The received signal strength indicator (RSSI) value of the beacon or probe response from the peer. This is in units of decibels referenced to 1.0 milliwatts (dBm). |
| UINT32 |   |   |   | The link quality value ranging from 0 through 100. A value of 100 specifies the highest link quality. |
| UINT32 |   |   |   | The logical channel number of the target BSS. |
| UINT32 |   |   |   | The Band ID of the target BSS. |
| TLV\<LIST\<UINT8>> | X |  | IHV component-provided context data about this peer. This can be usd to store per-BSS entry state that the IHV component wants to maintain. To avoid lifetime management issues, the IHV component must not use pointers in this field. |
| UINT8 {0, 1}  |   |   | Possible values: <ul><li>0: LCI report not needed.</li><li>1: LCI report should be requested.</li></ul> |

## Requirements

|   |   |
| --- | --- |
| Minimum supported client | Windows 10, version 1903 |
| Minimum supported server | Windows Server 2016 |
| Header | Wditypes.hpp |