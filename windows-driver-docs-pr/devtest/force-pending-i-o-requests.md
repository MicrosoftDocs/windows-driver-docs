---
title: Force Pending I/O Requests
description: Force Pending I/O Requests
ms.assetid: 0255fc5c-0e75-4108-ba29-f1a61ce9b0dd
keywords:
- Force Pending I/O Requests option WDK Driver Verifier
- STATUS_PENDING WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Force Pending I/O Requests


The Force Pending I/O Requests option randomly returns STATUS\_PENDING in response to a driver's calls to [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336). This option tests the driver's logic for responding to STATUS\_PENDING return values from **IoCallDriver**.

This option is supported only on Windows Vista and later versions of the Windows operating system.

**Caution**   Do not use this option on a driver unless you have detailed knowledge of the operation of the driver and have verified that the driver is designed to handle STATUS\_PENDING return values from all of its calls to **IoCallDriver**. Running this option on a driver that is not designed to handle STATUS\_PENDING from all calls can result in crashes, memory corruptions, and unusual system behavior that can be difficult to debug or correct.

 

### <span id="why_use_force_pending_i_o_requests_"></span><span id="WHY_USE_FORCE_PENDING_I_O_REQUESTS_"></span>Why Use Force Pending I/O Requests?

Higher-level drivers in a driver stack call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to pass an IRP down to lower-level drivers in the driver stack. The driver dispatch routine in the lower-level driver that receives the IRP can either complete the IRP immediately or return STATUS\_PENDING and complete the IRP at a later time.

Typically, the caller must be prepared to handle either outcome. However, because most dispatch routines handle the IRP immediately, the STATUS\_PENDING logic in the caller is not often exercised and serious logic errors might not be detected. The Force Pending I/O Requests option intercepts calls to **IoCallDriver** and returns STATUS\_PENDING to test the calling driver's infrequently used logic.

### <span id="when_do_you_use_force_pending_i_o_requests_"></span><span id="WHEN_DO_YOU_USE_FORCE_PENDING_I_O_REQUESTS_"></span>When do you use Force Pending I/O Requests?

Before running this test, review the driver design and source code and confirm that the driver is intended to handle STATUS\_PENDING from all of its [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) calls.

Many drivers are not designed to handle STATUS\_PENDING on all calls to **IoCallDriver**. They might be sending the IRP to a particular well-known driver that is guaranteed to complete the IRP immediately. Sending STATUS\_PENDING to a driver that does not handle it can cause driver and system crashes and memory corruption.

### <span id="how_should_drivers_handle_status_pending_"></span><span id="HOW_SHOULD_DRIVERS_HANDLE_STATUS_PENDING_"></span>How should drivers handle STATUS\_PENDING?

The higher-level driver that calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) must handle a STATUS\_PENDING return value as follows:

-   Before calling **IoCallDriver**, the driver must call [**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330) to arrange for synchronous processing of the IRP.

-   If **IoCallDriver** returns STATUS\_PENDING, the driver must wait for the completion of the IRP by calling [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) on the specified event.

-   The driver must anticipate that the IRP might be freed before the I/O Manager signals the event.

-   After calling **IoCallDriver**, the caller cannot reference the IRP.

### <span id="which_errors_does_force_pending_i_o_request_detect_"></span><span id="WHICH_ERRORS_DOES_FORCE_PENDING_I_O_REQUEST_DETECT_"></span>Which Errors Does Force Pending I/O Request Detect?

The Force Pending I/O Request option detects the following errors in the driver that calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) and receives a STATUS\_PENDING return value:

-   The driver does not call **IoBuildSynchronousFsdRequest** to arrange for synchronous processing.

-   The driver does not call **KeWaitForSingleObject**.

-   The driver references a value in the IRP structure after calling **IoCallDriver**. After calling **IoCallDriver**, the higher-level driver cannot access the IRP unless it has set a completion routine and then, only when all lower-level drivers have completed the IRP. If the IRP is freed, the driver will crash.

-   The driver calls a related function incorrectly. For example, the driver calls **KeWaitForSingleObject** and passes a handle to the event (as the *Object* parameter), instead of passing a pointer to an event object.

-   The driver waits for the wrong event. For example, the driver calls **IoSetCompletionRoutine**, but waits for an internal event that is signaled by its own completion routine, instead of waiting for the IRP event that is signaled by the I/O Manager when the IRP is complete.

### <span id="Force_Pending_I_O_Requests_Changes_Introduced_in_Windows_7"></span><span id="force_pending_i_o_requests_changes_introduced_in_windows_7"></span><span id="FORCE_PENDING_I_O_REQUESTS_CHANGES_INTRODUCED_IN_WINDOWS_7"></span>Force Pending I/O Requests Changes Introduced in Windows 7

