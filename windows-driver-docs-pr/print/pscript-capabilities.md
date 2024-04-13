---
title: Pscript Capabilities
description: Pscript Capabilities
keywords:
- PostScript Printer Driver WDK print , capabilities
- Pscript WDK print , capabilities
ms.date: 01/30/2023
---

# Pscript Capabilities

[!include[Print Support Apps](../includes/print-support-apps.md)]

The PostScript Printer Driver (Pscript) provides the following capabilities:

- Support for all PostScript printers, using printer-specific *PPD*-based [Pscript minidrivers](pscript-minidrivers.md) that describe each printer's characteristics.

- A [Pscript user interface](pscript-user-interface.md), based on the TreeView control and property sheets, that is consistent for all printers, but is also modifiable for each printer's unique options.

- A single [Pscript renderer](pscript-renderer.md) that, along with the GDI graphics engine, converts Microsoft Win32 GDI calls from applications into printer commands that can be sent to the print spooler.

- Support for version 3.1 of the Document Structuring Convention, described in the PostScript Language Reference Manual published by Adobe Systems, Inc.

- Support for printers that provide PostScript Level 1, Level 2, or Level 3 features.

- The following types of support for fonts:
  - Incremental downloading of OpenType fonts as PostScript Type 1 or Type 2 fonts.
  - Incremental downloading of TrueType fonts as PostScript Type 1, Type 3, Type 32, Type 42, or CID-based Type 42 fonts.
  - Incremental downloading of host-resident raster fonts as PostScript Type 3 or Type 32 fonts.
  - Full downloading of host-resident PostScript Type 1 fonts.
  - Printer-resident PostScript Type 1, Type 2, and CID fonts.
  - Font substitution per glyph, for glyphs that exist in the printer's character set.

- Support for ICM 2.0, and allowing image color management to be performed on the host system or by printer hardware.
