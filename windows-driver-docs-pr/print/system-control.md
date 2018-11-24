---
title: System Control
description: System Control
ms.assetid: 3ac58d53-daa7-4f50-a512-05325b95a17d
keywords:
- system-controlled color management WDK print
- default print color management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# System Control





System-controlled color management is the default color management type. It is also the recommended type for printers. If color management is enabled, GDI corrects the colors of all DIBs, pens, and brushes before sending them to the driver's printer graphics DLL, based on the input and output color spaces and installed ICC profiles.

No ICM-specific code needs to be added to a printer driver to support system-control color management, other than indicating support for CYMK color space (if appropriate), as described in [Supporting CMYK Color Space](supporting-cmyk-color-space.md).

 

 