Starting in Windows 7, the Force Pending I/O Requests option is more effective at forcing the exercising of the STATUS\_PENDING code paths in verified drivers. In earlier Windows versions, Driver Verifier forced an IRP completion to be delayed only when the first [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) for that IRP executes. This means that the effectiveness of verifying Driver1 can be reduced by the behavior of Driver2 from the same device stack. Driver2 might wait synchronously for the completion before it returns from its dispatch routine to Driver1. The forced delay of the IRP completion occurs precisely before the I/O request unwinds back into the verified driver on the completion path. This means that the STATUS\_PENDING code path of the verified driver is really exercised and the verified driver perceives a delay in the completion.

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

To activate Force Pending I/O Requests, you must also activate [I/O Verification](i-o-verification.md). You can activate the Force Pending I/O Requests option for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

The Force Pending I/O Requests option is supported only on Windows Vista and later versions of Windows.

-   **At the command line**

    To activate Force Pending I/O Requests, use a flag value of 0x210 or add 0x210 to the flag value. This value activates I/O Verification (0x10), and Force Pending I/O Requests (0x200).

    For example:

    ```
    verifier /flags 0x210 /driver MyDriver.sys
    ```

    The option will be active after the next boot.

    If you try to activate only Force Pending I/O Requests (verifier /flags 0x200), Driver Verifier automatically enables both Force Pending I/O Requests (0x200) and [I/O Verification](i-o-verification.md).

    You can also activate and deactivate Force Pending I/O Requests without rebooting the computer by adding the /volatile parameter to the command. For example:

    ```
    verifier /volatile /flags 0x210 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or reboot the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)**, and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select [I/O Verification](i-o-verification.md) and Force Pending I/O Requests.

    If you select only **Force Pending I/O Requests**, Driver Verifier Manager reminds you that [I/O Verification](i-o-verification.md) is required and offers to enable it for you.

### <span id="viewing_the_results"></span><span id="VIEWING_THE_RESULTS"></span>Viewing the Results

To view the results of the Force Pending I/O Requests test, use the **!verifier** debugger extension with a flag value of 0x40.

For information about **!verifier**, see the **!verifier** topic in the *Debugging Tools for Windows* documentation.

If the test machine crashes as a result of the Force Pending I/O Requests test, you can use the **!verifier 40** command to find the cause. In a current stack trace, find the address of the IRP that was recently used by your driver. For example, if you use the **kP** command, which displays the stack frame for a thread, you can find the IRP address among the function parameters of the current stack trace. Then, run **!verifier 40** and look for the address of the IRP. The most recent force pending stack traces appear at the top of the display.

For example, the following stack trace of Pci.sys shows its response to Force Pending I/O Requests. The test does not reveal any errors in the Pci.sys logic.

```
kd> !verifier 40
# Size of the log is 0x40
========================================================
IRP: 8f84ef00 - forced pending from stack trace:

     817b21e4 nt!IovpLocalCompletionRoutine+0xb2
     81422478 nt!IopfCompleteRequest+0x15c
     817b2838 nt!IovCompleteRequest+0x9c
     84d747df acpi!ACPIBusIrpDeviceUsageNotification+0xf5
     84d2d36c acpi!ACPIDispatchIrp+0xe8
     817b258f nt!IovCallDriver+0x19d
     8142218e nt!IofCallDriver+0x1c
     817c6a9d nt!ViFilterDispatchPnp+0xe9
     817b258f nt!IovCallDriver+0x19d
     8142218e nt!IofCallDriver+0x1c
     84fed489 pci!PciCallDownIrpStack+0xbf
     84fde1cb pci!PciDispatchPnpPower+0xdf
     817b258f nt!IovCallDriver+0x19d
     8142218e nt!IofCallDriver+0x1c
     817c6a9d nt!ViFilterDispatchPnp+0xe9
     817b258f nt!IovCallDriver+0x19d
     8142218e nt!IofCallDriver+0x1c
     84ff2ff5 pci!PciSendPnpIrp+0xbd
 84fec820 pci!PciDevice_DeviceUsageNotification+0x6e
     84fde1f8 pci!PciDispatchPnpPower+0x10c
 817b258f nt!IovCallDriver+0x19d
     8142218e nt!IofCallDriver+0x1c
     84d76ce2 acpi!ACPIFilterIrpDeviceUsageNotification+0x96
     84d2d36c acpi!ACPIDispatchIrp+0xe8
     817b258f nt!IovCallDriver+0x19d
     8142218e nt!IofCallDriver+0x1c
     84f7f16c PCIIDEX!PortWdmForwardIrpSynchronous+0x8e
     84f7b2b3 PCIIDEX!GenPnpFdoUsageNotification+0xcb
     84f7d301 PCIIDEX!PciIdeDispatchPnp+0x45
     817b258f nt!IovCallDriver+0x19d
     8142218e nt!IofCallDriver+0x1c
```

The stack trace shows that *Acpi.sys* was trying to complete IRP 8f84ef00. Driver Verifier forced a deferred completion, so *Acpi.sys* returned STATUS\_PENDING to **pci!PciCallDownIrpStack**. If this call had caused a crash, the driver owner would need to review the source code for **pci!PciCallDownIrpStack** and revise it to handle the STATUS\_PENDING properly.

 

 





