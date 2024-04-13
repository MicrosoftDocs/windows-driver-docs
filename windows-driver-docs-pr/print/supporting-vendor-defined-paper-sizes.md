---
title: Supporting Vendor-Defined Paper Sizes
description: Supporting Vendor-Defined Paper Sizes
keywords:
- vendor-supplied paper sizes WDK Unidrv
- nonstandard paper sizes WDK Unidrv
ms.date: 01/30/2023
---

# Supporting Vendor-Defined Paper Sizes

[!include[Print Support Apps](../includes/print-support-apps.md)]

Vendor-defined paper sizes are vendor-specific and must be fully described by each printer's GPD file. These sizes are also called nonstandard paper sizes, because they are not included in the [standard options](standard-options.md) for the PaperSize feature.

For each vendor-defined paper size that a printer supports, the GPD file's PaperSize feature must include an \*Option entry whose argument is not one of the standard option names. Within this entry, the following option attributes are required:

\*PageDimensions
\*PrintableArea
\*PrintableOrigin
\*rcNameID or \*Name
\*Command

The following option attributes can be used, but are not required:

\*CursorOrigin
\*RotateSize?
\*PageProtectMem
