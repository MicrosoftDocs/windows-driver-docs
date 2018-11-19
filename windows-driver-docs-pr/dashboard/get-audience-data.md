---
title: Get audience data
description: These methods from the Microsoft Hardware APIs get the applicable audiences for an organization to be used in a shipping label.
author: balapv
ms.author: balapv
ms.topic: article
ms.date: 08/21/2018
---
# Get audience data

Use the following method in *Microsoft Hardware APIs* to get the audiences applicable to your organization. Audiences allow you to restrict a publication to machines with a particular configuration. As an example, a test deployment can be delivered only to clients with a particular registry key installed.

```cpp
https://manage.devcenter.microsoft.com/v1.0/my/hardware/audiences
```

Before you can use these methods, the product and submission must already exist in your Dev Center account. To create or manage submissions for products, see the methods in [Manage product submissions](manage-product-submissions.md).

|Description|Method|URI|
|-|-|-|
|Get a list of audiences applicable to your organization.|GET|`https://manage.devcenter.microsoft.com/v1.0/my/hardware/audiences`|

## Prerequisites

If you have not done so already, complete all the [prerequisites](dashboard-api.md) for the Microsoft Hardware APIs before trying to use any of these methods.

## Data resources

The Microsoft Hardware APIs methods for getting shipping label data use the following JSON data resources.

### Audience resource

This resource represents an audience that is applicable to your organization.

```json
{
  "id": "9f4f44d8-bfec-48c6-a02c-2d9ea220f6e2",
  "name": "My Custom Audience",
  "description": "Matches machines that have the following registry key: HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\FOO-BAR",
  "audienceName": "Sample_Audience_Key"
}
```

This resource has the following values

| Value | Type | Description |
|:--|:--|:--|
|id|string|The ID of the audience. This is the value that will be received or sent in the shipping label.|
|name|string|Friendly name of the audience|
|description|string|Description of the audience|
|audienceName|string|Name of the audience|

## Request

This method has the following syntax.

|Method|Request URI|
|--|--|
|GET|`https://manage.devcenter.microsoft.com/v1.0/my/hardware/audience`|

### Request header

|Header|Type|Description|
|--|--|--|
|Authorization|string|Required. The Azure AD access token in the form **Bearer** *\<token\>*.|
|accept|string|Optional. Specifies the type of content. Allowed value is “application/json”|

### Request parameters

Do not provide request parameters for this method.

### Request body

Do not provide a request body for this method.

### Request examples

The following example demonstrates how to retrieve information about audiences applicable to your organization.

```cpp
GET https://manage.devcenter.microsoft.com/v1.0/my/hardware/audience HTTP/1.1
Authorization: Bearer <your access token>
```

## Response

The following example demonstrates the JSON response body returned by a successful request for all the audiences applicable to your organization. Details about the values in the response body appear in the table following the example.

```json
{
  "value": [
    {
      "id": "9f4f44d8-bfec-48c6-a02c-2d9ea220f6e2",
      "name": "Test Registry Key",
      "description": "Matches machines that have the following registry key: HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\Test Drivers - use at own risk",
      "audienceName": "Test_Registry_Key"
    },
    {
      "id": "10415bba-3572-421b-a3de-d0d347bace5f",
      "name": "Test Audience 2",
      "description": "Additional Audeince",
      "audienceName": "Test_Audeince_2"
    }
  ],
  "links": [
    {
      "href": "https://manage.devcenter..microsoft.com/api/v1/hardware/audiences",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

This resource has the following values

| Value | Type | Description |
|:--|:--|:--|
| value | array | An array of objects that contain information about each audience. For more information about the data in each object, see [audience resource](#audience-resource). |
| links | array | An array of objects with helpful links about the containing entity. See the [Link object](get-product-data.md#link-object) for more details.|

## See also

- [Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)
