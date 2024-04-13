---
title: WDI_TLV_PLDR_SUPPORT (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_PLDR_SUPPORT is a WIFiCx TLV that specifies if PLDR (Platform Level Reset) is supported.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_PLDR_SUPPORT Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PLDR\_SUPPORT (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_PLDR\_SUPPORT is a TLV that specifies if PLDR (Platform Level Reset) is supported.

 

## TLV Type


0x11A

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                                                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | Specifies if PLDR is supported. This value is set to 0 if the device or bus does not support reset functionality (usually by querying the ACPI or PCI methods). A non-zero value specifies that reset functionality is supported. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

## See also


[PLDR](../network/wdi-pldr-and-fldr.md)

 

