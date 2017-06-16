---
title: Handling Unsupported or Unrecognized Power IRPs
author: windows-driver-content
description: Handling Unsupported or Unrecognized Power IRPs
ms.assetid: 0664389c-f746-4025-969f-8c3b07139026
keywords: ["power IRPs WDK kernel , unsupported", "unsupported power IRPs WDK kernel", "unrecognized power IRPs WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Unsupported or Unrecognized Power IRPs


## <a href="" id="ddk-handling-unsupported-or-unrecognized-power-irps-kg"></a>


If a driver does not support a particular power IRP, it must nevertheless pass the IRP down the device stack to the next-lower driver. A driver further down the stack might be prepared to handle the IRP and must have the opportunity to do so.

To pass an unsupported or unrecognized power IRP, a driver should call the following routines in the sequence that is described in [Passing Power IRPs](passing-power-irps.md):

-   In Windows 7 and Windows Vista, call [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) and [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

-   In Windows Server 2003, Windows XP, and Windows 2000, call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776), **IoSkipCurrentIrpStackLocation**, and [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654).

The driver should not change anything in the IRP before passing the IRP down a device stack.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Unsupported%20or%20Unrecognized%20Power%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


