---
title: Building a WIA minidriver
description: Building a WIA minidriver
ms.date: 03/27/2023
---

# Building a WIA minidriver

The following header files and library files are required by all WIA minidrivers.

## Header files

All WIA minidrivers must include the header files that are shown in the following table.

| Header file | Description |
|--|--|
| *sti.h* | Defines the STI interfaces, structures, and event GUIDs that WIA minidrivers can use. |
| *stiusd.h* | Defines the [IStiUSD](/windows-hardware/drivers/ddi/_image/index) interface that all WIA minidrivers must implement. |
| *wiamindr.h* | Defines the [IWiaMiniDrv](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv) interface that all WIA minidrivers must implement. Other interfaces used by the WIA minidriver are defined here as well. |

WIA minidrivers may require additional header files. The headers that are required depend on the device type and the functionality that is implemented. These requirements are noted in the reference section.

## Library files

WIA uses the library files that are shown in the following table. All minidrivers require these libraries.

| Library file | Description |
|--|--|
| *wiaguid.lib* | Exports class identifiers (CLSIDs) and interface identifiers (IIDs). |
| *wiaservc.lib* | Exports the WIA service helper functions. |

In your build environment, the WDK *Include* and *Lib* directories should be the first directories in the search path. This ensures that you are using the most recent versions of headers and library files.
