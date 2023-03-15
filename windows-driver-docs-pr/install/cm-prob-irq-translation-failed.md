---
title: CM_PROB_IRQ_TRANSLATION_FAILED
description: CM_PROB_IRQ_TRANSLATION_FAILED
keywords:
- CM_PROB_IRQ_TRANSLATION_FAILED
ms.date: 03/03/2023
---

# Code 36 - CM_PROB_IRQ_TRANSLATION_FAILED

This Device Manager error message indicates that the IRQ translation failed for the device.

## Error Code

36

### Display Message

"This device is requesting a PCI interrupt but is configured for an ISA interrupt (or vice versa). Please use the computer's system setup program to reconfigure the interrupt for this device. (Code 36)"

### Recommended Resolution

Try using the BIOS setup utility to change settings for IRQ reservations, if such an option exists. (The BIOS might have options to reserve certain IRQs for PCI or ISA devices.)
