---
title: GetJobElementsRequest element
description: The required GetJobElementsRequest element requests information that is related to the job that the JobId element identifies.
MS-HAID:
- 'wsdss\_ops\_60b7bca4-d78a-42c6-981e-bab2cecb9d3d.xml'
- 'image.getjobelementsrequest'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ba8260f4-300f-447e-ad62-d2e4fa2811ef
keywords: ["GetJobElementsRequest element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn GetJobElementsRequest
api_type:
- Schema
---

# GetJobElementsRequest element


The required **GetJobElementsRequest** element requests information that is related to the job that the [**JobId**](jobid.md) element identifies.

Usage
-----

``` syntax
<wscn:GetJobElementsRequest>
  child elements
</wscn:GetJobElementsRequest>
```

Attributes
----------

There are no attributes.

## Child elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>JobId</strong>](jobid.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>RequestedElements</strong>](requestedelements.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service must support the **GetJobElementsRequest** operation.

A client can call **GetJobElementsRequest** to determine the values of job-related elements for the job that [**JobId**](jobid.md) identifies. The WSD Scan Service must respond with a **GetJobElementsResponse**. The information that the Scan Service returns must fully comply with the scan job-related portion of the schema.

This operation can return all of the [**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md). For more information about how to report errors, see [WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md).

**GetJobElementsRequest** might also return the following errors.

-   **ClientErrorJobIdNotFound**

    The scanner cannot find a job that matches the JobId value or the JobId value is not within the defined range.

    | Fault property | Definition                         |
    |----------------|------------------------------------|
    | \[Code\]       | soap:Sender                        |
    | \[Subcode\]    | wscn:ClientErrorJobIdNotFound      |
    | \[Reason\]     | The specified JobId was not found. |
    | \[Detail\]     | JobId: Incorrect JobId             |

     

Examples
--------

The following code example requests the status of the scan job that Fault property 1 identifies.

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
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/GetJobElements
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:GetJobElements>
      <wscn:JobId>1</wscn:JobId>
      <wscn:RequestedElements>
        <wscn:Name>JobStatus</wscn:Name>
      </wscn:RequestedElements>
    </wscn:GetJobElements>
  </soap:Body>
</soap:Envelope>
```

## <span id="see_also"></span>See also


[**GetJobElementsResponse**](getjobelementsresponse.md)

[**JobId**](jobid.md)

[**RequestedElements**](requestedelements.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20GetJobElementsRequest%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





