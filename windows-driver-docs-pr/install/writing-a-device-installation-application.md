---
title: Writing a Device Installation Application
description: Writing a Device Installation Application
ms.assetid: 9927e2e0-6c8e-437f-98ce-595bd304ec72
keywords:
- installation applications WDK , about writing installation applications
- device installation applications WDK , about writing installation applications
- Device setup WDK device installations , writing installation applications
- installing devices WDK , writing installation applications
- writing device installation applications
- installation applications WDK
- device installation applications WDK
- applications WDK device installation
- device installations WDK , applications
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing a Device Installation Application





**Note**  Features described in this section are not supported in universal or mobile driver packages. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

If your [driver package](driver-packages.md) includes drivers and INF files that replace "inbox" drivers and INF files, or if your package includes device-specific applications, it should include a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) that installs those components. The device installation application and distribution medium should be compatible with AutoRun, so that AutoRun starts the application automatically when a user inserts your distribution medium. For more information about AutoRun, see [Creating an AutoRun-Enabled Application](https://msdn.microsoft.com/library/windows/desktop/cc144206).

For guidelines about how to write a device installation application, see [Guidelines for Writing Device Installation Applications](guidelines-for-writing-device-installation-applications.md).

Your [driver package](driver-packages.md) must handle two situations:

1.  The user plugs in your hardware before inserting your distribution medium. This is commonly referred to as a [hardware-first installation](hardware-first-installation.md).

2.  The user inserts your distribution medium before plugging in your hardware. This is commonly referred to as a [software-first installation](software-first-installation.md).

 

 





