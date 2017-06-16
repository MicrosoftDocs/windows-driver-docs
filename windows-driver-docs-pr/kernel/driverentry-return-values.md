---
title: DriverEntry Return Values
author: windows-driver-content
description: DriverEntry Return Values
ms.assetid: 052be2ea-375a-4495-931e-8b66972125a5
keywords: ["DriverEntry WDK kernel , return values", "return values WDK DriverEntry routine"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DriverEntry Return Values


## <a href="" id="ddk-driverentry-return-values-kg"></a>


A [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine returns an [NTSTATUS value](ntstatus-values.md), either STATUS\_SUCCESS or an appropriate error status.

The **DriverEntry** routine should postpone any call to [**IoRegisterDriverReinitialization**](https://msdn.microsoft.com/library/windows/hardware/ff549511) until just before it returns STATUS\_SUCCESS. It must not make this call unless it will return STATUS\_SUCCESS.

If a **DriverEntry** routine returns an NTSTATUS value that is not a success or informational value, such as STATUS\_SUCCESS, the driver for that **DriverEntry** routine is not loaded.

A **DriverEntry** routine that will fail initialization must free any system objects, system resources, and registry resources it has already set up before it returns control. It should reset the driver's dispatch entry points in the driver object for [**IRP\_MJ\_FLUSH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff550760) and [**IRP\_MJ\_SHUTDOWN**](https://msdn.microsoft.com/library/windows/hardware/ff550807) to **NULL** if the driver supports these requests.

If a driver will fail initialization, the **DriverEntry** routine also should log an error before returning control. See [Logging Errors](logging-errors.md).

Note that a driver's [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine is not called if a driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine returns a failure status.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DriverEntry%20Return%20Values%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


