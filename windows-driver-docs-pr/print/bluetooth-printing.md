---
title: Bluetooth Printing
description: Bluetooth Printing
ms.assetid: 6c40c142-9b52-4878-a84b-82d411086304
keywords: ["printer drivers WDK , Bluetooth", "Bluetooth WDK , printing", "wireless connectivity WDK printer"]
---

# Bluetooth Printing


If a printing device supports Bluetooth, it should meet the following requirements:

-   If the printing device returns a 1284 ID on its USB or parallel buses, the Bluetooth bus must return a 1284 ID. If, for the purposes of [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) (PnP) and identification, a device returns a 1284 ID on either the parallel or USB buses, the Bluetooth bus must also employ a 1284 ID for PnP identification.
    **Note**  Devices that have never had parallel or USB ports should still contain a 1284 ID. Without a 1284 ID, PnP will not create a print queue.

     

-   The device should return the same 1284 ID that its USB or parallel buses return, so that the Microsoft Windows operating system can properly identify the device and does not confuse it with the same device that is connected through a different bus. If a device on any bus uses a 1284 ID, that same ID should be returned over Bluetooth.

    The Windows operating system does not use the 1284 ID to track a device that is attached through multiple buses. Printers should use the same 1284 ID so that the operating system can load appropriate drivers through a single INF entry. The printer bus drivers create PnP IDs with and without a bus specified. For example, Bluetooth printers get an ID of the form "BTHPRINT\\hpdeskje1234" and of the form "hpdeskje1234". The first form is bus-specific, the second form is bus-neutral. You can create an INF with either of these IDs, depending on whether your driver package is completely bus-neutral or not.

-   The device must support the Bluetooth Hard Copy Replacement Profile (HCRP). For more information about HCRP for Bluetooth, see the [Bluetooth Web site](http://go.microsoft.com/fwlink/p/?linkid=26268).
    **Note**  Microsoft supports the serial port profile (SPP), but authentication is required. However, we recommend the HCRP instead of the SPP because HCRP provides a better user experience.

     

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Bluetooth%20Printing%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




