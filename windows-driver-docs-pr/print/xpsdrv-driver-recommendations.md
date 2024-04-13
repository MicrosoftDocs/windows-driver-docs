---
title: XPSDrv Driver Recommendations
description: XPSDrv Driver Recommendations
keywords:
- Version 3 XPS drivers WDK XPSDrv , recommendations
ms.date: 01/31/2023
---

# XPSDrv Driver Recommendations

[!include[Print Support Apps](../includes/print-support-apps.md)]

In addition to the [XPSDrv Driver Requirements](xpsdrv-driver-requirements.md), you should consider the following best practices:

- **Use modular GPD or PPD files.** For Unidrv-based or PScript5-based configuration modules, the print driver should provide a separate GPD or PPD file for each filter. Then, a single "parent" print driver GPD or PPD file should reference all of the per-filter GPD or PPD files. Organizing the GPD and PPD files in a modular fashion by filter helps maintain the modularity and reuse of filters in the filter pipeline.

- **Map to public Print Schema keywords.** Whenever possible, you should map all print driver settings and print driver capabilities too their equivalent keywords in the public Print Schema. Mapping print driver settings to public Print Schema keywords makes it easier for applications to adopt new features. This mapping also provides better synchronization of printer settings between print drivers and applications and system.
