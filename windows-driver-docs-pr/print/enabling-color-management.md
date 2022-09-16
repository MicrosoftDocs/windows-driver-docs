---
title: Enable color management
description: Provides information about how to enable color management.
keywords:
- color management WDK print, enabling
ms.date: 09/12/2022
---

# Enable color management

Color management can be enabled by either an application or a printer driver. Applications can enable color management by either of the following two methods:

- Calling [**SetICMMode**](/win32/api/wingdi/nf-wingdi-seticmmode), specifying ICM_ON.

    This method enables system-controlled color management.

- Specifying a [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure when calling **CreateDC** to create a print job, and setting either DMICMMETHOD_SYSTEM, DMICMMETHOD_DRIVER, or DMICMMETHOD_DEVICE in the DEVMODE structure's **dmICMMethod** member.

    This method allows the application to select system-controlled, driver-controlled, or device-controlled color management (assuming the specified control type is supported).

Printer drivers can enable color management by setting either DMICMMETHOD_SYSTEM, DMICMMETHOD_DRIVER, or DMICMMETHOD_DEVICE in the **dmICMMethod** member of the driver's default DEVMODE structure. (An application can override the default setting if supplying a DEVMODE structure for **CreateDC**. Additionally, the driver is responsible for storing the user's choice for color management during execution of the driver's [**DrvDocumentPropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentpropertysheets) function.)
