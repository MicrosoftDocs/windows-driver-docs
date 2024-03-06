---
title: IPrintOemPS COM Interface
description: IPrintOemPS COM Interface
keywords:
- IPrintOemPS
ms.date: 07/17/2023
---

# IPrintOemPS COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintOemPS` COM interface is the means by which the [printer graphics DLL](printer-graphics-dll.md) for Pscript5 communicates with a rendering plug-in. The `IPrintOemPS` interface is implemented by each rendering plug-in.

The following table lists and describes all of the methods provided by the `IPrintOemPS` interface. Rendering plug-ins must define all the listed methods. If a method isn't needed, it can return E_NOTIMPL.

| Method | Description |
|--|--|
| [**IPrintOemPS::Command**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-command) | Allows a rendering plug-in to insert Postscript commands into the print job's data stream. |
| [**IPrintOemPS::DevMode**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-devmode) | Performs operations on a rendering plug-in's private [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) members. |
| [**IPrintOemPS::DisableDriver**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-disabledriver) | Frees resources that were allocated by a rendering plug-in's [**IPrintOemPS::EnableDriver**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enabledriver) method. |
| [**IPrintOemPS::DisablePDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-disablepdev) | Allows a rendering plug-in to delete the private PDEV structure that was allocated by its [**IPrintOemPS::EnablePDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enablepdev) method. |
| [**IPrintOemPS::EnableDriver**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enabledriver) | Allows a rendering plug-in to hook out some graphics DDI functions. This method and **IPrintOemPS::DisableDriver** must be considered as a pair; if one is implemented, the other must be implemented as well. |
| [**IPrintOemPS::EnablePDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enablepdev) | Allows a rendering plug-in to create its own PDEV structure. |
| [**IPrintOemPS::GetInfo**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-getinfo) | (Implementation required.) Returns rendering plug-in identification information. |
| [**IPrintOemPS::PublishDriverInterface**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-publishdriverinterface) | (Implementation required.) Supplies a pointer to the Pscript5 driver's [**IPrintOemDriverPS COM interface**](iprintoemdriverps-com-interface.md), [**IPrintCorePS2 COM interface**](iprintcoreps2-com-interface.md), or [**IPrintCoreHelperPS interface**](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperps) |
| [**IPrintOemPS::ResetPDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-resetpdev) | Allows a rendering plug-in to reset its PDEV structure. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
