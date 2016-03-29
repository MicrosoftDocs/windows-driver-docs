---
title: Autoconfiguration Details
description: Autoconfiguration Details
ms.assetid: ba596ce3-724d-45c4-85ee-2486a31a0c01
keywords: ["autoconfiguration WDK printer , about printer autoconfiguration", "printer autoconfiguration WDK printer , about printer autoconfiguration"]
---

# Autoconfiguration Details


Autoconfiguration works by means of bi-directional printer communication (also known as bidi communication) between the print subsystem and the printer. For autoconfiguration to work, the printer must be able to:

-   Understand a query sent by the port monitor.

-   Generate the appropriate response to the query.

To support autoconfiguration, both the printer driver and the port monitor must be modified.

The printer driver must:

-   Be aware of the bidi notification schema.

-   Be able to receive notifications about device configuration changes using the bidi notification schema.

-   Be able to solicit configuration data from the printer using the [bidi communication interfaces](bidirectional-communication-interfaces.md), and specifically the IBidiSpl2 COM interface.

The port monitor must:

-   Support a device protocol capable of querying the printer's configuration.

-   Be able to receive unsolicited status messages from the printer.

-   Convert unsolicited status messages to an appropriate driver notification.

-   Keep all of the device status and configuration data current by means of polling or alerts.

-   Inform the driver or application of any configuration changes in the device.

Autoconfiguration is supported in Windows Vista. However, in a configuration using Point and Print, the port monitor on the server and the driver on the client must both be capable of bidi communication.

This section contains the following topics:

[Autoconfiguration During Device Installation](autoconfiguration-during-device-installation.md)

[Autoconfiguration During Configuration Change](autoconfiguration-during-configuration-change.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autoconfiguration%20Details%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




