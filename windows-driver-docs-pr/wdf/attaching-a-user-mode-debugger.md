---
title: Attaching a User-Mode Debugger
description: Attaching a User-Mode Debugger
ms.assetid: ba8eeabd-946d-46fa-b9ed-b9a674315bd4
keywords:
- attaching user-mode debuggers WDK UMDF
- multiple-device debugger attachments WDK UMDF
- single-device debugger attachments WDK UMDF
- User-Mode Driver Framework WDK , user-mode debugger
- UMDF WDK , user-mode debugger
- user-mode debugger WDK UMDF
- user-mode debugger WDK UMDF , attaching
- user-mode drivers WDK UMDF , debugging
- debugging drivers WDK UMDF , attaching a user-mode debugger
- driver debugging WDK UMDF , attaching a user-mode debugger
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attaching a User-Mode Debugger


After the driver manager starts the driver host process for the device, you can attach a user-mode debugger. How you attach the debugger depends on how many devices are attached to the computer:

-   If a single device is attached, run the following command:

    ```cpp
    windbg -pn WUDFHost.exe
    ```

    Run this command repeatedly until a host process to debug is discovered.

-   If multiple devices are attached, determine the process identifier (PID) of a particular host and run the following command:

    ```cpp
    windbg -p PID
    ```

    You can use the operating system-supplied Tasklist.exe to determine the PID of a host process. (Tasklist.exe is a command-line application that provides a user with a list of processes that are running on the operating system.)

 

 





