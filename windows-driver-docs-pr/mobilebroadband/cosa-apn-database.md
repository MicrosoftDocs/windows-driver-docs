---
title: Introduction to COSA/APN Database
description: Introduction to COSA/APN database
ms.date: 01/02/2024
author: mhopkins-msft
ms.author: mhopkins
---

# Introduction to COSA/APN database

This section contains information about both COSA and apndatabase.xml (APN database). COSA is a newer format used in Windows 10, version 1703 and later, while APN database is used for Windows 8, Windows 8.1, and versions of Windows 10 before Windows 10, version 1703.

COSA and the APN database are used by Windows networking components, such as the Windows Connection Manager, to provide a seamless connection experience for end users by supplying and trying available connection APNs based on the user's mobile broadband device. COSA and the APN database contain the information needed to connect to the mobile broadband network, allowing Windows to connect automatically with minimal user input. They maintain access strings for different mobile network operators, enabling a user's connection to the operator's network prior to acquiring any additional software or metadata. For example, a user can get connected without having a mobile broadband app installed.

In addition to provisioning information, COSA and APN database also include a URL to the account experience website. After automatically connecting to the operator's network, the account experience website opens in the default browser, where the user can purchase a subscription or one-time access.

The following topics present further information about APNs, COSA, and APN database.

- [APN schema definition](apn-schema-definition.md)
- [APN elements](apn-elements.md)
- [COSA overview](cosa-overview.md)
- [APN database overview](apn-database-overview.md)
- [COSA/APN database submission](planning-your-desktop-cosa-apn-database-submission.md)
