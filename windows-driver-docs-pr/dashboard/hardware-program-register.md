---
title: Register for the Microsoft Windows Hardware Developer Program
description: How to register for the Microsoft Windows Hardware Developer Program
ms.topic: article
ms.date: 01/18/2023
---

# Register for the Microsoft Windows Hardware Developer Program

This article shows you how to register for the Microsoft Windows Hardware Developer Program. When you register for the Hardware Developer Program, you will be prompted to accept the following agreements

- Code Signing Agreement

- Windows Hardware Compatibility Agreement

- Windows Logo License Agreement (LLA) (ver. 2021)

- Windows Analytics Agreement (ver. 2.0)

## Prerequisites

- If you have an existing organization Dev Center account that you want to use for the Hardware program, sign in with it before you begin registration.

- You must have an Extended Validation (EV) code signing certificate. Check whether your organization already has a code signing certificate. If your company already has a certificate, have the certificate available. If your organization doesn't have a certificate, you'll need to [purchase an EV certificate](code-signing-reqs.md#ev-certificate-signed-drivers). You only need the certificate to register for the Hardware Developer Program. You don't need to sign your driver with it.

- You'll need to sign in with your organization’s Microsoft Entra ID [Global administrator](/azure/active-directory/users-groups-roles/directory-assign-admin-roles) account. If you don’t know whether your organization has an Microsoft Entra ID directory, contact your IT department. If your organization doesn’t have an Microsoft Entra ID directory, you'll be able to create one for free during the registration process.

- You must have the authority to sign legal agreements on behalf of your organization.

## Register for the Hardware Developer Program

To register for the Hardware Developer Program:

1. Go to the [Hardware Developer Program registration](https://partner.microsoft.com/dashboard/Registration/Hardware).

1. Read the prerequisites to make sure you have what you need, and then select **Next**.

    :::image type="content" source="./images/hardware-program-register/registration-start.png" alt-text="Screenshot of the first page of the Hardware Developer Program registration process. The 'Next' button is selected.":::

1. If your organization has an Microsoft Entra ID global administrator account, select **Sign in to Microsoft Entra ID**. If your organization doesn't have an Microsoft Entra ID directory, select **Create a new directory for free**. Follow the directions to create an account and sign in with your new global administrator user name and password.

    :::image type="content" source="./images/hardware-program-register/registration-work-account.png" alt-text="Screenshot of the Microsoft Entra ID page of the Hardware Developer Program registration process. The 'Sign in to Microsoft Entra ID' button is selected.":::

1. Now that you've signed in to Microsoft Entra ID, select the country or region where you live or where your business is located.

    :::image type="content" source="./images/hardware-program-register/registration-select-country.png" alt-text="Screenshot of the Account country page of the Hardware Developer Program registration process. ":::

>[!IMPORTANT]
>Once you complete your account information, you can't change your country/region.

1. Enter your company display name. Customers will see your apps, add-ins, extensions, or services listed under this name.

   :::image type="content" source="./images/hardware-program-register/registration-company-name.png" alt-text="Screenshot of the Company display name textbox in the Hardware Developer Program registration process. The textbox has the value 'Contoso Display Name' ":::

1. Enter your personal contact info. Microsoft will use this info for account verification and to contact you. When you're done, select **Next** at the top of the page.

   :::image type="content" source="./images/hardware-program-register/registration-personal-info.png" alt-text="Screenshot of the 'Your personal contact info' section in the Hardware Developer Program registration process.":::

1. You are now in the **Certificate** section of the registration process. In order to secure your digital information, you must use your company's Extended Validation (EV) code signing certificate. If your company doesn't have an EV certificate, you can purchase one from an authorized certificate authority. Once you have your code signing certificate, select **Next**.

   :::image type="content" source="./images/hardware-program-register/registration-ev-cert.png" alt-text="Screenshot of the 'Get a code signing certificate' section in the Hardware Developer Program registration process.":::

1. Now you'll need to sign and upload your file. Follow the steps as directed on the **Registration - Sign and upload your file** page.

    > [!NOTE]
    > You can sign the signable file with your certificate offline and return later to upload it. When you return, be sure to sign in with your Microsoft Entra ID global administrator account to resume the process.

1. After you've uploaded your file, select **Next** at the bottom of the page.

1. Review all of your information, and then select **Submit**.

## Next Steps

> [!div class="nextstepaction"]
> [Manage users and permissions](hardware-dashboard-users-manage.md)

To learn how to create your first hardware submission, see:

> [!div class="nextstepaction"]
> [Hardware submissions](hardware-submission-create.md).

## Support

If you need support during the registration process, you can [open a support ticket](https://aka.ms/AAgnelg).  
