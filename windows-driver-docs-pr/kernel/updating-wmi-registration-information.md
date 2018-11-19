---
title: Updating WMI Registration Information
description: Updating WMI Registration Information
ms.assetid: d24688e5-bb50-4bce-a4d4-4a3bf886f86d
keywords: ["WMI WDK kernel , registering with WMI", "registering WMI data providers", "data providers WDK WMI", "driver registrations WDK WMI", "event blocks WDK WMI", "blocks WDK WMI", "registering blocks", "updating WMI registration information"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Updating WMI Registration Information





After its initial registration with WMI, a driver changes its registration information by calling [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480) with one of the following actions:

-   WMIREG\_ACTION\_REREGISTER to replace all registration information previously supplied by the driver with new information.

    In response, WMI sends either an [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) request or an [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) request to the driver, with **Parameters.WMI.DataPath** set to WMIREGISTER. (On Windows 98 and Windows 2000, the system sends the **IRP\_MN\_REGINFO** request. On Windows XP and later, the system sends the **IRP\_MN\_REGINFO\_EX** request.)

    The driver supplies WMI with new registration information for all blocks it supports, as described in [Using the WMI Library to Register Blocks](using-the-wmi-library-to-register-blocks.md) and [Handling IRP\_MN\_REGINFO and IRP\_MN\_REGINFO\_EX to Register Blocks](handling-irp-mn-reginfo-and-irp-mn-reginfo-ex-to-register-blocks.md).

-   WMIREG\_ACTION\_UPDATE\_GUIDS to add or remove support for blocks or to change the static instance names of registered blocks.

    In response, WMI sends an [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) or [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) request to the driver, with **Parameters.Wmi.DataPath** set to WMIUPDATE.

    The driver supplies WMI with an updated registration information in which:

    -   The driver sets WMIREG\_FLAG\_REMOVE\_GUID to remove support for that block.

    -   The driver clears WMIREG\_FLAG\_REMOVE\_GUID to add a new block or update an existing block.

    -   The driver sets or clears WMIREG\_FLAG\_INSTANCE\_*XXX* and supplies any necessary instance name information to change a block's static instance names or change it to use dynamic instance names.

-   WMIREG\_ACTION\_DEREGISTER to instruct WMI that the driver will no longer provide WMI information.

    WMI does not send an **IRP\_MN\_REGINFO** or **IRP\_MN\_REGINFO\_EX** request in response to this call, because it requires no further information from the driver. A driver typically deregisters its blocks in response to an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request. Note that the deregister call will block until all WMI IRPs to the device have been completed. If a driver queues WMI IRPs, it must cancel them before calling [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480) to deregister.

 

 




