---
title: V4 Printer Driver Rendering
description: For rendering print jobs into the page description language for a print device, the v4 print driver model uses the XPSDrv Render Module.
ms.assetid: 8952063C-3706-43A0-BA6B-231E7CD01514
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# V4 Printer Driver Rendering


For rendering print jobs into the page description language for a print device, the v4 print driver model uses the [XPSDrv Render Module](xpsdrv-render-module.md).

The v4 driver model does not use the XPSDrv render module for any other purpose. So drivers for XPS-direct devices do not have to include any filters. But drivers for all other devices must either include filters that render into the device PDL, or they must utilize existing rendering support from a Print Class driver by using the **RequiredClass** directive in the v4 manifest file.

This section provides more information about v4 driver rendering in the following topics.

[V4 Printer Driver Rendering Architecture](v4-driver-rendering-architecture.md)

[Improvements in XPSDrv](improvements-in-xpsdrv.md)

[Standard XPS Filters](standard-xps-filters.md)

[V4 Print Class Driver Rendering](print-class-driver-rendering.md)

## Related topics
[Supported PrintTicket Features](supported-printticket-features.md)  
[V4 Printer Driver](v4-printer-driver.md)  
[XPSDrv Render Module](xpsdrv-render-module.md)  



