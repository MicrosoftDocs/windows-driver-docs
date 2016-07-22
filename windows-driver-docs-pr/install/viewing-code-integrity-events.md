---
title: Viewing Code Integrity Events
description: Viewing Code Integrity Events
ms.assetid: b1c8ea3e-1a10-41fd-bdc8-c1e6e7344d39
keywords: ["Event Viewer WDK driver signing", "viewing Code Integrity events", "displaying Code Integrity events"]
---

# Viewing Code Integrity Events


You can use the Event Viewer to view Code Integrity events. You can access the Event Viewer in the Computer Management Microsoft Management Console (MMC) or by running the *Eventvwr.exe* command from a command line.

To view Code Integrity events in the Event Viewer, expand the following sequence of subfolders under the **Event Viewer** folder in the left pane of the Computer Management MMC or the Event Viewer window:

1.  **Applications and Services Logs**

2.  **Microsoft**

3.  **Windows**

4.  **CodeIntegrity**

The following screen shot shows the result of expanding the **CodeIntegrity** subfolder under the **Event Viewer** folder.

![screen shot of the computer management window illustrating viewing code integrity events](images/signing-code-integrity-folder.png)

For more information about a particular Code Integrity log entry, right-click the entry and then select **Event Properties** on the pop-up menu. The following screen shot shows the details about a Code Integrity event.

![screen shot of the event properties dialog box illustrating unsigned driver error](images/event-prop.png)

This event indicates that the Toaster driver (toaster.sys) could not be loaded because it was unsigned (or the toaster.sys image that is trying to load is not the same one that was digitally-signed by the publisher).

For a list of all Code Integrity event log messages, see [Code Integrity Event Log Messages](code-integrity-event-log-messages.md).

The System log events are viewable in the Event Viewer under the Windows Logs, System log view.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Viewing%20Code%20Integrity%20Events%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




