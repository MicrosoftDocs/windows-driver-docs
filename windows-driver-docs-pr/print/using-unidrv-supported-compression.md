---
title: Using Unidrv-Supported Compression
description: Using Unidrv-Supported Compression
ms.assetid: feda6898-da2c-403f-a159-1423891f3dd5
keywords:
- raster data compression WDK Unidrv
- compressing raster data WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Unidrv-Supported Compression





If you include a CmdEnableTIFF4 command entry in your GPD file, Unidrv uses TIFF 4.0 compression.

If you include a CmdEnableDRC command entry in your GPD file, Unidrv uses DRC compression.

If you include a CmdEnableFE\_RLE command entry in your GPD file, Unidrv uses FE-RLE compression.

If your printer supports more than one of these compression methods, you can include a command entry for each supported method. For each scan line, Unidrv tries each compression algorithm and chooses the algorithm that produces the most compressed result. (You can also include a customized algorithm. See [Using Customized Compression](using-customized-compression.md).) When Unidrv finds the best algorithm, it compresses the scan line data. Then it sends to the printer the command specified by the appropriate command entry, followed by the compressed data.

If you specify a CmdDisableCompression command entry, then regardless of the compression methods available, Unidrv temporarily disables sending compressed data when it encounters an uncompressed data block that is smaller than its compressed form.

To limit unnecessary computations, do not enable a compression method (by specifying its command entry) if the method is unlikely to produce a usable result.

For most printers, acceptance of compressed data can be enabled or disabled by sending command strings outside of data blocks. When you specify CmdEnableTIFF4, CmdEnableDRC, CmdEnableFE\_RLE, and CmdDisableCompression entries for these printers, you include a command string.

For some printers (typically East Asian printers), compression selection commands are embedded in the raster data that is sent with a CmdSendBlockData command. When you specify CmdEnableTIFF4, CmdEnableDRC, or CmdEnableFE\_RLE entries for these printers, do not include a command string. Instead, specify an empty quoted string to represent the command. This tells Unidrv to use compression but to not send separate commands to enable it. For these printers, only one compression algorithm can be used. A CmdDisableCompression entry is not needed because there is no way for Unidrv to turn off compression in this case.

For more information about CmdEnableTIFF4, CmdEnableDRC, CmdEnableFE\_RLE, and CmdDisableCompression entries, see [Raster Data Compression Commands](raster-data-compression-commands.md).

For more information about CmdSendBlockData, see [Raster Data Emission Commands](raster-data-emission-commands.md).

 

 




