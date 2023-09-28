---
title: Introduction to the COSA database
description: Introduction to the COSA database
ms.date: 09/15/2023
---

# Introduction to the COSA database

This section contains information about the COSA database. COSA is a newer format used in Windows 10, version 1703 and later. The APN database is used for operating system releases before Windows 10, version 1703.

The Country and Operator Settings Asset (COSA) database is used by Windows networking components, such as the Windows Connection Manager, to provide a seamless connection experience for end users by supplying and trying available connection APNs based on the user's mobile broadband device. The COSA database contains the information needed to connect to the mobile broadband network, allowing Windows to connect automatically with minimal user input. The database contains access strings for different mobile network operators, enabling a user's connection to the operator's network prior to acquiring any additional software or metadata. For example, a user can get connected without having a mobile broadband app installed.

In addition to provisioning information, the COSA database also includes a URL to the account experience website. After automatically connecting to the operator's network, the account experience website opens in the default browser, where the user can purchase a subscription or one-time access.

The following topics present further information about APNs, COSA, and APN database.

- [COSA overview](cosa-overview.md)
- [COSA/APN database submission](planning-your-desktop-cosa-apn-database-submission.md)
