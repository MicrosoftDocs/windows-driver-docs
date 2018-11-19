---
title: WIA Driver Event Support
description: WIA Driver Event Support
ms.assetid: 544c756b-4222-4d59-8393-924d3691e0f8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Driver Event Support





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

 

 




