---
title: Microdriver Functions
description: Microdriver Functions
ms.date: 05/01/2023
---

# Microdriver Functions

The WIA Flatbed Driver responds to requests from the WIA service by calling the WIA microdriver functions. These functions must be implemented by every vendor-supplied microdriver and consist of the following:

| Function | Description |
|--|--|
| [**MicroEntry**](/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-microentry) | Responds to commands sent by the WIA Flatbed Driver. |
| [**Scan**](/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-scan) | Reads data from the device and returns the data to the WIA Flatbed Driver. |
| [**SetPixelWindow**](/windows-hardware/drivers/ddi/wiamicro/nf-wiamicro-setpixelwindow) | Sets the area to be scanned. |
