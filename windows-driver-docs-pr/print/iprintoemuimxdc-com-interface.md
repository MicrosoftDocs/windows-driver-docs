---
title: IPrintOemUIMXDC COM Interface
description: IPrintOemUIMXDC COM Interface
keywords:
- IPrintOemUIMXDC
ms.date: 07/17/2023
---

# IPrintOemUIMXDC COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintOemUIMXDC` COM interface enables an XPS filter-pipeline driver to view and modify information that the [printer interface DLL](printer-interface-dll.md) for printer configuration manages. The XPS driver accesses this COM interface through a [Unidrv or Pscript plug-in](xpsdrv-driver-options.md).

The following table lists and describes all the methods the `IPrintOemUIMXDC` interface defines.

| Method | Description |
|--|--|
| [**IPrintOEMUIMXDC::AdjustImageableArea**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuimxdc-adjustimageablearea) | Enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of the printable area, including orientation and direction of rotation. |
| [**IPrintOEMUIMXDC::AdjustImageCompression**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuimxdc-adjustimagecompression) | Enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of compression level for JPEG images. |
| [**IPrintOEMUIMXDC::AdjustDPI**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuimxdc-adjustdpi) | Enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of image resolution. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
