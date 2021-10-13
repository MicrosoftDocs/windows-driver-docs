---
title: OpenPrinter
description: OpenPrinter
keywords:
- OpenPrinter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# OpenPrinter


When a print queue is opened (by using the `OpenPrinter` function), the print driver is loaded and the following methods of the [IPrintTicketProvider interface](/previous-versions/windows/hardware/drivers/ff554375(v=vs.85)) are called in this order:

1.  [**IPrintTicketProvider::GetSupportedVersions**](/previous-versions/windows/hardware/drivers/ff554371(v=vs.85))

2.  [**IPrintTicketProvider::BindPrinter**](/previous-versions/windows/hardware/drivers/ff554354(v=vs.85))

3.  [**IPrintTicketProvider::QueryDeviceNamespace**](/previous-versions/windows/hardware/drivers/ff554378(v=vs.85))

The methods of the **IPrintTicketProvider** interface in a Unidrv or PScript5 print driver call the **IPrintOemPrintTicketProvider** methods of the each plug-in hosted by the driver. The following illustration and list show how these calls are made when `OpenPrinter` is called.

![diagram illustrating the openprinter calling sequence.](images/ptpcopen-uml.gif)

1.  For each plug-in, call [**IPrintOemPrintTicketProvider::GetSupportedVersions**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemprintticketprovider-getsupportedversions).

2.  For each plug-in, call [**IPrintOemPrintTicketProvider::BindPrinter**](/previous-versions/windows/hardware/drivers/ff553151(v=vs.85)).

3.  For each plug-in, call [**IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemprintticketprovider-querydevicedefaultnamespace).

 

