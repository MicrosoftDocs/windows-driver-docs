---
title: GetActiveJobsRequest element
description: The required GetActiveJobsRequest element requests a summary of all currently active jobs in the scan device.
ms.assetid: 4dc7bc64-b62f-4634-8f0e-64039b9f8609
keywords: ["GetActiveJobsRequest element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn GetActiveJobsRequest
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GetActiveJobsRequest element


The required **GetActiveJobsRequest** element requests a summary of all currently active jobs in the scan device.

Usage
-----

``` syntax
<wscn:GetActiveJobsRequest/>
```

Attributes
----------

There are no attributes.

## Child elements


There are no child elements.

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service must support the **GetActiveJobsRequest** operation.

A client calls **GetActiveJobsRequest** to retrieve a list that contains a summary of job-related variables for all currently active scan jobs. The WSD Scan Service must respond with a [**GetActiveJobsResponse**](getactivejobsresponse.md) element that contains the information that the client asked for or the appropriate error codes.

This operation can return all of the [**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md). For more information about how to report errors, see [WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md).

Examples
--------

The following code example shows a request for all active scan jobs.

```
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle=&#39;http://www.w3.org/2002/12/soap-encoding&#39; >

  <soap:Header>
    <wsa:To>AddressofScannerService</wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/GetActiveJobs
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:GetActiveJobsRequest />
  </soap:Body>
</soap:Envelope>
```

## <span id="see_also"></span>See also


[**GetActiveJobsResponse**](getactivejobsresponse.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20GetActiveJobsRequest%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





