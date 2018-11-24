---
title: Autoconfiguration Details
description: Autoconfiguration Details
ms.assetid: ba596ce3-724d-45c4-85ee-2486a31a0c01
keywords:
- autoconfiguration WDK printer , about printer autoconfiguration
- printer autoconfiguration WDK printer , about printer autoconfiguration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autoconfiguration Details


Autoconfiguration works by means of bi-directional printer communication (also known as bidi communication) between the print subsystem and the printer. For autoconfiguration to work, the printer must be able to:

-   Understand a query sent by the port monitor.

-   Generate the appropriate response to the query.

To support autoconfiguration, both the printer driver and the port monitor must be modified.

The printer driver must:

-   Be aware of the bidi notification schema.

-   Be able to receive notifications about device configuration changes using the bidi notification schema.

-   Be able to solicit configuration data from the printer using the [bidi communication interfaces](https://msdn.microsoft.com/library/windows/hardware/ff545163), and specifically the IBidiSpl2 COM interface.

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

 

 




