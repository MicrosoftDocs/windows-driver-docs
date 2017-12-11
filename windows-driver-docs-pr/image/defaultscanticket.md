---
title: DefaultScanTicket element
description: .
ms.assetid: 1c0f15c8-b14f-4607-8655-36e1397082e6
keywords: ["DefaultScanTicket element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DefaultScanTicket
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DefaultScanTicket element


Usage
-----

``` syntax
<wscn:DefaultScanTicket>
  child elements
</wscn:DefaultScanTicket>
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
<td><p>[<strong>DocumentParameters</strong>](documentparameters.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobDescription</strong>](jobdescription.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


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
<td><p>[<strong>ElementChanges</strong>](elementchanges.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ElementData Element for ScannerElements</strong>](elementdata-for-scannerelements-element.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **DefaultScanTicket** element is an instance of the [**ScanTicket**](scanticket.md) element. **DefaultScanTicket** describes the current set of default values that the WSD Scan Service will apply when a job is created without specific processing elements.

A client can request the scanner's **DefaultScanTicket** element through the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation and then use it without error when requesting a scan job through the [**CreateScanJobRequest**](createscanjobrequest.md) operation. The **DefaultScanTicket** will contain values for all **ScanTicket** options that the device supports.

Examples
--------

The following code example shows a sample DefaultScanTicket.

```
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

## <span id="see_also"></span>See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentParameters**](documentparameters.md)

[**ElementChanges**](elementchanges.md)

[**ElementData Element for ScannerElements**](elementdata-for-scannerelements-element.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**JobDescription**](jobdescription.md)

[**ScanTicket**](scanticket.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20DefaultScanTicket%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





