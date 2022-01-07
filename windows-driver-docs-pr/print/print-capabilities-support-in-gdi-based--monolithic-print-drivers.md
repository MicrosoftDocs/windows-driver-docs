---
title: Print Capabilities Support in GDI-based, Monolithic Print Drivers
description: Print Capabilities Support in GDI-based, Monolithic Print Drivers
keywords:
- Print Capabilities WDK , GDI-based monolithic print drivers
- GDI-based monolithic print drivers WDK
- monolithic print drivers WDK
ms.date: 04/20/2017
---

# Print Capabilities Support in GDI-based, Monolithic Print Drivers


To provide complete Print Ticket and Print Capabilities support, GDI-based, monolithic print drivers and [XPSDrv print drivers](xpsdrv-printer-drivers.md) that cannot use the GPD printer interface DLL must implement the [IPrintTicketProvider interface](/previous-versions/windows/hardware/drivers/ff554375(v=vs.85)). GDI-based, monolithic print drivers are not required to support this interface although this could limit the printer's features that are exposed in the PrintCapabilities document and supported by the PrintTicket document. XPSDrv print drivers, however, must implement **IPrintTicketProvider**.

**Note**   For Windows 7, the **MxdcGetPDEVAdjustment** function has new parameters for landscape rotation. For more information, see [**MxdcXDCGetPDEVAdjustment**](/windows-hardware/drivers/ddi/mxdc/nf-mxdc-mxdcgetpdevadjustment).

 

 

