---
title: Bluetooth Printing
description: Bluetooth Printing
ms.assetid: 6c40c142-9b52-4878-a84b-82d411086304
keywords:
- printer drivers WDK , Bluetooth
- Bluetooth WDK , printing
- wireless connectivity WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bluetooth Printing


If a printing device supports Bluetooth, it should meet the following requirements:

-   If the printing device returns a 1284 ID on its USB or parallel buses, the Bluetooth bus must return a 1284 ID. If, for the purposes of [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) (PnP) and identification, a device returns a 1284 ID on either the parallel or USB buses, the Bluetooth bus must also employ a 1284 ID for PnP identification.
    **Note**  Devices that have never had parallel or USB ports should still contain a 1284 ID. Without a 1284 ID, PnP will not create a print queue.

     

-   The device should return the same 1284 ID that its USB or parallel buses return, so that the Microsoft Windows operating system can properly identify the device and does not confuse it with the same device that is connected through a different bus. If a device on any bus uses a 1284 ID, that same ID should be returned over Bluetooth.

    The Windows operating system does not use the 1284 ID to track a device that is attached through multiple buses. Printers should use the same 1284 ID so that the operating system can load appropriate drivers through a single INF entry. The printer bus drivers create PnP IDs with and without a bus specified. For example, Bluetooth printers get an ID of the form "BTHPRINT\\hpdeskje1234" and of the form "hpdeskje1234". The first form is bus-specific, the second form is bus-neutral. You can create an INF with either of these IDs, depending on whether your driver package is completely bus-neutral or not.

-   The device must support the Bluetooth Hard Copy Replacement Profile (HCRP). For more information about HCRP for Bluetooth, see the [Bluetooth Web site](http://go.microsoft.com/fwlink/p/?linkid=26268).
    **Note**  Microsoft supports the serial port profile (SPP), but authentication is required. However, we recommend the HCRP instead of the SPP because HCRP provides a better user experience.

     

 

 




