---
title: Schedule a new report
description: How to schedule a custom error report based on the report template for the Microsoft Hardware Dev Center.
ms.topic: article
ms.author: shganesh
ms.date: 09/01/2018
ms.localizationpriority: medium
---

# Schedule a new report

Once you created a report template successfully and received the *templateID*, use this method to set a frequency and schedule the report to be delivered to you on a regular basis.

## Request syntax

|Method|Request URI|
|----|----|
|POST|`https://manage.devcenter.microsoft.com/analytics/driver/report`|

## Request header

|Header|Type|Description|
|----|----|----|
|Authorization|string|Required. The Azure AD access token in the form **Bearer** *\<token\>*|
|Content-Type|string|Application/JSON|

## Sample Request Payload

Define the schedule at which you need your custom report to run, using the following format:

```json
{
  "templateId": 15, // sample report template id
  "schedule":
    {
      "startTime": "2018-07-24T00:00:00Z",//Date Time in UTC
      "recurrenceInterval": 12, // in hours
      "recurrence": 10    // number of times you want the report to run
    }
  
}
```

## Parameters

This table contains descriptions of parameters in the Schedule Report JSON.

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Required</th>
           <th>Description</th>
        </tr>
    </thead>
    <tbody>
       <tr>
          <td>templateId</td>
          <td>Yes</td>
          <td>The templateId value received as a response to the Create Report Template API</td>
        </tr>
        <tr>
            <td>startTime</td>
            <td>Yes</td>
            <td>Time when the report is expected to run for the first time, in this format:<pre>yyyy-MM-ddTHH:mm:ssZ</pre></td>
        </tr>
        <tr>
           <td>recurrenceInterval</td>
           <td>Yes</td>
           <td>Time interval in hours, after which you expect the report to run again. The minimum time interval allowed is 12 hours.</td>
        </tr>
        <tr>
            <td>recurrence</td>
            <td>Yes</td>
            <td>Number of times you expect this report to run.</td>
        </tr>
        <tr>
           <td>CallbackURL</td>
           <td>No</td>
           <td>URL that needs to be notified once the report data is ready</td>
        </tr>

</tbody>
</table>

## Response

The response payload is structured as follows in JSON format:

<table>
<thead>
    <tr>
      <th>Item</th>
      <th>Description</th>
    </tr>
</thead>
    <tr>
      <td>Response Code</td>
      <td>201/500/400</td>
    </tr>
    <tr>
      <td>Response Payload</td>
      <td><pre>{
    "data": {
        "reportId": reportId
    },
    "errors": []
}
</pre>
      </td>
    </tr>
<tr></tr>
  </tbody>
</table>

## Response parameters

This table describes the parameter in the response.  

|Parameter|Description|
|----|----|
|reportId|Represents the ID of the scheduled report|

If you set up a Callback URL to get notified when the report data is ready, you can call the [Get Report Data](get-report-data.md) method to fetch the report data as soon as it is ready for download.

## See also

- [Analytics Reporting APIs (Swagger)](https://apidocs.microsoft.com/services/analyticsreportingapis)

- [Get Report Data](get-report-data.md)

- [Manage report templates](manage-report-templates-and-scheduled-reports.md)

- [Sample report templates](sample-report-templates.md)

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
