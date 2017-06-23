---
title: COSA/APN database
description: COSA/APN database
ms.assetid: 0E3DA610-090D-4D1E-B67E-A4747252E8BE
ms.author: windowsdriverdev
ms.date: 06/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# COSA/APN database

This section contains information about both COSA and apndatabase.xml (APN database). COSA is a newer format used in Windows 10, version 1703 and later, while APN database is used for Windows 8, Windows 8.1, and versions of Windows 10 before Windows 10, version 1703.

COSA and the APN database are used by Windows networking components, such as the Windows Connection Manager, to provide a seamless connection experience for end users by supplying and trying available connection APNs based on the user’s mobile broadband device. COSA and the APN database contain the information needed to connect to the mobile broadband network, allowing Windows to connect automatically with minimal user input. They maintain access strings for different mobile network operators, enabling a user’s connection to the operator’s network prior to acquiring any additional software or metadata. For example, a user can get connected without having a mobile broadband app installed.

In addition to provisioning information, COSA and APN database also include a URL to the account experience website. After automatically connecting to the operator’s network, the account experience website opens in the default browser, where the user can purchase a subscription or one-time access.

The following topics present further information about APNs, COSA, and APN database.

- [APN schema definition](apn-schema-definition.md)
- [APN elements](apn-elements.md)
- [COSA Overview](cosa-overview.md)
- [APN database overview](apn-database-overview.md)
- [COSA/APN database submission](cosa-apn-database-submission.md)]

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")