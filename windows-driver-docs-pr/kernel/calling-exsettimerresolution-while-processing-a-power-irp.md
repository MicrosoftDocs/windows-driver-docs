---
title: Calling ExSetTimerResolution While Processing a Power IRP
description: Calling ExSetTimerResolution While Processing a Power IRP
ms.assetid: 999a76ab-1586-4157-bfa7-8cc5dd517c71
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Calling ExSetTimerResolution While Processing a Power IRP


During the processing of an [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) request, the power manager holds a lock on a resource that [**ExSetTimerResolution**](https://msdn.microsoft.com/library/windows/hardware/ff545614) must acquire to complete. Consequently, a deadlock will occur if a driver directly or indirectly calls this routine while processing a power request, and then waits for the call to the routine to return before the driver completes the power request. While processing a power request, a driver can safely call **ExSetTimerResolution** only if the driver does not wait for the call to this routine to return before completing the power request. For example, a driver can create a worker thread that calls **ExSetTimerResolution**, as long as the driver then completes the power request without waiting for the call to this routine to return.

 

 




