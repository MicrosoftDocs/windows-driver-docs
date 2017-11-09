---
title: RetrieveImageRequest element
description: The required RetrieveImageRequest operation element contains the client's request to retrieve scan data from the device after a scan job has been created.
MS-HAID:
- 'wsdss\_ops\_d33777fc-19c7-48fe-a197-86fe2a06e86c.xml'
- 'image.retrieveimagerequest'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4f6d6bd0-b323-4f95-b380-2be9cec1ee6e
keywords: ["RetrieveImageRequest element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn RetrieveImageRequest
api_type:
- Schema
---

# RetrieveImageRequest element


The required **RetrieveImageRequest** operation element contains the client's request to retrieve scan data from the device after a scan job has been created.

Usage
-----

``` syntax
<wscn:RetrieveImageRequest>
  child elements
</wscn:RetrieveImageRequest>
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
<td><p>[<strong>DocumentDescription</strong>](documentdescription.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobId</strong>](jobid.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobToken</strong>](jobtoken.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service must support the **RetrieveImageRequest** operation element.

The Scan Service must validate the [**JobId**](jobid.md) and [**JobToken**](jobtoken.md) elements that the client provides to ensure that the job is valid and was created by the client that is requesting the retrieval. If the request is valid, the Scan Service must respond with a [**RetrieveImageResponse**](retrieveimageresponse.md) operation element.

This operation can return all of the [**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md). For more information about how to report errors, see [WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md).

This operation might also return the following errors:

-   **ClientErrorJobIdNotFound**The scanner cannot find a job that matches the JobId value or the JobId value is not within the defined range.

    | Fault property | Definition                         |
    |----------------|------------------------------------|
    | \[Code\]       | soap:Sender                        |
    | \[Subcode\]    | wscn:ClientErrorJobIdNotFound      |
    | \[Reason\]     | The specified JobId was not found. |
    | \[Detail\]     | JobId: Incorrect JobId             |

     

-   **ClientErrorNoImagesAvailable**The scanner does not have any more images available for the client to retrieve.

    | Fault property | Definition                                     |
    |----------------|------------------------------------------------|
    | \[Code\]       | soap:Sender                                    |
    | \[Subcode\]    | wscn:ClientErrorNoImagesAvailable              |
    | \[Reason\]     | The server has no images available to acquire. |
    | \[Detail\]     | None                                           |

     

-   **ClientErrorInvalidJobToken**The supplied JobToken value is not valid for the specified scan JobId.

    | Fault property | Definition                                                          |
    |----------------|---------------------------------------------------------------------|
    | \[Code\]       | soap:Sender                                                         |
    | \[Subcode\]    | wscn:ClientErrorInvalidJobToken                                     |
    | \[Reason\]     | The JobToken parameter value is not valid with the JobId parameter. |
    | \[Detail\]     | None                                                                |

     

-   **ClientErrorJobCancelled**

    | Fault property | Definition                              |
    |----------------|-----------------------------------------|
    | \[Code\]       | soap:Sender                             |
    | \[Subcode\]    | wscn:ClientErrorJobCancelled            |
    | \[Reason\]     | The current scan job has been canceled. |
    | \[Detail\]     | None                                    |

     

Examples
--------

The following code example shows a client request to retrieve image data for the job identified by JobId 1.

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
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/RetrieveImage
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:RetrieveImageRequest>
      <wscn:JobId>1</wscn:JobId>
      <wscn:JobToken>Job9876TokenString</wscn:JobToken>
      <wscn:DocumentDescription>
        <wscn:DocumentName>Scan001.jpg</DocumentName>
      </wscn:DocumentDescription>
    </wscn:RetrieveImageRequest>
  </soap:Body>
</soap:Envelope>
```

## <span id="see_also"></span>See also


[**DocumentDescription**](documentdescription.md)

[**JobId**](jobid.md)

[**JobToken**](jobtoken.md)

[**RetrieveImageResponse**](retrieveimageresponse.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20RetrieveImageRequest%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





