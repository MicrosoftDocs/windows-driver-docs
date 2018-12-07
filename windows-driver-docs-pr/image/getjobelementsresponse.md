---
title: GetJobElementsResponse element
description: The required GetJobElementsResponse element returns the job-related information that a client requests.
ms.assetid: b27c1aba-eb5f-4446-ab34-c03a969e954f
keywords: ["GetJobElementsResponse element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn GetJobElementsResponse
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# GetJobElementsResponse element


The required **GetJobElementsResponse** element returns the job-related information that a client requests.

Usage
-----

```xml
<wscn:GetJobElementsResponse>
  child elements
</wscn:GetJobElementsResponse>
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
<td><p><a href="jobelements.md" data-raw-source="[&lt;strong&gt;JobElements&lt;/strong&gt;](jobelements.md)"><strong>JobElements</strong></a></p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service must support the **GetJobElementsResponse** operation.

A client calls **GetJobElementsRequest** to determine the values of job-related elements for the job that [**JobId**](jobid.md) identifies. The WSD Scan Service must respond with a **GetJobElementsResponse** element that contains the requested information. The information that the Scan Service returns must fully comply with the scan job-related portion of the schema.

Examples
--------

In the following code example, the Scan Service returns the job status for the job that JobId 1 identifies.

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
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/GetJobElements
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheGetJobElementsRequest</wsa:RelatesTo>
  </soap:Header>

  <soap:Body>
    <wscn:GetJobElementsResponse>
      <wscn:JobElements>
        <wscn:ElementData wscn:Name="JobStatus" wscn:Valid="true">
          <wscn:JobStatus>
            <wscn:JobId>1</wscn:JobId>
            <wscn:JobState>Completed</wscn:JobState>
            <wscn:JobStateReasons>
              <wscn:JobStateReason>None</wscn:JobStateReason>
            </wscn:JobStateReasons>
            <wscn:ScansCompleted>1</wscn:ScansCompleted>
          </wscn:JobStatus>
        </wscn:ElementData>
      </wscn:JobElements>
    </wscn:GetJobElementsResponse >
  </soap:Body>
</soap:Envelope>
```

## See also


[**GetJobElementsRequest**](getjobelementsrequest.md)

[**JobElements**](jobelements.md)

[**JobId**](jobid.md)










