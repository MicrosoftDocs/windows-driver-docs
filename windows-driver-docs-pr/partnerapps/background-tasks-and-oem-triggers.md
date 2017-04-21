---
title: Background tasks and custom triggers
description: Background tasks and custom triggers
ms.assetid: 672d3501-da84-495b-b70e-f07de32aff53
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Background tasks and custom triggers


Background tasks are one method on Windows 10 Mobile for running code in the background. They are part of the standard application platform and essentially provide an app with the ability to register for a system event (trigger) and when that event occurs run a predefined block of code in the background. System triggers include events such as changes in network connectivity or the system time zone.

Under some circumstances, the provided system triggers are not enough to address partner scenarios. To give partners more flexibility and allow for the use of background tasks for more circumstances, partners can create custom triggers that apps can register for. Custom triggers are defined within a device driver and can be used to raise events for any hardware condition that you’d like. When the custom trigger is raised, your app can execute a background task in the exact same manner as the standard app model.

## <span id="Implementing_a_custom_trigger"></span><span id="implementing_a_custom_trigger"></span><span id="IMPLEMENTING_A_CUSTOM_TRIGGER"></span>Implementing a custom trigger


There are two steps to implementing a custom trigger. Specifically, the trigger must be defined and raised within a device driver and an app with a background task must be created.

### <span id="Creating_the_custom_trigger"></span><span id="creating_the_custom_trigger"></span><span id="CREATING_THE_CUSTOM_TRIGGER"></span>Creating the custom trigger

A custom trigger is defined and raised within a native service or device driver through the **RaiseDeviceManufacturerNotificationTrigger** function (OemTriggerHelper.h). It can then be registered for from a universal app and used to initiate a background task in relatively the same manner as a system defined trigger.

The following code excerpt illustrates how to raise a custom trigger.

``` syntax
BYTE pszTriggerQualifier = L"fabrikam.audio-jack.connected";
NTSTATUS Status = RaiseDeviceManufacturerNotificationTrigger(pszTriggerQualifier);
```

Within the code sample above, the string passed as a parameter to the **RaiseDeviceManufacturerNotificationTrigger** function defines the name of the trigger that the app will register for when creating the background task. This identifier must be unique. For that reason, Microsoft recommends that a GUID or fully qualified namespace be used.

### <span id="Creating_a_background_task"></span><span id="creating_a_background_task"></span><span id="CREATING_A_BACKGROUND_TASK"></span>Creating a background task

Creating a background task and registering it for a custom trigger is very similar to the process used for background tasks that work with the standard system triggers.

1.  Begin by creating a Windows 10 Mobile app.

2.  Define the background task in the app manifest file as shown in the following example. Note that the **Type** attribute of the **Task** element is set to `“systemEvent”`

    ``` syntax
    <Applications>
      <Application Id="OemBackgroundTaskSample.App" Executable="$targetnametoken$.exe" EntryPoint=" OemBackgroundTaskSample.App">
        <Extensions>
          <Extension Category="windows.backgroundTasks" EntryPoint="OemBackgroundTask.SampleOemBackgroundTask">
            <BackgroundTasks>
              <Task Type="systemEvent" />
            </BackgroundTasks>
          </Extension>
        </Extensions>
      </Application>
    </Applications>
    ```

3.  Register the app to listen for the custom trigger you created as shown in the following code excerpt. Note that the string used when instantiating the **DeviceManufacturerNotificationTrigger** must match the string used when creating the trigger in your native service or device driver.

    ``` syntax
    public void InitBackgroundTask()
    {
       // Create a new background task builder.
       BackgroundTaskBuilder taskBuilder = new BackgroundTaskBuilder();

       // Create a new OEM trigger.
       var oemTrigger = new DeviceManufacturerNotificationTrigger(
          "fabrikam.audio-jack.connected",//Trigger Qualifier
          false); //OneShot 

       // Associate the OemTrigger trigger with the background task builder.
       taskBuilder.SetTrigger(oemTrigger);

       // Specify the background task to run when the trigger fires.
       taskBuilder.TaskEntryPoint = OemBackgroundTask.SampleOemBackgroundTask;

       // Name the background task.
       taskBuilder.Name = “fabrikam.audio-jack.connected Task”;

       // Register the background task.
       BackgroundTaskRegistration taskRegistration = taskBuilder.Register();

       // Associate completed event handler with the new background task.
       taskRegistration.Completed += new BackgroundTaskCompletedEventHandler(OnCompleted); 
    }
    ```

4.  Create the background task as shown in the following code excerpt.

    ``` syntax
    namespace OemBackgroundTask
    {
       public sealed class SampleOemBackgroundTask : IBackgroundTask
       {
       // Called by the system when it's time to run our task
          public void Run(IBackgroundTaskInstance instance)
          {
             DoWork();
          }
       }
    }
    ```

For additional guidance about creating, configuring, and working with background tasks and triggers, see [Quickstart: Create and register a background task](http://msdn.microsoft.com/library/windows/apps/hh977055.aspx) on MSDN.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_phPartAppDev\p_phPartAppDev%5D:%20Background%20tasks%20and%20custom%20triggers%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




