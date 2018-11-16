---
ms.assetid: 2F30E68B-B643-4387-9430-793D08AAF0E7
description: Use this method in the Microsoft Store analytics API to get aggregate error reporting data for Windows 7 and Windows 8.x drivers for a given date range and other optional filters. This method is intended only for IHVs.
title: Get error reporting data for Windows 7 and Windows 8.x drivers
ms.author: eliotgra
ms.topic: article
ms.date: 08/28/2018
keywords: windows 10, uwp, Store services, Microsoft Store analytics API, errors
ms.localizationpriority: medium
---

# Get error reporting data for Windows 7 and Windows 8.x drivers

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

Use this method in the Microsoft Store analytics API to get aggregate reporting data for Windows 7/Windows 8.x driver errors for a given date range and other optional filters. You can retrieve additional error information by using the [get details for a Windows 7 or Windows 8.x driver error](get-details-for-a-windows-7-or-windows-8.x-driver-error.md) method.

> [!NOTE]
> This method can only be used by developer accounts that belong to the [Windows Hardware Dev Center program](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/get-started-with-the-hardware-dashboard).

## Prerequisites

To use this method, you need to first do the following:

* If you have not done so already, complete all the [prerequisites](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services#prerequisites) for the Microsoft Store analytics API.
* [Obtain an Azure AD access token](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services#obtain-an-azure-ad-access-token) to use in the request header for this method. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can obtain a new one.

## Request


### Request syntax

| Method | Request URI                                                          |
|--------|----------------------------------------------------------------------|
| GET    | `https://manage.devcenter.microsoft.com/v1.0/my/analytics/ihvdriver/failurehits` |


### Request header

| Header        | Type   | Description                                                                 |
|---------------|--------|-----------------------------------------------------------------------------|
| Authorization | string | Required. The Azure AD access token in the form **Bearer** &lt;*token*&gt;. |


### Request parameters

| Parameter        | Type   |  Description      |  Required  
|---------------|--------|---------------|------|
| startDate | date | The start date in the date range of error reporting data to retrieve. The default is the current date. |  No  |
| endDate | date | The end date in the date range of error reporting data to retrieve. The default is the current date. |  No  |
| top | int | The number of rows of data to return in the request. The maximum value and the default value if not specified is 10000. If there are more rows in the query, the response body includes a next link that you can use to request the next page of data. |  No  |
| skip | int | The number of rows to skip in the query. Use this parameter to page through large data sets. For example, top=10000 and skip=0 retrieves the first 10000 rows of data, top=10000 and skip=10000 retrieves the next 10000 rows of data, and so on. |  No  |
| filter | string  | One or more statements that filter the rows in the response. Each statement contains a field name from the response body and value that are associated with the **eq** or **ne** operators, and statements can be combined using **and** or **or**. String values must be surrounded by single quotes in the *filter* parameter. You can specify the following fields from the response body:<p/><ul><li><strong>date</strong></li><li><strong>failureName</strong></li><li><strong>failureHash</strong></li><li><strong>symbol</strong></li><li><strong>osVersion</strong></li></li><li><strong>eventType</strong></li><li><strong>market</strong></li><li><strong>deviceType</strong></li><li><strong>driverName</strong></li><li><strong>driverVersion</strong></li><li><strong>oemName</strong></li><li><strong>oemModel</strong></li><li><strong>flightRing</strong></li><li><strong>architecture</strong></li></ul> | No   |
| aggregationLevel | string | Specifies the time range for which to retrieve aggregate data. Can be one of the following strings: <strong>day</strong>, <strong>week</strong>, or <strong>month</strong>. If unspecified, the default is <strong>day</strong>. If you specify <strong>week</strong> or <strong>month</strong>, the <em>failureName</em> and <em>failureHash</em> values are limited to 1000 buckets. | No |
| orderby | string | A statement that orders the result data values. The syntax is <em>orderby=field [order],field [order],...</em>. You can specify the following fields from the response body:<p/><ul><li><strong>date</strong></li><li><strong>failureName</strong></li><li><strong>failureHash</strong></li><li><strong>symbol</strong></li><li><strong>osVersion</strong></li><li><strong>osName</strong></li><li><strong>eventType</strong></li><li><strong>market</strong></li><li><strong>deviceType</strong></li><li><strong>driverName</strong></li><li><strong>driverVersion</strong></li><li><strong>oemName</strong></li><li><strong>oemModel</strong></li><li><strong>flightRing</strong></li><li><strong>architecture</strong></li></ul><p>The <em>order</em> parameter is optional, and can be <strong>asc</strong> or <strong>desc</strong> to specify ascending or descending order for each field. The default is <strong>asc</strong>.</p><p>Here is an example <em>orderby</em> string: <em>orderby=date,market</em></p> |  No  |
| groupby | string | A statement that applies data aggregation only to the specified fields. You can specify the following fields from the response body:<p/><ul><li><strong>failureName</strong></li><li><strong>failureHash</strong></li><li><strong>symbol</strong></li><li><strong>osVersion</strong></li><li><strong>eventType</strong></li><li><strong>market</strong></li><li><strong>deviceType</strong></li><li><strong>driverName</strong></li><li><strong>driverVersion</strong></li><li><strong>oemName</strong></li><li><strong>oemModel</strong></li><li><strong>flightRing</strong></li><li><strong>architecture</strong></li></ul><p>The returned data rows will contain the fields specified in the <em>groupby</em> parameter as well as the following:</p><ul><li><strong>date</strong></li><li><strong>eventCount</strong></li></ul><p>The <em>groupby</em> parameter can be used with the <em>aggregationLevel</em> parameter. For example: <em>&amp;groupby=failureName,market&amp;aggregationLevel=week</em></p></p> |  No  |


### Request example

The following examples demonstrate several requests for getting OEM hardware error reporting data.

```syntax
GET https://manage.devcenter.microsoft.com/v1.0/my/analytics/ihvdriver/failurehits?startDate=1/1/2015&endDate=2/1/2015&top=10&skip=0 HTTP/1.1
Authorization: Bearer <your access token>

GET https://manage.devcenter.microsoft.com/v1.0/my/analytics/ihvdriver/failurehits?startDate=8/1/2015&endDate=8/31/2015&skip=0&filter=market eq 'US' and deviceType eq 'PC' HTTP/1.1
Authorization: Bearer <your access token>
```

## Response


### Response body

| Value      | Type    | Description     |
|------------|---------|--------------|
| Value      | array   | An array of objects that contain aggregate error reporting data. For more information about the data in each object, see the following table.     |
| @nextLink  | string  | If there are additional pages of data, this string contains a URI that you can use to request the next page of data. For example, this value is returned if the **top** parameter of the request is set to 10000 but there are more than 10000 rows of errors for the query. |
| TotalCount | integer | The total number of rows in the data result for the query.     |


Elements in the *Value* array contain the following values.

| Value           | Type    | Description        |
|-----------------|---------|---------------------|
| date            | string  | The first date in the date range for the error data. If the request specified a single day, this value is that date. If the request specified a week, month, or other date range, this value is the first date in that date range. |
| sellerId   | string  | The seller ID value that is associated with the developer account (this matches the **Seller ID** value in the Dev Center account settings). |
| failureName     | string  | The name of the failure, which is made up of four parts: one or more problem classes, an exception/bug check code, the name of the driver where the failure occurred, and the associated function name.  |
| failureHash     | string  | The unique identifier for the error.   |
| symbol          | string  | The symbol assigned to this error. |
| osVersion       | string  | The four-part build version of the OS on which the error occurred.  |
| osName       | string  | The name of the OS on which the error occurred.  |
| eventType       | string  | The type of the error that occurred.      |
| market          | string  | The ISO 3166 country code of the device market.   |
| deviceType      | string  | The type of device on which the error occurred.    |
| driverName     | string  | The unique name of the driver that is associated with this error.      |
| driverVersion  | string  | The version of the driver that is associated with this error.   |
| architecture | string |  The architecture of the device on which the error occurred.  |
| oemName | string | The name of OEM for the device on which the error occurred. |
| oemModel | string | The name of the device model on which the error occurred. |
| flightRing | string | The name of the OS flight on which the error occurred. |
| eventCount      | integer | The number of events that are attributed to this error for the specified aggregation level.      |


### Response example

The following example demonstrates an example JSON response body for this request.

```json
{
  "Value": [
    {
      "date": "2017-02-26",
      "sellerId":"14313740",
      "driverName": "fastboot.sys",
      "osVersion": "6.3.9600.9600",
      "osName": "Windows 8.1",
      "flightRing": "Unknown",
      "oemName": "Contoso",
      "oemModel": "C-122",
      "market": "US",
      "symbol": "fastboot",
      "failureName": "AV_fastboot!unknown_function",
      "failureHash": "f060c0b6-fbe6-463f-a9f1-b7ebc1cc722f",
      "architecture": "x64",
      "driverVersion": "2.1.1.0",
      "deviceType": "Unknown",
      "eventType": "System crash",
      "deviceCount": 1.0,
      "eventCount": 1.0
    }]
}
```

## Related topics

- [Get details for a Windows 7 or Windows 8.x driver error](get-details-for-a-windows-7-or-windows-8.x-driver-error.md)

- [Download the CAB file for a Windows 7 or Windows 8.x driver error](download-the-cab-file-for-a-windows-7-or-windows-8.x-driver-error.md)
