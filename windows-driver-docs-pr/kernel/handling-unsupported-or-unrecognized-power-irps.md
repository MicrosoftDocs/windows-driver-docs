---
title: Handling Unsupported or Unrecognized Power IRPs
description: Handling Unsupported or Unrecognized Power IRPs
keywords: ["power IRPs WDK kernel , unsupported", "unsupported power IRPs WDK kernel", "unrecognized power IRPs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Unsupported or Unrecognized Power IRPs





If a driver does not support a particular power IRP, it must nevertheless pass the IRP down the device stack to the next-lower driver. A driver further down the stack might be prepared to handle the IRP and must have the opportunity to do so.

To pass an unsupported or unrecognized power IRP, a driver should call the following routines in the sequence that is described in [Passing Power IRPs](passing-power-irps.md):

-   In Windows 7 and Windows Vista, call [**IoSkipCurrentIrpStackLocation**](./mm-bad-pointer.md) and [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver).

-   In Windows Server 2003, Windows XP, and Windows 2000, call [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp), **IoSkipCurrentIrpStackLocation**, and [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver).

The driver should not change anything in the IRP before passing the IRP down a device stack.

 

