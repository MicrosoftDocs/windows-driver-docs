---
title: Wait/Wake IRP Requests
description: Wait/Wake IRP Requests
ms.assetid: c67d6dcb-f4a9-4df0-abb8-9d84fc44ec40
keywords: ["sending wait/wake IRPs", "wake-up signal enabled WDK kernel", "wait/wake IRPs WDK power management , sending"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Wait/Wake IRP Requests





To send an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766), a driver calls [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734), passing (among other parameters) a pointer to the target PDO, a system power state, and a pointer to a callback routine.

The system power state specifies the least-powered state from which this IRP can wake the system. The value must be equal to or more powered than the [**SystemWake**](systemwake.md) state in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure. For example, if a driver passes **PowerSystemSleeping2** in the IRP, the associated IRP could cause the system to wake from states S0, S1, and S2. In such a case, the system must support S0 and S2 (the highest- and lowest-powered states in the range) but need not support S1.

Every driver that requests a wait/wake IRP should specify a [callback routine](wait-wake-callback-routines.md), which is invoked after all other drivers have completed the IRP. In this routine, the driver can do whatever is necessary to return its device to the working state.

In response to **PoRequestPowerIrp**, the power manager allocates a power IRP with minor code **IRP\_MN\_WAIT\_WAKE** and sends it to the top of the device stack for the target PDO. The caller is returned a pointer to the allocated IRP, which it can use later if it has to cancel the IRP.

If no errors occur, **PoRequestPowerIrp** returns STATUS\_PENDING. This status means that the IRP has been sent successfully and is pending completion.

A wait/wake IRP does not change the power state of the system or of a device. It simply enables a device's wake-up signal. The IRP remains pending until an external signal causes the system or device to awaken.

 

 




