---
title: WDI_TLV_LINK_QUALITY_BAR_MAP (dot11wificxtypes.h)
description: WDI_TLV_LINK_QUALITY_BAR_MAP is a WiFiCx TLV that contains the mapping of signal quality to Wi-Fi signal strength bars.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_LINK_QUALITY_BAR_MAP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_LINK\_QUALITY\_BAR\_MAP (dot11wificxtypes.h)


WDI\_TLV\_LINK\_QUALITY\_BAR\_MAP is a TLV that contains the mapping of signal quality to Wi-Fi signal strength bars.

## TLV Type


0xD8

## Length


The size (in bytes) of the array of WDI\_LINK\_QUALITY\_BAR\_MAP\_PARAMETERS elements. The array must contain 1 or more elements.

**Note**  WDI\_LINK\_QUALITY\_BAR\_MAP\_PARAMETERS is not a WiFiCx structure. It is defined in the WiFiCx TLV parser generator, and is used for documentation purposes only.

 

## Values


| Type                                         | Description                                         |
|----------------------------------------------|-----------------------------------------------------|
| WDI\_LINK\_QUALITY\_BAR\_MAP\_PARAMETERS\[\] | An array of signal strength bar mapping parameters. |

 

WDI\_LINK\_QUALITY\_BAR\_MAP\_PARAMETERS consists of the following elements.

| Type  | Description                                                                  |
|-------|------------------------------------------------------------------------------|
| UINT8 | The lower limit link quality (0-100) for the current signal strength bar.    |
| UINT8 | The upper limit of link quality (0-100) for the current signal strength bar. |
| UINT8 | The signal strength bar number.                                              |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|


 

 




