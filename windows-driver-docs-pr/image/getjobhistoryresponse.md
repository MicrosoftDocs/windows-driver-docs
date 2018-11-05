---
title: GetJobHistoryResponse element
description: The required GetJobHistoryResponse element returns a summary of completed jobs.
ms.assetid: 85c9edb4-fe6c-49a7-899a-71ce65e38852
keywords: ["GetJobHistoryResponse element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn GetJobHistoryResponse
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# GetJobHistoryResponse element


The required **GetJobHistoryResponse** element returns a summary of completed jobs.

Usage
-----

```xml
<wscn:GetJobHistoryResponse>
  child elements
</wscn:GetJobHistoryResponse>
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
<td><p><a href="jobhistory.md" data-raw-source="[&lt;strong&gt;JobHistory&lt;/strong&gt;](jobhistory.md)"><strong>JobHistory</strong></a></p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service must support the **GetJobHistoryResponse** operation element.

A client can call [**GetJobHistoryRequest**](getjobhistoryrequest.md) to determine the values of job-related variables for previously completed jobs. The WSD Scan Service must respond with a **GetJobHistoryResponse** operation element that contains the information that the client asked for or the appropriate error codes.

The amount of job history that the WSD Scan Service maintains is implementation-specific.

Examples
--------

The following code example shows how to return no job history in response to a client's request for job history.

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
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/GetJobHistory
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheGetJobHistoryRequest</wsa:RelatesTo>
  </soap:Header>

  <soap:Body>
    <wscn:GetJobHistoryResponse>
      <wscn:JobHistory />
    </wscn:GetJobHistoryResponse >
  </soap:Body>
</soap:Envelope>
```

The following code example returns a list of jobs and associated data for the last two completed jobs.

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
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/GetJobHistory
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheGetJobHistoryRequest</wsa:RelatesTo>
  </soap:Header>

  <soap:Body>
    <wscn:GetJobHistoryResponse>
      <wscn:JobHistory>
        <wscn:JobSummary>
          <wscn:JobId>1</wscn:JobId>
          <wscn:JobName>SampleJob 1</wscn:JobName>
          <wscn:JobOriginatingUserName>Joe.Smith</wscn:JobOriginatingUserName>
          <wscn:JobState>Completed</wscn:JobState>
          <wscn:JobStateReasons>
            <wscn:JobStateReason>None</wscn:JobStateReason>
          </wscn:JobStateReasons>
          <wscn:ScansCompleted>4</wscn:ScansCompleted>
        </wscn:JobSummary>
        <wscn:JobSummary>
          <wscn:JobId>2</wscn:JobId>
          <wscn:JobName>Sample Job 2</wscn:JobName>
          <wscn:JobOriginatingUserName>JaneRogers</wscn:JobOriginatingUserName>
          <wscn:JobState>Canceled</wscn:JobState>
          <wscn:JobStateReasons>
            <wscn:JobStateReason>JobCanceledAtDevice</wscn:JobStateReason>
          </wscn:JobStateReasons>
          <wscn:ScansCompleted>1</wscn:ScansCompleted>
        </wscn:JobSummary>
      </wscn:JobHistory>
    </wscn:GetJobHistoryResponse >
  </soap:Body>
</soap:Envelope>
```

## See also


[**GetJobHistoryRequest**](getjobhistoryrequest.md)

[**JobHistory**](jobhistory.md)










