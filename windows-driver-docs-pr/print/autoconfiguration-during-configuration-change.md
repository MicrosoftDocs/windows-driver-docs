---
title: Autoconfiguration During Configuration Change
description: Autoconfiguration During Configuration Change
ms.assetid: 0294d34d-06e4-4e57-8f4d-4100ab482852
keywords: ["autoconfiguration WDK printer , during configuration changes", "printer autoconfiguration WDK printer , during configuration changes"]
---

# Autoconfiguration During Configuration Change


After the device has been installed, the port monitor is responsible for keeping the configuration data current either by sending events or by polling. Whenever a driver or application is interested in the current configuration of the device, it can use the [bidi communication interfaces](bidirectional-communication-interfaces.md) and the [bidi communications schema](bidi-communications-schema-reference.md) to query the port monitor for this information.

The following figure shows the data flow in autoconfiguration when the device's configuration changes:

![diagram illustrating the data flow in autoconfiguration when the device's configuration changes](images/autocfgcfgchange.png)

1.  When the device configuration changes, a device that uses the Web Services Eventing (WS-Eventing) protocol notifies the print subsystem that its status has changed, but does not describe the specific change. The standard TCP/IP port monitor polls devices that do not support WS-Eventing.

2.  The port monitor generates a notification that the device configuration has changed and sends the notification to the spooler.

3.  The spooler sends a notification to the driver by calling `DrvPrinterEvent` and passing PRINTER\_EVENT\_CONFIGURATION\_UPDATE in the call. This function call serves to inform the driver that the configuration of the device has changed.

The driver can determine when there is a change in configuration for the device, because the notification message carries the changed value (the schema is defined in the Bidi Notification design specification). However, if the notification is too large to be sent through the notification mechanism, the notification will have one or more ReducedSchema instances, each of which indicates that a device characteristic has changed, but without any details of its new value.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autoconfiguration%20During%20Configuration%20Change%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




