---
title: OID_WDI_SET_LOCATION_PRIVACY (dot11wificxintf.h)
ms.topic: reference
description: The OID_WDI_SET_LOCATION_PRIVACY command sets the current location privacy setting.
ms.date: 08/30/2021
keywords:
 - OID_WDI_SET_LOCATION_PRIVACY Network Drivers Starting with Windows Vista
---

# OID_WDI_SET_LOCATION_PRIVACY (dot11wificxintf.h)

OID_WDI_SET_LOCATION_PRIVACY sets the current location privacy setting. This setting allows the device to control privacy-sensitive location operations such as those in 802.11mc. The primary purpose of this setting is to disable such features, revoking consent. A **true** setting should not be considered as unconditionally granting consent. If other settings that affect location privacy are used, the most privacy-conscious outcome should take effect.

## Command parameters

| TLV | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| [WDI_TLV_LOCATION_PRIVACY](wdi-tlv-location-privacy.md) |  |  | If **false**, the adapter is not permitted to perform privacy-sensitive location operations, such as sharing the device’s precise location. If **true**, the adapter may perform such operations unless it is restricted by other settings. |


## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|
