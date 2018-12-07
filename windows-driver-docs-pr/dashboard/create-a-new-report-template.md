---
title: Create a new report template
description: Describes how to create a new report template for driver failure reports. Includes REST API information. 
ms.author: shganesh
ms.topic: article
ms.date: 09/01/2018
ms.localizationpriority: medium
---

# Create a new report template

Use this method to create a new reporting template based on your business needs. You can manage your existing reporting templates using the methods listed in [Manage report templates and scheduled reports](manage-report-templates-and-scheduled-reports.md)

## Request syntax

|Method|Request URI|
|----|----|
|POST|`https://manage.devcenter.microsoft.com/analytics/driver/reporttemplate`|

## Request header

|Header|Type|Description|
|----|----|----|
|Authorization|string|Required. The Azure AD access token in the form **Bearer** *\<token\>*|
|Content-Type|string|Application/JSON|

## Request Payload

Define your reporting template in JSON format as specified below.

```json
{
  "view": " IHVDriver", // select “OEMDriver” for OEM Hardware Error data

  "projection": [
    "column1",
    "column2",
    "column3"
  ],

  "dateRange":
    {
      "reportPeriod": "Yesterday" // select date range
    }
  ,

  "condition": {
    "and": [
      {
        "attribute": "column1",
        "operator": "eq",
        "value": "1" // value that you desire to compare
      },
      {
        "condition": {
          "or": [
            {
              "attribute": "column2",
              "operator": "eq",
              "value": "2" //value that you desire to compare
            },
            {
              "attribute": "column3",
              "operator": "eq",
              "value": "3" //value that you desire to compare
            }
          ]
        }
      }
    ],

    "or": []
  },

  "aggregation": {
    "aggregatedColumns": [
      "SUM(column1)",
      "DCOUNT(column2)"
    ],

    "condition": {
      "or": [
        {
          "attribute": "column5",
          "operator": "gt",
          "value": "100" //value that you desire to compare
        }
      ]
    }
  },

  "orderby": [
    {
      "attribute": "column4",
      "sort": "desc"
    }
  ],

  "limit": 100
}
```

## Parameters

This table describes the parameters in the Report Template Creation JSON.

<table>
    <thead>
      <tr>
            <th>Parameter</th>
            <th>Required</th>
            <th>Description</th>
            <th>Allowed values</th>
        </tr>
    </thead>
    <tbody>
    <tr>
        <td>view</td>
        <td>Yes</td>
        <td>Select <b>IHVDriver</b> if you are an IHV/ISV and are looking for a driver failure report.<br/>Select <b>OEMDriver</b> if you are an OEM partner looking for a hardware failure report.</td>
        <td><b>IHVDriver</b> <br/><b>OEMDriver</b></td>
    <tr/>
    <tr>
        <td>projection</td>
        <td>Yes</td>
        <td>List of columns needed in the report. This varies depending on whether the view is <b>IHVDriver</b> or <b>OEMDriver<b> </td>
        <td>List of columns available is below</td>
    </tr>
    <tr>
        <td>reportPeriod</td>
        <td>Yes</td>
        <td>Date Range for which the failure data is requested</td>
        <td>Yesterday<br/>Last3Days<br/>Last7Days<br/>Last10Days<br/>Last15Days<br/>Last30Days<br/>Last60Days<br/>Last90Days</td>
    </tr>
    <tr>
        <td>operator</td>
        <td>No</td>
        <td>Supported set of operators for filter conditions</td>
        <td>IN<br/>EQ<br/>NEQ<br/>LT<br/><br/>GT<br/>LTE<br/>GTE<br/>LIKE</td>
    </tr>
    <tr>
        <td>aggregatedColumns</td>
        <td>No</td>
        <td>Supported set of aggregations on error data</td>
        <td>SUM<br/>AVG<br/>COUNT<br/>DCOUNT<br/>MAX<br/>MIN</td>
    </tr>
    <tr>
        <td>orderby attribute</td>
        <td>No</td>
        <td>Defines ordering of the result set – allows sorting in asc (ascending) or desc (descending) order</td>
        <td>Supported for all available columns </td>
    </tr>
    <tr>
        <td>limit</td>
        <td>No</td>
        <td>Limits the number of rows in response</td>
        <td>Integers &gt;=0<br/>0 indicates all records</td>
    </tr>
    </tbody>
</table>

## Response

The response payload is structured as follows in JSON format.

