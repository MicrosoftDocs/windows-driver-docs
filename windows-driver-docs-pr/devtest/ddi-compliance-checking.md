---
title: DDI compliance checking
description: The DDI compliance checking option determines whether the driver correctly interacts with the Windows operating system kernel.
ms.assetid: 1E536DE0-071B-4529-B228-DB5DAE71099C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DDI compliance checking


The DDI compliance checking option determines whether the driver correctly interacts with the Windows operating system kernel.

**Note**  This option is available starting with Windows 8. Starting in Windows 8.1, you can test additional rules, by selecting [Activating the DDI compliance checking (additional) option](#activating-the-ddi-compliance-checking-additional-option).



| DDI compliance checking |
|-------------------------|
|                         |

The DDI compliance checking option applies the same device driver interface (DDI) usage rules that [Static Driver Verifier](static-driver-verifier.md) uses to verify that your driver makes function calls at the required IRQL for the function, or correctly acquires and releases spinlocks.

When this option is active and Driver Verifier detects that the driver violates one of the DDI compliance rules, Driver Verifier issues bug check 0xC4 (with Parameter 1 equal to the identifier of the specific compliance rule).

When you select the DDI compliance checking option, the following rules are included.

[**GuardedRegions**](https://msdn.microsoft.com/library/windows/hardware/hh975150) (Starting in Windows 8.1)

[**IoSetCompletionExCompleteIrp**](https://msdn.microsoft.com/library/windows/hardware/hh975178) (Starting in Windows 8.1)

[**IrqlApcLte**](https://msdn.microsoft.com/library/windows/hardware/ff547740)

[**IrqlDispatch**](https://msdn.microsoft.com/library/windows/hardware/ff547743)

[**IrqlExAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff547747)

[**IrqlExApcLte1**](https://msdn.microsoft.com/library/windows/hardware/ff547748)

[**IrqlExApcLte2**](https://msdn.microsoft.com/library/windows/hardware/ff547751)

[**IrqlExApcLte3**](https://msdn.microsoft.com/library/windows/hardware/ff547753)

[**IrqlExPassive**](https://msdn.microsoft.com/library/windows/hardware/ff547756)

[**IrqlIoApcLte**](https://msdn.microsoft.com/library/windows/hardware/ff547759)

[**IrqlIoDispatch**](https://msdn.microsoft.com/library/windows/hardware/jj157234)

[**IrqlIoPassive1**](https://msdn.microsoft.com/library/windows/hardware/ff547763)

[**IrqlIoPassive2**](https://msdn.microsoft.com/library/windows/hardware/ff547766)

[**IrqlIoPassive3**](https://msdn.microsoft.com/library/windows/hardware/ff547780)

[**IrqlIoPassive4**](https://msdn.microsoft.com/library/windows/hardware/ff547787)

[**IrqlIoPassive5**](https://msdn.microsoft.com/library/windows/hardware/ff547796)

[**IrqlKeApcLte1**](https://msdn.microsoft.com/library/windows/hardware/ff547803)

[**IrqlKeApcLte2**](https://msdn.microsoft.com/library/windows/hardware/ff547806)

[**IrqlKeDispatchLte**](https://msdn.microsoft.com/library/windows/hardware/ff547812)

[**IrqlKeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff547830)

[**IrqlKeSetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff547835)

[**IrqlMmApcLte**](https://msdn.microsoft.com/library/windows/hardware/ff547855)

[**IrqlMmDispatch**](https://msdn.microsoft.com/library/windows/hardware/hh975186)

[**IrqlObPassive**](https://msdn.microsoft.com/library/windows/hardware/ff547873)

[**IrqlPsPassive**](https://msdn.microsoft.com/library/windows/hardware/ff547882)

[**IrqlReturn**](https://msdn.microsoft.com/library/windows/hardware/ff547886) (Starting in Windows 8.1)

[**IrqlRtlPassive**](https://msdn.microsoft.com/library/windows/hardware/ff547893)

[**IrqlZwPassive**](https://msdn.microsoft.com/library/windows/hardware/ff547897)

[**NdisOidComplete**](https://msdn.microsoft.com/library/windows/hardware/dn305115) (Starting in Windows 8.1)

[**NdisOidDoubleComplete**](https://msdn.microsoft.com/library/windows/hardware/dn305116) (Starting in Windows 8.1)

[**PnpRemove**](https://msdn.microsoft.com/library/windows/hardware/dn322052) (Starting in Windows 8.1)

[**RequestedPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff551613) (Starting in Windows 8.1)

[**QueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551494) (Starting in Windows 8.1)

[**SpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551861) (Starting in Windows 8.1)

## <span id="Activating_the_DDI_compliance_checking_option"></span><span id="activating_the_ddi_compliance_checking_option"></span><span id="ACTIVATING_THE_DDI_COMPLIANCE_CHECKING_OPTION"></span>Activating the DDI compliance checking option


You can activate the DDI compliance checking feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the DDI compliance checking option. The DDI compliance checking feature is activated when you use the standard settings (**/standard**).

-   **At the command line**

    At the command line, DDI compliance checking is represented by **verifier /flags 0x00020000** (Bit 17). To activate DDI compliance checking, use a flag value of 0x00020000 or add 0x00020000 to the flag value. For example:

    ```
    verifier /flags 0x00020000 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **DDI compliance checking**.
    5.  Restart the computer.

## <span id="DDI_compliance_checking_additional"></span><span id="ddi_compliance_checking_additional"></span><span id="DDI_COMPLIANCE_CHECKING_ADDITIONAL"></span>


| DDI compliance checking (additional) |
|--------------------------------------|
|                                      |

Starting in Windows 8.1, the **DDI compliance checking (additional) option** option provides additional rules to determine whether the driver correctly interacts with the Windows operating system kernel. When you select the **DDI compliance checking (additional) option**, the following rules are tested:

-   [**CriticalRegions**](https://msdn.microsoft.com/library/windows/hardware/ff543603)

-   [**QueuedSpinLockRelease**](https://msdn.microsoft.com/library/windows/hardware/ff551496)

-   [**SpinlockRelease**](https://msdn.microsoft.com/library/windows/hardware/ff552780)

## Activating the DDI compliance checking (additional) option


You can activate the **DDI compliance checking (additional)** rules for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the **DDI compliance checking (additional)** option.

-   **At the command line**

    At the command line, DDI compliance checking is represented by **verifier /flags 0x00080000** (Bit 19). To activate **DDI compliance checking (additional)**, use a flag value of 0x00080000 or add 0x00080000 to the flag value. For example:

    ```
    verifier /flags 0x00080000 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **DDI compliance checking (additional)**.
    5.  Restart the computer.









