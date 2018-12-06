---
title: RetrieveImageRequest element
description: The required RetrieveImageRequest operation element contains the client's request to retrieve scan data from the device after a scan job has been created.
ms.assetid: 4f6d6bd0-b323-4f95-b380-2be9cec1ee6e
keywords: ["RetrieveImageRequest element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn RetrieveImageRequest
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# RetrieveImageRequest element


The required **RetrieveImageRequest** operation element contains the client's request to retrieve scan data from the device after a scan job has been created.

Usage
-----

```xml
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
<td><p><a href="documentdescription.md" data-raw-source="[&lt;strong&gt;DocumentDescription&lt;/strong&gt;](documentdescription.md)"><strong>DocumentDescription</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobid.md" data-raw-source="[&lt;strong&gt;JobId&lt;/strong&gt;](jobid.md)"><strong>JobId</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="jobtoken.md" data-raw-source="[&lt;strong&gt;JobToken&lt;/strong&gt;](jobtoken.md)"><strong>JobToken</strong></a></p></td>
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

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='http://www.w3.org/2002/12/soap-encoding' >

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

## See also


[**DocumentDescription**](documentdescription.md)

[**JobId**](jobid.md)

[**JobToken**](jobtoken.md)

[**RetrieveImageResponse**](retrieveimageresponse.md)

 

 






