---
title: Manage hardware submissions
description: Manage hardware submissions for the Partner Center
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing hardware submissions in the Partner Center

After you submit your product for the Windows Hardware Compatibility Program for Windows 10 (or the certification program for previous Windows versions), you can manage it through the dashboard.

## Find a hardware submission

See [Find hardware submission](find-hardware-submission.md).

## Update an HCK or HLK hardware submission using the Driver Update Acceptable (DUA) process

> [!Note]
> DUA submissions can only be created off of an Initial Submission.
> - DUA submissions shared with another company will not see the download DUA Shell button as you cannot do a DUA on a DUA submission.

For instructions on how to create a DUA submission from a DUA Shell, see [Create a driver only update package](/windows-hardware/test/hlk/user/create-a-driver-only-update-package).

## Registering an ExtensionId

When you submit an extension INF to be signed, the dashboard checks if the specified **ExtensionId** was previously registered with a different account.
If it was, you'll see a message prompting you to provide a different ID. If not, the dashboard associates it with your account.

For more information about specifying **ExtensionId**, see [Using an extension INF file](../install/using-an-extension-inf-file.md).

Note that in your submissions, you may only use ExtensionIDs that are registered to your account.

## Related topics

- [Create a new hardware submission](create-a-new-hardware-submission.md)
- [Get drivers signed by Microsoft for multiple Windows versions](get-drivers-signed-by-microsoft-for-multiple-windows-versions.md)
- [Driver flighting](driver-flighting.md)
