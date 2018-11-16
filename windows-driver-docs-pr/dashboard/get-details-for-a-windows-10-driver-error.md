---
ms.assetid: 79DC7C99-70F1-499A-856B-D2A83FC6F867
description: Use this method in the Microsoft Store analytics API to get detailed data for a Windows 10 driver error. This method is intended only for IHVs.
title: Get details for a Windows 10 driver error
ms.author: eliotgra
ms.topic: article
ms.date: 08/28/2018
keywords: windows 10, uwp, Store services, Microsoft Store analytics API, errors, details
ms.localizationpriority: medium
---

# Get details for a Windows 10 driver error

> [!IMPORTANT]
> This topic contains deprecated material. It describes older methods for collecting data about driver submission failures. It is supplied only for legacy support.
>
> Use these newer topics instead:
>
> - [Schedule Custom Reports for your driver failure details](schedule-custom-reports-for-driver-failure-details.md)
> - [Create new report template](create-a-new-report-template.md)
> - [Schedule a new report](schedule-a-new-report.md)
> - [Get Report Data](get-report-data.md)
> - [Download Failure Cabs](download-failure-cabs.md)

Use this method in the Microsoft Store analytics API to get detailed data for a specific Windows 10 driver error in JSON format. Before you can use this method, you must first use the [get error reporting data for Windows 10 drivers](get-error-reporting-data-for-windows-10-drivers.md) method to retrieve the ID of the error for which you want to get detailed info.

> [!NOTE]
> This method can only be used by developer accounts that belong to the [Windows Hardware Dev Center program](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/get-started-with-the-hardware-dashboard).

## Prerequisites

To use this method, you need to first do the following:

