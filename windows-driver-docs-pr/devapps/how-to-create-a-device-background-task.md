---
title: Creating a device background task in Windows 8.1
description: This topic describes how to create a device background task that uses the DeviceUseTrigger or DeviceServicingTrigger.
ms.assetid: 34263DB8-BB42-480B-AF7F-CC45772E6E84
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a device background task in Windows 8.1 (UWP device apps)


In Windows 8.1, your UWP app can synchronize data on your peripheral device. If your app is associated with device metadata, that UWP device app can also perform device updates, such as firmware updates. This topic describes how to create a device background task that uses the [DeviceUseTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308967) or [DeviceServicingTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308965). Device background agents that use these triggers are subject to policies that ensure user consent and help preserve battery life while devices are being synced and updated. For more info about device background tasks, see [Device sync and update for UWP device apps](device-sync-and-update-for-uwp-device-apps.md).

**Note**  This topic corresponds to the [Custom USB device sample](http://go.microsoft.com/fwlink/p/?LinkId=301975 ). The Custom USB device sample demonstrates a background task that performs device sync with the DeviceUseTrigger. To see an example of a background task that performs a firmware update with the DeviceServicingTrigger, download the [Firmware update USB device sample](http://go.microsoft.com/fwlink/p/?LinkId=309186).



Although the device background task in the [Custom USB device sample](http://go.microsoft.com/fwlink/p/?LinkId=301975 ) features a DeviceUseTrigger, everything discussed in this topic can also be applied to device background tasks that use DeviceServicingTrigger. The only difference between using the two triggers are the policy checks made by Windows.

## <span id="The_app_manifest"></span><span id="the_app_manifest"></span><span id="THE_APP_MANIFEST"></span>The app manifest


To use a device background task, your app must declare it in the app manifest file of your foreground app, like is done for system-triggered background tasks. For more info, see [Device sync and update for UWP device apps](device-sync-and-update-for-uwp-device-apps.md).

In this example from an app package manifest file, **DeviceLibrary.SyncContent** is an entry points from the foreground app. **DeviceLibrary.SyncContent** is the entry point for the background task that uses the [DeviceUseTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308967).

```XML
<Extensions>
  <Extension Category="windows.backgroundTasks" EntryPoint="DeviceLibrary.SyncContent">
    <BackgroundTasks>
      <m2:Task Type="deviceUse" /> 
    </BackgroundTasks>
  </Extension>
</Extensions>
```

## <span id="The_device_background_task"></span><span id="the_device_background_task"></span><span id="THE_DEVICE_BACKGROUND_TASK"></span>The device background task


The device background task class implements the `IBackgroundTask` interface and contains the actual code you create to either sync or update your peripheral device. The background task class is executed when the background task is triggered and from the entry point provided in your app’s application manifest.

The device background class in the [Custom USB device sample](http://go.microsoft.com/fwlink/p/?LinkId=301975 ) contains the code to perform a sync to a USB device using the [DeviceUseTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308967) background task. For complete details, download the sample. For more info about implementing `IBackgroundTask` and the background task infrastructure of Windows see [Supporting your app with background tasks](http://go.microsoft.com/fwlink/p/?LinkID=254337).

Key portions of the device background task in [Custom USB device sample](http://go.microsoft.com/fwlink/p/?LinkId=301975 ) include:

1.  The `IoSyncBackgroundTask` class implements the `IBackgroundTask` interface required by the Windows background task infrastructure.

2.  The `IoSyncBackgroundTask` class obtains the `DeviceUseDetails` instance passed to the class in the `IoSyncBackgroundTask` class’s Run method and uses this instance to report progress back to the Microsoft Store app and to register for cancelation events.

3.  The `IoSyncBackgroundTask` class’s Run method also calls the private `OpenDevice` and `WriteToDeviceAsync` methods that implement the background device sync code.

## <span id="The_foreground_app"></span><span id="the_foreground_app"></span><span id="THE_FOREGROUND_APP"></span>The foreground app


The foreground app in the [Custom USB device sample](http://go.microsoft.com/fwlink/p/?LinkId=301975 ) registers and triggers a device background task that uses [DeviceUseTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308967). This section provides an overview of the steps your foreground app will take to register, trigger and handle progress for a device background task.

The foreground app in the [Custom USB device sample](http://go.microsoft.com/fwlink/p/?LinkId=301975 ) performs the following steps to use a device background task:

1.  Creates new [DeviceUseTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308967) and `BackgroundTaskRegistration` objects.

2.  Checks to see if any background tasks were previously registered by this app and cancels them by calling the [BackgroundTaskRegistration.Unregister](http://go.microsoft.com/fwlink/p/?LinkId=309315) method on the task.

3.  The private `SetupBackgroundTask` method registers the background task that will sync with the device. The `SetupBackgroundTask` method is called from the `SyncWithDeviceAsync` method in the next step.

    1.  Initializes the `DeviceUseTrigger` and saves it for later use.
    2.  Creates a new `BackgroundTaskBuilder` object and uses its `Name`, `TaskEntryPoint` and `SetTrigger` properties and method to register the app’s `DeviceUseTrigger` object and background task name. The `BackgroundTaskBuilder` object’s `TaskEntryPoint` property is set to the full name of the background task class that will be run when the background task is triggered.
    3.  Registers for completion and progress events from the background task so the foreground app can provide completion and progress updates to the user.

4.  The private `SyncWithDeviceAsync` method registers the background task that will sync with the device and starts the background sync.

    1.  Calls the `SetupBackgroundTask` method from the previous step and registers the background task that will sync with the device.
    2.  Calls the private `StartSyncBackgroundTaskAsync` method which starts the background task. That method closes the app’s handle to the device to ensure that the background task is able to open the device when it starts.

        **Important**  The background task will need to open the device to perform the update so the foreground app must close its connections to the device before calling `RequestAsync`.




    Next, the `StartSyncBackgroundTaskAsync` method calls the `DeviceUseTrigger` object’s `RequestAsync` method which starts triggers the background task and returns the `DeviceTriggerResults` object from `RequestAsync` used to determine if the background task started successfully.

    **Important**  Windows checks to ensure that all necessary task initiation policy checks have been completed. If all policy checks are completed the update operation is now running as a background task outside of the foreground app, allowing the app to be safely suspended while the operation is in progress. Windows will also enforce any runtime requirements and cancel the background task if those requirements are no longer met.



3.  Finally, the `SyncWithDeviceAsync` method uses the `DeviceTriggerResults` object returned from `StartSyncBackgroundTaskAsync` to determine if the background task started successfully. A switch statement is used to inspect the result from `DeviceTriggerResults`


5.  The foreground app implements a private `OnSyncWithDeviceProgress` event handler that will update the app UI with progress from the device background task.

6.  The foreground app implements a private `OnSyncWithDeviceCompleted` event handler to handle the transition from background tasks to foreground app when the background task has completed.

    1.  Uses the `CheckResults` method of the `BackgroundTaskCompletedEventArgs` object to determine if any exceptions were thrown by the background task.
    2.  The foreground app reopens the device for use by the app now that the background task is complete and updates the UI to notify the user.

7.  The foreground app implements private button click event handlers from the UI to start and cancel the background task.

    1.  The private `Sync_Click` event handler calls the `SyncWithDeviceAsync` method described in the previous steps.
    2.  The private `CancelSync_Click` event handler calls the private `CancelSyncWithDevice` method to cancel the background task.

8.  The private `CancelSyncWithDevice` method unregisters and cancels any active device syncs so the device can be reopened by using the [BackgroundTaskRegistration.Unregister](http://go.microsoft.com/fwlink/p/?LinkId=309315) method.

## <span id="related_topics"></span>Related topics


[Custom USB device sample](http://go.microsoft.com/fwlink/p/?LinkId=301975 )

[Firmware update USB device sample](http://go.microsoft.com/fwlink/p/?LinkId=309186)

[Device sync and update for UWP device apps](device-sync-and-update-for-uwp-device-apps.md)

[Launching, resuming, and multitasking](http://go.microsoft.com/fwlink/p/?LinkId=309316)

[Supporting your app with background tasks](http://go.microsoft.com/fwlink/p/?LinkID=254337)










