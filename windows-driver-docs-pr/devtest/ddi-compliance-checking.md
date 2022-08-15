---
title: DDI compliance checking
description: The DDI compliance checking option determines whether the driver correctly interacts with the Windows operating system kernel.
ms.date: 04/03/2020
---

# DDI compliance checking

The Device Driver Interface (DDI) compliance checking option determines whether the driver correctly interacts with the Windows operating system kernel.

**Note**  This option is available starting with Windows 8. Starting in Windows 8.1, you can test additional rules, by selecting [Activating the DDI compliance checking (additional) option](#activating-the-ddi-compliance-checking-additional-option).

| DDI compliance checking |
|-------------------------|
|                         |

The DDI compliance checking option applies the same device driver interface (DDI) usage rules that [Static Driver Verifier](static-driver-verifier.md) uses to verify that your driver makes function calls at the required IRQL for the function, or correctly acquires and releases spinlocks.

When this option is active and Driver Verifier detects that the driver violates one of the DDI compliance rules, Driver Verifier issues bug check 0xC4 (with Parameter 1 equal to the identifier of the specific compliance rule).

When you select the DDI compliance checking option, the following rules are included.

[**GuardedRegions**](./wdm-guardedregions.md) (Starting in Windows 8.1)

[**IoSetCompletionExCompleteIrp**](./wdm-iosetcompletionexcompleteirp.md) (Starting in Windows 8.1)

[**IrqlApcLte**](./wdm-irqlapclte.md)

[**IrqlDispatch**](./wdm-irqldispatch.md)

[**IrqlExAllocatePool**](./wdm-irqlexallocatepool.md)

[**IrqlExApcLte1**](./wdm-irqlexapclte1.md)

[**IrqlExApcLte2**](./wdm-irqlexapclte2.md)

[**IrqlExApcLte3**](./wdm-irqlexapclte3.md)

[**IrqlExPassive**](./wdm-irqlexpassive.md)

[**IrqlIoApcLte**](./wdm-irqlioapclte.md)

[**IrqlIoDispatch**](./wdm-irqliodispatch.md)

[**IrqlIoPassive1**](./wdm-irqliopassive1.md)

[**IrqlIoPassive2**](./wdm-irqliopassive2.md)

[**IrqlIoPassive3**](./wdm-irqliopassive3.md)

[**IrqlIoPassive4**](./wdm-irqliopassive4.md)

[**IrqlIoPassive5**](./wdm-irqliopassive5.md)

[**IrqlKeApcLte1**](./wdm-irqlkeapclte1.md)

[**IrqlKeApcLte2**](./wdm-irqlkeapclte2.md)

[**IrqlKeDispatchLte**](./wdm-irqlkedispatchlte.md)

[**IrqlKeReleaseSpinLock**](./wdm-irqlkereleasespinlock.md)

[**IrqlKeSetEvent**](./wdm-irqlkesetevent.md)

[**IrqlMmApcLte**](./wdm-irqlmmapclte.md)

[**IrqlMmDispatch**](./wdm-irqlmmdispatch.md)

[**IrqlObPassive**](./wdm-irqlobpassive.md)

[**IrqlPsPassive**](./wdm-irqlpspassive.md)

[**IrqlReturn**](./wdm-irqlreturn.md) (Starting in Windows 8.1)

[**IrqlRtlPassive**](./wdm-irqlrtlpassive.md)

[**IrqlZwPassive**](./wdm-irqlzwpassive.md)

[**NdisOidComplete**](./ndis-ndisoidcomplete.md) (Starting in Windows 8.1)

[**NdisOidDoubleComplete**](./ndis-ndisoiddoublecomplete.md) (Starting in Windows 8.1)

[**PnpRemove**](./wdm-pnpremove.md) (Starting in Windows 8.1)

[**RequestedPowerIrp**](./wdm-requestedpowerirp.md) (Starting in Windows 8.1)

[**QueuedSpinLock**](./wdm-queuedspinlock.md) (Starting in Windows 8.1)

[**SpinLock**](./wdm-spinlock.md) (Starting in Windows 8.1)

These two rules are currently optional, but recommended.

[(Optional) **IrqlNtifsApcPassive**](./wdm-irqlntifsapcpassive.md)

[(Optional) **IrqlIoRtlZwPassive**](./wdm-irqliortlzwpassive.md)

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

- [**CriticalRegions**](./wdm-criticalregions.md)

- [**QueuedSpinLockRelease**](./wdm-queuedspinlockrelease.md)

- [**SpinlockRelease**](./wdm-spinlockrelease.md)

## Activating the DDI compliance checking (additional) option

>[!Note]
> **This check is deprecated starting in Windows 10 Build 19042 and above**


You can activate the **DDI compliance checking (additional)** rules for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the **DDI compliance checking (additional)** option.

-   **At the command line**

    At the command line, DDI compliance checking is represented by **verifier /flags 0x00080000** (Bit 19). To activate **DDI compliance checking (additional)**, use a flag value of 0x00080000 or add 0x00080000 to the flag value. For example:

    ```
    verifier /flags 0x00080000 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

-   **Using Driver Verifier Manager**

    1.  To start Driver Verifier Manager, type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **DDI compliance checking (additional)**.
    5.  Restart the computer.

## Activating the DDI compliance checking (additional IRQL) option

You can activate the DDI Compliance additional IRQL rules for one or more drivers by using the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the DDI Compliance additional IRQL rules.

At the command line, DDI Compliance additional IRQL checking is represented by a rule class value of 35. For example:

`verifier /ruleclasses 35 /driver MyDriver.sys`

OR

`verifier /rc 35 /driver MyDriver.sys`

The additional IRQL rule set consists of the following two rules.

[(Optional) **IrqlNtifsApcPassive**](./wdm-irqlntifsapcpassive.md)

[(Optional) **IrqlIoRtlZwPassive**](./wdm-irqliortlzwpassive.md)
