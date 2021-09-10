---
title: WDI_TLV_ADDITIONAL_IES (dot11wificxtypes.hpp)
description: WDI_TLV_ADDITIONAL_IES is a WiFiCx TLV that contains additional Information Element (IE) settings.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_ADDITIONAL_IES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ADDITIONAL\_IES (dot11wificxtypes.hpp)


WDI\_TLV\_ADDITIONAL\_IES is a TLV that contains additional Information Element (IE) settings.

## TLV Type


0x8A

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                       | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_ADDITIONAL\_BEACON\_IES**](wdi-tlv-additional-beacon-ies.md)                                 |                                | X        | An array of beacon IEs. The Wi-Fi Direct port must add these additional IEs to the beacon packets when it is acting as a Group Owner. This is ignored when the Wi-Fi Direct port is operating in device or client mode.                                                                                              |
| [**WDI\_TLV\_ADDITIONAL\_PROBE\_RESPONSE\_IES**](wdi-tlv-additional-probe-response-ies.md)                |                                | X        | An array of probe response IEs. The Wi-Fi Direct port must add these additional IEs to the probe response packets when it is acting as a Wi-Fi Direct device or Group Owner. This is ignored when the Wi-Fi Direct port is operating in client mode.                                                                 |
| [**WDI\_TLV\_ADDITIONAL\_PROBE\_REQUEST\_DEFAULT\_IES**](wdi-tlv-additional-probe-request-default-ies.md) |                                | X        | An array of additional probe request IEs. This offset is relative to the start of the buffer that contains this structure. The Wi-Fi Direct port must add these additional IEs to the probe request packets that it transmits. Note that a Wi-Fi Direct discover request may override the default probe request IEs. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




