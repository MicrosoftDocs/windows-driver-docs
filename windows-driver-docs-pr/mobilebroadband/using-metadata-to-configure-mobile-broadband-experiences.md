---
title: Using metadata to configure mobile broadband experiences
description: Using metadata to configure mobile broadband experiences
ms.assetid: d3ceab6e-550f-4852-8ee0-4a261c238434
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using metadata to configure mobile broadband experiences


You can provide metadata to customize various aspects of the Windows 8, Windows 8.1, and Windows 10 mobile broadband application experience. These include customizing Windows Connection Manager with operator branding, integrating the mobile broadband app with Windows Connection Manager, providing updated information for the Windows APN database, and providing data to provision the PC. Windows 8, Windows 8.1, and Windows 10 includes three sources of metadata you can use:

-   **Windows APN database** The Windows APN database contains pre-provisioned data that is required to connect to the operator's network for the first time. The database is part of Windows 8, Windows 8.1, and Windows 10 and is updated by using Windows Update. The Windows APN database is always available on the PC. For more info about COSA and the APN database, see [COSA/APN database](cosa-apn-database.md).

> [!IMPORTANT] 
> Starting in Windows 10, version 1703, the APN database is replaced by a new format called COSA. Windows 8, Windows 8.1, and versions of Windows 10 before Version 1703 will continue to use the APN database while Windows 10, version 1703 and later use COSA. For a list of frequently asked questions about COSA, see [COSA overview](cosa-overview.md).

-   **Service metadata** Information required for subscription purchase and operator branding. You provide this information as part of the service metadata package. It is stored on the Windows Metadata and Internet Services (WMIS) and downloaded after a mobile broadband device is detected using any available Internet connection. This metadata can also be preinstalled onto a PC by the OEM, but you must preinstall the package that was downloaded from the hardware developer section of the Windows Dev Center - Hardware. For more info about the service metadata, see [Service metadata](service-metadata.md).

-   **Account provisioning metadata** Information generated after a subscription purchase, including Wi-Fi credentials and plan information. This metadata is provided by you to Windows after payment validation, this metadata can be updated by using the provisioning-refresh mechanism. For more info about the account provisioning metadata, see [Account provisioning](account-provisioning.md).

The following diagram shows how the different metadata sources are related and how they are serviced. The service metadata takes priority over information in the Windows APN database.

![this is an overview of mobile broadband](images/mbae-sxs-overview.jpg)

Use the links in this section to learn more about the different types of mobile broadband metadata:

-   [Account provisioning](account-provisioning.md)

-   [COSA/APN database](cosa-apn-database.md)

-   [Service metadata](service-metadata.md)

 

 





