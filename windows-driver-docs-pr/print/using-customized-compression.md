---
title: Using Customized Compression
description: Using Customized Compression
keywords:
- raster data compression WDK Unidrv
- compressing raster data WDK Unidrv
- customized raster data compression WDK Unidrv
ms.date: 01/31/2023
---

# Using Customized Compression

[!include[Print Support Apps](../includes/print-support-apps.md)]

If you want to supply a customized compression algorithm, you include a CmdEnableOEMComp command entry to specify the command that enables your algorithm. If your printer can disable compression, you can optionally include a CmdDisableCompression entry to specify the command that disables compression. You must also provide a [rendering plug-in](rendering-plug-ins.md) that implements the [**IPrintOemUni::Compression**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-compression) method.

If you provide a customized compression algorithm, you can also enable the use of Unidrv-supported algorithms. For each scan line, Unidrv tries each compression algorithm and chooses the algorithm that produces the most compressed result. (For information about Unidrv-supported algorithms, see [Using Unidrv-Supported Compression](using-unidrv-supported-compression.md).) When Unidrv finds the best algorithm, it compresses the scan line data. Then it sends to the printer the command specified by the appropriate command entry, followed by the compressed data.

For more information about CmdEnableOEMComp and CmdDisableCompression entries, see [Raster Data Compression Commands](raster-data-compression-commands.md).

For more information about customized compression, see [Customized Data Stream Compression](customized-data-stream-compression.md).
