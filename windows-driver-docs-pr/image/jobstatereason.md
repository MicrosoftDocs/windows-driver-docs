---
title: JobStateReason element
description: The optional JobStateReason element specifies one reason why a job is in its current state.
MS-HAID:
- 'wsdss\_job\_3deb7502-f57a-4f35-8359-c3b6e50a5857.xml'
- 'image.jobstatereason'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: daaa288b-fa56-4d29-92f6-0283fbbd2fe8
keywords: ["JobStateReason element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobStateReason
api_type:
- Schema
---

# JobStateReason element


The optional **JobStateReason** element specifies one reason why a job is in its current state.

Usage
-----

``` syntax
<wscn:JobStateReason>
  text
</wscn:JobStateReason>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="InvalidScanTicket"></span><span id="invalidscanticket"></span><span id="INVALIDSCANTICKET"></span>InvalidScanTicket</p></td>
<td><p>The job was rejected because the WSD Scan Service could not process the ScanTicket.</p></td>
</tr>
<tr class="even">
<td><p><span id="DocumentFormatError"></span><span id="documentformaterror"></span><span id="DOCUMENTFORMATERROR"></span>DocumentFormatError</p></td>
<td><p>The WSD Scan Service does not support the requested document format.</p></td>
</tr>
<tr class="odd">
<td><p><span id="ImageTransferError"></span><span id="imagetransfererror"></span><span id="IMAGETRANSFERERROR"></span>ImageTransferError</p></td>
<td><p>The data transfer of an image in a job failed. If this error occurs, the WSD Scan Service must abort the job.</p></td>
</tr>
<tr class="even">
<td><p><span id="JobCanceledAtDevice"></span><span id="jobcanceledatdevice"></span><span id="JOBCANCELEDATDEVICE"></span>JobCanceledAtDevice</p></td>
<td><p>The current scan job was canceled at the scan device's front panel.</p></td>
</tr>
<tr class="odd">
<td><p><span id="JobCompletedWithErrors"></span><span id="jobcompletedwitherrors"></span><span id="JOBCOMPLETEDWITHERRORS"></span>JobCompletedWithErrors</p></td>
<td><p>The job completed with at least one error.</p></td>
</tr>
<tr class="even">
<td><p><span id="JobCompletedWithWarnings"></span><span id="jobcompletedwithwarnings"></span><span id="JOBCOMPLETEDWITHWARNINGS"></span>JobCompletedWithWarnings</p></td>
<td><p>The job completed with at least one warning. The job data is expected to be successfully transferred. This warning might indicate that the WSD Scan Service made alterations to the scan ticket to process the job.</p></td>
</tr>
<tr class="odd">
<td><p><span id="JobScanning"></span><span id="jobscanning"></span><span id="JOBSCANNING"></span>JobScanning</p></td>
<td><p>The scanner is digitizing the job data.</p></td>
</tr>
<tr class="even">
<td><p><span id="JobScanningAndTransferring"></span><span id="jobscanningandtransferring"></span><span id="JOBSCANNINGANDTRANSFERRING"></span>JobScanningAndTransferring</p></td>
<td><p>The scanner is digitizing the job data, and the data is being transferred to the client.</p></td>
</tr>
<tr class="odd">
<td><p><span id="JobTimedOut"></span><span id="jobtimedout"></span><span id="JOBTIMEDOUT"></span>JobTimedOut</p></td>
<td><p>The WSD Scan Service ended the job after no RetrieveImageRequest operations followed a CreateScanJobRequest operation in a timely fashion.</p></td>
</tr>
<tr class="even">
<td><p><span id="JobTransferring"></span><span id="jobtransferring"></span><span id="JOBTRANSFERRING"></span>JobTransferring</p></td>
<td><p>The job data is being transferred to the client.</p></td>
</tr>
<tr class="odd">
<td><p><span id="None"></span><span id="none"></span><span id="NONE"></span>None</p></td>
<td><p>The job has no additional information about the state of the job.</p></td>
</tr>
<tr class="even">
<td><p><span id="ScannerStopped"></span><span id="scannerstopped"></span><span id="SCANNERSTOPPED"></span>ScannerStopped</p></td>
<td><p>The scan device is stopped because of an active condition and the job cannot continue until the condition is corrected.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p>[<strong>JobCompletedStateReasons</strong>](jobcompletedstatereasons.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobStateReasons</strong>](jobstatereasons.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

You must support the values that represent conditions that WSD Scan Service implementations can detect. Therefore, you can support only a subset of allowed values if specific **JobStateReason** reasons are undetectable in your implementation.

You can extend the allowed values, but extending this list has implications on the client. The client typically localizes the **JobStateReason** value (as with other string variable values) to the language of the user. However, the client will not recognize a vendor-extended value. The client can display the value that is received "as is", but this value will appear in English, so some users might not understand the value.

## <span id="see_also"></span>See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**JobCompletedStateReasons**](jobcompletedstatereasons.md)

[**JobStateReasons**](jobstatereasons.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20JobStateReason%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





