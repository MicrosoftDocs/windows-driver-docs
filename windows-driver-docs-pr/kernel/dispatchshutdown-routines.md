---
title: DispatchShutdown Routines
author: windows-driver-content
description: DispatchShutdown Routines
ms.assetid: e0d4ed56-a614-4dc8-9bb2-abfe38f05946
keywords: ["IRP_MJ_SHUTDOWN I/O function code", "dispatch routines WDK kernel , DispatchShutdown routine", "DispatchShutdown routine", "shutdown dispatch routines WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DispatchShutdown Routines


## <a href="" id="ddk-dispatchshutdown-routines-kg"></a>


A driver's [*DispatchShutdown*](https://msdn.microsoft.com/library/windows/hardware/ff543405) routine handles IRPs for the [**IRP\_MJ\_SHUTDOWN**](https://msdn.microsoft.com/library/windows/hardware/ff550807) I/O function code. Drivers of mass-storage devices that have internal caches for data must handle this request. Drivers of mass-storage devices and intermediate drivers layered over them also must handle this request if an underlying driver maintains internal buffers for data.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DispatchShutdown%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


