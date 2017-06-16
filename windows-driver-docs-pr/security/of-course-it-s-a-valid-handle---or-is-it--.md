---
title: Of course it's a valid handle (Or is it )
description: How to use user-mode handle safely and protect kernel handles from misuse by user-mode applications.
ms.assetid: 758969A5-659E-41BB-9A5D-37F0C4B01FFA
---

# Of course it's a valid handle! (Or is it?)


**Last updated:**

-   May 27, 2007

How to use user-mode handle safely and protect kernel handles from misuse by user-mode applications.

Handles that are passed to a driver by a caller do not pass through the I/O Manager, so the I/O Manager cannot perform any validation checks on the handles. Never assume a handle is valid; always make sure the handle has the correct object type, appropriate access for the required tasks, the correct access mode, and that the access mode is compatible with the access requested.

Drivers should be careful when using handles, especially those received from user-mode applications. First, such handles are specific to a process context, so they're only valid in the process that opened the handle—when used from a different process context or from a worker thread, the handle could reference a different object or it could simply be invalid. Second, an attacker might close and reopen the handle to change what it refers to while the driver is using it. Third, an attacker might pass in such a handle to trick a driver into performing operations that are illegal for the application, such as calling **Zw*Xxx*** functions. Access checks are skipped for kernel-mode callers of these functions, so an attacker can use this mechanism to bypass validation.

Drivers should also make certain that user-mode applications cannot misuse handles created by the driver. Setting the OBJ\_KERNEL\_HANDLE attribute for a handle makes it a kernel handle, which can be used in any process context but is only accessible from kernel mode (which is especially important for handles that are passed to the ZwXxx routines). A user-mode process cannot access, close, or replace a kernel handle.

## <span id="What_should_you_do__"></span><span id="what_should_you_do__"></span><span id="WHAT_SHOULD_YOU_DO__"></span>What should you do?


-   After receiving any handle, call [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679) immediately to swap the user-mode handle for an object pointer:
    -   Always specify the object type you expect so you can take advantage of the type-checking provided by [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679).
    -   For a user-mode handle, specify UserMode for *AccessMode* (assuming the user is expected to have the same access to the file object as your driver).
    -   Always check the status code returned by [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679), and only proceed if it is STATUS\_SUCCESS.
    -   When you finish using the object pointer provided by [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679), call [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) to release the pointer and avoid a resource leak.
-   Before creating a handle for use in kernel mode, call [**InitializeObjectAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff547804) to initialize an OBJECT\_ATTRIBUTES structure where Attributes has the value OBJ\_KERNEL\_HANDLE set.

The following code fragment shows proper usage of [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679), in this case for a handle to an event.

```ManagedCPlusPlus
NTSTATUS status;
PKEVENT userEvent;
HANDLE handle;
handle = RetrieveHandleFromIrpBuffer(…);
status = ObReferenceObjectByHandle(handle,
    EVENT_MODIFY_STATE,
    *ExEventObjectType,
    UserMode,
    (PVOID*) &amp;userEvent,
    NULL);
if (NT_SUCCESS(status)) {
    // do something interesting here
    KeSetEvent(userEvent, IO_NO_INCREMENT, FALSE);
    ObDereferenceObject(userEvent);
}
```

## <span id="related_topics"></span>Related topics


[Kernel-Mode Drivers: Fixing Common Driver Reliability Issues](http://download.microsoft.com/download/5/7/7/577a5684-8a83-43ae-9272-ff260a9c20e2/drvqa.doc)

[User-Mode Interactions: Guidelines for Kernel-Mode Drivers](http://msdn.microsoft.com/en-US/library/windows/hardware/gg487414)

[**InitializeObjectAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff547804)

[**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679)

[**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Of%20course%20it's%20a%20valid%20handle!%20%28Or%20is%20it?%29%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





