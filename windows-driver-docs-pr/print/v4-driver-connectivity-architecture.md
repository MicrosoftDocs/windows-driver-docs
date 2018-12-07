---
title: V4 Driver Connectivity Architecture
description: The v4 print driver model provides rich support for bidirectional communications via the Bidirectional Schema, referred to simply as Bidi.
ms.assetid: ED7C4A2D-449E-4271-9348-86EAC03B6E64
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# V4 Driver Connectivity Architecture


The key goal of connectivity components in the v4 print driver model is to provide rich support for bidirectional communications via the Bidirectional Schema, sometimes referred to simply as Bidi.

The v4 print driver model supports a simplified connectivity stack compared to the v3 print driver model.

**Port monitors and language monitors**

Third-party port monitors and language monitors are not supported in the v4 driver model or with print class drivers. The v4 print driver model continues to employ the WSDMon Bidi Extension file format, as well as the SNMP Bidi Extension file format. New in v4 is the ability to support Bidi over USB using the USBMon Bidi Extension XML and JavaScript files.

**Bidirectional schema**

The following table shows the files and the information that you must provide, depending on the features that you want to support and the type of communication protocol that you select for your print device.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Communication type</th>
<th>No extension files</th>
<th>Bidi extension files</th>
<th>Enhanced auto configuration</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>USB</td>
<td><p>The following properties are populated into the Bidi Schema by the port monitor:</p>
<p>\Printer.DeviceInfo:Manufacturer</p>
<p>\Printer.DeviceInfo:ModelName</p>
<p>\Printer.DeviceInfo:IEEE1284DeviceId</p>
<p>\Printer.DeviceInfo:HardwareId</p>
<p>\Printer.DeviceInfo:CompatibleId</p>
<p>\Printer.DeviceInfo:SerialNumber</p></td>
<td><p>You must provide the following files:</p>
- XML Bidi extension file
- JavaScript Bidi extension file</td>
<td>Print device must support this feature and you must provide Bidi extension files.</td>
</tr>
<tr class="even">
<td>WSD</td>
<td>The standard properties from the <a href="https://msdn.microsoft.com/library/windows/hardware/gg463146.aspx" data-raw-source="[WS-Print Specification](https://msdn.microsoft.com/library/windows/hardware/gg463146.aspx)">WS-Print Specification</a> or WS-Print v1.1 Specification are populated into the Bidi Schema by the port monitor.</td>
<td><p>You must provide the following file:</p>
XML Bidi extension file</td>
<td>Print device must support the WS-Print v1.1 protocol.</td>
</tr>
<tr class="odd">
<td>TCP/IP (SNMP)</td>
<td><p>If Port Monitor MIB is implemented, then the following properties are populated into the Bidi Schema by the port monitor:</p>
<p>\Printer.DeviceInfo:Manufacturer</p>
<p>\Printer.DeviceInfo:ModelName</p>
<p>\Printer.DeviceInfo:IEEE1284DeviceId</p>
<p>\Printer.DeviceInfo:HardwareId</p>
<p>\Printer.DeviceInfo:CompatibleId</p>
<p>\Printer.DeviceInfo.NetworkingInfo:PresentationUrl</p>
<p>\Printer.Configuration.Memory:Size</p>
<p>\Printer.Configuration.HardDisk:Installed</p>
<p>\Printer.Configuration.DuplexUnit:Installed</p></td>
<td><p>You must provide the following file:</p>
XML Bidi extension file</td>
<td>Print device must support this feature and you must provide Bidi extension files.</td>
</tr>
</tbody>
</table>

 

For more information, see [Bidirectional Communication Schema](https://msdn.microsoft.com/library/windows/hardware/ff545169.aspx) and [WSDMon port monitors](wsdmon-port-monitor.md). And to read about customizing port monitors to extend the Bidi schema, see [Customizing the Printer Port Monitors](https://msdn.microsoft.com/library/windows/hardware/ff547327.aspx).

## Related topics
[Bidirectional Communication Schema](https://msdn.microsoft.com/library/windows/hardware/ff545169.aspx)  
[Customizing the Printer Port Monitors](https://msdn.microsoft.com/library/windows/hardware/ff547327.aspx)  
[V4 Printer Driver Connectivity](v4-printer-driver-connectivity.md)  
[WSDMon port monitors](wsdmon-port-monitor.md)  



