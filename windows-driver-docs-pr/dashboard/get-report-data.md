---
title: Get report data
description: Query the status of a failure report for Windows driver submission and get the failure details report.
ms.author: shganesh
ms.topic: article
ms.date: 09/01/2018
ms.localizationpriority: medium
---

# Get Report Data

Use this method to query the status of a report using the reportId and fetch the failure details report. The method returns the report download link if ready and status otherwise.

## Request syntax

|Method|Request URI|
|----|----|
|GET|`https://manage.devcenter.microsoft.com/analytics/driver/reportdata/{reportId}?startDate={yyyy-mm-dd}&endDate={yyyy-mm-dd}`|

## Request header

|Header|Type|Description|
|----|----|----|
|Authorization|string|Required. The Azure AD access token in the form **Bearer** *\<token\>*|
|Content-Type|String|Application/JSON|

## Parameters

The following table describes the parameters in the in the Get Failure Details API.

|Parameter|Description|
|----|----|
|reportId|The reportId for the report received on calling the [Schedule Report API](schedule-a-new-report.md)|
|startDate|Start date in `yyyy-mm-dd` format from when the reports generated are requested|
|endDate|End date in `yyyy-mm-dd` format until when the reports generated are requested|

## Response

The response payload is structured as a value array as shown in the following table.

<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Response Code</td>
      <td>200/500/400</td>
    </tr>
    <tr>
      <td>Response Payload</td>
      <td><pre>{
    "data": [
        {
            "ReportDatetime": "2018-01-20T05:35:32",
            "ReportStatus": "Completed",
            "ReportLocation": "https://hardwareanalyticsint.blob.core.windows.net/drivers/Reports/2.txt?sv=2017 .... "
        },
        {
            "ReportDatetime": "2018-01-23T05:35:32",
            "ReportStatus": "Failed",
            "ReportLocation": ""
        }
    ],
    "errors": []
}</pre></td>
    </tr>
  </tbody>
</table>

## Response parameters

The following tables describes the parameters in the response.

|Parameter|Description|
|----|----|
|ReportDatetime|The date when the report ran|
|ReportStatus|The status of the report on ReportDateTime. Values can be  “Completed”, “Pending”, “In Progress”, “Failed”.|
|ReportLocation|The download link of the report if ReportStatus returns “Completed”|

> [!NOTE]
> The ReportLocation link expires in 12 hours. You must use the Get Report Data API to get a new report link if you don’t download the data within the 12-hour window.

You can manage your report templates using the methods described in [Manage report templates and scheduled reports](manage-report-templates-and-scheduled-reports.md).

## See also

- [Analytics Reporting APIs (Swagger )](https://apidocs.microsoft.com/services/analyticsreportingapis)

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
