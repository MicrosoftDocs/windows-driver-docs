---
title: Main I/O Path
description: Main I/O Path
ms.assetid: 643842e4-a75e-4d86-a1f7-d1a4468b5e17
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Main I/O Path


One of the architectural improvements that Storport has to offer is the HwBuildIo routine. Although this Storport miniport driver entry point is optional, it is highly recommended. The LSI\_U3 driver takes advantage of this improvement by implementing the LsiU3BuildIo routine. This entry point is called before the HwStartIo routine with no locks held, and as long as no shared memory is modified, this routine may perform processing that was previously done in the HwStartIo routine in the case of a Scsiport-based miniport driver. This allows most of the processing required to start separate I/O requests to be done in parallel on multiprocessor systems.

The LsiU3StartIo routine assigns driver queue tags to I/O requests. This is needed since Storport assigns queue tags on a per-LUN basis, not a per-adapter basis. The adapter hardware is limited to a maximum of 256 outstanding I/Os.

 

 




