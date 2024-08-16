---
title: Testing your Desktop COSA Database Submission
description: Before submitting a COSA update request to Microsoft, test your desktop COSA database submission by following the steps in this topic.
ms.date: 02/08/2024
author: mhopkins-msft
ms.author: mhopkins
---

# Testing your desktop COSA database submission

Before submitting a COSA update request to Microsoft, it is important for the MNO or MVNO to validate the APN entries that they are about to submit. Microsoft does not have access to your network, so it is your responsibility to ensure the values that are being submitted are valid and work correctly.

## Test your submission for desktop COSA

Use this process for Windows 10, version 1703 and later, including Windows 11.

After you have updated the COSA database with your new APN information via the MO Config Portal, you can [generate a test provisioning package (PPKG)](mobile-operator-configuration-portal-guide.md#create-a-test-package) file to install and test your settings updates.

For more information about installing a provisioning package file, see [Apply a provisioning package](/windows/configuration/provisioning-packages/provisioning-apply-package).

### Modify the local COSA database (desktop COSA)

Follow these steps to test the updated COSA provisioning package (PPKG) you received from Microsoft.

These steps require a script from Microsoft to apply and test the PPKG file. [Download the latest version of the script](https://download.microsoft.com/download/4/d/9/4d9aa128-8ba9-4e78-99e0-b033f5935969/ApplyCosaProvisioning.BAT).

#### Apply the test PPKG file

> [!IMPORTANT]
> Create a backup of the original provisioning package before performing the following actions. The original provisioning package is located at: `%systemroot%\Provisioning\Cosa\Microsoft\Microsoft.Windows.Cosa.Desktop.Client.ppkg`.

1. Remove any SIM from the device.
1. Copy the script and the new PPKG file to a local directory.
1. Open an elevated command prompt window and change to the directory containing the script.
1. Run the script with this syntax to apply the PPKG: `ApplyCosaProvisioning.BAT -a <full path to the PPKG local directory>`.
1. Insert the SIM and await provisioning.

#### Restore the original PPKG file

> [!WARNING]
> Once validation of the new PPKG received from Microsoft has completed, always restore it with the following steps. Restoring back to the original PPKG will ensure that you receive the latest COSA updates via Windows Update.

1. Once validated, remove the SIM from the device.
1. Run the script with this syntax to restore the original PPKG: `ApplyCosaProvisioning.BAT -r`.
1. Insert the SIM for provisioning to take effect, reading the original PPKG.

#### Collect logs in case of failure

To collect logs in the event of a failure during the testing process, follow these steps:

1. Remove any SIM from the device.
1. Run the script with this syntax to start *netsh* logging: `ApplyCosaProvisioning.BAT -l`.
1. Insert the SIM and wait for provisioning to fail.
1. Follow the tool's prompts to end logging.
1. Send the logs to Microsoft in zipped format.

## Submitting COSA changes

Once you’ve finished validation of the PPKG, you can [submit your COSA changes in the MOCP](mobile-operator-configuration-portal-guide.md#making-a-submission).
