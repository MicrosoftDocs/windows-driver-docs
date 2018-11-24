---
title: Security Checks
description: Security Checks
ms.assetid: fca92bad-7bb8-4a30-b303-48fd54c20c42
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Security Checks


The Security Checks option of Driver Verifier monitors the driver for common errors that can result in security vulnerabilities. This option is available starting in Windows Vista.

Specifically, the Security Checks option looks for the following improper driver behavior:

- **Calling kernel ZwXxx routines with user-mode addresses as parameters.** When the driver calls any **Zw*Xxx*** routines, Driver Verifier checks that none of the parameters are user-mode addresses. When calling any **Zw*Xxx*** routine, the current KPROCESSOR\_MODE becomes **KernelMode**, and any parameters passed to that routine are treated as though they are kernel-mode addresses. Thus, the driver must probe any user-mode buffers received from applications and place it into kernel-mode memory (for example, in a pool block or data structure allocated on the kernel stack) prior to calling the kernel **Zw*Xxx*** routine. The driver must use the captured buffer rather than the user-mode buffer as a parameter of the **Zw*Xxx*** routine.

- **Calling kernel ZwXxx routines with malformed UNICODE\_STRINGs as parameters.** When the driver calls any **Zw*Xxx*** routine, Driver Verifier checks any parameters that are UNICODE\_STRING values. Common errors detected by Driver Verifier in such strings include:
  -   **The buffer field points to user-mode memory.**
  -   **The Length or MaximumLength parameters are incorrect.** For example, *MaximumLength* &lt; *Length*. Or one or both of these values is an odd number. Both of these values must always be even because they represent the number of bytes used for representing a Unicode string.
- **Calling kernel ZwXxx routines with an incorrect OBJECT\_ATTRIBUTES structure as a parameter.** When the driver calls any **Zw*Xxx*** routine, Driver Verifier checks any parameters that are OBJECT\_ATTRIBUTE structures. The members of each OBJECT\_ATTRIBUTE structure parameter are subjected to the same checks for user-mode addresses and UNICODE\_STRING values that are described above.

- **Inconsistent Irp-&gt;RequestorMode and I/O Request parameters.** Whenever the **Irp-&gt; RequestorMode** is set to **KernelMode**, Driver Verifier checks that no I/O Request parameters, **Irp-&gt;AssociatedIrp.SystemBuffer** or **Irp-&gt;UserBuffer**, are user-mode addresses.

Beginning with Windows 7, when you enable any Driver Verifier option, Driver Verifier checks for the following driver behavior:

**Object reference counter changes from 0 to 1.**
When the Windows kernel object manager creates an object, such as a File object or a Thread object, the new object's reference counter is set to 1. Calls to system functions such as [**ObReferenceObjectByPointer**](https://msdn.microsoft.com/library/windows/hardware/ff558686) or [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679) increment the reference counter. Every call to [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) for the same object decrements the reference counter.

After the reference counter reaches the 0 value, the object becomes eligible to be freed. The object manager might free it immediately, or it might free it later. Driver Verifier checks for subsequent calls to [**ObReferenceObjectByPointer**](https://msdn.microsoft.com/library/windows/hardware/ff558686) and [**ObReferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff558678) for the same object. These calls change the reference counter from 0 to 1, which means the driver has incremented the reference counter of an already freed object. This is always incorrect because it can corrupt other memory allocations.

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

You can activate the Security Checks option for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

-   **Using the command line**

    At the command line, the Security Checks option is represented by **Bit 8 (0x100)**. To activate Security Checks, use a flag value of 0x100 or add 0x100 to the flag value. For example:

    ```
    verifier /flags 0x100 /driver MyDriver.sys
    ```

    The option will be active after you restart the computer.

    Starting with Windows Vista, you can also activate and deactivate Security Checks without restarting the computer by adding the **/volatile** parameter to the command. For example:

    ```
    verifier /volatile /flags 0x100 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or restart the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

    The Security Checks option is also included in the standard settings. For example:

    ```
    verifier /standard /driver MyDriver.sys
    ```

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)**, and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select **Security Checks**.

    The Security Checks feature is also included in the standard settings. To use this feature in Driver Verifier Manager, click **Create Standard Settings**.

 

 





