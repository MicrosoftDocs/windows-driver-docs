---
title: Handling Exceptions
author: windows-driver-content
description: Handling Exceptions
MS-HAID:
- 'Other\_f7259c51-1557-42e6-8264-ac8dae0177e3.xml'
- 'kernel.handling\_exceptions'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 20040d86-5088-48ec-a5b9-54760d143871
keywords: ["structured exception handling WDK kernel", "exceptions WDK kernel", "access violations WDK kernel", "hardware-defined exceptions WDK kernel", "software-defined exceptions WDK kernel", "errors WDK kernel", "guard-page violations WDK kernel", "page-read errors WDK kernel"]
---

# Handling Exceptions


## <a href="" id="ddk-handling-exceptions-kg"></a>


The operating system uses [structured exception handling](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-structured-exception-handling) to signal certain kinds of errors. A routine called by a driver can raise an exception that the driver must handle.

The system traps the following general kinds of exceptions:

1.  Hardware-defined faults or traps, such as,

    -   Access violations (see below)
    -   Data-type misalignments (such as a 16-bit entity aligned on an odd-byte boundary)
    -   Illegal and privileged instructions
    -   Invalid lock sequences (attempting to execute an invalid sequence of instructions within an interlocked section of code)
    -   Integer divides by zero and overflows
    -   Floating-point divides by zero, overflows, underflows, and reserved operands
    -   Breakpoints and single step execution (to support debuggers)

2.  System software-defined exceptions, such as,

    -   Guard-page violations (attempting to load or store data from or to a location within a guard page)
    -   Page-read errors (attempting to read a page into memory and encountering a concurrent I/O error)

An *access violation* is an attempt to perform an operation on a page that is not permitted under the current page protection settings. Access violations occur in the following situations:

-   An invalid read or write operation, such as writing to a read-only page.

-   To access memory beyond the limit of the current program's address space (known as a length violation).

-   To access a page that is currently resident but dedicated to the use of a system component. For example, user-mode code is not allowed access a page that the kernel is using.

If an operation might cause an exception, the driver should enclose the operation in a **try/except** block. Accesses of locations in user-mode are typical causes of exceptions. For example, the [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) routine checks that the driver can actually write to a user-mode buffer. If it cannot, the routine raises a STATUS\_ACCESS\_VIOLATION exception. In the following code example, the driver calls **ProbeForWrite** in a **try/except** so that it can handle the resulting exception, if one should occur.

```
try {
    ...
    ProbeForWrite(Buffer, BufferSize, BufferAlignment);
 
    /* Note that any access (not just the probe, which must come first,
     * by the way) to Buffer must also be within a try-except.
     */
    ...
} except (EXCEPTION_EXECUTE_HANDLER) {
    /* Error handling code */
    ...
}
```

Drivers must handle any raised exceptions. An exception that is not handled causes the system to bug check. The driver that causes the exception to be raised must handle it: a lower-level driver cannot rely on a higher-level driver to handle the exception.

Drivers can directly raise an exception, by using the [**ExRaiseAccessViolation**](https://msdn.microsoft.com/library/windows/hardware/ff545509), [**ExRaiseDatatypeMisalignment**](https://msdn.microsoft.com/library/windows/hardware/ff545524), or [**ExRaiseStatus**](https://msdn.microsoft.com/library/windows/hardware/ff545529) routines. The driver must handle any exceptions that these routines raise.

The following is a partial list of routines that, at least in certain situations, can raise an exception:

-   [**MmMapLockedPages**](https://msdn.microsoft.com/library/windows/hardware/ff554622)

-   [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664)

-   [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876)

-   [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879)

Memory accesses to user-mode buffers can also cause access violations. For more information, see [Errors in Referencing User-Space Addresses](errors-in-referencing-user-space-addresses.md).

Note that structured exception handling is distinct from C++ exceptions. The kernel does not support C++ exceptions.

For more information about structured exception handling, see the Microsoft Windows SDK, and the Visual Studio documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Exceptions%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


