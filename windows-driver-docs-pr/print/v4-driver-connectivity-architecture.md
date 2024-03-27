---
title: V4 Driver Connectivity Architecture
description: The v4 print driver model provides rich support for bidirectional communications via the Bidirectional Schema, referred to simply as Bidi.
ms.date: 02/21/2024
---

# V4 driver connectivity architecture

[!include[Print Support Apps](../includes/print-support-apps.md)]

The key goal of connectivity components in the v4 print driver model is to provide rich support for bidirectional communications via the Bidirectional Schema, sometimes referred to simply as Bidi.

The v4 print driver model supports a simplified connectivity stack compared to the v3 print driver model.

## Port monitors and language monitors

Non-Microsoft port monitors and language monitors aren't supported in the v4 driver model or with print class drivers. The v4 print driver model continues to employ the WSDMon Bidi Extension file format, and the Simple Network Management Protocol (SNMP) Bidi Extension file format. New in v4 is the ability to support Bidi over USB using the USBMon Bidi Extension XML and JavaScript files.

## Bidirectional schema

This table shows files and the information that you must provide, depending on the features that you want to support. And the type of communication protocol that you select for your print device.

| Communication type | No extension files | Bidi extension files | Enhanced auto configuration |
|--|--|--|--|
| USB | The following properties are populated into the Bidi Schema with the port monitor:<br><br>\Printer.DeviceInfo:Manufacturer<br><br>\Printer.DeviceInfo:ModelName<br><br>\Printer.DeviceInfo:IEEE1284DeviceId<br><br>\Printer.DeviceInfo:HardwareId<br><br>\Printer.DeviceInfo:CompatibleId<br><br>\Printer.DeviceInfo:SerialNumber | You must provide the following files:<br><br>XML Bidi extension file - JavaScript Bidi extension file | Print device must support this feature and you must provide Bidi extension files. |
| Web Services for Devices (WSD) | The standard properties from the [WS-Print specification](/windows-hardware/design/whitepapers/implementing-web-services-on-devices-for-printing) or WS-Print v1.1 Specification are populated into the Bidi Schema with the port monitor. | You must provide the following file:<br><br>XML Bidi extension file | Print device must support the WS-Print v1.1 protocol. |
| TCP/IP (SNMP) |  |
| If Port Monitor MIB is implemented, then the following properties are populated into the Bidi Schema with the port monitor:<br><br>\Printer.DeviceInfo:Manufacturer<br><br>\Printer.DeviceInfo:ModelName<br><br>\Printer.DeviceInfo:IEEE1284DeviceId<br><br>\Printer.DeviceInfo:HardwareId<br><br>\Printer.DeviceInfo:CompatibleId<br><br>\Printer.DeviceInfo.NetworkingInfo:PresentationUrl<br><br>\Printer.Configuration.Memory:Size<br><br>\Printer.Configuration.HardDisk:Installed<br><br>\Printer.Configuration.DuplexUnit:Installed | You must provide the following file:<br><br>XML Bidi extension file | Print device must support this feature and you must provide Bidi extension files. |

For more information, see [Bidirectional communication schema](./bidirectional-communication-schema.md) and [WSDMon port monitors](wsdmon-port-monitor.md). And to read about customizing port monitors to extend the Bidi schema, see [Customizing the printer port monitors](./customizing-the-printer-port-monitors.md).

## Related articles

[Bidirectional communication schema](./bidirectional-communication-schema.md)  

[Customizing the printer port monitors](./customizing-the-printer-port-monitors.md)  

[V4 printer driver connectivity](v4-printer-driver-connectivity.md)  

[WSDMon port monitors](wsdmon-port-monitor.md)
