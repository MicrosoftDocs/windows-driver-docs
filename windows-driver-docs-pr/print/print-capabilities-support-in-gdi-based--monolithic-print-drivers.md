---
title: Print capabilities support in GDI-based monolithic print drivers
description: Provides information about print capabilities support in GDI-based monolithic print drivers.
keywords:
- Print Capabilities WDK , GDI-based monolithic print drivers
- GDI-based monolithic print drivers WDK
- monolithic print drivers WDK
ms.date: 01/30/2023
---

# Print capabilities support in GDI-based monolithic print drivers

[!include[Print Support Apps](../includes/print-support-apps.md)]

To provide complete Print Ticket and Print Capabilities support, GDI-based, monolithic print drivers and [XPSDrv print drivers](xpsdrv-printer-drivers.md) that cannot use the GPD printer interface DLL must implement the [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface. GDI-based, monolithic print drivers are not required to support this interface although this could limit the printer's features that are exposed in the PrintCapabilities document and supported by the PrintTicket document. XPSDrv print drivers, however, must implement **IPrintTicketProvider**.

For Windows 7, the **MxdcGetPDEVAdjustment** function has new parameters for landscape rotation. For more information, see [**MxdcXDCGetPDEVAdjustment**](/windows-hardware/drivers/ddi/mxdc/nf-mxdc-mxdcgetpdevadjustment).
