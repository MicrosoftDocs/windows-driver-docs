---
title: Register for the Microsoft Windows Hardware Developer Program
description: How to register for the Microsoft Windows Hardware Developer Program
ms.topic: article
ms.date: 04/20/2017
---

# How to register for the Microsoft Windows Hardware Developer Program

This article shows you how to register for the Microsoft Windows Hardware Developer Program.

## Prerequisites

- If you have an existing organization Dev Center account that you want to use for the Hardware program, sign in with it before you begin registration.

- You must have an Extended Validation (EV) code signing certificate. Check whether your organization already has a code signing certificate. If your company already has a certificate, have the certificate available, as you will be asked to sign a file. If your organization doesn't have a certificate, you'll need to buy one as part of the registration process.

    For information about code signing certificates and how to get a certificate, see [Get a code signing certificate](get-a-code-signing-certificate.md).

- You'll need to sign in with your organization’s Azure Active Directory (Azure AD) [Global administrator](/azure/active-directory/users-groups-roles/directory-assign-admin-roles) account. If you don’t know whether your organization has an Azure AD directory, contact your IT department. If your organization doesn’t have an Azure AD directory, you'll be able to create one for free during the registration process'

- You must have the authority to sign legal agreements on behalf of your organization.

## Register for the Hardware Developer Program

To register for the Hardware Developer Program:

1. Go to the [Hardware Developer Program registration page](https://go.microsoft.com/fwlink/?LinkID=828002).

1. Read the prerequisites to make sure you have what you need, and then select **Next**.

    :::image type="content" source="./images/register-for-the-hardware-program/registration-start.png" alt-text="Screenshot of the first page of the Hardware Developer Program registration process. The 'Next' button is selected.":::

1. If your organization has an Azure AD global administrator account, select **Sign in to Azure AD**. If your organization doesn't have an Azure AD directory, select **Create a new directory for free** and follow the directions to create an account.

    :::image type="content" source="./images/register-for-the-hardware-program/registration-work-account.png" alt-text="Screenshot of the Azure AD page of the Hardware Developer Program registration process. The 'Sign in to Azure AD' button is selected.":::

1. Download `signtool.exe`. `signtool.exe` is available as part of the [Windows SDK download](https://developer.microsoft.com/windows/downloads/windows-10-sdk).

1. Sign and upload the file provided to you within the **Sign and upload** portion of the registration process.
    > [!NOTE]
    > The following three steps no longer need to be completed within the same browser session.

    1. Download the provided signable file.
    2. Sign the file with signtool.exe and your code signing certificate.
    3. Upload the signed file. Your organization name and ID number is extracted from the signed file.

4. Sign in with an Azure AD Global administrator account

    - If your organization already has an Azure AD directory, sign in with a [Global administrator](/azure/active-directory/users-groups-roles/directory-assign-admin-roles) account.

    - If your organization does not have an Azure AD directory, you must create one and sign in.

5. Account details

    - Enter in account details, such as your organization display name and personal contact information.

    - Sign the required hardware developer legal agreements, located in the account settings tab as shown below:

        ![an image showing the 'agreements' button.](images/legal-agreements-location.png)

## After registration

After your registration is complete, additional administrative tasks are available:

- [Manage users and permissions](managing-user-roles.md)

When you are finished with any administrative tasks, you are ready to create your first hardware submission. See [Hardware submissions](hardware-certification-submissions.md) for information and instructions.

## Support

If you need support during the registration process, you can [open a support ticket](https://aka.ms/AAgnelg).  
