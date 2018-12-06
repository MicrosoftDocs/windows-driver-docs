---
title: CreateScanJobResponse element
description: The required CreateScanJobResponse element contains the WSD Scan Service's response to a client's scan request.
ms.assetid: a832bdc2-9c47-41da-ac78-a844b8f84ec1
keywords: ["CreateScanJobResponse element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn CreateScanJobResponse
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# CreateScanJobResponse element


The required **CreateScanJobResponse** element contains the WSD Scan Service's response to a client's scan request.

Usage
-----

```xml
<wscn:CreateScanJobResponse>
  child elements
</wscn:CreateScanJobResponse>
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
<td><p><a href="documentfinalparameters.md" data-raw-source="[&lt;strong&gt;DocumentFinalParameters&lt;/strong&gt;](documentfinalparameters.md)"><strong>DocumentFinalParameters</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="imageinformation.md" data-raw-source="[&lt;strong&gt;ImageInformation&lt;/strong&gt;](imageinformation.md)"><strong>ImageInformation</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="jobid.md" data-raw-source="[&lt;strong&gt;JobId&lt;/strong&gt;](jobid.md)"><strong>JobId</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobtoken.md" data-raw-source="[&lt;strong&gt;JobToken&lt;/strong&gt;](jobtoken.md)"><strong>JobToken</strong></a></p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service must support the **CreateScanJobResponse** operation element.

The WSD Scan Service sends a **CreateScanJobResponse** operation element to the client in response to a client's [**CreateScanJobRequest**](createscanjobrequest.md).

If the client has made a valid scan request, the WSD Scan Service must return the following information:

-   A unique [**JobId**](jobid.md) to identify the job. The scanner generates **JobId** in an implementation-defined manner within the defined ranges. The Scan Service must not reuse values that were recently assigned so that clients do not confuse jobs with older jobs.
-   A unique identifier in JobToken. JobToken is paired with JobId to uniquely represent the scan job. JobToken is passed to the Scan Service in the RetrieveImageRequest operation element to enable the scan device to verify that the scan requester actually created the scan job.
-   ImageInformation, which contains information about the resulting image data from a scan made with the ScanTicket that is currently being validated.
-   DocumentFinalParameters, which contains the actual DocumentParameters element that the Scan Service uses for this scan job.

The client must retrieve the actual image data from the Scan Service by sending one or more [**RetrieveImageRequest**](retrieveimagerequest.md) operation elements. The client has 60 seconds to send a **RetrieveImageRequest** operation element after the Scan Service has responded to the client's [**CreateScanJobRequest**](createscanjobrequest.md). If the Scan Service does not receive a **RetrieveImageRequest** within this time, it should abort the job with a [**JobStateReason**](jobstatereason.md) of **JobTimedOut**. If the job consists of multiple documents, this time-out applies between each successive **RetrieveImageRequest/Response** operation.

Examples
--------

The following code example illustrates a WSD Scan Service response to a CreateScanJobRequest.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='http://www.w3.org/2002/12/soap-encoding' >

  <soap:Header>
    <wsa:To>
      http://schemas.xmlsoap.org/ws/2003/03/addressing/role/anonymous
    </wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/CreateScanJob
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheCreateScanJobRequest</wsa:RelatesTo>
  </soap:Header>

  <soap:Body>
    <wscn:CreateScanJobResponse>
      <wscn:JobId>1</wscn:JobId>
      <wscn:JobToken>Job9876TokenString</wscn:JobToken>
      <wscn:ImageInformation>
        <wscn:MediaFrontImageInfo>
          <wscn:PixelsPerLine>900</wscn:PixelsPerLine>
          <wscn:NumberOfLines>1500</wscn:NumberOfLines>
          <wscn:BytesPerLine>113</wscn:BytesPerLine>
        </wscn:MediaFrontImageInfo>
      </wscn:ImageInformation>
      <wscn:DocumentFinalParamters>
        <wscn:Format>jfif</wscn:Format>
        <wscn:CompressionQualityFactor>45</wscn:CompressionQualityFactor>
        <wscn:ImagesToTransfer>0</wscn:ImagesToTransfer>
        <wscn:InputSource>Platen</wscn:InputSource>
        <wscn:ContentType>Auto</wscn:ContentType>
        <wscn:InputSize>
          <wscn:InputMediaSize>
            <wscn:Width wscn:Override="true">8500</wscn:Width>
            <wscn:Height wscn:Override="true">11000</wscn:Height>
          </wscn:InputMediaSize>
        </wscn:InputSize>
        <wscn:Exposure>
          <wscn:ExposureSettings>
            <wscn:Contrast wscn:UsedDefault="true">0</wscn:Contrast>
            <wscn:Brightness wscn:UsedDefault="true">0</wscn:Brightness>
            <wscn:Sharpness wscn:UsedDefault="true">0</wscn:Sharpness>
          </wscn:ExposureSettings>
        </wscn:Exposure>
        <wscn:Scaling>
          <wscn:ScalingWidth>125</wscn:ScalingWidth>
          <wscn:ScalingHeight>125</wscn:ScalingHeight>
        </wscn:Scaling>
        <wscn:Rotation wscn:UsedDefault="true">0</wscn:Rotation>
        <wscn:MediaSides>
          <wscn:MediaFront>
            <wscn:ScanRegion>
              <wscn:ScanRegionXOffset wscn:UsedDefault="true">
                0
              </wscn:ScanRegionXOffset>
              <wscn:ScanRegionYOffset wscn:UsedDefault="true">
                0
              </wscn:ScanRegionYOffset>
              <wscn:ScanRegionWidth wscn:UsedDefault="true">
                8500
              </wscn:ScanRegionWidth>
              <wscn:ScanRegionHeight wscn:UsedDefault="true">
                11000
              </wscn:ScanRegionHeight>
            </wscn:ScanRegion>
            <wscn:ColorProcessing wscn:UsedDefault="true">
              RGB24
            </wscn:ColorProcessing>
            <wscn:Resolution>
              <wscn:Width>300</wscn:Width>
              <wscn:Height>300</wscn:Height>
            </wscn:Resolution>
          </wscn:MediaFront>
        </wscn:MediaSides>
      </wscn:DocumentFinalParamters>
    </wscn:CreateScanJobResponse>
  </soap:Body>
</soap:Envelope>
```

## See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**ImageInformation**](imageinformation.md)

[**JobId**](jobid.md)

[**JobStateReason**](jobstatereason.md)

[**JobToken**](jobtoken.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)

 

 






