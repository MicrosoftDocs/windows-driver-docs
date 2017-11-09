---
title: ScannerState element
description: The required ScannerState element identifies the current state of the scanning portion of the scan device.
MS-HAID:
- 'wsdss\_status\_7161321e-cc96-4337-a365-0f0fc124f983.xml'
- 'image.scannerstate'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 64cd5319-a52d-4ff3-976c-060886381d11
keywords: ["ScannerState element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerState
api_type:
- Schema
---

# ScannerState element


The required **ScannerState** element identifies the current state of the scanning portion of the scan device.

Usage
-----

``` syntax
<wscn:ScannerState>
  text
</wscn:ScannerState>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following string values.

| Value      | Description                                                  |
|------------|--------------------------------------------------------------|
| Idle       | The scanner is available and can start processing a new job. |
| Processing | The scanner is currently processing jobs.                    |
| Stopped    | No jobs can be processed and intervention is needed.         |

 

## Child elements


There are no child elements.

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
<td><p>[<strong>ScannerStatus</strong>](scannerstatus.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>StatusSummary</strong>](statussummary.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

The WSD Scan Service informs a client about changes to the scanner's status by sending a [**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md) event. A client can directly query the scanner's state by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation.

You can both extend and subset the allowed values for this element.

## <span id="see_also"></span>See also


[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerStatus**](scannerstatus.md)

[**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md)

[**StatusSummary**](statussummary.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScannerState%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





