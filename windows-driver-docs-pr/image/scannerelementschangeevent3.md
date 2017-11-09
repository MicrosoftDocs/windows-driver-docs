---
title: ScannerElementsChangeEvent
description: ScannerElementsChangeEvent
MS-HAID:
- 'dsm\_ref\_dsd\_5eca2d17-b791-4f22-b5bf-46667cefef0a.xml'
- 'image.scannerelementschangeevent3'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b6a7d972-2376-499b-b063-88de733a1068
keywords: ["ScannerElementsChangeEvent"]
---

# ScannerElementsChangeEvent


The scanner sends the **ScannerElementsChangeEvent** event to the control point when something has changed in the **ScannerDescription** element, the **ScannerConfiguration** element, the **DefaultScanTicket** element, or an IHV extension in the scanner. The body of the **ScannerElementsChangeEvent** element contains the complete XML data of the element that has changed. If an optional element is missing from returned XML, the implication is that that element is no longer supported by the scanner. For example, such a case might occur after the removal of a film scan option or a duplex scanning mode. The client on the control point is then responsible for comparing the incoming element to previous data to determine which values have changed.

The **ScannerElementsChangeEvent** event supports the following sub-element:

[ScannerElementsChangeEvent.ElementChanges](scannerelementschangeevent-elementchanges.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScannerElementsChangeEvent%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




