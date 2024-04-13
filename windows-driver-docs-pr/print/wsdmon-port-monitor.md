---
title: WSDMON Port Monitor
description: WSDMON Port Monitor
keywords:
- print monitors WDK , WSDMON
- WSDMON port monitors WDK
- port monitors WDK print , WSDMON
- Web Services for Devices WDK WIA , port monitor
- WSD compliance WDK print
ms.date: 04/20/2017
---

# WSDMON Port Monitor


The WSDMON port monitor is a printer port monitor that supports printing to network printers that comply with the [Web Services for Devices (WSD) technology](./web-services-for-devices-print-service-schema.md). The WSDMON port monitor listens for WSD events and updates the printer status accordingly. This port monitor is new for Windows Vista.

The WSDMON port monitor can:

-   Discover network printers and install them.

-   Send jobs to WSD printers.

-   Monitor the status and configuration of the WSD printers and update the printer object status accordingly.

-   Respond to bidirectional (bidi) queries for supported [bidi schemas](bidirectional-communication-schema.md).

-   Monitor bidi Schema value changes and send notifications

WSDMON operates in a manner similar to the TCP/IP port monitor ([TCPMON](tcpmon-xcv-interface.md)). The following TCPMON commands are not supported in WSDMON:

AddPort

DeletePort

MonitorUI

WSDMON supports the following Xcv commands:

[CleanupPort](cleanupport.md)

[DeviceID](deviceid2.md)

[PnPXID](pnpxid.md)

[ResetCommunication](resetcommunication.md)

[ServiceID](serviceid.md)

For more information about Web Services for Devices, see the Microsoft Windows SDK documentation.

 

