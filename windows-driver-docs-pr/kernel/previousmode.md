---
title: PreviousMode
author: windows-driver-content
description: PreviousMode
ms.assetid: 1251cca9-604c-48c0-a136-21dd1fe4fa72
keywords: ["PreviousMode", "RequestorMode"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PreviousMode


When a user-mode application calls the **Nt** or **Zw** version of a native system services routine, the system call mechanism traps the calling thread to kernel mode. To indicate that the parameter values originated in user mode, the trap handler for the system call sets the **PreviousMode** field in the [thread object](introduction-to-thread-objects.md) of the caller to **UserMode**. The native system services routine checks the **PreviousMode** field of the calling thread to determine whether the parameters are from a user-mode source.

If a kernel-mode driver calls a native system services routine and passes parameter values to the routine that are from a kernel-mode source, the driver must make sure that the **PreviousMode** field in the current thread object is set to **KernelMode**.

A kernel-mode driver can run in the context of an arbitrary thread, and the **PreviousMode** field of this thread might be set to **UserMode**. In this situation, a kernel-mode driver can call the **Zw** version of a native system services routine to inform the routine that the parameter values are from a trusted, kernel-mode source. The **Zw** call goes to a thin wrapper function that overrides the **PreviousMode** value in the current thread object. The wrapper function sets **PreviousMode** to **KernelMode** and calls the **Nt** version of the routine. On return from the **Nt** version of the routine, the wrapper function restores the original **PreviousMode** value of the thread object and returns.

A kernel-mode driver can directly call the **Nt** version of a native system services routine. When a kernel-mode driver processes an I/O request that can originate either in user mode or in kernel mode, the driver can call the **Nt** version of the routine so that the **PreviousMode** value of the current thread remains unaltered during the call. The **Nt*Xxx*** routine checks the calling thread's **PreviousMode** value to determine whether the parameter values are from a user-mode application or a kernel-mode component, and treats them accordingly.

An error can occur if a kernel-mode driver calls an **Nt*Xxx*** routine and the **PreviousMode** value in the current thread object does not accurately indicate whether the parameter values are from a user-mode or a kernel-mode source.

For example, assume that a kernel-mode driver is running in the context of an arbitrary thread, and that the **PreviousMode** value for this thread is set to **UserMode**. If the driver passes a kernel-mode file handle to the [**NtClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417) routine, this routine checks the **PreviousMode** value and decides that the handle must be a user-mode handle. When **NtClose** does not find the handle in the user-mode handle table, it returns the STATUS\_INVALID\_HANDLE error code. Meanwhile, the driver leaks the kernel-mode handle, which was never closed.

For another example, if the parameters for an **Nt*Xxx*** routine include an input or output buffer, and if **PreviousMode** = **UserMode**, the routine calls the [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) or [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) routine to validate the buffer. If the buffer was allocated in system memory instead of in user-mode memory, the **ProbeFor*Xxx*** routine raises an exception, and the **Nt*Xxx*** routine returns the STATUS\_ACCESS\_VIOLATION error code.

If it is necessary, a driver can call the [**ExGetPreviousMode**](https://msdn.microsoft.com/library/windows/hardware/ff545288) routine to get the **PreviousMode** value from the current thread object. Or, the driver can read the **RequestorMode** field from the [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) structure that describes the requested I/O operation. The **RequestorMode** field contains a copy of the **PreviousMode** value from the thread that requested the operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20PreviousMode%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


