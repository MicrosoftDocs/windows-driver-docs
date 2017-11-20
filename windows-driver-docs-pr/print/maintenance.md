---
title: Maintenance
description: Maintenance
MS-HAID:
- 'autocfg\_7b8b5708-dca0-4949-8159-e36afd88c78b.xml'
- 'print.maintenance'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 228759ed-f6de-4680-adf2-ca88b83ff4a0
---

# Maintenance


Schema Path:\\Printer.Maintenance

Node Type:Property

The Maintenance property contains information about the maintenance of the print device.

The Maintenance property contains two child values: **AlignHead** and **CleanHead**.

### <span id="alignhead"></span><span id="ALIGNHEAD"></span> AlignHead

Schema Path:\\Printer.Maintenance.AlignHead

Node Type: Value

Data Type: BIDI\_BOOL

Description: This value represents a command to perform a head alignment procedure on the device. This value is a write-only value. An attempt to read this value should be rejected. If the value is set to 1, the device should perform the command.

### <span id="cleanhead"></span><span id="CLEANHEAD"></span> CleanHead

Schema Path:\\Printer.Maintenance.CleanHead

Node Type: Value

Data Type: BIDI\_BOOL

Description: This value represents a command to perform a head cleaning procedure on the device. This value is a write-only value. An attempt to read this value should be rejected. If the value is set to 1, the device should perform the command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Maintenance%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




