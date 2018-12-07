---
title: DriverEntry Return Values
description: DriverEntry Return Values
ms.assetid: 052be2ea-375a-4495-931e-8b66972125a5
keywords: ["DriverEntry WDK kernel , return values", "return values WDK DriverEntry routine"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DriverEntry Return Values





A [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine returns an [NTSTATUS value](ntstatus-values.md), either STATUS\_SUCCESS or an appropriate error status.

The **DriverEntry** routine should postpone any call to [**IoRegisterDriverReinitialization**](https://msdn.microsoft.com/library/windows/hardware/ff549511) until just before it returns STATUS\_SUCCESS. It must not make this call unless it will return STATUS\_SUCCESS.

If a **DriverEntry** routine returns an NTSTATUS value that is not a success or informational value, such as STATUS\_SUCCESS, the driver for that **DriverEntry** routine is not loaded.

A **DriverEntry** routine that will fail initialization must free any system objects, system resources, and registry resources it has already set up before it returns control. It should reset the driver's dispatch entry points in the driver object for [**IRP\_MJ\_FLUSH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff550760) and [**IRP\_MJ\_SHUTDOWN**](https://msdn.microsoft.com/library/windows/hardware/ff550807) to **NULL** if the driver supports these requests.

If a driver will fail initialization, the **DriverEntry** routine also should log an error before returning control. See [Logging Errors](logging-errors.md).

Note that a driver's [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine is not called if a driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine returns a failure status.

 

 




