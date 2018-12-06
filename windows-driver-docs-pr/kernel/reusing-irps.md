---
title: Reusing IRPs
description: Reusing IRPs
ms.assetid: 19b09cf8-b88d-4808-9af0-038d3d02dceb
keywords: ["IRPs WDK kernel , reusing", "reusing IRPs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Reusing IRPs





Under certain circumstances, drivers can *reuse* IRPs. The driver can allocate a pool of memory buffers that it uses to hold IRPs as they need to be created.

Drivers must not attempt to reuse IRPs issued by the I/O manager. In particular, drivers should not attempt to reuse IRPs created by the [**IoMakeAssociatedIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549397), [**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330), [**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310), or [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) routines.

Drivers can safely reuse IRPs that they have created, as follows:

1.  If a driver allocates an IRP as raw memory (for example, by calling [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520)), and then initializes it with [**IoInitializeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549315), then it can safely call **IoInitializeIrp** or [**IoReuseIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549661) to reinitialize the memory buffer.

2.  On Microsoft Windows 2000 and later operating systems, drivers that create an IRP with [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) can reuse the IRP by calling **IoReuseIrp**.

3.  If a driver allocates an IRP by calling **IoAllocateIrp** with the *ChargeQuota* parameter set to **FALSE**, then it can safely use **IoInitializeIrp** to reinitialize the IRP. Drivers that must work on Windows 98/Me can use this method as a work-around. Drivers designed strictly for Windows 2000 and later operating systems should use the previous method.

 

 