<table>
    <thead>
        <tr>
           <th>Item</th>
           <th>Description</th>
        </tr>
    </thead>
    <tbody>
      <tr>
        <td>Response code</td>
        <td>201/500/400</td>
      </tr>
    	<tr>
      <td>Response Payload</td>
          <td><pre>{
    &quot;data&quot;: {
        &quot;templateId&quot;: templateId
  },
  &quot;errors&quot;: null  }`</td>
      </tr>
     </tbody>
</table>

## Response parameters

This table contains descriptions of parameters in the response.

|Parameter|Description|
|----|----|
|templateId|This is the template Id of the report template created. This will be used as the input for the Schedule Report API. See [Schedule a new report](schedule-a-new-report.md) for more info.

You can manage your existing reports using the methods shown in [Manage report templates and scheduled reports](manage-report-templates-and-scheduled-reports.md). You can find a list of sample report templates in [Sample report templates](sample-report-templates.md).

## Columns available for projection (IHV and OEM View)

You can select from the following columns in the Windows 10, Windows 8.x, and Windows 7 driver reports for IHVs or ISVs.

<table>
  <thead>
    <tr>
      <th>Column name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ReportId</td>
      <td>ReportId of the report that contains this record</td>
    </tr>
    <tr>
      <td>FailureDate</td>
      <td>Date when the failure occurred in mmddyy format</td>
    </tr>
    <tr>
      <td>FailureDateTime</td>
      <td>Timestamp when the failure occurred</td>
    </tr>
    <tr>
      <td>ApplicationId</td>
      <td>(Available in <i>IHVDriver</i> view only) ApplicationId or the PrivateProductId of the driver submission where the failure occurred</td>
    </tr>
    <tr>
      <td>SubmissionId</td>
      <td>(Available in <i>IHVDriver</i> view only) Submission ID of the driver where the failure occurred</td>
    </tr>
    <tr>
      <td>FailureName</td>
      <td>Name of the failure bucket</td>
    </tr>
    <tr>
      <td>FailureHash</td>
      <td>Value of the failure hash for the failure bucket</td>
    </tr>
    <tr>
      <td>Symbol</td>
      <td>Symbols if present for the failure</td>
    </tr>
    <tr>
      <td>OSVersion</td>
      <td>Version of the operating system where the failure occurred</td>
    </tr>
    <tr>
      <td>OSName</td>
      <td>(Available in <i>IHVDriver</i> view only) - Friendly Name of the Operating System where the failure occurred</td>
    </tr>
    <tr>
      <td>EventType</td>
      <td>Indicates if the failure event was a system failure event or a kernel failure event</td>
    </tr>
    <tr>
      <td>Market</td>
      <td>Market where the failure occurred</td>
    </tr>
    <tr>
      <td>DeviceType</td>
      <td>Device Type where the failure occurred</td>
    </tr>
    <tr>
      <td>DriverName</td>
      <td>Name of the driver that caused the failure</td>
    </tr>
    <tr>
      <td>DriverVersion</td>
      <td>Version of the driver that caused the failure</td>
    </tr>
    <tr>
      <td>Architecture</td>
      <td>Architecture where the failure occurred</td>
    </tr>
    <tr>
      <td>OEMName</td>
      <td>(Available in <i>IHVDriver</i> view only) Name of the OEM where the failure occurred</td>
    </tr>
    <tr>
      <td>OEMModel / Model</td>
      <td>Name of the OEM model where the failure occurred<br/>Called <i>OEMModel</i> in <i>IHVDriver</i> view<br/>Called <i>Model</i> in <i>OEMDriver</i> view
</td>
    </tr>
    <tr>
      <td>FlightRing</td>
      <td>Flight Ring where the failure occurred</td>
      </tr>
    <tr>
      <td>Mode</td>
      <td>Indicates if the failure occurred in kernel mode or user mode</td>
    </tr>
    <tr>
      <td>CPUName</td>
      <td>CPU Name of the device where the crash occurred</td>
    </tr>
    <tr>
      <td>OSSKUType</td>
      <td>Name of the OS SKU where the failure occurred</td>
    </tr>
    <tr>
      <td>ReleaseName</td>
      <td>OS Release name of the OS where the failure occurred</td>
    </tr>
    <tr>
      <td>Baseboard</td>
      <td>(Available in <i>OEMDriver</i> view only) indicates the BaseBoard where the failure occurred</td>
    </tr>
    <tr>
      <td>ModelFamily</td>
      <td>(Available in <i>OEMDriver</i> view only) indicates the ModelFamily where the failure occurred</td>
    </tr>
    <tr>
      <td>CabType</td>
      <td>Indicates if the Cab available is a kernel cab, MINI cab or a FULL cab</td>
    </tr>
    <tr>
      <td>CabIdHash</td>
      <td>Hash of the CabID that can be used to download the cab file using the <a href="https://manage.devcenter.microsoft.com/v1.0/my/analytics/driver/cabdownload" data-raw-source="[CabDownload](https://manage.devcenter.microsoft.com/v1.0/my/analytics/driver/cabdownload)">CabDownload</a> API</td>
    </tr>
    <tr>
      <td>DeviceId</td>
      <td>DeviceId where the failure happened</td>
    </tr>
    <tr>
      <td>HardwareId</td>
      <td>HardwareID for the device where the failure occurred</td>
    </tr>
    <tr>
      <td>CabCollectionTime</td>
      <td>Timestamp when the cab was collected by Microsoft servers</td>
    </tr>
    <tr>
      <td>CabExpirationTime</td>
      <td>Time when the cab will expire and be no longer available for download</td>
    </tr>
    <tr>
      <td>EventCount</td>
      <td>Number of failure events that occurred for that failure hash</td>
    </tr>
  </tbody>
</table>

You can manage your existing reports using the methods shown in [Manage report templates and scheduled reports](manage-report-templates-and-scheduled-reports.md). You can find a list of sample report templates in [Sample report templates](sample-report-templates.md).

## See also

- [Analytics Reporting APIs (Swagger )](https://apidocs.microsoft.com/services/analyticsreportingapis)

- [Schedule a new report](schedule-a-new-report.md)

- [Manage report templates](manage-report-templates-and-scheduled-reports.md)

- [Sample report templates](sample-report-templates.md)

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
