---
title: WSDMON Port Monitor
description: WSDMON Port Monitor
ms.assetid: fd6b0136-ca6e-4882-b6b9-be868f0dfc18
keywords: ["print monitors WDK , WSDMON", "WSDMON port monitors WDK", "port monitors WDK print , WSDMON", "Web Services for Devices WDK WIA , port monitor", "WSD compliance WDK print"]
---

# WSDMON Port Monitor


The WSDMON port monitor is a printer port monitor that supports printing to network printers that comply with the [Web Services for Devices (WSD) technology](https://msdn.microsoft.com/library/windows/hardware/ff563758). The WSDMON port monitor listens for WSD events and updates the printer status accordingly. This port monitor is new for Windows Vista.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WSDMON%20Port%20Monitor%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




