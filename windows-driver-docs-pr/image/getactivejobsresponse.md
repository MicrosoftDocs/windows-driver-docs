---
title: GetActiveJobsResponse element
description: The required GetActiveJobsResponse element returns a summary of job-related variables for all currently active scan jobs.
ms.assetid: 77efef7f-451d-49f8-80c1-6ab12c98ee7b
keywords: ["GetActiveJobsResponse element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn GetActiveJobsResponse
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# GetActiveJobsResponse element


The required **GetActiveJobsResponse** element returns a summary of job-related variables for all currently active scan jobs.

Usage
-----

```xml
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
<td><p><a href="activejobs.md" data-raw-source="[&lt;strong&gt;ActiveJobs&lt;/strong&gt;](activejobs.md)"><strong>ActiveJobs</strong></a></p></td>
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

## See also


[**ActiveJobs**](activejobs.md)

[**GetActiveJobsRequest**](getactivejobsrequest.md)










