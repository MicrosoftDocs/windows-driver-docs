---
title: Manage your service account credentials
description: Manage your service account credentials
ms.assetid: 6e51fc43-257f-4fba-9e6f-5a289b834ab9
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Manage your service account credentials


> [!IMPORTANT]  
> The dashboard submission REST APIs will no longer be available for use as of the end of October 2016. APIs for driver submissions are under consideration for a future release.

 

As an administrator, you can create, manage, and disable service accounts for your organization. The credentials associated with these service accounts are required to authenticate and authorize your clients who are using the [File Signing Services](https://msdn.microsoft.com/library/windows/hardware/dn771767.aspx). If your organization would like access to this functionality, contact <sysdev@microsoft.com>

**In this section:**

-   [To generate a new service account](#to-generate-a-new-service-account)

-   [To get the service account credentials](#to-get-the-service-account-credentials)

-   [To generate a new password](#to-generate-a-new-password)

-   [To disable a service account](#to-disable-a-service-account)

## To generate a new service account


1.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account. This account must be an Administrator for your organization in the Dashboard.

2.  On the **Dashboard** page, click **Administration**.

3.  On the **Administration** page on **Your organization** tile, click **Create and manage your service credentials**.

4.  Under **Generate service account credential**, in **Account name** enter a user friendly name for the service account you are creating, and then click **Generate**.

    Note that the effective data is today's date and the expiration date is three years from today. This is set by default and you cannot change the dates.

A new account is created and provisioned with Azure Access Control service (ACS). The account details are displayed at the top of the table under **Manage service account credentials**. To get the service account credentials, click on the account ID, which takes you to the account details page.

**Note**  
Microsoft does not store the password associated with this account.

 

## To get the service account credentials


1.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account. This account must be an Administrator for your organization in the Dashboard.

2.  On the **Dashboard** page, click **Administration**.

3.  On the **Administration** page on **Your organization** tile, click **Create and manage your service account credentials**.

4.  On the **Manage service account credentials** page, click on the account ID of the service account that you want.

    It takes you the account details page and displays the **Account ID**, **Account password**, **Effective date**, and **Expiration date**. The dates are shown are in UTC time zone.

5.  Copy the account ID and password and provide them in a secure manner to the authorized users in your organization.

## To generate a new password


You can only generate a new password for an active service account; if the account is disabled or expired, you cannot generate a new password.

1.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account. This account must be an Administrator for your organization in the Dashboard.

2.  On the **Dashboard** page, click **Administration**.

3.  On the **Administration** page on **Your organization** tile, click **Create and manage your service account credentials**.

4.  On the **Manage service account credentials** page, click on the account ID.

5.  On the **Manage account: &lt;Your account name&gt;** page, click the **Password** tab, and then click **Regenerate** to create a new password.

    The password is effective immediately.

6.  Copy the account ID and password and provide them in a secure manner to the authorized users in your organization.

**Note**  
Don't forget to send the new password to your account users.

 

## To disable a service account


1.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account. This account must be an Administrator for your organization in the Dashboard.

2.  On the **Dashboard** page, click **Administration**.

3.  On the **Administration** page on **Your organization** tile, click **Create and manage your service account credentials**.

4.  On the **Manage service account credentials** page, click on the account ID.

5.  On the **Manage account: &lt;Your account name&gt;** page, click the **Disable** tab, and then click **Disable**.

This disables the account permanently. You must create a new account or use an existing account for access.

 

 

