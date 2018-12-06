---
title: ScannerElementsChangeEvent element
description: The required ScannerElementsChangeEvent element informs the client that a change has occurred in the scanner.
ms.assetid: 5a3eb934-631d-432b-befa-c67360fe68d1
keywords: ["ScannerElementsChangeEvent element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerElementsChangeEvent
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScannerElementsChangeEvent element


The required **ScannerElementsChangeEvent** element informs the client that a change has occurred in the scanner.

Usage
-----

```xml
<wscn:ScannerElementsChangeEvent>
  child elements
</wscn:ScannerElementsChangeEvent>
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
<td><p><a href="elementchanges.md" data-raw-source="[&lt;strong&gt;ElementChanges&lt;/strong&gt;](elementchanges.md)"><strong>ElementChanges</strong></a></p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service should send a **ScannerElementsChangeEvent** element to the client when an element has changed within [**ScannerDescription**](scannerdescription.md), [**ScannerConfiguration**](scannerconfiguration.md), [**DefaultScanTicket**](defaultscanticket.md), or a vendor extension in the scanner.

The body of **ScannerElementsChangeEvent** must contain an [**ElementChanges**](elementchanges.md) element with the complete XML for the updated element. If an optional element is missing from the returned XML, the WSD Scan Service is indicating to the client that the service no longer supports that element. This change in support could be caused by removal of an option, such as the film scan option or duplex scanning mode. The client must compare the information in **ElementChanges** against previous data to determine which values have changed and must update its internal data store.

Examples
--------

The following code example shows how the device reports updated scanner configuration information because of the installation of a film scanning option.

```xml
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
  xmlns:wse="http://schemas.xmlsoap.org/ws/2004/08/eventing"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='http://www.w3.org/2002/12/soap-encoding'>

  <soap:Header>
    <wsa:To>AddressofEventSink</wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/ScannerElementsChangeEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:ScannerElementsChangeEvent>
      <wscn:ElementChanges>
        <wscn:ScannerConfiguration>

          <wscn:DeviceSettings>
            <wscn:FormatsSupported>
              <wscn:FormatValue>dib</wscn:FormatValue>
              <wscn:FormatValue>exif</wscn:FormatValue>
              <wscn:FormatValue>jpeg2k</wscn:FormatValue>
              <wscn:FormatValue>pdf-a</wscn:FormatValue>
              <wscn:FormatValue>png</wscn:FormatValue>
              <wscn:FormatValue>tiff-single-uncompressed</wscn:FormatValue>
              <wscn:FormatValue>tiff-single-g4</wscn:FormatValue>
              <wscn:FormatValue>tiff-multi-uncompressed</wscn:FormatValue>
              <wscn:FormatValue>tiff-multi-g4</wscn:FormatValue>
              <wscn:FormatValue>xps</wscn:FormatValue>
            </wscn:FormatsSupported>
            <wscn:CompressionQualityFactorSupported>
              <wscn:MinValue>15</wscn:MinValue>
              <wscn:MaxValue>100</wscn:MaxValue>
            </wscn:CompressionQualityFactorSupported>
            <wscn:ContentTypesSupported>
              <wscn:ContentTypeValue>Auto</wscn:ContentTypeValue>
              <wscn:ContentTypeValue>Text</wscn:ContentTypeValue>
              <wscn:ContentTypeValue>Photo</wscn:ContentTypeValue>
              <wscn:ContentTypeValue>Halftone</wscn:ContentTypeValue>
              <wscn:ContentTypeValue>Mixed</wscn:ContentTypeValue>
            </wscn:ContentTypesSupported>
            <wscn:DocumentSizeAutoDetectSupported>
              true
            </wscn:DocumentSizeAutoDetectSupported>
            <wscn:AutoExposureSupported>true</wscn:AutoExposureSupported>
            <wscn:BrightnessSupported>true</wscn:BrightnessSupported>
            <wscn:ContrastSupported>true</wscn:ContrastSupported>
            <wscn:ScalingRangeSupported>
              <wscn:ScalingWidth>
                <wscn:MinValue>50</wscn:MinValue>
                <wscn:MaxValue>500</wscn:MaxValue>
              </wscn:ScalingWidth>
              <wscn:ScalingHeight>
                <wscn:MinValue>50</wscn:MinValue>
                <wscn:MaxValue>500</wscn:MaxValue>
              </wscn:ScalingHeight>
            </wscn:ScalingRangeSupported>
            <wscn:RotationsSupported>
              <wscn:RotationValue>0</wscn:RotationValue>
              <wscn:RotationValue>90</wscn:RotationValue>
              <wscn:RotationValue>180</wscn:RotationValue>
              <wscn:RotationValue>270</wscn:RotationValue>
            </wscn:RotationsSupported>
          </wscn:DeviceSettings>

          <wscn:Platen>
            <wscn:PlatenOpticalResolution>
              <wscn:Width>1200</wscn:Width>
              <wscn:Height>1200</wscn:Height>
            </wscn:PlatenOpticalResolution>
            <wscn:PlatenResolutions>
              <wscn:Widths>
                <wscn:Width>150</wscn:Width>
                <wscn:Width>204</wscn:Width>
                <wscn:Width>300</wscn:Width>
                <wscn:Width>600</wscn:Width>
                <wscn:Width>1200</wscn:Width>
              </wscn:Widths>
              <wscn:Heights>
                <wscn:Height>96</wscn:Height>
                <wscn:Height>150</wscn:Height>
                <wscn:Height>204</wscn:Height>
                <wscn:Height>300</wscn:Height>
                <wscn:Height>600</wscn:Height>
                <wscn:Height>900</wscn:Height>
                <wscn:Height>1200</wscn:Height>
              </wscn:Heights>
            </wscn:PlatenResolutions>
            <wscn:PlatenColor>
              <wscn:ColorEntry>BlackAndWhite1</wscn:ColorEntry>
              <wscn:ColorEntry>Grayscale4</wscn:ColorEntry>
              <wscn:ColorEntry>Grayscale8</wscn:ColorEntry>
              <wscn:ColorEntry>RGB24</wscn:ColorEntry>
              <wscn:ColorEntry>RGB48</wscn:ColorEntry>
              <wscn:ColorEntry>RGBa32</wscn:ColorEntry>
              <wscn:ColorEntry>RGBa64</wscn:ColorEntry>
            </wscn:PlatenColor>
            <wscn:PlatenMinimumSize>
              <wscn:Width>250</wscn:Width>
              <wscn:Height>250</wscn:Height>
            </wscn:PlatenMinimumSize>
            <wscn:PlatenMaximumSize>
              <wscn:Width>11000</wscn:Width>
              <wscn:Height>14000</wscn:Height>
            </wscn:PlatenMaximumSize>
          </wscn:Platen>

          <wscn:ADF>
            <wscn:ADFSupportsDuplex>false</wscn:ADFSupportsDuplex>
            <wscn:ADFFront>
              <wscn:ADFOpticalResolution>
                <wscn:Width>600</wscn:Width>
                <wscn:Height>600</wscn:Height>
              </wscn:ADFOpticalResolution>
              <wscn:ADFResolutions>
                <wscn:Widths>
                  <wscn:Width>150</wscn:Width>
                  <wscn:Width>204</wscn:Width>
                  <wscn:Width>300</wscn:Width>
                  <wscn:Width>600</wscn:Width>
                </wscn:Widths>
                <wscn:Heights>
                  <wscn:Height>96</wscn:Height>
                  <wscn:Height>150</wscn:Height>
                  <wscn:Height>204</wscn:Height>
                  <wscn:Height>300</wscn:Height>
                  <wscn:Height>600</wscn:Height>
                </wscn:Heights>
              </wscn:ADFResolutions>
              <wscn:ADFColor>
                <wscn:ColorEntry>BlackAndWhite1</wscn:ColorEntry>
                <wscn:ColorEntry>Grayscale4</wscn:ColorEntry>
                <wscn:ColorEntry>RGB24</wscn:ColorEntry>
              </wscn:ADFColor>
              <wscn:ADFMinimumSize>
                <wscn:Width>4000</wscn:Width>
                <wscn:Height>6000</wscn:Height>
              </wscn:ADFMinimumSize>
              <wscn:ADFMaximumSize>
                <wscn:Width>8500</wscn:Width>
                <wscn:Height>11000</wscn:Height>
              </wscn:ADFMaximumSize>
            </wscn:ADFFront>
          </wscn:ADF>

          <wscn:Film>
            <wscn:FilmScanModesSupported>
              <wscn:FilmScanModeValue>
                ColorSlideFilm
              </wscn:FilmScanModeValue>
              <wscn:FilmScanModeValue>
                ColorNegativeFilm
              </wscn:FilmScanModeValue>
              <wscn:FilmScanModeValue>
                BlackandWhiteNegativeFilm
              </wscn:FilmScanModeValue>
            </wscn:FilmScanModesSupported>
            <wscn:FilmOpticalResolution>
              <wscn:Width>600</wscn:Width>
              <wscn:Height>600</wscn:Height>
            </wscn:FilmOpticalResolution>
            <wscn:FilmResolutions>
              <wscn:Widths>
                <wscn:Width>150</wscn:Width>
                <wscn:Width>300</wscn:Width>
                <wscn:Width>600</wscn:Width>
              </wscn:Widths>
              <wscn:Heights>
                <wscn:Height>150</wscn:Height>
                <wscn:Height>300</wscn:Height>
                <wscn:Height>600</wscn:Height>
              </wscn:Heights>
            </wscn:FilmResolutions>
            <wscn:FilmColor>
              <wscn:ColorEntry>BlackAndWhite1</wscn:ColorEntry>
              <wscn:ColorEntry>Grayscale4</wscn:ColorEntry>
              <wscn:ColorEntry>RGB24</wscn:ColorEntry>
              <wscn:ColorEntry>RGBa32</wscn:ColorEntry>
            </wscn:FilmColor>
            <wscn:FilmMinimumSize>
              <wscn:Width>1378</wscn:Width>
              <wscn:Height>1378</wscn:Height>
            </wscn:FilmMinimumSize>
            <wscn:FilmMaximumSize>
              <wscn:Width>2756</wscn:Width>
              <wscn:Height>10000</wscn:Height>
            </wscn:FilmMaximumSize>
          </wscn:Film>

        </wscn:ScannerConfiguration>
      </wscn:ElementChanges>
    </wscn:ScannerElementsChangeEvent>
  </soap:Body
</soap:Envelope>
```

## See also


[**DefaultScanTicket**](defaultscanticket.md)

[**ElementChanges**](elementchanges.md)

[**ScannerConfiguration**](scannerconfiguration.md)

[**ScannerDescription**](scannerdescription.md)

 

 






