---
title: Driver Verifier Manager (Windows 2000)
description: Driver Verifier Manager (Windows 2000)
ms.assetid: d1266d2d-2388-472d-a1c4-875ed24913d4
keywords:
- Driver Verifier Manager
- Verifier utility
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Verifier Manager (Windows 2000)


## <span id="ddk_driver_verifier_manager_windows_2000__tools"></span><span id="DDK_DRIVER_VERIFIER_MANAGER_WINDOWS_2000__TOOLS"></span>


The Windows 2000 version of Driver Verifier Manager has five separate panels:

1.  The **Driver Status** screen displays which drivers are loaded and are being verified, and which Driver Verifier options are active. See [Viewing Driver Verifier Settings](viewing-driver-verifier-settings.md) for details.

2.  The **Global Counters** screen displays statistics related to Driver Verifier's actions. Although some of these statistics are related to certain Driver Verifier options, these statistics will be displayed regardless of which options are active. See [Monitoring Global Counters](monitoring-global-counters.md) for details.

3.  The **Pool Tracking** screen displays information about pool allocations. See [Monitoring Individual Counters](monitoring-individual-counters.md) for details.

4.  The **Settings** screen is used to activate and configure Driver Verifier's actions. Changes made from this screen take effect after the next boot. See [Selecting Driver Verifier Options](selecting-driver-verifier-options.md) and [Selecting Drivers to be Verified](selecting-drivers-to-be-verified.md) for details.

5.  The **Volatile Settings** screen is used to alter Driver Verifier's volatile actions. Changes made from this screen take effect immediately. See [Using Volatile Settings](using-volatile-settings.md) for details.

Several screens have a **Refresh Frequency** section on them. This is used to control how often the information displayed on that screen is updated. **Low**, **Medium**, and **High** instruct Driver Verifier to refresh the screen every 1, 5, or 10 seconds, respectively. **Manual** disables automatic updating. The **Refresh Now** button causes the screen to be refreshed immediately.

To exit Driver Verifier Manager, use the **Exit** button. If you have made any changes and have not pressed the corresponding **Apply** button, you will be asked if you wish to save your changes.

 

 





