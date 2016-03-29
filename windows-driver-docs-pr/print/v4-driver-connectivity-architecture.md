---
title: V4 Driver Connectivity Architecture
description: The key goal of connectivity components in the v4 print driver model is to provide rich support for bidirectional communications via the Bidirectional Schema, sometimes referred to simply as Bidi.
ms.assetid: ED7C4A2D-449E-4271-9348-86EAC03B6E64
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
<th align="left">Communication type</th>
<th align="left">No extension files</th>
<th align="left">Bidi extension files</th>
<th align="left">Enhanced auto configuration</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">USB</td>
<td align="left"><p>The following properties are populated into the Bidi Schema by the port monitor:</p>
<p>\Printer.DeviceInfo:Manufacturer</p>
<p>\Printer.DeviceInfo:ModelName</p>
<p>\Printer.DeviceInfo:IEEE1284DeviceId</p>
<p>\Printer.DeviceInfo:HardwareId</p>
<p>\Printer.DeviceInfo:CompatibleId</p>
<p>\Printer.DeviceInfo:SerialNumber</p></td>
<td align="left"><p>You must provide the following files:</p>
- XML Bidi extension file
- JavaScript Bidi extension file</td>
<td align="left">Print device must support this feature and you must provide Bidi extension files.</td>
</tr>
<tr class="even">
<td align="left">WSD</td>
<td align="left">The standard properties from the [WS-Print Specification](http://msdn.microsoft.com/library/windows/hardware/gg463146.aspx) or WS-Print v1.1 Specification are populated into the Bidi Schema by the port monitor.</td>
<td align="left"><p>You must provide the following file:</p>
XML Bidi extension file</td>
<td align="left">Print device must support the WS-Print v1.1 protocol.</td>
</tr>
<tr class="odd">
<td align="left">TCP/IP (SNMP)</td>
<td align="left"><p>If Port Monitor MIB is implemented, then the following properties are populated into the Bidi Schema by the port monitor:</p>
<p>\Printer.DeviceInfo:Manufacturer</p>
<p>\Printer.DeviceInfo:ModelName</p>
<p>\Printer.DeviceInfo:IEEE1284DeviceId</p>
<p>\Printer.DeviceInfo:HardwareId</p>
<p>\Printer.DeviceInfo:CompatibleId</p>
<p>\Printer.DeviceInfo.NetworkingInfo:PresentationUrl</p>
<p>\Printer.Configuration.Memory:Size</p>
<p>\Printer.Configuration.HardDisk:Installed</p>
<p>\Printer.Configuration.DuplexUnit:Installed</p></td>
<td align="left"><p>You must provide the following file:</p>
XML Bidi extension file</td>
<td align="left">Print device must support this feature and you must provide Bidi extension files.</td>
</tr>
</tbody>
</table>

 

For more information, see [Bidirectional Communication Schema](http://msdn.microsoft.com/library/windows/hardware/ff545169.aspx) and [WSDMon port monitors](wsdmon-port-monitor.md). And to read about customizing port monitors to extend the Bidi schema, see [Customizing the Printer Port Monitors](http://msdn.microsoft.com/library/windows/hardware/ff547327.aspx).

## Related topics


[Bidirectional Communication Schema](http://msdn.microsoft.com/library/windows/hardware/ff545169.aspx)

[Customizing the Printer Port Monitors](http://msdn.microsoft.com/library/windows/hardware/ff547327.aspx)

[V4 Printer Driver Connectivity](v4-printer-driver-connectivity.md)

[WSDMon port monitors](wsdmon-port-monitor.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20V4%20Driver%20Connectivity%20Architecture%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





