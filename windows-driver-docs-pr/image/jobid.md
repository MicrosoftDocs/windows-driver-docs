---
title: JobId element
description: The required JobId element uniquely identifies a job within a scanner.
ms.assetid: ae9199c1-c45a-4147-b4f0-f37a9a0f1b22
keywords: ["JobId element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobId
api_type:
- Schema
---

# JobId element


The required **JobId** element uniquely identifies a job within a scanner.

Usage
-----

``` syntax
<wscn:JobId>
  text
</wscn:JobId>
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
<td><p>[<strong>CancelJobRequest</strong>](canceljobrequest.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>CreateScanJobResponse</strong>](createscanjobresponse.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>GetJobElementsRequest</strong>](getjobelementsrequest.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobEndState</strong>](jobendstate.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobStatus</strong>](jobstatus.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobSummary</strong>](jobsummary.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>RetrieveImageRequest</strong>](retrieveimagerequest.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service returns a **JobId** element to a client through a [**CreateScanJobResponse**](createscanjobresponse.md) operation element. The client uses the returned **JobId** when it initiates a scan request through the [**RetrieveImageRequest**](retrieveimagerequest.md) operation element.

**JobId** does not need to be globally unique. The WSD Scan Service should not reuse a recently assigned value so that a client does not confuse a current scan job with an older job.

You cannot extend the allowed values for the **JobId** element.

## <span id="see_also"></span>See also


[**CancelJobRequest**](canceljobrequest.md)

[**CreateScanJobResponse**](createscanjobresponse.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**JobEndState**](jobendstate.md)

[**JobStatus**](jobstatus.md)

[**JobSummary**](jobsummary.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobId%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





