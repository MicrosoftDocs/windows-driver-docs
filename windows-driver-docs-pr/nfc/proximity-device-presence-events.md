---
title: Proximity device presence events
author: windows-driver-content
description: Proximity device presence events
ms.assetid: 8E0E44D5-E6DD-4385-988E-EFDAA75C6D59
---

# Proximity device presence events


NFP providers enable clients to receive an event whenever an NFP provider detects the arrival or departure of a proximate device (the window of the triggering action). Whenever the NFP provider detects proximity, meaning that the provider can currently communicate with one or more proximate devices, the provider needs to issue a *DeviceArrived* event. When the NFP provider can no longer communicate with any proximate devices, it needs to issue a *DeviceDeparted* event.

The NFP provider also needs to track the presence of proximate devices in order to properly ensure that a published message is only transmitted once while a device is within proximity. These events should be based on the same metric. For an NFP provider that happens to be able to communicate with multiple proximate devices simultaneously, the presence events should be the aggregate of all presence. If the provider supports 0 to N simultaneously proximate devices, the events are only delivered on transitions from 0-to-1 and 1-to-0 currently proximate devices. Note that NFC does NOT support this.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Proximity%20device%20presence%20events%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




