---
title: Sample report templates
description: Compilation of sample report templates for Windows driver submission failure reports. Code is REST APIs and JSON formatting. 
ms.topic: article
ms.author: shganesh
ms.date: 09/01/2018
ms.localizationpriority: medium
---

# Sample report templates

This article contains several report templates that cover common submissions failures for common business needs. You can reuse any or these templates or customize them based on your business needs.

## Request syntax

|Method|Request URI|
|----|----|
|POST|`https://manage.devcenter.microsoft.com/analytics/driver/reporttemplate`|

## Request headers

|Header|Type|Description|
|----|----|----|
|Authorization|string|Required. The Azure AD access token in the form **Bearer** *\<token\>*|
|Content-Type|string|Application/JSON|

## Sample 1:  Show all available columns for *IHV failure* details for the last 7 days

The following API request payload lists all available columns in the IHV failure report and sets the reportPeriod to the last seven days.

```json
{
   "view":"IHVDriver",
   "projection":[
      "ReportId",
      "FailureDate",
      "FailureDateTime",
      "ApplicationId",
      "SubmissionId",
      "FailureName",
      "FailureHash",
      "Symbol",
      "OSVersion",
      "OSName",
      "EventType",
      "Market",
      "DeviceType",
      "DriverName",
      "DriverVersion",
      "Architecture",
      "OEMName",
      "OEMModel",
      "FlightRing",
      "Mode",
      "CPUName",
      "OSSKUType",
      "ReleaseName",
      "CabType",
      "CabIdHash",
      "CabExpirationTime",
      "DeviceId",
      "HardwareId",
      "CabCollectionTime",
      "EventCount"
   ],
   "dateRange":{
      "reportPeriod":"Last7Days"
   }
}
```

## Sample 2: Show all available columns for *OEM failure* details for the last 7 days

The following API request payload lists all available columns in the *OEM failure* report and sets the reportPeriod to the last seven days.

```json
{
   "view":"OEMDriver",
   "projection":
  [
      "ReportId",
      "FailureDate",
      "FailureDateTime",
      "FailureName",
      "FailureHash",
      "Symbol",
      "OSVersion",
      "EventType",
      "Market",
      "DeviceType",
      "DriverName",
      "DriverVersion",
      "Architecture",
      "Model",
      "Baseboard",
      "ModelFamily",
      "FlightRing",
      "Mode",
      "CPUName",
      "OSSKUType",
      "ReleaseName",
      "CabType",
      "CabIdHash",
      "CabExpirationTime",
      "DeviceId",
      "HardwareId",
      "CabCollectionTime",
      "EventCount"
   ],
   "dateRange":{
      "reportPeriod":"Last7Days"
   }
}
```

## Sample 3:  Show the number of IHV failures, the unique devices impacted for each driver, over the last 30 days, and sort by devices impacted

This API request payload calls for an IHV failure report that lists the sum of driver failures reported as well as the unique devices impacted for each driver for the last 30 days. It sorts the report by the devices impacted.

```json
{
   "view":"IHVDriver",
   "projection":
  [
      "DriverName",
      "DriverVersion",
      "FailureName",
      "FailureHash"
   ],
   "dateRange":{
      "reportPeriod":"Last30Days"
   },
   "aggregation":{
      "aggregatedColumns":[
         "SUM(EventCount)",
         "DCOUNT(DeviceId)"
      ]
   },
   "orderby":[
      {
         "attribute":"DCOUNT(DeviceId)",
         "sort":"desc"
      }
   ]
}
```

## Sample 4: List the number of OEM failure details over the past seven days, for which the number of kernel crashes is greater than 1000

This API request payload calls for an OEM failure report that lists all of the failures reported over the past seven days, filtered by failures that have more than 1000 kernel crashes during that time period.

```json
{
   "view":"OEMDriver",
   "projection":[
      "FailureName",
      "FailureHash"
   ],
   "dateRange":{
      "reportPeriod":"Last7Days"
   },
   "condition":{
      "and":[
         {
            "attribute":"EventType",
            "operator":"eq",
            "value":"Kernel"
         }
      ]
   },
   "aggregation":{
      "aggregatedColumns":[
         "SUM(EventCount)"
      ],
      "condition":{
         "or":[
            {
               "attribute":"SUM(EventCount)",
               "operator":"gt",
               "value":"1000"
            }
         ]
      }
   }
}
```

## Sample 5: List the top 10 drivers that impact the maximum number of unique devices in the last 90 days

This API request payload calls for an IHV failure report for all drivers. It then aggregates and orders the list by the number of devices affected by the failures and shows the top ten drivers affecting devices.

```json
{
  "view": "IHVDriver",
  "projection": [
    "DriverName"
  ],
  "dateRange": {
    "reportPeriod": "Last90Days"
  },
  
  "aggregation": {
    "aggregatedColumns": [
      "DCOUNT(DeviceId)"
    ]
  },
  "orderby": [
      {
        "attribute": "DCOUNT(DeviceId)",
        "sort": "desc"
      }
    ],
    "limit": 10  
}
```

## See also

- [Create a new report template](create-a-new-report-template.md)

- [Analytics Reporting APIs (Swagger )](https://apidocs.microsoft.com/services/analyticsreportingapis)

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
