---
title: ScansCompleted element
description: The required ScansCompleted element specifies the number of images that are scanned.
MS-HAID:
- 'wsdss\_job\_df52277c-d852-40e6-a690-d6a18719916e.xml'
- 'image.scanscompleted'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 71634b6b-1c61-46a0-8cde-01a975c09270
keywords: ["ScansCompleted element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScansCompleted
api_type:
- Schema
---

# ScansCompleted element


The required **ScansCompleted** element specifies the number of images that are scanned.

Usage
-----

``` syntax
<wscn:ScansCompleted>
  text
</wscn:ScansCompleted>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. An integer value from 1 through 2147483648.

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
<td><p>[<strong>JobEndState</strong>](jobendstate.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobStatus</strong>](jobstatus.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobSummary</strong>](jobsummary.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

If a sheet of media is scanned multiple times, the WSD Scan Service must increment the **ScansCompleted** count every time. Each side of a media sheet is scanned in duplex mode, generating two scans in the **ScansCompleted** count.

The **ScansCompleted** count might not be known until the scanner has completed processing the job. The WSD Scan Service must update the **ScansCompleted** element when more exact information is available.

## <span id="see_also"></span>See also


[**JobEndState**](jobendstate.md)

[**JobStatus**](jobstatus.md)

[**JobSummary**](jobsummary.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScansCompleted%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





