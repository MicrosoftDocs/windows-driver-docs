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

[**GuardedRegions**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-guardedregions) (Starting in Windows 8.1)

[**IoSetCompletionExCompleteIrp**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-iosetcompletionexcompleteirp) (Starting in Windows 8.1)

[**IrqlApcLte**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlapclte)

[**IrqlDispatch**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqldispatch)

[**IrqlExAllocatePool**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlexallocatepool)

[**IrqlExApcLte1**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlexapclte1)

[**IrqlExApcLte2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)

[**IrqlExApcLte3**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlexapclte3)

[**IrqlExPassive**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlexpassive)

[**IrqlIoApcLte**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlioapclte)

[**IrqlIoDispatch**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqliodispatch)

[**IrqlIoPassive1**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqliopassive1)

[**IrqlIoPassive2**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqliopassive2)

[**IrqlIoPassive3**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqliopassive3)

[**IrqlIoPassive4**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqliopassive4)

[**IrqlIoPassive5**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqliopassive5)

[**IrqlKeApcLte1**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlkeapclte1)

[**IrqlKeApcLte2**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlkeapclte2)

[**IrqlKeDispatchLte**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlkedispatchlte)

[**IrqlKeReleaseSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlkereleasespinlock)

[**IrqlKeSetEvent**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlkesetevent)

[**IrqlMmApcLte**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlmmapclte)

[**IrqlMmDispatch**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlmmdispatch)

[**IrqlObPassive**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlobpassive)

[**IrqlPsPassive**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlpspassive)

[**IrqlReturn**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlreturn) (Starting in Windows 8.1)

[**IrqlRtlPassive**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlrtlpassive)

[**IrqlZwPassive**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-irqlzwpassive)

[**NdisOidComplete**](https://docs.microsoft.com/windows-hardware/drivers/devtest/ndis-ndisoidcomplete) (Starting in Windows 8.1)

[**NdisOidDoubleComplete**](https://docs.microsoft.com/windows-hardware/drivers/devtest/ndis-ndisoiddoublecomplete) (Starting in Windows 8.1)

[**PnpRemove**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-pnpremove) (Starting in Windows 8.1)

[**RequestedPowerIrp**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-requestedpowerirp) (Starting in Windows 8.1)

[**QueuedSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-queuedspinlock) (Starting in Windows 8.1)

[**SpinLock**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-spinlock) (Starting in Windows 8.1)

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

-   [**CriticalRegions**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-criticalregions)

-   [**QueuedSpinLockRelease**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-queuedspinlockrelease)

-   [**SpinlockRelease**](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdm-spinlockrelease)

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









