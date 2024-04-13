---
title: Supporting Standard Paper Sizes
description: Supporting Standard Paper Sizes
keywords:
- standard paper sizes WDK Unidrv
ms.date: 01/30/2023
---

# Supporting Standard Paper Sizes

[!include[Print Support Apps](../includes/print-support-apps.md)]

Standard paper sizes are represented by the [standard options](standard-options.md) for the PaperSize feature.

For each standard paper size that a printer supports, the GPD file's PaperSize feature must include an \*Option entry whose argument is one of the standard option names (except CUSTOMSIZE).

Within this entry, the following option attributes are required:

\*PrintableArea
\*PrintableOrigin
\*rcNameID
\*Command

The following option attributes can be used, but are not required:

\*CursorOrigin
\*RotateSize?
\*PageProtectMem

For all standard paper sizes, the RCID_DMPAPER_SYSTEM_NAME resource identifier (defined in stdnames.gpd) should be used as the argument to \***rcNameID**.
