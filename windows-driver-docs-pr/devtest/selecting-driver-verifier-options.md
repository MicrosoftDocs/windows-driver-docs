---
title: Selecting Driver Verifier Options
description: Selecting Driver Verifier Options
ms.assetid: 02ef5dd6-7532-4979-b45c-a9ee81582788
keywords:
- Driver Verifier WDK , option selections
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Selecting Driver Verifier Options


## <span id="ddk_selecting_driver_verifier_options_tools"></span><span id="DDK_SELECTING_DRIVER_VERIFIER_OPTIONS_TOOLS"></span>


Driver Verifier options can be selected by using the [**Verifier Command Line**](verifier-command-line.md), or by using Driver Verifier Manager. There are two versions of Driver Verifier Manager -- one for [Windows 2000](driver-verifier-manager--windows-2000-.md) and one for [Windows XP and later](driver-verifier-manager--windows-xp-and-later-.md).

### <span id="verifier_command_line"></span><span id="VERIFIER_COMMAND_LINE"></span>Verifier Command Line

To activate or deactivate individual options, specify the desired options after the **/flags** parameter.

(Windows 2000 only) To control the level of I/O Verification, use the **/iolevel** parameter.

(Windows XP and later) To activate the standard options -- [Special Pool](special-pool.md), [Force IRQL Checking](force-irql-checking.md), [Pool Tracking](pool-tracking.md), [I/O Verification](i-o-verification.md), [DMA Verification](dma-verification.md), and [Deadlock Detection](deadlock-detection.md) -- use the **/standard** parameter. Starting with Windows Vista, the standard options also include [Security Checks](security-checks.md) and [Miscellaneous Checks](miscellaneous-checks.md). Starting with Windows 8, the standard options also include [DDI compliance checking](ddi-compliance-checking.md).

(Windows Server 2003 and later) To activate [Disk Integrity Checking](disk-integrity-checking.md), use the **/disk** parameter.

To deactivate all options and clear the verified driver list, use the **/reset** parameter.

See [**Verifier Command Line**](verifier-command-line.md) for details.

### <span id="driver_verifier_manager__windows_2000_"></span><span id="DRIVER_VERIFIER_MANAGER__WINDOWS_2000_"></span>Driver Verifier Manager (Windows 2000)

To activate or deactivate individual options, select the **Settings** tab. Driver Verifier's options are listed in the **Verification Type** section ([Special Pool](special-pool.md), [Force IRQL Checking](force-irql-checking.md), [Low Resources Simulation](low-resources-simulation.md), [Pool Tracking](pool-tracking.md), and [I/O Verification](i-o-verification.md)). Check whichever options you wish to activate, and clear those you wish to deactivate. If I/O Verification is selected, you can choose between Level 1 and Level 2 (choosing Level 2 enables both Level 1 and Level 2 tests). To choose which drivers you wish to verify, see [Selecting Drivers to be Verified](selecting-drivers-to-be-verified.md).

To turn on the standard options -- [Special Pool](special-pool.md), [Force IRQL Checking](force-irql-checking.md), [Pool Tracking](pool-tracking.md), and [I/O Verification](i-o-verification.md) Level 2 -- select the **Settings** tab. Press the **Preferred Settings** button. This button also selects the **Verify All Drivers** option button. If you wish to now change the list of drivers verified, see [Selecting Drivers to be Verified](selecting-drivers-to-be-verified.md); otherwise, press **Apply**.

To deactivate all options and clear the verified driver list, select the **Settings** tab. Press the **Reset All** button. Then press **Apply**.

### <span id="driver_verifier_manager__windows_xp_and_later_"></span><span id="DRIVER_VERIFIER_MANAGER__WINDOWS_XP_AND_LATER_"></span>Driver Verifier Manager (Windows XP and later)

In Windows XP and later, Driver Verifier Manager can select options in a variety of ways:

-   To control exactly which options are active, select the **Create custom settings** task and press **Next**. On the next screen, select **Select individual settings from a full list**, and press **Next**. The next screen lists all of Driver Verifier's options (Special Pool, Pool Tracking, Force IRQL Checking, I/O Verification, Enhanced I/O Verification, Deadlock Detection, DMA Verification, and Low Resources Simulation -- plus Disk Integrity Checking in Windows Server 2003 and later). Starting with Windows Vista, the options also include [Security Checks](security-checks.md) and [Miscellaneous Checks](miscellaneous-checks.md). Starting with Windows 8, the options also include [Power Framework Delay Fuzzing](concurrency-stress-test.md), [DDI compliance checking](ddi-compliance-checking.md), [Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md), and [Invariant MDL Checking for Driver](invariant-mdl-checking-for-driver.md). Starting with Windows 8.1, the options also include [NDIS/WIFI verification](ndis-wifi-verification.md), [Kernel synchronization delay fuzzing](kernel-synchronization-delay-fuzzing.md), [VM switch verification](vm-switch-verification.md), and [Systematic low resources simulation](systematic-low-resource-simulation.md). Check whichever options you wish to activate.

-   To choose from predefined sets of options, select the **Create custom settings** task and press **Next**. On the next screen, select **Enable predefined settings** and select any of the check boxes. Selecting the **Standard settings** enables Special Pool, Force IRQL Checking, Pool Tracking, I/O Verification, DMA Verification, and Deadlock Detection. Starting with Windows Vista, selecting the standard options also enables [Security Checks](security-checks.md) and [Miscellaneous Checks](miscellaneous-checks.md). Starting with Windows 8, selecting the standard options also enables [DDI compliance checking](ddi-compliance-checking.md). Selecting the **Low resource simulation** check box enables Low Resources Simulation. Selecting the **Enhanced I/O Verification** check box enables Enhanced I/O Verification. In Windows Server 2003 and later, selecting the **Disk integrity checking** check box enables Disk Integrity Checking.

-   To choose the standard options, select the **Create standard settings** task. The standard settings include Special Pool, Force IRQL Checking, Pool Tracking, I/O Verification, DMA Verification, and Deadlock Detection. Starting with Windows Vista, the standard settings also include [Security Checks](security-checks.md) and [Miscellaneous Checks](miscellaneous-checks.md). Starting with Windows 8, the standard settings also include [DDI compliance checking](ddi-compliance-checking.md).

Note that starting with Windows Vista, if the **Low resources simulation** check box is selected using either of the first two methods listed above, the next screen is the screen for setting the Probability, Applications, Pool Tags, and System Start Delay Time options for Low Resources Simulation. Set these options to the desired values.

When you have completed one of these steps, press **Next**. See [Selecting Drivers to be Verified](selecting-drivers-to-be-verified.md) for the next step.

To deactivate all options and clear the verified driver list, select the **Delete existing settings** task. Then press **Finish**.

### <span id="reboot_required"></span><span id="REBOOT_REQUIRED"></span>Reboot Required

Beginning in Windows Vista, you can activate and deactivate all options without restarting ("rebooting") the computer except for [DDI compliance checking](ddi-compliance-checking.md), [Power Framework Delay Fuzzing](concurrency-stress-test.md), [Storport Verification](dv-storport-verification.md), or [SCSI Verification](scsi-verification.md). For details, see [Using Volatile Settings](using-volatile-settings.md).

On systems prior to Windows Vista, you can activate and deactivate certain options without rebooting, but only after you have enabled Driver Verifier on at least one driver then rebooted the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

 

 





