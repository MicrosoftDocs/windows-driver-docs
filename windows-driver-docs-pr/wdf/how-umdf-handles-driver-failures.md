---
title: How UMDF Handles Driver Failures
description: This topic describes actions that User-Mode Driver Framework (UMDF) and the operating system take when a UMDF driver fails. It applies to both UMDF versions 1 and 2.
ms.assetid: 1811f131-6a51-4e53-bc8d-da511619f6fd
keywords:
- User-Mode Driver Framework WDK , driver failures
- UMDF WDK , driver failures
- user-mode drivers WDK UMDF , driver failures
- failed drivers WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How UMDF Handles Driver Failures


This topic describes actions that User-Mode Driver Framework (UMDF) and the operating system take when a UMDF driver fails. It applies to both UMDF versions 1 and 2.

The following events occur in the order presented:

-   The operating system notifies the reflector (*WUDFRd.sys*).

-   The reflector tracks outstanding I/O in the host process:
    -   The reflector completes outstanding I/O with the STATUS\_DRIVER\_PROCESS\_TERMINATED error code.
    -   Microsoft Win32 applications receive the ERROR\_DRIVER\_PROCESS\_TERMINATED error code for the outstanding I/O.

    **Note**   The reflector that runs on Microsoft Windows XP completes outstanding I/O with STATUS\_DRIVER\_INTERNAL\_ERROR, and Win32 applications, in turn, receive the ERROR\_IO\_DEVICE error code for the outstanding I/O. Therefore, applications that run on Windows XP should not use ERROR\_IO\_DEVICE to detect a driver failure because they cannot determine any difference from the status that is returned from a typical I/O request (for example, the status that is returned from a call to the Win32 [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function).

     

-   The reflector sends the GUID\_WUDF\_DEVICE\_HOST\_PROBLEM custom Plug and Play (PnP) event to the operating system after the operating system reports a problem with the host process.

    If an application previously called the Win32 **RegisterDeviceNotification** function to register GUID\_WUDF\_DEVICE\_HOST\_PROBLEM for the device, that application will receive a DBT\_CUSTOMEVENT notification when the host process fails. For more information about **RegisterDeviceNotification** and DBT\_CUSTOMEVENT, see the Windows SDK documentation.

-   The operating system writes an entry to the system event log that indicates that the driver failed. It also indicates how many more times the operating system will restart the driver. The operating system writes the following event numbers into the system event log to indicate the specified problems:

    -   10110 if the host process was at fault
    -   10111 if the device went offline and was restarted
    -   10112 if the device went offline and was not restarted

    The framework can attempt to restart a failing driver. The UMDF code verifier provides a [registry value](using-umdf-verifier.md) that controls the number of restart attempts. If the user either disables and enables the device in the Device Manager or unplugs and plugs in the device, the operating system creates a new instance of the device and the framework resets the restart counter.

-   The operating system unloads the kernel drivers in the device stack.

    **Note**   The operating system will not tear down and restart the device stack until all handles to the old stack have closed. An application will detect the device failure and a surprise removal notification for the device (DBT\_REMOVEDEVICEPENDING). However, if any handle to the old stack is kept open, the device is not restarted.

     

-   The driver manager either restarts or disables the device. If the device is disabled, the operating system displays a yellow exclamation point in Device Manager.

Note that after a UMDF driver fails, the following operations can occur in an arbitrary order:

-   The operating system tears down and restarts the device.

-   The reflector sends the GUID\_WUDF\_DEVICE\_HOST\_PROBLEM PnP event to the operating system.

-   The reflector completes outstanding I/O with STATUS\_DRIVER\_PROCESS\_TERMINATED.

Therefore, an application might receive ERROR\_DRIVER\_PROCESS\_TERMINATED for the outstanding I/O after the operating system has restarted the device. After receiving ERROR\_DRIVER\_PROCESS\_TERMINATED, the application might also receive the DBT\_CUSTOMEVENT notification that results from the GUID\_WUDF\_DEVICE\_HOST\_PROBLEM event.

 

 





