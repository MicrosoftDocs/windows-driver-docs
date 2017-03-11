---
title: COSA/APN database
description: COSA/APN database
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 699b797e-c225-47ba-96a5-26b15c91a759
---

# COSA/APN database

Windows 8, Windows 8.1, and Windows 10 include an APN database that is used by Windows Connection Manager to provide a seamless connection experience for end users by supplying and trying available connection APNs based on the user’s mobile broadband device. The APN database contains the information needed to connect to the mobile broadband network, allowing Windows to connect automatically with minimal user input. The database maintains access strings for different mobile network operators, enabling a user’s connection to the operator’s network prior to acquiring any additional software or metadata. For example, a user can get connected without having a mobile broadband app installed.

In addition to provisioning information, the database also includes a URL to the account experience website. After automatically connecting to the operator’s network, the account experience website opens in the default browser, where the user can purchase a subscription or one-time access.

> [!NOTE] 
> Starting in Windows 10 Version 1703, the APN database is replaced by a new format called COSA. Windows 8, Windows 8.1, and versions of Windows 10 before Version 1703 will continue to use the APN database while Windows 10 Version 1703 and later use COSA. For a list of frequently asked questions about COSA, see [COSA FAQ](cosa---faq.md).

## <span id="apndbcon"></span><span id="APNDBCON"></span>APN database contents


To connect to a mobile broadband network, the user typically provides the following information:

-   In Global System for Mobile Communications (GSM) networks, an APN such as **data.contoso.com**.

-   In CDMA networks, an access string that includes a special dial code such as **\#777**, or a Network Access Identifier (NAI) such as **ann@contoso.com**.

-   The user’s credentials (username and password) for the network connection.

Specifically, the APN database includes the following data:

-   **Operator identification data**

    -   For a GSM network, you can submit database entries for the International Mobile Subscriber Identity (IMSI) or Integrated Circuit Card Identifier (ICCID) ranges that your network uses. If you are a mobile virtual network operator (MVNO), you can specify one or more ranges of IMSIs or subscriber identification module (SIM) ICC IDs that you leased from a mobile network operator (MNO).

    -   For CDMA networks, you can submit new database entry for each Provider ID or Provider Name.

    -   To better understand how you can identify MVNOs, see [Delivering experiences for MVNOs](delivering-experiences-for-mvnos.md).

-   **List of purchase APNs and access strings**

    -   For a GSM network, a list of APNs that have a username and password to purchase the subscription.

    -   For a CDMA network, a list of NAIs to purchase the subscription.

-   **List of Internet connect APNs and access strings**

    -   For a GSM network, a list of APNs that have a username and password to connect to the Internet.

    -   For a CDMA network, a list of NAIs that are used to connect to the Internet.

-   **Account Experience URL** URL for a first-time purchase account experience web site.

-   **Certificate Data** Certificate information for account provisioning metadata. This includes Certificate Issuer Name and Subject Name, and is used to verify that Account Provisioning that is provided by a purchase web site comes from the user’s authorized web service.

For more information on the APN database XML schema, see [APN database schema reference](apn-database-schema-reference.md).

## <span id="abndbsub"></span><span id="ABNDBSUB"></span>APN database submission and maintenance


If you want to request a new APN or update an existing one, see [APN database submission](apn-database-submission.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20APN%20database%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




