---
title: Schedule Custom Reports for your driver failure details
description: Overview of the process for creating error reports for the Microsoft Hardware Dev Center.
author: balapv
ms.author: balapv
ms.date: 04/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Schedule custom reports for your driver failure details

Use these asynchronous methods to access reporting data for your Win10/ Win 8.x driver errors and OEM hardware errors. You can define reporting templates based on your needs, set a schedule and you will have data delivered to you at regular intervals.

>[!NOTE]

- >These methods can only be used by developer accounts that belong to the [Windows Hardware Dev Center program](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/get-started-with-the-hardware-dashboard).
- >These methods can be used in place of the existing methods to determine [Windows 10 driver errors](https://docs.microsoft.com/windows/uwp/monetize/get-error-reporting-data-for-windows-10-drivers),  [Windows 7 and Windows 8.x driver errors](https://docs.microsoft.com/windows/uwp/monetize/get-error-reporting-data-for-windows-7-and-windows-8.x-drivers) (for IHVs), and [hardware errors](https://docs.microsoft.com/windows/uwp/monetize/get-oem-hardware-error-reporting-data) (for OEMs).
- >These methods expose a rich set of new dimensions and supports look back for as much as 90 days in the past.

## Prerequisites

To use this method, you need to first do the following:

- If you have not done so already, complete all the [prerequisites](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services) for the Microsoft Store analytics API.
- Obtain an [Azure AD access token](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services) to use in the request header for this method. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can obtain a new one.

For more information, see [Access analytics data using Microsoft Store services](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services)

> [!IMPORTANT]
> As a reminder, the [Windows Analytics Agreement](https://go.microsoft.com/fwlink/?linkid=866941) states: “You must not store Personal Information for longer than thirty (30) days. Following such 30-day period, you will immediately destroy the Personal Information.”

## Workflow to schedule custom reports for driver failure

The following diagram explains the API call pattern to create a new report template, schedule the custom report and retrieve failure data.

<<<<<<< HEAD
![Image showing the workflow between—top to bottom—Creating a custom report template, scheduling a custom report template, getting report data, and cab download.](./images/failure-reporting-workflow.png)

1. The Client Application defines the report schema in JSON format and call the [Create Report Template API](#create-a-new-report-template).

2. On success, the Create New Report Template API returns the TemplateId.

3. The client application calls the [Schedule Custom Report API](#schedule-a-new-report) using the TemplateId along with the report start date, Repeat Interval and Recurrence.

4. On Success, the Schedule Custom Report API returns the ReportID.

5. The client application then uses the [Get Report Data API](#get-report-data) to query the status of the report with the Report ID and date range.

6. On success, the report download link is returned and the application can initiate download of the data.

7. The report data contains the CabIdHash that can be used as input to the Cab Download API, to download the cab files.

8. The [Cab Download API](#download-failure-cabs) returns the cab download link that can be used to download the cab files.

## See Also

- [Create a new report template](create-a-new-report-template.md)

- [Sample report templates](sample-report-templates.md)
=======


//Template content
## Request

This method has the following syntax. See the following sections for usage examples and descriptions of the header and request body.

| Method | Request URI |
|:--|:--|
| POST | `https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/{productID}/submissions` |

The productId in the method is the product for which the submission is intended.

### Request header

| Header | Type | Description |
|:--|:--|:--|
| Authorization | String | Required. The Azure AD access token in the form **Bearer** \<token\>. |
| Accept | String | Optional. Specifies the type of content. Allowed value is “application/json” |

### Request parameters

Do not provide request parameters for this method.

### Request body

The following example demonstrates the JSON request body for creating a new submission.

```json
{
  "name": "VST_apdevtest1_init",
  "type": "initial"
}
```

For details about the fields in the request, refer to [Submission resource](get-product-data.md#submission-resource).

### Request examples

The following example demonstrates how to create a new submission.

```
POST https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14631253285588838/submissions HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for creating a new submission for a product. For more details about the values in the response body, see the following section.

```json
{
  "id": 1152921504621465124,
  "productId": 14631253285588838,
  "downloads": {
    "items": [
      {
        "type": "initialPackage",
        "url": "https://ingestionpackagesint1.blob.core.windows.net/ingestion/38c19eaf-7377-4834-893c-28d5791f7896?sv=2017-04-17&sr=b&sig=SlD5j5e067oA4Y3hdk1sPW3UycTSUVlIp80WbWvj4A8%3D&se=2018-03-20T05:00:14Z&sp=rwl"
      }
    ],
    "messages": []
  },
  "links": [
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14631253285588838/submissions/1152921504621465124",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://manage.devcenter.microsoft.com/v1.0/my/hardware/products/14631253285588838/submissions/1152921504621465124",
      "rel": "update_submission",
      "method": "PATCH"
    }
  ],
  "commitStatus": "commitPending",
  "name": "VST_apdevtest1_init",
  "type": "initial"
}
```

### Response body

Refer to [Submission resource](get-product-data.md#submission-resource) for more details.

## Error codes

For more info, see [Error codes](get-product-data.md#error-codes).
>>>>>>> master
