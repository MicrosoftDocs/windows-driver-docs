---
title: Manage report templates and scheduled reports
description: Use these APIs to view and modify existing Windows driver submission reporting templates and manage your scheduled reports 
author: balapv
ms.author: balapv
ms.date: 08/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Manage report templates and scheduled reports

Use these methods to view, modify your existing reporting templates and manage your scheduled reports.

## Request headers

|Header|Type|Description|
|----|----|----|
|Authorization|string|Required. The Azure AD access token in the form **Bearer** *\<token\>*|
|Content-Type|string|Application/JSON|

## View Report Template Definition

Use this method to view the definition of the report template.

<table>
  <thead>
    <tr>
      <th>item</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GET</td>
      <td>https://manage.devcenter.microsoft.com/analytics/driver/reporttemplate/{templateId}</td>
    </tr>
    <tr>
      <td>Response code</td>
      <td>200/500/400</td>
    </tr>
    <tr>
      <td>Response Payload</td>
      <td><pre>{
    "data": {
        "templateId": <templateId>
        " template": "{report template}”,
    "errors": []
}</pre></td>
    </tr>
  </tbody>
</table>

## View all Report Templates available

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
      <td>https://manage.devcenter.microsoft.com/analytics/driver/reporttemplate</td>
    </tr>
    <tr>
      <td>Response code</td>
      <td200/500/400></td>
    </tr>
    <tr>
      <td>Response Payload</td>
      <td><pre>{
    "data": [
        {
            "templateId": <templateid>,
            "template": "{report template}",
            "createdDatetime": "2018-06-24T16:39:46.683",
            "modifiedDatetime": "2018-06-24T16:39:46.683"
        }
        {
            "templateId": <templateid>,
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

## Edit Report Template

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
      <td>https://manage.devcenter.microsoft.com/analytics/driver/reporttemplate/{templateId} </td>
    </tr>
    <tr>
      <td>Sample payload</td>
      <td><pre>{  
   "view":"IHVDriver",
   "projection":[  
      "EventType",
      "DriverName"
   ],
   "dateRange":{  
      "reportPeriod":"Yesterday"
   },
   "condition":{  

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

## View Reports Scheduled

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
      <td>https://manage.devcenter.microsoft.com/analytics/driver/report</td>
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
    "data": [
        {
            "reportId": 2, 
            "templateId": 7,
            "schedule": "{report details}",
            "isActive": true,
            "createdDatetime": "2018-06-24T17:04:18.487",
            "modifiedDatetime": "2018-06-25T08:28:42.063"
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

## Edit Scheduled Report

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
      <td>https://manage.devcenter.microsoft.com/analytics/driver/report/{reportId}</td>
    </tr>
    <tr>
      <td>Payload</td>
      <td><pre>{
   "templateId":<templateid>,
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
        "reportId": <reportId>
    },
    "errors": []
}</pre></td>
    </tr>
  </tbody>
</table>