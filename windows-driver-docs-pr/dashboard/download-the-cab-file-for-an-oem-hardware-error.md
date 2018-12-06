---
ms.assetid: E64030CA-EC00-4113-9939-26D5688C61BC
description: Use this method in the Microsoft Store analytics API to download the CAB file for a hardware error. This method is intended only for OEMs.
title: Download the CAB file for an OEM hardware error
ms.topic: article
ms.date: 03/17/2017
keywords: windows 10, uwp, Microsoft Store analytics API, download CAB
ms.localizationpriority: medium
---

# Download the CAB file for an OEM hardware error

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

Use this method in the Microsoft Store analytics API to download the CAB file that is associated with a particular OEM hardware error. Before you can use this method, you must first use the [get details for an OEM hardware error](get-details-for-an-oem-hardware-error.md) method to retrieve the ID of the CAB file you want to download.

You can get other info about OEM hardware errors by using the [get OEM hardware error reporting data](get-oem-hardware-error-reporting-data.md) and [get details for an OEM hardware error](get-details-for-an-oem-hardware-error.md) methods in the Microsoft Store analytics API.

> [!NOTE]
> This method can only be used by developer accounts that belong to the [Windows Hardware Dev Center program](https://msdn.microsoft.com/windows/hardware/drivers/dashboard/get-started-with-the-hardware-dashboard).

## Prerequisites

To use this method, you need to first do the following:

* If you have not done so already, complete all the [prerequisites](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services#prerequisites) for the Microsoft Store analytics API.
* [Obtain an Azure AD access token](https://docs.microsoft.com/windows/uwp/monetize/access-analytics-data-using-windows-store-services#obtain-an-azure-ad-access-token) to use in the request header for this method. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can obtain a new one.
* Get the ID of the CAB file you want to download. To get this ID, use the [get details for an OEM hardware error](get-details-for-an-oem-hardware-error.md) method to retrieve details for a specific hardware error, and use the **cabIdHash** value in the response body of that method.

## Request


### Request syntax

| Method | Request URI                                                          |
|--------|----------------------------------------------------------------------|
| GET    | `https://manage.devcenter.microsoft.com/v1.0/my/analytics/hardware/cabdownload` |


### Request header

| Header        | Type   | Description                                                                 |
|---------------|--------|-----------------------------------------------------------------------------|
| Authorization | string | Required. The Azure AD access token in the form **Bearer** &lt;*token*&gt;. |


### Request parameters

| Parameter        | Type   |  Description      |  Required  |
|---------------|--------|---------------|------|
| cabIdHash | string | The unique ID of the CAB file you want to download. To get this ID, use the [get details for an OEM hardware error](get-details-for-an-oem-hardware-error.md) method to retrieve details for a specific error in your app, and use the **cabIdHash** value in the response body of that method. |  Yes  |

 
### Request example

The following example demonstrates how to download a CAB file using this method.

```syntax
GET https://manage.devcenter.microsoft.com/v1.0/my/analytics/hardware/cabdownload?cabIdHash=c1a51104-d682-4230-be14-7278b18e3555 HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

This method returns a 302 (redirect) response code, and the **Location** header in the response is assigned to the shared access signature (SAS) URI of the CAB file. The caller is redirected to this URI to automatically download the CAB file.

## Related topics

- [Get OEM hardware error reporting data](get-oem-hardware-error-reporting-data.md)
- [Get details for an OEM hardware error](get-details-for-an-oem-hardware-error.md)
