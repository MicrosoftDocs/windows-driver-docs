---
title: MB NITZ support
description: MB NITZ support
keywords:
- MB NITZ support, Mobile Broadband NITZ support
ms.date: 03/13/2019
ms.localizationpriority: medium
ms.custom: 19H1
---

# MB NITZ support

## Overview

Starting in Windows 10, version 1903, Windows supports Network Identity and Time Zone (NITZ) at the OS level for mobile broadband (MBB) devices. In previous versions of Windows, the only network time available at the OS level was Network Time Protocol (NTP), even though NITZ was supported at the modem level by all 3GPP-compliant modems. With NITZ support, Windows is able to receive unsolicited NITZ notifications from modems and publish necessary events to notify consumers of the NITZ timestamps.

For MBIM functions, no additional NITZ-related setup and provisioning is required. As long as a data connection is established over a cellular bearer, a modem can notify the OS any time it has received a NITZ timestamp from the network. Modems can receive NITZ notifications from the network infrastructure based on the mobile operator's own defined cadence and schedule, within the 3GPP specifications. NITZ notifications are unsolicited. Upon receiving the NITZ notification, the OS publishes the notification that NITZ data is available.

## NDIS interface extension

The following OID has been defined to support NITZ.

- [OID_WWAN_NITZ](oid-wwan-nitz.md)

## MBIM service and CID values

| Service name | UUID | UUID value |
| --- | --- | --- |
| Microsoft Basic IP Connectivity Extensions | UUID_VOICEEXTENSIONS | 8d8b9eba-37be-449b-8f1e-61cb034a702e |

The following table specifies the UUID and command code for each CID, as well as whether the CID supports Set, Query, or Event (notification) requests. See each CID’s individual Section within this topic for more info about its parameters, data structures, and notifications. 

| CID | UUID | Command code | Set | Query | Notify |
| --- | --- | --- | --- | --- | --- |
| MBIM_CID_NITZ | UUID_VOICEEXTENSIONS | 10 | N | Y | Y |

## MBIM_CID_NITZ

### Parameters

| Operation | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Not applicable | Not applicable | Not applicable |
| Response | Not applicable | MBIM_NITZ_INFO | MBIM_NITZ_INFO |

### Query

Queries the current network time. The InformationBuffer of MBIM_COMMAND_MSG is not used. The following MBIM_NITZ_INFO structure is used in the InformationBuffer of MBIM_COMMAND_DONE.

#### MBIM_NITZ_INFO

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | Year | UINT32 | The year as an integer. For example, **2014**. |
| 4 | 4 | Month | UINT32 | The month (1..12), where January == 1. |
| 8 | 4 | Day | UINT32 | The day of the month, (1..31). |
| 12 | 4 | Hour | UINT32 | The hour, (0..23). |
| 16 | 4 | Minute | UINT32 | The minute, (0..59). |
| 20 | 4 | Second | UINT32 | The second, (0..59). |
| 24 | 4 | TimeZoneOffsetMinutes | UINT32 | The time zone offset, in minutes, from UTC. This value includes any adjustment for the current state of daylight saving time. This value should be set to 0xFFFFFFFF when time zone info is not available. |
| 28 | 4 | DaylightSavingTimeOffsetMinutes | UINT32 | The offset for daylight saving time, in minutes. This value should be set to 0xFFFFFFFF when daylight saving time is not available. |
| 32 | 4 | DataClasses | UINT32 | Data classes supported by this network. If this information is not available, this field should be set to MBIMDataClassNone. |

### Set

Not applicable.

### Response

The InformationBuffer in MBIM_COMMAND_DONE contains an MBIM_NITZ_INFO structure.

### Unsolicited Events

This unsolicited event provides the current network time and time zone information.

### Status Codes

This CID only uses generic status codes defined in Section 9.4.5 of the [MBIM specification revision 1.0](https://www.usb.org/sites/default/files/MBIM10Errata1_073013.zip).
