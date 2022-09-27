---
title: Print capabilities support in GDI-based monolithic print drivers
description: Provides information about print capabilities support in GDI-based monolithic print drivers.
keywords:
- Print Capabilities WDK , GDI-based monolithic print drivers
- GDI-based monolithic print drivers WDK
- monolithic print drivers WDK
ms.date: 09/07/2022
---

# Print capabilities support in GDI-based monolithic print drivers

To provide complete Print Ticket and Print Capabilities support, GDI-based, monolithic print drivers and [XPSDrv print drivers](xpsdrv-printer-drivers.md) that cannot use the GPD printer interface DLL must implement the [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface. GDI-based, monolithic print drivers are not required to support this interface although this could limit the printer's features that are exposed in the PrintCapabilities document and supported by the PrintTicket document. XPSDrv print drivers, however, must implement **IPrintTicketProvider**.

> [!NOTE]
> For Windows 7, the **MxdcGetPDEVAdjustment** function has new parameters for landscape rotation. For more information, see [**MxdcXDCGetPDEVAdjustment**](/windows-hardware/drivers/ddi/mxdc/nf-mxdc-mxdcgetpdevadjustment).
