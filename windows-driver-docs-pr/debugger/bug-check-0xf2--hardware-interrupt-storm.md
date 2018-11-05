---
title: Bug Check 0xF2 HARDWARE_INTERRUPT_STORM
description: The HARDWARE_INTERRUPT_STORM bug check has a value of 0x000000F2. This indicates that the kernel detected an interrupt storm.
ms.assetid: 04751AB2-E9B3-40AD-A872-8DDA9B96C6CA
keywords: ["Bug Check 0xF2 HARDWARE_INTERRUPT_STORM", "HARDWARE_INTERRUPT_STORM"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- HARDWARE_INTERRUPT_STORM
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xF2: HARDWARE\_INTERRUPT\_STORM


The HARDWARE\_INTERRUPT\_STORM bug check has a value of 0x000000F2. This indicates that the kernel detected an interrupt storm.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## HARDWARE\_INTERRUPT\_STORM Parameters


| Parameter | Description                                                                               |
|-----------|-------------------------------------------------------------------------------------------|
| 1         | Address of the ISR (or first ISR in the chain) connected to the storming interrupt vector |
| 2         | ISR context value                                                                         |
| 3         | Address of the interrupt object for the storming interrupt vector                         |
| 4         | 0x1 if the ISR is not chained, 0x2 if the ISR is chained                                  |

 

Cause
-----

This bugcheck indicates that the kernel has detected an interrupt storm. An interrupt storm is defined as a level triggered interrupt signal staying in the asserted state. This is fatal to the system in the manner that the system will hard hang, or "bus lock".

This can happen because of the following:

-   A piece of hardware does not release its interrupt signal after being told to do so by the device driver.
-   A device driver does not instruct its hardware to release the interrupt signal because it does not believe the interrupt was initiated from its hardware.
-   A device driver claims the interrupt even though the interrupt was not initiated from its hardware. Note that this can only occur when multiple devices are sharing the same IRQ.
-   The ELCR (edge level control register) is set incorrectly.
-   Edge and Level interrupt triggered devices share an IRQ.

All of these cases will instantly hard hang your system. Instead of hard hanging the system, this bugcheck is initiated since in many cases it can identify the culprit.

When the bugcheck occurs, the module containing the ISR (interrupt service routine) of the storming IRQ is displayed on the screen. This is an example of what you would see:

```console
*** STOP: 0x000000F2 (0xFCA7C55C, 0x817B9B28, 0x817D2AA0, 0x00000002)
An interrupt storm has caused the system to hang.
*** Address FCA7C55C base at FCA72000, Datestamp 3A72BDEF - ACPI.sys
```

In the event the fourth parameter is a 0x00000001, the module pointed to is very likely the culprit. Either the driver is broken, or the hardware is malfunctioning.

In the event the fourth parameter is a 0x00000002, the module pointed to is the first ISR in the chain, and is never guaranteed to be the culprit.

Resolution
----------

A user experiencing this bugcheck repeatedly should try to isolate the problem by looking for devices that are on the same IRQ as the one for which the module is a driver for (in this case, the same IRQ that ACPI is using).

 

 




