---
title: ScannerElementsChangeEvent.ElementChanges
description: ScannerElementsChangeEvent.ElementChanges
MS-HAID:
- 'dsm\_ref\_dsd\_801f358c-9433-4f52-98d9-01cb362fa8da.xml'
- 'image.scannerelementschangeevent\_elementchanges'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bf047894-e97d-459d-a126-180e5a725e68
keywords: ["ScannerElementsChangeEvent.ElementChanges"]
---

# ScannerElementsChangeEvent.ElementChanges


The **ElementChanges** element should contain the entire element of the scanner schema that contains changed values. For example, if this event was sent when an automatic document feeder (ADF) was installed, the complete **ScannerDescription** element would be sent. Likewise, if a value changed in the **DefaultScanTicket**, the complete **DefaultScanTicket** element would be sent.

The **ElementChanges** element supports the following sub-elements:

[ScannerElementsChangeEvent.ElementChanges.ScannerDescription](scannerelementschangeevent-elementchanges-scannerdescription.md)

[ScannerElementsChangeEvent.ElementChanges.ScannerConfiguration](scannerelementschangeevent-elementchanges-scannerconfiguration.md)

[ScannerElementsChangeEvent.ElementChanges.DefaultScanTicket](scannerelementschangeevent-elementchanges-defaultscanticket.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScannerElementsChangeEvent.ElementChanges%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




