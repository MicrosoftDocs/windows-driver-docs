---
title: Manage report templates and scheduled reports
description: Use these APIs to view and modify existing Windows driver submission reporting templates and manage your scheduled reports 
ms.topic: article
ms.author: shganesh
ms.date: 09/01/2018
ms.localizationpriority: medium
---

# Manage report templates and scheduled reports

Use these methods to view, modify your existing reporting templates and manage your scheduled reports.

## Request headers

|Header|Type|Description|
|----|----|----|
|Authorization|string|Required. The Azure AD access token in the form **Bearer** *\<token\>*|
|Content-Type|string|Application/JSON|

## View a definition of a report template

Use this method to view the definition of the report template.

<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GET</td>
      <td><pre>https://manage.devcenter.microsoft.com/analytics/driver/reporttemplate/{templateId}</pre></td>
    </tr>
    <tr>
      <td>Response code</td>
      <td>200/500/400</td>
    </tr>
    <tr>
      <td>Response Payload</td>
      <td><pre>{
    "data": {
        "templateId": &lt;templateid&gt;
        " template": "{report template}”,
    "errors": []
}</pre></td>
    </tr>
  </tbody>
</table>

## View all available report templates

Use this method to view all report templates you created for your account.

<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GET</td>
      <td><pre>https://manage.devcenter.microsoft.com/analytics/driver/reporttemplate</pre></td>
    </tr>
    <tr>
      <td>Response code</td>
      <td>200/500/400</td>
    </tr>
    <tr>
      <td>Response Payload</td>
      <td><pre>{
    "data": [
        {
            "templateId": &lt;templateid&gt;,
            "template": "{report template}",
            "createdDatetime": "2018-06-24T16:39:46.683",
            "modifiedDatetime": "2018-06-24T16:39:46.683"
        }
        {
            "templateId": &lt;templateid&gt;,
            "template": "{report template}",
            "createdDatetime": "2018-06-27T14:09:27.243",
            "modifiedDatetime": "2018-06-27T14:09:32.733"
        }
],
    "errors": []
}
</pre></td>
    </tr>
  </tbody>
</table>

## Edit a report template

Use this method to edit an existing report template.

<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>POST</td>
      <td><pre>https://manage.devcenter.microsoft.com/analytics/driver/reporttemplate/{templateId}</pre></td>
    </tr>
    <tr>
      <td>Sample payload</td>
      <td><pre>{<br/>   &quot;view&quot;:&quot;IHVDriver&quot;,
   &quot;projection&quot;:[<br/>      &quot;EventType&quot;,
      &quot;DriverName&quot;
   ],
   &quot;dateRange&quot;:{<br/>      &quot;reportPeriod&quot;:&quot;Yesterday&quot;
   },
   &quot;condition&quot;:{  

   },
   "aggregation":{  
      "aggregatedColumns":[  
         "sum(EventCount)"
      ]
   }
}</pre></td>
    </tr>
    <tr>
      <td>Response code</td>
      <td>201/500/400</td>
    </tr>
    <tr>
      <td>Response Payload</td>
      <td><pre>{
    "data": {
        "templateId": “templateId”
    },
    "errors": []
}</pre></td>
    </tr>
  </tbody>
</table>

## View the scheduled reports

Use this method to view the list of scheduled reports.

<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Get</td>
      <td><pre>https://manage.devcenter.microsoft.com/analytics/driver/report</pre></td>
    </tr>
    <tr>
      <td>Payload</td>
      <td>None</td>
    </tr>
    <tr>
      <td>Response code</td>
      <td>201/500/400</td>
    </tr>
    <tr>
      <td>Sample Response Payload</td>
      <td><pre>{
    &quot;data&quot;: [
        {
            &quot;reportId&quot;: 2,
            &quot;templateId&quot;: 7,
            &quot;schedule&quot;: &quot;{report details}&quot;,
            &quot;isActive&quot;: true,
            &quot;createdDatetime&quot;: &quot;2018-06-24T17:04:18.487&quot;,
            &quot;modifiedDatetime&quot;: &quot;2018-06-25T08:28:42.063&quot;
        },

                  {
            "reportId": 4,
            "templateId": 12,
            "schedule": "{report details}",
            "isActive": true,
            "createdDatetime": "2018-06-28T10:11:44.873",
            "modifiedDatetime": "2018-06-28T10:30:27.93"
        }
           ],
    "errors": []
}
</pre></td>
    </tr>
  </tbody>
</table>

## Edit a scheduled report

Use this method to edit an existing scheduled report.

<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>POST</td>
      <td><pre>https://manage.devcenter.microsoft.com/analytics/driver/report/{reportId}</pre></td>
    </tr>
    <tr>
      <td>Payload</td>
      <td><pre>{
   "templateId":&lt;templateid&gt;,
   "Schedule":{
      "StartTime":"2018-07-24T00:00:00Z", //Datetime in UTC
      "RecurrenceInterval":12, // in hours
      "Recurrence":2
   }
}</pre></td>
    </tr>
    <tr>
      <td>Response code</td>
      <td>201/500/400</td>
    </tr>
    <tr>
      <td>Response Payload</td>
      <td><pre>{
    "data": {
        "reportId": &lt;reportId&gt;
    },
    "errors": []
}</pre></td>
    </tr>
  </tbody>
</table>

## Pause a report

Use this method to pause a scheduled report.

<table>
  <tbody>
    <tr>
      <td>POST</td>
      <td><pre>https://manage.devcenter.microsoft.com/analytics/driver/report/pause/{reportId}</pre></td>
    </tr>
    <tr>
      <td>Response Code</td>
      <td>201/500/400</td>
    </tr>
    <tr>
      <td>Response Payload</td>
      <td><pre>{
    "data": {
        "reportId": &lt;reportId&gt;
    },
    "errors": []
}</pre></td>
    </tr>
  </tbody>
</table>

## Resume a report

Use this method to resume a scheduled report.

<table>
  <tbody>
    <tr>
      <td>POST</td>
      <td><pre>https://manage.devcenter.microsoft.com/analytics/driver/report/resume/{reportId}</pre></td>
    </tr>
    <tr>
      <td>Response Code</td>
      <td>201/500/400</td>
    </tr>
    <tr>
      <td>Response Payload</td>
      <td><pre>{
    "data": {
        "reportId": &lt;reportId&gt;
    },
    "errors": []
}</pre></td>
    </tr>
  </tbody>
</table>

## See also

- [Analytics Reporting APIs (Swagger )](https://apidocs.microsoft.com/services/analyticsreportingapis)

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
