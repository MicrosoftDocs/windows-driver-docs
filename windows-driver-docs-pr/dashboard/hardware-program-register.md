---
title: Register for the Microsoft Windows Hardware Developer Program
description: How to register for the Microsoft Windows Hardware Developer Program
ms.topic: article
ms.date: 01/15/2025
---

# Register for the Microsoft Windows Hardware Developer Program

This article shows you how to register for the Microsoft Windows Hardware Developer Program. When you register for the Hardware Developer Program, you're prompted to accept the following agreements

- Code Signing Agreement
- Windows Hardware Compatibility Agreement
- Microsoft Marks License Agreement (MMLA) (ver. 2024)
- Windows Analytics Agreement (ver. 2.0)

## Prerequisites

- If you have an existing organization Dev Center account that you want to use for the Hardware program, sign in with it before you begin registration.
- You must have an Extended Validation (EV) code signing certificate. Check whether your organization already has a code signing certificate. If your company already has a certificate, have the certificate available. If your organization doesn't have a certificate, you must [purchase an EV certificate](code-signing-reqs.md#ev-certificate-signed-drivers). You only need the certificate to register for the Hardware Developer Program. You don't need to sign your driver with it.
- Sign in with your organization's Microsoft Entra ID [Global administrator](/azure/active-directory/users-groups-roles/directory-assign-admin-roles) account. If you don't know whether your organization has a Microsoft Entra ID directory, contact your IT department. If your organization doesn't have a Microsoft Entra ID directory, you're able to create one for free during the registration process.
- You must have the authority to sign legal agreements on behalf of your organization.

## Register for the Hardware Developer Program

To register for the Hardware Developer Program:

1. Go to the [Hardware Developer Program registration](https://partner.microsoft.com/dashboard/account/exp/enrollment/welcome?cloudInstance=Global&accountProgram=hardware).

1. If your organization has a Microsoft Entra ID global administrator account, select **Login with work account**. If your organization doesn't have a Microsoft Entra ID directory, select **Create work account**. Follow the directions to create an account and sign in with your new global administrator user name and password.

    :::image type="content" source="./images/hardware-program-register/registration-work-account.png" alt-text="Screenshot of the Microsoft Partner Center page for the Hardware Developer Program registration process. The **Login with work account** button is selected.":::

1. Confirm that you signed in with global administrator credentials and select **Next**.

    :::image type="content" source="./images/hardware-program-register/registration-welcome.png" alt-text="Screenshot of the Microsoft Partner Center welcome page.":::

1. In next screen, you'll see list of available programs in Partner Center. The **Hardware** program is selected by default. Select **Go to Dashboard**.

    :::image type="content" source="./images/hardware-program-register/registration-program-join.png" alt-text="Screenshot of the Microsoft Partner Center 'Join programs' page.":::

1. Provide your company information or D-U-N-S number and select **Search** to find your company details in external company databases.

    :::image type="content" source="./images/hardware-program-register/registration-company-info.png" alt-text="Screenshot of the Microsoft Partner Center company information page.":::

1. Select a record from search results that represents your company. If no record matches, you can choose to provide company details manually by selecting **I don't have D-U-N-S number** at bottom right corner of screen.

    :::image type="content" source="./images/hardware-program-register/registration-company-search.png" alt-text="Screenshot of the Microsoft Partner Center company search page.":::

1. Provide company information and ensure the details are accurate.

1. Provide a legal contact with the authority to sign agreements on behalf of your company. Microsoft emails the legal contact for account verification purposes.

1. Review the agreement terms and select **Accept and Continue**.

1. Your registration request is now submitted. Now, upload the extended validation (EV) code signing certificate from Manage certificates page. Review the instructions and upload the EV certificate. The EV certificate is required for your request to be considered for approval.

    :::image type="content" source="./images/hardware-program-register/registration-manage-certificates.png" alt-text="Screenshot of the Microsoft Partner Center manage certificates page.":::

1. After uploading the certificate, monitor the global administrator mail box for a questionnaire requiring more information about your business. Complete the questionnaire when received.

1. After all approvals are complete, your global administrator will receive an email confirming approvals and next steps.

## Next Steps

> [!div class="nextstepaction"]
> [Manage users and permissions](hardware-dashboard-users-manage.md)

To learn how to create your first hardware submission, see:

> [!div class="nextstepaction"]
> [Hardware submissions](hardware-submission-create.md).

## Support

If you need support during the registration process, you can [open a support ticket](https://aka.ms/AAgnelg).  
