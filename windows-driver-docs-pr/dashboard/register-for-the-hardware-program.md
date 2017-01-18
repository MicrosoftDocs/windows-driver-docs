---
title: Register for the Hardware Program
description: Register for the Hardware Program
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8E947636-7F0E-4C31-9149-D6BF60D84226
---

# Register for the Hardware Program


Your company's administrator must [register](http://go.microsoft.com/fwlink/?LinkID=828002) for the Windows Hardware Dev Center program.

## <span id="Before_you_sign_up"></span><span id="before_you_sign_up"></span><span id="BEFORE_YOU_SIGN_UP"></span>Before you sign up


Review the following requirements before you start the registration process.

-   If you have an existing company Dev Center account that you want to use for the Hardware program, sign in with it before you begin registration.

-   You must have an Extended Validation (EV) code signing certificate. Check whether your company already has a code signing certificate. If your company already has a certificate, have the certificate available as you will be asked to sign a file. If your company does not have a certificate, you will need to buy one as part of the registration process.

    For information about code signing certificates and how to get a certificate, see [Get a code signing certificate](get-a-code-signing-certificate.md).

-   You will need to sign in with your organization’s Azure Active Directory (Azure AD) [Global administrator](http://go.microsoft.com/fwlink/?LinkId=746654) account. If you don’t know whether your organization has an Azure AD directory, contact your IT department. If your organization doesn’t have an Azure AD directory, you must be able to create one.

-   You must have the authority to sign legal agreements on behalf of your organization.

## <span id="Registration_steps"></span><span id="registration_steps"></span><span id="REGISTRATION_STEPS"></span>Registration steps


There are four main steps to the Hardware Program registration.

1.  Get a code signing certificate

    -   Ensure you have a code signing certificate

    -   If you do not have a certificate, you must buy one and have it available.

2.  Sign and upload a file

    -   Download the provided signable file.

    -   Download the signtool.exe signing tool. The tool is available as part of the [Windows SDK download](http://go.microsoft.com/fwlink/p/?linkid=84091).

    -   Sign the signable file with your code signing certificate.

    -   Upload the signed file. Your company name and ID number is extracted from the signed file.

3.  Sign in with an Azure AD Global administrator account

    -   If your company already has an Azure AD directory, sign in with a [Global administrator](http://go.microsoft.com/fwlink/?LinkId=746654)account.

    -   If your company does not have an Azure AD directory, you must create one and sign in.

4.  Account details

    -   Enter in account details, such as company display name and personal contact information.

    -   Sign the required hardware developer legal agreements.

## <span id="After_registration"></span><span id="after_registration"></span><span id="AFTER_REGISTRATION"></span>After registration


After your registration is complete, additional administrative tasks are available:

-   [Manage users and permissions](https://msdn.microsoft.com/library/windows/hardware/mt786457)

When you are finished with administrative tasks, you are ready to create your first hardware submission. See [Hardware submissions](hardware-certification-submissions.md) for information and instructions.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Register%20for%20the%20Hardware%20Program%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




