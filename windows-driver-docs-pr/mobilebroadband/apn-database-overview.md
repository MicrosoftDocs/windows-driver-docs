---
title: APN database overview
description: APN database overview
ms.assetid: 699b797e-c225-47ba-96a5-26b15c91a759
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# APN database overview

The APN database, or apndatabase.xml, is the provisioning database that Mobile Operators (MOs) use to configure mobile broadband experiences for their networks. It is available in Windows 8, Windows 8.1, and versions of Windows 10 before Windows 10, version 1703.

Starting in Windows 10, version 1703, the APN database is replaced by a new format called COSA. Windows 8, Windows 8.1, and versions of Windows 10 before version 1703 will continue to use the APN database while Windows 10, version 1703 and later use COSA. 

For more info about COSA, see [COSA overview](cosa-overview.md).

To see a list of available settings MOs can configure in the APN database, see [Desktop COSA/APN database settings](desktop-cosa-apn-database-settings.md).

## <span id="apndbcon"></span><span id="APNDBCON"></span>APN database contents


To connect to a mobile broadband network, the user typically provides the following information:

- In Global System for Mobile Communications (GSM) networks, an APN such as **data.contoso.com**.

- In CDMA networks, an access string that includes a special dial code such as **\#777**, or a Network Access Identifier (NAI) such as <strong>ann@contoso.com</strong>.

- The user’s credentials (username and password) for the network connection.

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


If you want to request a new APN or update an existing one, see [COSA/APN database submission](cosa-apn-database-submission.md).
 





