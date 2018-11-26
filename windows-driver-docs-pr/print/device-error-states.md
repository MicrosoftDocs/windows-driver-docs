---
title: Device Error States
description: Device Error States
ms.assetid: 7d0fee11-0fdf-4490-88d0-fb074cbf4082
keywords:
- error states WDK printer
- printer error states WDK
- states WDK printer
- offline state WDK printer
- hot-pluggable bus WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




