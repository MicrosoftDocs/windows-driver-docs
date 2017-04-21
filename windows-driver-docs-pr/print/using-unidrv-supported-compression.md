---
title: Using Unidrv-Supported Compression
author: windows-driver-content
description: Using Unidrv-Supported Compression
ms.assetid: feda6898-da2c-403f-a159-1423891f3dd5
keywords:
- raster data compression WDK Unidrv
- compressing raster data WDK Unidrv
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Unidrv-Supported Compression


## <a href="" id="ddk-using-unidrv-supported-compression-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20Unidrv-Supported%20Compression%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


