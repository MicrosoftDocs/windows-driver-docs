---
title: Enabling Color Management
description: Enabling Color Management
keywords:
- color management WDK print , enabling
ms.date: 04/20/2017
---

# Enabling Color Management





Color management can be enabled by either an application or a printer driver. Applications can enable color management by either of the following two methods:

-   Calling **SetICMMode** (described in the Microsoft Windows SDK documentation), specifying ICM\_ON.

    This method enables system-controlled color management.

-   Specifying a [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure when calling **CreateDC** to create a print job, and setting either DMICMMETHOD\_SYSTEM, DMICMMETHOD\_DRIVER, or DMICMMETHOD\_DEVICE in the DEVMODE structure's **dmICMMethod** member.

    This method allows the application to select system-controlled, driver-controlled, or device-controlled color management (assuming the specified control type is supported).

Printer drivers can enable color management by setting either DMICMMETHOD\_SYSTEM, DMICMMETHOD\_DRIVER, or DMICMMETHOD\_DEVICE in the **dmICMMethod** member of the driver's default DEVMODE structure. (An application can override the default setting if supplying a DEVMODE structure for **CreateDC**. Additionally, the driver is responsible for storing the user's choice for color management during execution of the driver's [**DrvDocumentPropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentpropertysheets) function.)

 

