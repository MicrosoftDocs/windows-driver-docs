---
title: Locking and Unlocking Stream Pointers
description: Locking and Unlocking Stream Pointers
ms.assetid: 3826a5bc-4ba5-4ada-a8aa-e7bbd949187e
keywords:
- stream pointers WDK AVStream , locked and unlocked
- locked stream pointers WDK AVStream
- unlocked stream pointers WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Locking and Unlocking Stream Pointers





Each stream pointer maintains a lock status: either locked or unlocked.

Locked stream pointers are guaranteed to reference data in the queue. Data frames pointed to by locked stream pointers cannot be canceled. As such, minidrivers should minimize the time that they spend holding locked stream pointers.

An unlocked stream pointer is not guaranteed to reference a data frame within the queue. By holding an unlocked stream pointer, a minidriver can retain a data pointer, but still allow the frame to be canceled.

It is possible to access data pointed to by an unlocked stream pointer. If the *CancelCallback* routine you provide in [**KsStreamPointerClone**](https://msdn.microsoft.com/library/windows/hardware/ff567129) calls [**KsStreamPointerDelete**](https://msdn.microsoft.com/library/windows/hardware/ff567130), you should synchronize *CancelCallback* and any data access that it performs. The minidriver must ensure that the cancellation callback routine does not delete the stream pointer while another thread is using it.

If the cancellation callback routine does not call **KsStreamPointerDelete**, synchronization might not be necessary.

To lock a stream pointer, call [**KsStreamPointerLock**](https://msdn.microsoft.com/library/windows/hardware/ff567134). To unlock a stream pointer, call [**KsStreamPointerUnlock**](https://msdn.microsoft.com/library/windows/hardware/ff567137).

When an IRP is canceled, AVStream calls the cancellation callbacks for all unlocked stream pointers that point to frames within the IRP.

Unlock the leading and trailing edge stream pointers only when they are not in use.

 

 




