---
title: Hardware dashboard API
description: The Microsoft Hardware APIs programmatically query and create submissions for hardware products within your organization's Partner Center account.
ms.topic: article
ms.date: 09/21/2018
ms.localizationpriority: medium
---

# Hardware dashboard API

Use the *Microsoft Hardware APIs* to programmatically query and create submissions for hardware products within your organization's Partner Center account. These APIs are useful if your account manages many products, and you want to automate and optimize the submission process for these assets. These APIs use Azure Active Directory (Azure AD) to authenticate the calls from your app or service.
The following steps describe the end-to-end process of using the Microsoft Hardware API:

1. These APIs can only be used by accounts that belong to the Hardware [Partner Center program](./get-started-with-the-hardware-dashboard.md).

2. Make sure that you have completed the prerequisites below.

3. Before you call a method in the Microsoft Hardware API, obtain an Azure AD access token, as illustrated below. After you obtain a token, you have 60 minutes to use this token in calls to the Microsoft Store submission API before the token expires. After the token expires, you can generate a new token.

4. Call the Microsoft Hardware API.

## Complete the prerequisites for using the Microsoft Hardware API

Before you start writing code to call the Microsoft Hardware API, make sure that you have completed the following required prerequisites.

* You (or your organization) must have an Azure AD directory and you must have [Global administrator](/azure/active-directory/users-groups-roles/directory-assign-admin-roles)  permission for the directory. If you already use Microsoft 365 or other business services from Microsoft, you already have Azure AD directory. Otherwise, you can [create a new Azure AD in Partner Center](/windows/uwp/publish/associate-azure-ad-with-partner-center#create-a-brand-new-azure-ad-to-associate-with-your-partner-center-account) for no additional charge.

* If an Azure AD application does not already exist, [you must create one](/windows/uwp/publish/add-users-groups-and-azure-ad-applications#create-a-new-azure-ad-application-account-in-your-organizations-directory-and-add-it-to-your-partner-center-account).

* You must [associate an Azure AD application with your Partner Center account](/windows/uwp/publish/associate-azure-ad-with-partner-center) and assign it the **Manager** role.

* Gather your [Azure AD application tenant ID, client ID, and key](/windows/uwp/publish/add-users-groups-and-azure-ad-applications#manage-keys-for-an-azure-ad-application).  **Be sure to print or copy this key info, as you won't be able to access it again after you leave the key creation page.** 

## Assigning the appropriate Hardware roles to your Azure AD application

After you have completed the above prerequisites we must now assign the appropriate roles so that the Azure AD application can create and manage submissions and shipping labels.

1. From Partner Center, select the gear icon (near the upper right corner of the dashboard) and then select **Developer settings**. In the **Settings** menu, select **Users**.

2. On the **Users** page, select **Azure AD applications** and the Azure AD application that represents the app or service that you will use to access submissions for your Partner Center account.  

3. On this page, under **Roles**, select **Hardware**.

    ![an image showing the Hardware tab in the Roles section.](images/hardware-tab-in-roles-section.png)

    Select **Driver Submitter**, **Shipping Label owner**, and if available, **Shipping Label promoter**.  [Learn more about these roles](./managing-user-roles.md)
    

## Obtain an Azure AD access token

Before you call any of the methods in the Microsoft Hardware API, you must first obtain an Azure AD access token that you pass to the **Authorization** header of each method in the API. After you obtain an access token, you have 60 minutes to use it before it expires. After the token expires, you can refresh the token, so you can continue to use it in further calls to the API. To obtain the access token, follow the instructions in [Service to Service Calls Using Client Credentials](/azure/active-directory/azuread-dev/v1-oauth2-client-creds-grant-flow) to send an HTTP POST to the `https://login.microsoftonline.com/<tenant_id>/oauth2/token` endpoint. Here is a sample request.

```cpp
POST https://login.microsoftonline.com/<tenant_id>/oauth2/token HTTP/1.1
Host: login.microsoftonline.com
Content-Type: application/x-www-form-urlencoded; charset=utf-8

grant_type=client_credentials
&client_id=<your_client_id>
&client_secret=<your_client_secret>
&resource=https://manage.devcenter.microsoft.com
```

For the *tenant_id* value in the POST URI and the *client_id* and *client_secret* parameters, specify the tenant ID, client ID and the key for your application that you retrieved from Partner Center in the previous section. For the *resource* parameter, you must specify `https://manage.devcenter.microsoft.com`.

After your access token expires, you can refresh it by following the instructions in [Refreshing the access tokens](/azure/active-directory/azuread-dev/v1-protocols-oauth-code#refreshing-the-access-tokens).

## Use the Microsoft Hardware API

After you have an Azure AD access token, you can call methods in the Microsoft Hardware API. The API includes many methods that are grouped into scenarios. To create or update submissions, you typically call multiple methods in the Microsoft Hardware API in a specific order. For information about each scenario and the syntax of each method, see the articles in the following table.

| Scenario | Description |
|:--|:--|
| Drivers | Get, create and update drivers registered to your Partner Center Account. For more information about these methods, see the following articles:<ul><li>[Get product data](get-product-data.md)</li><li>[Manage product submissions](manage-product-submissions.md)</li><li>[Get shipping label data](get-shipping-labels.md)</li><li>[Manage shipping labels](manage-shipping-labels.md)</li></ul>|

## Code examples

The following sample provides detailed code that demonstrate how to use the Microsoft Hardware API along with a complete end to end prebuilt solution created by the Microsoft Surface and Devices team:

* [C# sample](https://download.microsoft.com/download/C/F/4/CF404E53-87A0-4204-BA13-A64B09A237C1/HardwareApiCSharpSample.zip)

[Hardware dashboard API samples (GitHub)](https://aka.ms/hpc_async_api_samples)

[Surface Dev Center Manager tool (GitHub)](https://github.com/Microsoft/SDCM)

## Additional help

If you have questions about the Microsoft Store submission API or need assistance managing your submissions with this API, visit the [support page](https://partner.microsoft.com/dashboard/account/help?returnUri=https://developer.microsoft.com/dashboard/hardware) and request help.

## Related topics

[What is Azure Active Directory?](/azure/active-directory/fundamentals/active-directory-whatis)