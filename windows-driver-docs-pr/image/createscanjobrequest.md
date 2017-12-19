---
title: CreateScanJobRequest element
description: The required CreateScanJobRequest operation prepares a scan device to scan.
ms.assetid: ce3aafe2-71b0-4875-852a-f3ab78684329
keywords: ["CreateScanJobRequest element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn CreateScanJobRequest
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CreateScanJobRequest element


The required **CreateScanJobRequest** operation prepares a scan device to scan.

Usage
-----

``` syntax
<wscn:CreateScanJobRequest>
  child elements
</wscn:CreateScanJobRequest>
```

Attributes
----------

There are no attributes.

Text value
----------

None

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
<td><p>[<strong>DestinationToken</strong>](destinationtoken.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScanIdentifier</strong>](scanidentifier.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScanTicket</strong>](scanticket.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service must support the **CreateScanJobRequest** operation.

The **CreateScanJobRequest** operation is the main mechanism to prepare a scan device to scan the images that are available to it. This operation can be initiated in two different methods. Each method will send different arguments to **CreateScanJobRequest**. The two methods and arguments are:

-   The user selects a destination and pushes the scan button at the device. In this method, the client sends a **CreateScanJobRequest** with the following child elements:
    -   The ScanIdentifier element that the Scan Service returns to the client through ScanAvailableEvent. The Scan Service should check this identifier to ensure that the correct client is requesting the scan after the user has selected the destination.
    -   The DestinationToken element that the WSD Scan Service returns to the client when it subscribed to receive ScanAvailableEvent events. The Scan Service should check that the correct client is requesting the scan by checking this token.
    -   A ScanTicket element to control the processing of the scan. The values in the scan ticket are the default values that are set at the client before the user went to the device to initiate the scan.
-   The user starts an application on the client and acquires an image. In this method, the client sends **CreateScanJobRequest** with only the **ScanTicket** element.

Certain elements within the **CreateScanJobRequest** hierarchy can contain the **MustHonor** Boolean attribute. If **MustHonor** is present and true, the WSD Scan Service must honor the requested element and its value or reject the scan job request. If an unsupported element does not have a **MustHonor** attribute, or if its **MustHonor** attribute is false, the WSD Scan Service must ignore it. If a supported element's **MustHonor** attribute is false, the WSD Scan Service must substitue the requested value with a supported one.

If the client supplies a conflicting combination of elements in the scan job request (such as [**InputSource**](inputsource.md) and [**Resolution**](resolution.md)), the WSD Scan Service must reject the scan job request if the conflicting elements have a **MustHonor** attribute value of true.

The following elements can have the **MustHonor** attribute: [**ColorProcessing**](colorprocessing.md), [**CompressionQualityFactor**](compressionqualityfactor.md), [**ContentType**](contenttype.md), [**Exposure**](exposure.md), [**FilmScanMode**](filmscanmode.md), [**ImagesToTransfer**](imagestotransfer.md), [**InputSize**](inputsize.md), [**InputSource**](inputsource.md), [**MediaSides**](mediasides.md), [**Resolution**](resolution.md), [**Rotation**](rotation.md), [**Scaling**](scaling.md), [**ScanRegionHeight**](scanregionheight.md), [**ScanRegionWidth**](scanregionwidth.md), [**ScanRegionXOffset**](scanregionxoffset.md), and [**ScanRegionYOffset**](scanregionyoffset.md).

This operation can return all of the [**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md). For more information about how to report errors, see [WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md).

**CreateScanJobRequest** can also return the following errors:

-   **ServerErrorNotAcceptingJobs** The server cannot accept a new scan job. This error might occur because the scanner has been put into service mode or because there is a user intervention condition and all the memory buffers have been exhausted. The client can try the unmodified request again at some later point in time with an expectation that the server has become unblocked and the scanner is accepting jobs again.

    | Fault property | Definition                                                                         |
    |----------------|------------------------------------------------------------------------------------|
    | \[Code\]       | soap:Receiver                                                                      |
    | \[Subcode\]    | wscn:ServerErrorNotAcceptingJobs                                                   |
    | \[Reason\]     | The service is temporarily blocked and cannot accept new job or document requests. |
    | \[Detail\]     | None                                                                               |

     

-   **ClientErrorFormatNotSupported** The scanner does not support the supplied Format value.

    | Fault property | Definition                                                                                                                                      |
    |----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
    | \[Code\]       | soap:Sender                                                                                                                                     |
    | \[Subcode\]    | wscn:ClientErrorFormatNotSupported                                                                                                              |
    | \[Reason\]     | The Document Format parameter value is not supported.                                                                                           |
    | \[Detail\]     | Optional. The Scan Service can return a list of supported formats. The data in this element should be of type &lt;wscn:FormatSupportedType&gt;. |

     

-   **ClientErrorInvalidScanIdentifier** The supplied ScanIdentifier value is not currently valid within the scan device.

    | Fault property | Definition                                                 |
    |----------------|------------------------------------------------------------|
    | \[Code\]       | soap:Sender                                                |
    | \[Subcode\]    | wscn:ClientErrorInvalidScanIdentifier                      |
    | \[Reason\]     | The ScanIdentifier parameter value is not currently valid. |
    | \[Detail\]     | None                                                       |

     

-   **ClientErrorInvalidDestinationToken** The supplied DestinationToken value is not valid for the scan device.

    | Fault property | Definition                                                   |
    |----------------|--------------------------------------------------------------|
    | \[Code\]       | soap:Sender                                                  |
    | \[Subcode\]    | wscn:ClientErrorInvalidDestinationToken                      |
    | \[Reason\]     | The DestinationToken parameter value is not currently valid. |
    | \[Detail\]     | None                                                         |

     

-   **ClientErrorNoImagesAvailable** The server can’t accept a new scan job because there is no media to be scanned. For example, this error is generated when a scan job is executed from the Automatic Document Feeder attached to the scanner, and the feeder is empty. The client can try the unmodified request again later, with the expectation that the condition was fixed and the scanner now has media to be scanned.

    | Fault property | Definition                                     |
    |----------------|------------------------------------------------|
    | \[Code\]       | soap:Sender                                    |
    | \[Subcode\]    | wscn:ClientErrorNoImagesAvailable              |
    | \[Reason\]     | The server has no images available to acquire. |
    | \[Detail\]     | None                                           |

     

Examples
--------

The following code example shows a scan job request when the scan is initiated from the scanning device.

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
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/CreateScanJob
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:CreateScanJobRequest>
      <wscn:ScanIdentifier>
        uuid:12e7a983-1034-5428-d298-0016f11097fa
      </wscn:ScanIdentifier>
      <wscn:DestinationToken>
        Dest1234TokenString
      </wscn:DestinationToken>
      <wscn:ScanTicket>
        <wscn:JobDescription>
          <wscn:JobName>Photo Scan</wscn:JobName>
          <wscn:JobOriginatingUserName>RogerSmith</JobOriginatingUserName>
        </wscn:JobDescription>
        <wscn:DocumentParameters>
          <wscn:Format>jfif</wscn:Format>
          <wscn:CompressionQualityFactor>45</wscn:CompressionQualityFactor>
          <wscn:InputSource>Platen</wscn:InputSource>
          <wscn:ContentType>Auto</wscn:ContentType>
          <wscn:InputSize>
            <wscn:DocumentSizeAutoDetect>true</wscn:DocumentSizeAutoDetect>
          </wscn:InputSize>
          <wscn:Scaling wscn:MustHonor="1">
            <wscn:ScalingWidth>125</wscn:ScalingWidth>
            <wscn:ScalingHeight>125</wscn:ScalingHeight>
          </wscn:Scaling>
          <wscn:MediaSides>
            <wscn:MediaFront>
              <wscn:Resolution wscn:MustHonor="1">
                <wscn:Width>300</wscn:Width>
                <wscn:Height>300</wscn:Height>
              </wscn:Resolution>
            </wscn:MediaFront>
          </wscn:MediaSides>
        </wscn:DocumentParameters>
      </wscn:ScanTicket>
    </wscn:CreateScanJobRequest>
  </soap:Body>
</soap:Envelope>
```

The following code example shows a scan job request when the scan is initiated from an application on the client.

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
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/CreateScanJob
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:CreateScanJobRequest>
      <wscn:ScanTicket>
        <wscn:JobDescription>
          <wscn:JobName>Application Scan</wscn:JobName>
          <wscn:JobOriginatingUserName>RogerSmith</JobOriginatingUserName>
        </wscn:JobDescription>
        <wscn:DocumentParameters>
          <wscn:Format>xps</wscn:Format>
          <wscn:ImagesToTransfer>0</wscn:ImagesToTransfer>
          <wscn:InputSource>ADF</wscn:InputSource>
          <wscn:ContentType>Auto</wscn:ContentType>
          <wscn:InputSize>
            <wscn:DocumentSizeAutoDetect>true</wscn:DocumentSizeAutoDetect>
          </wscn:InputSize>
          <wscn:MediaSides>
            <wscn:MediaFront>
              <wscn:ColorProcessing>RGB48</wscn:ColorProcessing>
              <wscn:Resolution>
                <wscn:Width>1200</wscn:Width>
              </wscn:Resolution>
            </wscn:MediaFront>
          </wscn:MediaSides>
        </wscn:DocumentParameters>
        <wscn:DocumentDescription>
          <wscn:DocumentName>Scan001.jpg</DocumentName>
        </wscn:DocumentDescription>
      </wscn:ScanTicket>
    </wscn:CreateScanJobRequest>
  </soap:Body>
</soap:Envelope>
```

## <span id="see_also"></span>See also


[**ColorProcessing**](colorprocessing.md)

[**CompressionQualityFactor**](compressionqualityfactor.md)

[**ContentType**](contenttype.md)

[**CreateScanJobResponse**](createscanjobresponse.md)

[**DestinationToken**](destinationtoken.md)

[**Exposure**](exposure.md)

[**FilmScanMode**](filmscanmode.md)

[**ImagesToTransfer**](imagestotransfer.md)

[**InputSize**](inputsize.md)

[**InputSource**](inputsource.md)

[**MediaSides**](mediasides.md)

[**Resolution**](resolution.md)

[**Rotation**](rotation.md)

[**Scaling**](scaling.md)

[**ScanAvailableEvent**](scanavailableevent.md)

[**ScanIdentifier**](scanidentifier.md)

[**ScanRegionHeight**](scanregionheight.md)

[**ScanRegionWidth**](scanregionwidth.md)

[**ScanRegionXOffset**](scanregionxoffset.md)

[**ScanRegionYOffset**](scanregionyoffset.md)

[**ScanTicket**](scanticket.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20CreateScanJobRequest%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





