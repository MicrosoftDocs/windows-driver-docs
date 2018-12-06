---
title: Supporting Standard Paper Sizes
description: Supporting Standard Paper Sizes
ms.assetid: 04f8fbdb-88f8-4595-b5d2-74315c02bb41
keywords:
- standard paper sizes WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Standard Paper Sizes





Standard paper sizes are represented by the [standard options](standard-options.md) for the PaperSize feature.

For each standard paper size that a printer supports, the GPD file's PaperSize feature must include an \*Option entry whose argument is one of the standard option names (except CUSTOMSIZE). Within this entry, the following option attributes are required:

\*PrintableArea
\*PrintableOrigin
\*rcNameID
\*Command
The following option attributes can be used, but are not required:

\*CursorOrigin
\*RotateSize?
\*PageProtectMem
For all standard paper sizes, the RCID\_DMPAPER\_SYSTEM\_NAME resource identifier (defined in stdnames.gpd) should be used as the argument to \***rcNameID**.

 

 




