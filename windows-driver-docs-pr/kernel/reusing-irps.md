---
title: Reusing IRPs
author: windows-driver-content
description: Reusing IRPs
ms.assetid: 19b09cf8-b88d-4808-9af0-038d3d02dceb
keywords: ["IRPs WDK kernel , reusing", "reusing IRPs WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reusing IRPs


## <a href="" id="ddk-reusing-irps-kg"></a>


Under certain circumstances, drivers can *reuse* IRPs. The driver can allocate a pool of memory buffers that it uses to hold IRPs as they need to be created.

Drivers must not attempt to reuse IRPs issued by the I/O manager. In particular, drivers should not attempt to reuse IRPs created by the [**IoMakeAssociatedIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549397), [**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330), [**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310), or [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) routines.

Drivers can safely reuse IRPs that they have created, as follows:

1.  If a driver allocates an IRP as raw memory (for example, by calling [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520)), and then initializes it with [**IoInitializeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549315), then it can safely call **IoInitializeIrp** or [**IoReuseIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549661) to reinitialize the memory buffer.

2.  On Microsoft Windows 2000 and later operating systems, drivers that create an IRP with [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) can reuse the IRP by calling **IoReuseIrp**.

3.  If a driver allocates an IRP by calling **IoAllocateIrp** with the *ChargeQuota* parameter set to **FALSE**, then it can safely use **IoInitializeIrp** to reinitialize the IRP. Drivers that must work on Windows 98/Me can use this method as a work-around. Drivers designed strictly for Windows 2000 and later operating systems should use the previous method.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Reusing%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


