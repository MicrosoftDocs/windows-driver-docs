---
title: Writing a Co-installer
description: Writing a Co-installer
ms.assetid: d5637321-9cff-4b24-8941-d3ca16b0d8c1
keywords:
- Device setup WDK device installations , co-installers
- device installations WDK , co-installers
- installing devices WDK , co-installers
- co-installers WDK device installations , about co-installers
- coinstallers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing a Co-installer





**Note**  Features described in this section are not supported in universal or mobile driver packages. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

A co-installer is a Microsoft Win32 DLL that assists in device installation. Co-installers are called by SetupAPI as "helpers" for Class Installers. For example, a vendor can provide a co-installer to write device-specific information to the registry that cannot be handled by the INF file.

This section includes the following topics:

[Co-installer Operation](co-installer-operation.md)

[Co-installer Interface](co-installer-interface.md)

[Co-installer Functionality](co-installer-functionality.md)

[Handling DIF Codes](handling-dif-codes.md)

[Registering a Co-installer](registering-a-co-installer.md)

 

 





