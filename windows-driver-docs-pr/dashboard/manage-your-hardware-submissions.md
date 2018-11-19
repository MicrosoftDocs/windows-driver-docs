---
title: Manage hardware submissions
description: Manage hardware submissions for the Windows Hardware Dev Center Dashboard
ms.assetid: C4C3C56F-8E92-4CB1-A57B-942E466ECD3D
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing hardware submissions in the Windows Hardware Dev Center dashboard


After you submit your product for the Windows Hardware Compatibility Program for Windows 10 (or the certification program for previous Windows versions), you can manage it through the dashboard.

## Find a hardware submission

See [Find hardware submission](find-hardware-submission.md).

## Update an HCK hardware submission using the Driver Update Acceptable (DUA) process

See [Create a driver only update package](https://docs.microsoft.com/windows-hardware/test/hlk/user/create-a-driver-only-update-package).

## Registering an ExtensionId

When you submit an extension INF to be signed, the dashboard checks if the specified **ExtensionId** was previously registered with a different account.
If it was, you'll see a message prompting you to provide a different ID. If not, the dashboard associates it with your account.

For more information about specifying **ExtensionId**, see [Using an extension INF file](https://docs.microsoft.com/windows-hardware/drivers/install/using-an-extension-inf-file). 

Note that in your submissions, you may only use ExtensionIDs that are registered to your account. 

## Related topics

- [Create a new hardware submission](create-a-new-hardware-submission.md)
- [Get drivers signed by Microsoft for multiple Windows versions](get-drivers-signed-by-microsoft-for-multiple-windows-versions.md)
- [Driver flighting](driver-flighting.md)


