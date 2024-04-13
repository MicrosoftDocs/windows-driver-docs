---
title: DefaultScanTicket Element
description: Learn about the 'DefaultScanTicket' element. See code examples and view additional available resources.
keywords: ["DefaultScanTicket element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DefaultScanTicket
api_type:
- Schema
ms.date: 04/21/2023
---

# DefaultScanTicket element

## Usage

```xml
<wscn:DefaultScanTicket>
  child elements
</wscn:DefaultScanTicket>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**DocumentParameters**](documentparameters.md) |
| [**JobDescription**](jobdescription.md) |

## Parent elements

| Element |
|--|
| [**ElementChanges**](elementchanges.md) |
| [**ElementData Element for ScannerElements**](elementdata-for-scannerelements-element.md) |

## Remarks

The **DefaultScanTicket** element is an instance of the [**ScanTicket**](scanticket.md) element. **DefaultScanTicket** describes the current set of default values that the WSD Scan Service will apply when a job is created without specific processing elements.

A client can request the scanner's **DefaultScanTicket** element through the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation and then use it without error when requesting a scan job through the [**CreateScanJobRequest**](createscanjobrequest.md) operation. The **DefaultScanTicket** will contain values for all **ScanTicket** options that the device supports.

## Examples

The following code example shows a sample DefaultScanTicket.

```xml
<wscn:DefaultScanTicket>
  <wscn:JobDescription>
    <wscn:JobName>Scan Job</wscn:JobName>
    <wscn:JobOriginatingUserName></wscn:JobOriginatingUserName>
    <wscn:JobInformation>User Selected Scan Job</wscn:JobInformation>
  </wscn:JobDescription>
  <wscn:DocumentParameters>
    <wscn:Format>tiff-multi-uncompressed</wscn:Format>
    <wscn:CompressionQualityFactor>100</wscn:CompressionQualityFactor>
    <wscn:ImagesToTransfer>0</wscn:ImagesToTransfer>
    <wscn:InputSource>Platen</wscn:InputSource>
    <wscn:FilmScanMode>NotApplicable</wscn:FilmScanMode>
    <wscn:ContentType>Auto</wscn:ContentType>
    <wscn:InputSize>
      <wscn:InputMediaSize>
      <wscn:Width>8500</wscn:Width>
      <wscn:Height>11000</wscn:Height>
      </wscn:InputMediaSize>
    </wscn:InputSize>
    <wscn:Exposure>
      <wscn:AutoExposure>true</wscn:AutoExposure>
    </wscn:Exposure>
    <wscn:Scaling>
      <wscn:ScalingWidth>100</wscn:ScalingWidth>
      <wscn:ScalingHeight>100</wscn:ScalingHeight>
    </wscn:Scaling>
    <wscn:Rotation>0</wscn:Rotation>
    <wscn:MediaSides>
      <wscn:MediaFront>
        <wscn:ScanRegion>
          <wscn:ScanRegionXOffset>0</wscn:ScanRegionXOffset>
          <wscn:ScanRegionYOffset>0</wscn:ScanRegionYOffset>
          <wscn:ScanRegionWidth>8500</wscn:ScanRegionWidth>
          <wscn:ScanRegionHeight>11000</wscn:ScanRegionHeight>
        </wscn:ScanRegion>
        <wscn:ColorProcessing>RGB24</wscn:ColorProcessing>
        <wscn:Resolution>
          <wscn:Width>600</wscn:Width>
          <wscn:Height>600</wscn:Height>
        </wscn:Resolution>
      </wscn:MediaFront>
    </wscn:MediaSides>
  </wscn:DocumentParameters>
</wscn:DefaultScanTicket>
```

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentParameters**](documentparameters.md)

[**ElementChanges**](elementchanges.md)

[**ElementData Element for ScannerElements**](elementdata-for-scannerelements-element.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**JobDescription**](jobdescription.md)

[**ScanTicket**](scanticket.md)
