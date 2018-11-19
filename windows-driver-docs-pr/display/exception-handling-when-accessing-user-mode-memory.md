---
title: Exception Handling When Accessing User-Mode Memory
description: Exception Handling When Accessing User-Mode Memory
ms.assetid: 44ed69a0-da0e-4335-9128-a78a83ea80dd
keywords:
- user-mode memory WDK Windows 2000 display
- user-mode memory WDK Windows 2000 display , exception handling
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Exception Handling When Accessing User-Mode Memory


## <span id="ddk_exception_handling_when_accessing_user_mode_memory_gg"></span><span id="DDK_EXCEPTION_HANDLING_WHEN_ACCESSING_USER_MODE_MEMORY_GG"></span>


A display or video miniport driver must use exception handling around code that accesses data structures allocated in user mode. The Microsoft Direct3D runtime secures ownership of such data structures before passing them to the driver. To secure ownership of user-mode memory, the runtime calls the [**MmSecureVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff556374) function. When the runtime secures ownership of user-mode memory, it prevents any other thread from modifying the type of access to the memory. For example, if the runtime secures ownership of a data structure that a user-mode thread has allocated with read and write access, other threads cannot restrict the data structure's access type to read-only. Also, securing ownership of user-mode memory does not guarantee that the memory remains valid.

Therefore, unless exception handling is implemented around code that accesses such memory, the operating system crashes if the driver attempts to access invalid user-mode memory. For invalid kernel-memory accesses, the only available option for the operating system is to crash. However, for invalid user-memory accesses, the driver can terminate the application that invalidated the memory and leave the operating system and the driver's device in a stable state.

The driver must implement exception handling rather than rely on the runtime to handle exceptions. If the runtime handled exceptions and the driver accessed invalid user-mode memory, the stack would return to the exception-handling code in the runtime, leaving the driver or the device in an unknown state. The driver must implement exception handling so that it can perform the following operations if an exception occurs:

-   Restore its state and the state of its device.

-   Release any spin locks that it acquired.

In the following scenarios, the runtime secures ownership of memory allocated in user mode before passing the memory to the driver.

-   The driver processes vertex data that is specified by a pointer to user-mode memory. The driver receives this memory pointer in a call to its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function. In this *D3dDrawPrimitives2* call, the D3DHALDP2\_USERMEMVERTICES flag of the **dwFlags** member of the [**D3DHAL\_DRAWPRIMITIVES2DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545957) structure is set.

-   The driver updates the render state array to which the **lpdwRStates** member of D3DHAL\_DRAWPRIMITIVES2DATA points. The driver updates this array during a call to its *D3dDrawPrimitives2* function.

-   The driver updates its state at the **lpdwStates** member of the [**DD\_GETDRIVERSTATEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551551) structure during a call to its [**D3dGetDriverState**](https://msdn.microsoft.com/library/windows/hardware/ff544708) function.

-   The driver bit-block transfers or accesses a system texture that was allocated in user memory.

A display driver can use the **try/except** mechanism to implement exception handling. For more information about **try/except**, see the Microsoft Visual C++ documentation.

The following code example shows how the driver can use the **try/except** mechanism to throw an exception if an error occurs due to accessing invalid memory.

```cpp
__try
{
    // Access user-mode memory.
}
__except(EXCEPTION_EXECUTE_HANDLER)
{
    // Recover and leave driver and hardware in a stable state.
}
```

**Note**   Aside from accessing and copying the user-mode value into a local variable, the driver should not perform any other operations inside the **\_\_try** block. Other operations can cause their own exceptions to occur. The operating system handles these exceptions differently.

 

 

 





