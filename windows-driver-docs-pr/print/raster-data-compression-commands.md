---
title: Raster Data Compression Commands
description: Raster Data Compression Commands
keywords:
- data compression raster printing commands WDK Unidrv
- compression raster printing commands WDK Unidrv
ms.date: 01/29/2024
---

# Raster data compression commands

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the raster data compression commands. All commands are specified using the [command entry format](command-entry-format.md).

For more information about raster data compression commands, see [Compressing Raster Data](compressing-raster-data.md).

| Command | Description | Comments |
|--|--|--|
| CmdDisableCompression | Command to disable the printer's acceptance of all compressed data types. | Optional |
| CmdEnableDRC | Command to enable the printer's acceptance of DRC-compressed data. | Optional. If not specified, Unidrv does not use Delta-Row compression. |
| CmdEnableFE_RLE | Command to enable the printer's acceptance of FE-RLE-compressed data. | Optional. If not specified, Unidrv does not use FE-RLE compression. |
| CmdEnableOEMComp | Command to enable the printer's acceptance of a customized compressed data type. | Optional. If not specified, Unidrv does not use customized data compression. |
| CmdEnableTIFF4 | Command to enable the printer's acceptance of TIFF 4.0-compressed data. | Optional. If not specified, Unidrv does not use TIFF4.0 compression. |

For GPD examples, see [Sample GPD files](sample-gpd-files.md).
