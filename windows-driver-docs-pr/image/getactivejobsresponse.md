---
title: GetActiveJobsResponse element
description: The required GetActiveJobsResponse element returns a summary of job-related variables for all currently active scan jobs.
MS-HAID:
- 'wsdss\_ops\_6b719824-2f18-4b43-b745-5c4ad291ba0b.xml'
- 'image.getactivejobsresponse'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 77efef7f-451d-49f8-80c1-6ab12c98ee7b
keywords: ["GetActiveJobsResponse element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn GetActiveJobsResponse
api_type:
- Schema
---

# GetActiveJobsResponse element


The required **GetActiveJobsResponse** element returns a summary of job-related variables for all currently active scan jobs.

Usage
-----

``` syntax
<wscn:GetActiveJobsResponse>
  child elements
</wscn:GetActiveJobsResponse>
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
<td><p>[<strong>ActiveJobs</strong>](activejobs.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service must support the **GetActiveJobsResponse** operation.

A client can call [**GetActiveJobsRequest**](getactivejobsrequest.md) to determine the values of job-related variables for all currently active scan jobs. The WSD Scan Service must respond with a **GetActiveJobsResponse** element that contains the information that the client asked for or the appropriate error codes.

**GetActiveJobsResponse** contains an [**ActiveJobs**](activejobs.md) element that contains a summary of all jobs.

Examples
--------

The following code example shows how to return the fact that there are no active scan jobs.

```
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle=&#39;http://www.w3.org/2002/12/soap-encoding&#39; >

  <soap:Header>
    <wsa:To>
      http://schemas.xmlsoap.org/ws/2003/03/addressing/role/anonymous
    </wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/GetActiveJobs
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheGetActiveJobsRequest</wsa:RelatesTo>
  </soap:Header>

  <soap:Body>
    <wscn:GetActiveJobsResponse>
      <wscn:ActiveJobs/>
    </wscn:GetActiveJobsResponse >
  </soap:Body>
</soap:Envelope>

```

The following code example reports two active scan jobs.

```
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle=&#39;http://www.w3.org/2002/12/soap-encoding&#39; >

  <soap:Header>
    <wsa:To>
      http://schemas.xmlsoap.org/ws/2003/03/addressing/role/anonymous
    </wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/GetActiveJobs
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheGetActiveJobsRequest</wsa:RelatesTo>
  </soap:Header>

  <soap:Body>
    <wscn:GetActiveJobsResponse>
      <wscn:ActiveJobs>
        <wscn:JobSummary>
          <wscn:JobId>1</wscn:JobId>
          <wscn:JobName>SampleJob 1</wscn:JobName>
          <wscn:JobOriginatingUserName>Joe.Smith</wscn:JobOriginatingUserName>
          <wscn:JobState>Processing</wscn:JobState>
          <wscn:JobStateReasons>
            <wscn:JobStateReason>JobScanning</wscn:JobStateReason>
          </wscn:JobStateReasons>
          <wscn:ScansCompleted>2</wscn:ScansCompleted>
        </wscn:JobSummary>
        <wscn:JobSummary>
          <wscn:JobId>2</wscn:JobId>
          <wscn:JobName>Sample Job 2</wscn:JobName>
          <wscn:JobOriginatingUserName>JaneSmith</wscn:JobOriginatingUserName>
          <wscn:JobState>Pending</wscn:JobState>
          <wscn:JobStateReasons>
            <wscn:JobStateReason>None</wscn:JobStateReason>
          </wscn:JobStateReasons>
          <wscn:ScansCompleted>0</wscn:ScansCompleted>
        </wscn:JobSummary>
      </wscn:ActiveJobs>
    </wscn:GetActiveJobsResponse >
  </soap:Body>
</soap:Envelope>
```

## <span id="see_also"></span>See also


[**ActiveJobs**](activejobs.md)

[**GetActiveJobsRequest**](getactivejobsrequest.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20GetActiveJobsResponse%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





