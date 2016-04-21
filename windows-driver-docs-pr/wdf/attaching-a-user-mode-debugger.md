---
title: Attaching a User-Mode Debugger
author: windows-driver-content
description: Attaching a User-Mode Debugger
ms.assetid: ba8eeabd-946d-46fa-b9ed-b9a674315bd4
keywords: ["attaching user-mode debuggers WDK UMDF", "multiple-device debugger attachments WDK UMDF", "single-device debugger attachments WDK UMDF", "User-Mode Driver Framework WDK , user-mode debugger", "UMDF WDK , user-mode debugger", "user-mode debugger WDK UMDF", "user-mode debugger WDK UMDF , attaching", "user-mode drivers WDK UMDF , debugging", "debugging drivers WDK UMDF , attaching a user-mode debugger", "driver debugging WDK UMDF , attaching a user-mode debugger"]
---

# Attaching a User-Mode Debugger


After the driver manager starts the driver host process for the device, you can attach a user-mode debugger. How you attach the debugger depends on how many devices are attached to the computer:

-   If a single device is attached, run the following command:

    ```
    windbg -pn WUDFHost.exe
    ```

    Run this command repeatedly until a host process to debug is discovered.

-   If multiple devices are attached, determine the process identifier (PID) of a particular host and run the following command:

    ```
    windbg -p PID
    ```

    You can use the operating system-supplied Tasklist.exe to determine the PID of a host process. (Tasklist.exe is a command-line application that provides a user with a list of processes that are running on the operating system.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Attaching%20a%20User-Mode%20Debugger%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




