---
title: WSD Scan Service Operation Elements
description: WSD Scan Service Operation Elements
ms.assetid: e06d7683-bec4-49af-bc03-06ef02169999
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WSD Scan Service Operation Elements


This section describes the XML operation elements and operation-specific child elements that the WSD Scan Service schema defines. The client sends a *Xxx***Request** operation element to the WSD Scan Service; the WSD Scan Service responds with the corresponding *Xxx***Response** operation element or appropriate error code.

You cannot extend the operation list within the WSDL Service description. If you want to implement nonstandard operations, they must be a part of a new **portType** type that extends the for the WSD Scan Service definition.

The WSD Scan Service Schema defines the following operation elements and operation-specific child elements:

[**BytesPerLine**](bytesperline.md)

[**CancelJobRequest**](canceljobrequest.md)

[**CancelJobResponse**](canceljobresponse.md)

[**CreateScanJobRequest**](createscanjobrequest.md)

[**CreateScanJobResponse**](createscanjobresponse.md)

[**ElementData for JobElements Element**](elementdata-for-jobelements-element.md)

[**ElementData for ScannerElements Element**](elementdata-for-scannerelements-element.md)

[**GetActiveJobsRequest**](getactivejobsrequest.md)

[**GetActiveJobsResponse**](getactivejobsresponse.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**GetJobElementsResponse**](getjobelementsresponse.md)

[**GetJobHistoryRequest**](getjobhistoryrequest.md)

[**GetJobHistoryResponse**](getjobhistoryresponse.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**GetScannerElementsResponse**](getscannerelementsresponse.md)

[**ImageInformation**](imageinformation.md)

[**JobElements**](jobelements.md)

[**JobHistory**](jobhistory.md)

[**JobSummary**](jobsummary.md)

[**JobToken**](jobtoken.md)

[**MediaBackImageInfo**](mediabackimageinfo.md)

[**MediaFrontImageInfo**](mediafrontimageinfo.md)

[**Name for RequestedElements Element**](name-for-requestedelements-element.md)

[**NumberOfLines**](numberoflines.md)

[**PixelsPerLine**](pixelsperline.md)

[**RequestedElements**](requestedelements.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)

[**RetrieveImageResponse**](retrieveimageresponse.md)

[**ScanData**](scandata.md)

[**ScannerElements**](scannerelements.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)

[**ValidateScanTicketResponse**](validatescanticketresponse.md)

[**ValidationInfo**](validationinfo.md)

[**ValidScanTicket**](validscanticket.md)

[**ValidTicket**](validticket.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WSD%20Scan%20Service%20Operation%20Elements%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




