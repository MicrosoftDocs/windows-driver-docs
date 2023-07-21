---
title: IPrintOemUni COM Interface
description: IPrintOemUni COM Interface
keywords:
- IPrintOemUni
ms.date: 07/17/2023
---

# IPrintOemUni COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintOemUni` COM interface is the means by which the [printer graphics DLL](printer-graphics-dll.md) for Unidrv communicates with a rendering plug-in. The `IPrintOemUni` interface is implemented by each rendering plug-in.

The following table lists and describes all of the methods provided by the `IPrintOemUni` interface. Rendering plug-ins must define all listed methods. If a method is not needed, it can simply return E_NOTIMPL.

| Method | Description |
|--|--|
| [**IPrintOemUni::CommandCallback**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-commandcallback) | Allows a rendering plug-in to provide dynamically generated printer commands. |
| [**IPrintOemUni::Compression**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-compression) | Allows a rendering plug-in to provide a customized bitmap compression method. |
| [**IPrintOemUni::DevMode**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-devmode) | Performs operations on a rendering plug-in's private DEVMODE members. |
| [**IPrintOemUni::DisableDriver**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-disabledriver) | Frees resources that were allocated by a rendering plug-in's **IPrintOemUni::EnableDriver** method. |
| [**IPrintOemUni::DisablePDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-disablepdev) | Allows a rendering plug-in to delete the private PDEV structure that was allocated by its [**IPrintOemUni::EnablePDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enablepdev) method. |
| [**IPrintOemUni::DownloadCharGlyph**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-downloadcharglyph) | Allows a rendering plug-in to download a character glyph for a specified soft font to the printer. |
| [**IPrintOemUni::DownloadFontHeader**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-downloadfontheader) | Allows a rendering plug-in to download a font's header information to a printer. |
| [**IPrintOemUni::DriverDMS**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-driverdms) | Allows a rendering plug-in to indicate that it will use a device-managed drawing surface. |
| [**IPrintOemUni::EnableDriver**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enabledriver) | Allows a rendering plug-in to hook out some graphics DDI functions. Note that this method and **IPrintOemUni::DisableDriver** must be considered as a pair; if one is implemented, the other must be implemented as well. |
| [**IPrintOemUni::EnablePDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enablepdev) | Allows a rendering plug-in to create its own PDEV structure. |
| [**IPrintOemUni::FilterGraphics**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-filtergraphics) | Allows a rendering plug-in to modify scan line data and send it to the spooler. |
| [**IPrintOemUni::GetImplementedMethod**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-getimplementedmethod) | (Implementation required.) Allows Unidrv to determine which **IPrintOemUni** interface methods have been implemented by a rendering plug-in. |
| [**IPrintOemUni::GetInfo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-getinfo) | (Implementation required.) Returns a rendering plug-in's identification information. |
| [**IPrintOemUni::HalftonePattern**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-halftonepattern) | Allows a rendering plug-in to create or modify a halftone pattern before it is used in a halftoning operation. |
| [**IPrintOemUni::ImageProcessing**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing) | Allows a rendering plug-in to modify image bitmap data, in order to perform color formatting or halftoning. |
| [**IPrintOemUni::MemoryUsage**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-memoryusage) | Allows a rendering plug-in to specify the amount of memory required for use by its [**IPrintOemUni::ImageProcessing**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing) method. |
| [**IPrintOemUni::OutputCharStr**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-outputcharstr) | Allows a rendering plug-in to control the printing of font glyphs. |
| [**IPrintOemUni::PublishDriverInterface**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-publishdriverinterface) | (Implementation required.) Supplies a pointer to the Unidrv driver's [**IPrintOemDriverUni** COM interface](iprintoemdriveruni-com-interface.md) or [**IPrintCoreHelperUni** interface](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperuni). |
| [**IPrintOemUni::ResetPDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-resetpdev) | Allows a rendering plug-in to reset its PDEV structure. |
| [**IPrintOemUni::SendFontCmd**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-sendfontcmd) | Allows a rendering plug-in to modify a printer's font selection command and then send it to the printer. |
| [**IPrintOemUni::TextOutAsBitmap**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-textoutasbitmap) | Allows a rendering plug-in to create a bitmap image of a text string. |
| [**IPrintOemUni::TTDownloadMethod**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-ttdownloadmethod) | Allows a rendering plug-in to indicate the format that Unidrv should use for a specified TrueType font. |
| [**IPrintOemUni::TTYGetInfo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-ttygetinfo) | Allows a rendering plug-in to supply Unidrv with information relevant to text-only printers. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
