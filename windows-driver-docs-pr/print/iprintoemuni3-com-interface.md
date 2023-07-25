---
title: IPrintOemUni3 COM Interface
description: IPrintOemUni3 COM Interface
keywords:
- IPrintOemUni3
ms.date: 07/17/2023
---

# IPrintOemUni3 COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

The `IPrintOemUni3` COM interface contains all the methods of, and extends the capabilities of, the [IPrintOemUni COM Interface](iprintoemuni-com-interface.md) and the [IPrintOemUni2 COM Interface](iprintoemuni2-com-interface.md).

The following table lists and describes all of the methods provided by the `IPrintOemUni3` interface. Rendering plug-ins must define all listed methods. If a method is not needed, it can simply return E_NOTIMPL.

| Method | Description |
|--|--|
| [**IPrintOemUni3::DownloadPattern**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni3-downloadpattern) | Enables a plug-in to download a pattern to a printer. |
| [**IPrintOemUni3::GetPDEVAdjustment**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni3-getpdevadjustment) | Enables a plug-in to override specific **PDEV** settings. |
| [**IPrintOemUni3::SetBandSize**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni3-setbandsize) | Enables a plug-in to specify the desired band size on the printed output. |

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
