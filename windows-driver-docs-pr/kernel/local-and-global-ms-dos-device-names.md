---
title: Local and Global MS-DOS Device Names
author: windows-driver-content
description: Local and Global MS-DOS Device Names
ms.assetid: bfb7e41c-0f80-4cb9-b036-d1b44473f9fb
keywords: ["MS-DOS device names WDK kernel", "local MS-DOS device names WDK kernel", "global MS-DOS device names WDK kernel", "DosDevices contexts WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Local and Global MS-DOS Device Names


## <a href="" id="ddk-local-and-global-ms-dos-device-names-kg"></a>


The Microsoft Windows 2000 and later versions of the Windows NT-based operating system maintain multiple versions of the **DosDevices** directory.

On these operating systems, there is one *global* **\\DosDevices** directory and multiple *local* **\\DosDevices** directories. The global **\\DosDevices** directory holds the MS-DOS device names that are visible system-wide. A local **\\DosDevices** directory holds MS-DOS device names that are visible only in a particular *local* **DosDevices** *context*.

The local **DosDevices** contexts are as follows.

-   On Windows XP and later, each logon session has its own local **DosDevices** context. System threads, and any thread that is running as the LocalSystem user, do not run in a local **DosDevices** context.

-   On Windows 2000, each terminal server session has its own local **DosDevices** context. Any thread that is running as part of the console session does not run in a local **DosDevices** context.

Each thread has a current **DosDevices** context, which can change over the lifetime of a thread. A thread that does not run in a local **DosDevices** context is said to run in the *global* **DosDevices** *context*. Thus, the system account runs in the global **DosDevices** context.

If a thread is currently running in a local **DosDevices** context, any MS-DOS device names that it creates are created only in the local **DosDevices** directory. Thus, threads that are running in a local **DosDevices** context cannot affect the MS-DOS device names that are visible to threads that are running in another local **DosDevices** context or in the global **DosDevices** context. For example, if a user on Windows XP or later mounts a network drive as **X:**, this does not affect the meaning of **X:** for any other user, or for the system as a whole.

On Windows XP and later, when the object manager looks up a name in **\\DosDevices**, it first searches the local **\\DosDevices** directory, and then the global **\\DosDevices** directory. If the name exists in both places, the local name shadows the global name.

On Windows 2000, whenever a new terminal server session is initiated, the system builds local \\**DosDevices** directory by copying the global **\\DosDevices** directory. Any subsequent changes to the global directory are not propagated to the local directory.

A driver that must create its MS-DOS device names in the global **\\DosDevices** directory can do so by creating its symbolic links in a standard driver routine that is guaranteed to run in a system thread context, such as **DriverEntry**. Alternatively, the global **\\DosDevices** directory is available as **\\DosDevices\\Global**; drivers can use a name of the **\\DosDevices\\Global\\***DosDeviceName* to specify a name in the global directory.

Note that **\\DosDevices\\Global** does not exist on platforms that do not support local and global versions of **\\DosDevices**, such as Windows 98/Me. The following code example creates a global symbolic link that works on Windows 98/Me as well as Windows 2000 and later operating systems:

```
UNICODE_STRING deviceName; // Already initialized.
UNICODE_STRING symbolicLinkName; // Initializing below.
NTSTATUS status;

if (IoIsWdmVersionAvailable(1, 0x10)) {
    // We&#39;re on Windows 2000 or later, so we use \DosDevices\Global.
 
    RtlInitUnicodeString(&symbolicLinkName, L"\\DosDevices\\Global\\SymbolicLinkName");

} else {
    // Windows 98/Me.  We just use DosDevices.
 
    RtlInitUnicodeString(&symbolicLinkName, L"\\DosDevices\\SymbolicLinkName");
}

status = IoCreateSymbolicLink(&symbolicLinkName, &deviceName);
if (!NT_SUCCESS(status)) {
  /* Symbolic link creation failed.  Handle error appropriately. */
}
```

A driver can create MS-DOS device names in a local **\\DosDevices** directories by creating the symbolic link in response to an IOCTL. When a thread in a particular local **DosDevices** context sends the IOCTL, the driver's *DispatchDeviceControl* is called from within the current thread context.

For more information about the context in which a standard driver routine runs, see [Dispatch Routines and IRQLs](dispatch-routines-and-irqls.md).

The system distinguishes local **\\DosDevices** directories as follows:

-   On Windows XP and later, local **\\DosDevices** directories are identified by the **AuthenticationID** for the logon session's access token. For more information about the **AuthenticationID**, see the description of the **TOKEN\_STATISTICS** structure in the Microsoft Windows SDK documentation.

-   On Windows 2000, local **\\DosDevices** directories are identified by the **SessionId** for the terminal server session. For more information about the **SessionId**, see the description of the **WTS\_SESSION\_INFO** structure in the Windows SDK documentation.

Windows NT 4.0 Terminal Server Edition supports local \\**DosDevices** directories in the exact same manner as Windows 2000.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Local%20and%20Global%20MS-DOS%20Device%20Names%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


