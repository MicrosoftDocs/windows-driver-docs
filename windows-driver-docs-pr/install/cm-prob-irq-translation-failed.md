---
title: CM_PROB_IRQ_TRANSLATION_FAILED
description: CM_PROB_IRQ_TRANSLATION_FAILED
ms.assetid: fafd40d5-43bf-4243-907a-df523e1b501e
keywords:
- CM_PROB_IRQ_TRANSLATION_FAILED
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CM_PROB_IRQ_TRANSLATION_FAILED

This function is reserved for system use.


## <a href="" id="ddk-cm-prob-irq-translation-failed-dg"></a>


The IRQ translation failed for the device.

### Error Code

36

### Display Message (Windows 2000 and later versions of Windows)

"This device is requesting a PCI interrupt but is configured for an ISA interrupt (or vice versa). Please use the computer's system setup program to reconfigure the interrupt for this device. (Code 36)"

### Recommended Resolution (Windows 2000 and later versions of Windows)

Try using the BIOS setup utility to change settings for IRQ reservations, if such an option exists. (The BIOS might have options to reserve certain IRQs for PCI or ISA devices.)

 

 