- If you have not done so already, complete all the [prerequisites](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services#prerequisites) for the Microsoft Store analytics API.

- [Obtain an Azure AD access token](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services#obtain-an-azure-ad-access-token) to use in the request header for this method. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can obtain a new one.

- Get the ID of the error for which you want to get detailed info. To get this ID, use the [get error reporting data for Windows 10 drivers](get-error-reporting-data-for-windows-10-drivers.md) method and use the **failureHash** value in the response body of that method.

## Request

### Request syntax

| Method | Request URI                                                          |
|--------|----------------------------------------------------------------------|
| GET    | `https://manage.devcenter.microsoft.com/v1.0/my/analytics/driver/failuredetails` |

### Request header

| Header|Type| Description|
|-----|-----|----|
|Authorization|string|Required. The Azure AD access token in the form **Bearer** *\<token\>*. |

### Request parameters

|Parameter|Type|Description|Required|
|------|-----|-----|------|
|applicationId|string|The product ID value of the driver for which you want to retrieve error data.|Yes|
|failureHash|string|The unique ID of the error for which you want to get detailed info. To get this value for the error you are interested in, use the [Get OEM hardware error reporting data](get-oem-hardware-error-reporting-data.md) method and use the **failureHash** value in the response body of that method.|Yes|
|startDate|date|The start date in the date range of detailed error data to retrieve. The default is 30 days before the current date.|No|
|endDate|date|The end date in the date range of detailed error data to retrieve. The default is the current date. |  No  |
| top | int | The number of rows of data to return in the request. The maximum value and the default value if not specified is 10000. If there are more rows in the query, the response body includes a next link that you can use to request the next page of data. |  No  |
| skip | int | The number of rows to skip in the query. Use this parameter to page through large data sets. For example, top=10 and skip=0 retrieves the first 10 rows of data, top=10 and skip=10 retrieves the next 10 rows of data, and so on. |  No  |
| filter |string  | One or more statements that filter the rows in the response. Each statement contains a field name from the response body and value that are associated with the **eq** or **ne** operators, and statements can be combined using **and** or **or**. String values must be surrounded by single quotes in the *filter* parameter. You can specify the following fields from the response body:<p/><ul><li><strong>date</strong></li><li><strong>submissionId</strong></li><li><strong>failureName</strong></li><li><strong>failureHash</strong></li><li><strong>symbol</strong></li><li><strong>osVersion</strong></li><li><strong>osName</strong></li><li><strong>eventType</strong></li><li><strong>market</strong></li><li><strong>deviceType</strong></li><li><strong>driverName</strong></li><li><strong>driverVersion</strong></li><li><strong>oemName</strong></li><li><strong>oemModel</strong></li><li><strong>architecture</strong></li><li><strong>cabIdHash</strong></li><li><strong>clientDeviceId</strong></li><li><strong>cabType</strong></li><li><strong>cabExpirationTime</strong></li></ul> | No   |
| orderby | string | A statement that orders the result data values. The syntax is <em>orderby=field [order],field [order],...</em>. You can specify the following fields from the response body:<p/><ul><li><strong>date</strong></li><li><strong>submissionId</strong></li><li><strong>failureName</strong></li><li><strong>failureHash</strong></li><li><strong>symbol</strong></li><li><strong>osVersion</strong></li><li><strong>osName</strong></li><li><strong>eventType</strong></li><li><strong>market</strong></li><li><strong>deviceType</strong></li><li><strong>driverName</strong></li><li><strong>driverVersion</strong></li><li><strong>oemName</strong></li><li><strong>oemModel</strong></li><li><strong>flightRing</strong></li><li><strong>architecture</strong></li><li><strong>cabType</strong></li><li><strong>cabExpirationTime</strong></li></ul><p>The <em>order</em> parameter is optional, and can be <strong>asc</strong> or <strong>desc</strong> to specify ascending or descending order for each field. The default is <strong>asc</strong>.</p><p>Here is an example <em>orderby</em> string: <em>orderby=date,market</em></p> |  No  |

### Request example

The following examples demonstrate several requests for getting detailed error data.

```syntax
GET https://manage.devcenter.microsoft.com/v1.0/my/analytics/driver/failuredetails?applicationId=18430592857500421&failureHash=012e33e3-dbc9-b12f-c124-9d9810f05d8b&startDate=2016-11-05&endDate=2016-11-06&top=10&skip=0 HTTP/1.1
Authorization: Bearer <your access token>

GET https://manage.devcenter.microsoft.com/v1.0/my/analytics/driver/failuredetails?applicationId=18430592857500421&failureHash=012e33e3-dbc9-b12f-c124-9d9810f05d8b&startDate=2016-11-05&endDate=2016-11-06&top=10&skip=0&filter=market eq 'US' and deviceType eq 'PC' HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

### Response body

| Value      | Type    | Description    |
|------------|---------|------------|
| Value      | array   | An array of objects that contain detailed error data. For more information about the data in each object, see the following table.          |
| @nextLink  | string  | If there are additional pages of data, this string contains a URI that you can use to request the next page of data. For example, this value is returned if the **top** parameter of the request is set to 10 but there are more than 10 rows of errors for the query. |
| TotalCount | integer | The total number of rows in the data result for the query.        |

Elements in the *Value* array contain the following values.

| Value           | Type    | Description     |
|-----------------|---------|----------------------------|
| date            | string  | The first date in the date range for the error data. If the request specified a single day, this value is that date. If the request specified a week, month, or other date range, this value is the first date in that date range. |
| applicationId   | string  | The product ID value of the driver for which you retrieved error data. |
| submissionId   | string  | The submission ID that is associated with the driver. |
| failureName     | string  |The name of the failure, which is made up of four parts: one or more problem classes, an exception/bug check code, the name of the driver where the failure occurred, and the associated function name.             |
| failureHash     | string  | The unique identifier for the error.     |
| symbol     | string  | The symbol assigned to this error.     |
| osVersion       | string  | The four-part build version of the OS on which the error occurred.    |
| osName       | string  | The name of the OS on which the error occurred.  |
| eventType       | string  | The type of the error that occurred.      |
| market          | string  | The ISO 3166 country code of the device market.     |
| deviceType      | string  | One of the following strings that specifies the type of device on which the error occurred:<p/><ul><li><strong>PC</strong></li><li><strong>Phone</strong></li><li><strong>Console</strong></li><li><strong>IoT</strong></li><li><strong>Holographic</strong></li><li><strong>Unknown</strong></li></ul>     |
| driverName     | string  | The unique name of the driver that is associated with this error.      |
| driverVersion  | string  | The version of the driver that is associated with this error.   |
| architecture | string |  The architecture of the device on which the error occurred.  |
| oemName | string | The name of OEM for the device on which the error occurred. |
| oemModel | string | The name of the device model on which the error occurred. |
| flightRing | string | The name of the OS flight on which the error occurred. |
| clientDeviceId | string | The ID of the device on which the error occurred. |
| cabIdHash         | string  | The unique ID of the CAB file that is associated with this error.   |
| cabType         | string  | The type of the CAB file.   |
| cabExpirationTime  | string  | The date and time when the CAB file is expired and can no longer be downloaded, in ISO 8601 format.   |

### Response example

The following example demonstrates an example JSON response body for this request.

```json
{
  "Value": [
    {   
      "submissionId":"29989500_13736592797500435_1152921504626321174",
      "applicationId":"18430592857500421",
      "architecture": "x64",
      "cabExpirationTime": "2017-03-16 01:04:55",
      "cabIdHash": "1d7b4184-8f18-4207-88b5-36b276363eb5",
      "cabType": "MINI",
      "clientDeviceId": null,
      "date": "2017-02-14 01:04:55",
      "deviceType": "Unknown",
      "driverName": "fastboot.sys",
      "driverVersion": "2.1.1.0",
      "failureHash": "0d901479-bf1f-b842-76f2-3db7e4feaedd",
      "failureName": "AV_fastboot!unknown_function",
      "market": "US",
      "oemModel": "C-122",
      "oemName": "Contoso",
      "osName": "Windows 10",
      "osVersion": "10.0.14393.693"
    }]
}
```

## See also

- [Get error reporting data for Windows 10 drivers](get-error-reporting-data-for-windows-10-drivers.md)

- [Download the CAB file for a Windows 10 driver error](download-the-cab-file-for-a-windows-10-driver-error.md)
