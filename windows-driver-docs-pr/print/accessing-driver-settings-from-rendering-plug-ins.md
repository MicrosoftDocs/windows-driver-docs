---
title: Access driver settings from rendering plug-ins
description: Provides information on how to access driver settings from rendering plug-ins.
keywords:
- rendering plug-ins WDK print , accessing driver settings
- status information WDK print plug-ins
ms.date: 01/26/2023
---

# Access driver settings from rendering plug-ins

[!include[Print Support Apps](../includes/print-support-apps.md)]

A rendering plug-in can obtain the current status of printer features and other internal driver information. The following COM interface methods are implemented within Microsoft's printer drivers and can be called by rendering plug-ins.

## Unidrv rendering plug-ins implement the following methods

- [**IPrintOemDriverUni::DrvGetDriverSetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvgetdriversetting)

- [**IPrintOemDriverUni::DrvGetStandardVariable**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvgetstandardvariable)

- [**IPrintOemDriverUni::DrvGetGPDData**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriveruni-drvgetgpddata)

## Pscript5 rendering plug-ins implement the following method

- [**IPrintOemDriverPS::DrvGetDriverSetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverps-drvgetdriversetting)
