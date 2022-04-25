---
title: Update a hardware submission
description: Learn how update a specific Windows hardware submission.
ms.topic: article
ms.date: 09/24/2018
---

# Update a hardware submission

After you submit your product for the Windows Hardware Compatibility Program for Windows 10 (or the certification program for previous Windows versions), you can then update it through the dashboard. This article describes the different options for updating your drivers.

## Use the Driver Update Acceptable (DUA) process

 DUA submissions can only be created off of an initial submission. DUA submissions shared with another company won't see the download DUA Shell button as you cannot do a DUA on a DUA submission.

For instructions on how to create a DUA submission from a DUA Shell, see [Create a driver only update package](/windows-hardware/test/hlk/user/create-a-driver-only-update-package).

## Register an ExtensionId

Prior to Windows 10, Windows selected a single driver package to install for a given device. This resulted in large, complex driver packages that included code for all scenarios and configurations, and each minor update required an update to the entire driver package. Starting in Windows 10, you can split INF functionality into multiple components, each of which can be serviced independently. The core driver package installed on a device is now called the base driver package and is handled by the system in the same way driver packages have been handled prior to Windows 10. To extend a base driver package's functionality, provide an extension INF in a separate driver package. For more information about using **ExtensionId**, see [Using an extension INF file](../install/using-an-extension-inf-file.md).

>[!NOTE]
>In your submissions, you may only use ExtensionIDs that are registered to your account.

## Next Steps

> [!div class="nextstepaction"]
> [Create a hardware submission](hardware-submission-create.md)

> [!div class="nextstepaction"]
> [Manage hardware submissions](hardware-submission-manage.md)

> [!div class="nextstepaction"]
> [Windows HLK Getting Started Guide](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started.md)

> [!div class="nextstepaction"]
> [Driver flighting](driver-flighting.md)
