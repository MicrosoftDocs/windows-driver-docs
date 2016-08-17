---
title: WIA Driver Event Support
description: WIA Driver Event Support
MS-HAID:
- 'WIA\_db\_event\_a066dfd4-3544-4fb3-b70d-1fbd37dad32e.xml'
- 'image.wia\_driver\_event\_support'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 544c756b-4222-4d59-8393-924d3691e0f8
---

# WIA Driver Event Support


## <a href="" id="ddk-wia-driver-event-support-si"></a>


There are two types of event mechanisms that WIA minidrivers can support:

<a href="" id="interrupt-events"></a>Interrupt Events  
The device sends an unsolicited asynchronous notification to the minidriver whenever an action occurs on the device.

<a href="" id="polling-events"></a>Polling Events  
The WIA service periodically asks the minidriver to query the device to determine if any new events have occurred. By default, the WIA service polls the driver every second. This value is configurable in the device's INF file (see [INF Files for WIA Devices](inf-files-for-wia-devices.md) for details).

Only one of these event mechanisms can be used in a WIA minidriver. The interrupt event mechanism is recommended because of increased reliability and performance.

There are three supported event mechanisms.

1.  In Windows Me, an STI event launches the application that has registered for STI events. This application opens the device's TWAIN data source.

2.  In Windows Me, Windows XP and later, a WIA event launches the application that has registered for WIA events. This application uses the WIA service to access the device.

3.  In Windows XP and later, the WIA service translates WIA events into STI events for an application that has registered for STI events. This application uses the TWAIN-to-WIA compatibility layer to access the device through TWAIN.

This section contains the following topics:

[Adding Interrupt Event Support](adding-interrupt-event-support.md)

[Adding Polling Event Support](adding-polling-event-support.md)

[Providing Event Notification](providing-event-notification.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Driver%20Event%20Support%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




