---
title: Specify account information in the Mobile Broadband Metadata Authoring Wizard
description: Specify account information in the Mobile Broadband Metadata Authoring Wizard
ms.assetid: FFE19760-360F-482C-BBD8-7068D2DD34E5
keywords:
- Specify account information in the Mobile Broadband Metadata Authoring Wizard
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specify account information in the Mobile Broadband Metadata Authoring Wizard


To specify your mobile broadband account information, fill out the following optional fields on the **Accounts** tab:

-   Next to **Purchase Profile**, click **Browse**, and then select the profile based on the WWAN v2 profile schema that defines which APN to connect to in order to complete the purchase of the plan that the user selected.

    **Purchase Profile** is used to establish limited connectivity to enable end users to purchase a new subscription. GSM operators who have only one Purchase APN for all subscribers can use the mobile broadband service metadata to provide that to the PC. If you have multiple Purchase APNs, don't specify a Purchase Profile here. Instead, use APN Database or Account Provisioning Metadata to set the appropriate purchase APN.

-   Next to **Internet Profile**, click **Browse**, and then select the profile based on the WWAN v2 profile schema that defines which APN to connect to the Internet.

    **Internet Profile** is used by Connection Manager to automatically connect to the network. Every mobile broadband subscription can have one default profile that's used to connect to the home network operator. GSM operators who have only one Internet Profile for all subscribers can use the mobile broadband service metadata to provide it to the PC. If you have multiple Purchase APNs, don't specify an Internet Profile here. Instead, use APN Database or Account Provisioning Metadata to set the appropriate Internet APN.

    For more detailed information on the mobile broadband profile schema, see [Service Metadata Package Schema Reference for Windows 8](http://go.microsoft.com/fwlink/p/?LinkId=226755).

-   Next to **PIN unlock function**, select **Allow standard users to perform PIN unlock on mobile broadband SIMs** to enable standard users to perform PIN unlock functions on their mobile broadband SIMs for your service.

    For more information about PIN unlock, see [Overview of Mobile Broadband in Windows 8](http://go.microsoft.com/fwlink/p/?LinkId=242052).

-   Under **Trusted Certificates**, fill out the **Subject** and **Issuer** fields. This information comes from the certificate that you're using to sign your metadata package.

    (If you're not using web browser-based XML provisioning, you can skip this step.)

    Trusted certificate hashes are used to validate the digital signature on a provisioning file delivered from the mobile network operator’s web page or captive portal during initial setup. This supports the scenario where a user purchases the service before the mobile broadband app is installed. Both fields should be formatted as Distinguished Names and must match the **Subject** and **Issuer** fields of the digital certificate that's used to sign provisioning files on the purchase web site. For more information about Distinguished Names, see Section RFC 4514 in [String Representation of Distinguished Names on the Internet Engineering Task Force website](http://go.microsoft.com/fwlink/p/?LinkId=242261).

    For more information about provisioning, see [Service Metadata Package Schema Reference for Windows 8](http://go.microsoft.com/fwlink/p/?LinkId=226755).

 

 





