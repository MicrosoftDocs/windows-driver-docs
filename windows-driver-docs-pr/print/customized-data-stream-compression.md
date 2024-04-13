---
title: Customized Data Stream Compression
description: Customized Data Stream Compression
keywords:
- Unidrv, data stream compression
- data stream compression WDK Unidrv
- customized data stream compression WDK Unidrv
- compressed data streams WDK Unidrv
- Unidrv WDK print
ms.date: 01/27/2023
---

# Customized Data Stream Compression

[!include[Print Support Apps](../includes/print-support-apps.md)]

Unidrv allows you to perform data compression operations using customized code. To perform customized compression operations, perform the following steps:

1. Provide a rendering plug-in that implements the [**IPrintOemUni::Compression**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-compression) method.

1. Include a CmdEnableOEMComp command entry in the printer's *GPD* file.

The IPrintOemUni::Compression method receives scan line data as input. The method must compress the data and then return the result to Unidrv. The **CmdEnableOEMComp** command entry specifies the command that must be sent to the printer so that the printer can accept the compressed data. For each scan line that is to be sent to the printer, Unidrv calls IPrintOemUni::Compression to compress the scan line data. Then, if this is the only compression method available, Unidrv sends to the printer the command specified by the **CmdEnableOEMComp** command entry, followed by the compressed data.

If the printer minidriver contains GPD entries that also enable Unidrv-supported compression methods, Unidrv tries each compression algorithm for each scan line and chooses the algorithm that produces the best result. For more information about Unidrv's compression capabilities, see [Compressing Raster Data](compressing-raster-data.md).

Only one customized compression method can be enabled at one time.
