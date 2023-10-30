---
title: Print capabilities in Unidrv and PScript5 print drivers
description: Provides information about print capabilities in Unidrv and PScript5 print drivers.
keywords:
- Print Capabilities WDK, Unidrv
- Print Capabilities WDK, PScript5
ms.date: 01/30/2023
---

# Print capabilities in Unidrv and PScript5 print drivers

[!include[Print Support Apps](../includes/print-support-apps.md)]

The Unidrv and PScript5 minidrivers provide the Print Ticket and Print Capabilities interfaces that are required to support the Print Capabilities feature. These print drivers provide Print Ticket and Print Capabilities support for the features that are described in the [generic printer description (GPD) file](introduction-to-gpd-files.md) or the PostScript printer description (PPD) file, as appropriate, whether the feature information is in the public or private portion of the [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure.

[XPSDrv print drivers](xpsdrv-printer-drivers.md) can also use the Unidrv printer configuration DLL to provide the required support for both the GDI-based printer configuration interface and the [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface. If you use the Unidrv configuration DLL, you can expedite the development of XPSDrv printer drivers for basic-functionality printers or pass-through print drivers.
