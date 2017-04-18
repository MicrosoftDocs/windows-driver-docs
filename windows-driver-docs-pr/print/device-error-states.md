---
title: Device Error States
author: windows-driver-content
description: Device Error States
ms.assetid: 7d0fee11-0fdf-4490-88d0-fb074cbf4082
keywords: ["error states WDK printer", "printer error states WDK", "states WDK printer", "offline state WDK printer", "hot-pluggable bus WDK printer"]
---

# Device Error States


Print devices and their drivers should recover gracefully from any error states that a user can encounter. It is pertinent to test all of your device's possible error states. Ensure that the device notifies the user of each error state, and that the device cancels the action, recovers, and restarts from each error state. First set up the error state, and then verify that the user is informed of the proper error state.

Common printer error states include:

-   **Out of Paper**

-   **Print Door Open**

-   **Out of Toner**

-   **Paper Jam**

-   **Offline**

-   **Hot-Pluggable Bus Errors**

Test each of these error states, both before and during print job operations, with the following procedure:

1.  Set up the error state and then send a print job.

2.  Verify that the job can be canceled, recovered from, and restarted.

3.  Set up the error state to occur during a print job, and then again verify that the job can be canceled, recovered from, and restarted.

You should also perform the following additional test procedures for offline and hot-pluggable error states:

-   **Offline**
    -   When the printer goes into the offline state, verify that the print job remains in the job queue until the device becomes ready for printing again. The job should then complete successfully.
    -   Unplug the power from the printer during and before print jobs. Confirm that the printer reacquires the job queue and starts printing again. See more details in [Power Management](power-management.md).
-   **Hot-Pluggable Bus Errors**
    -   With the device connected, unload and load the device stack (for example, the [USB Driver Stack](https://msdn.microsoft.com/library/windows/hardware/hh406256)). Send print jobs before, during, and after unloading the stack. For example, with USB devices connected, uninstall the USB root hub or host controller to which the device is connected.
    -   Test unloading and loading the device stack with and without print jobs in progress. Verify that the job can be canceled, recovered from, and restarted.
    -   Reload the device stack to allow the print job to recover gracefully.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Device%20Error%20States%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


