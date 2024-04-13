---
title: Background Tasks and Custom Triggers
description: Background tasks provide an app with the ability to register a system event that runs a predefined block of code.
ms.date: 03/17/2023
---

# Background tasks and custom triggers

Background tasks are one method on Windows 10 for running code in the background. They are part of the standard application platform and essentially provide an app with the ability to register for a system event (trigger) and when that event occurs run a predefined block of code in the background. System triggers include events such as changes in network connectivity or the system time zone.

Under some circumstances, the provided system triggers are not enough to address partner scenarios. **Starting Windows 10 version 1803**, to give partners more flexibility and allow for the use of background tasks for more circumstances, partners can create custom triggers that apps can register for. Custom triggers are defined within a device driver and can be used to raise events for any hardware condition that you'd like. When the custom trigger is raised, your app can execute a background task in the exact same manner as the standard app model.

## Implementing a custom trigger

There are two steps to implementing a custom trigger. Specifically, the trigger must be defined and raised within a device driver or system service and an app with a background task must be created.

### Creating the custom trigger

A custom trigger is defined and raised within a native service or device driver through the **RtlRaiseCustomSystemEventTrigger** function. It can then be registered for from a universal app and used to initiate a background task in relatively the same manner as a system defined trigger.

The following code excerpt illustrates how to raise a custom trigger.

```cpp
#define GUID_MY_CUSTOMSYSTEMEVENTTRIGGERID L"{9118718B-FF80-4AFE-BAF1-D88A4525F3AB}"

CUSTOM_SYSTEM_EVENT_TRIGGER_CONFIG triggerConfig;
CUSTOM_SYSTEM_EVENT_TRIGGER_INIT(&triggerConfig,
                                 GUID_MY_CUSTOMSYSTEMEVENTTRIGGERID);

NTSTATUS status = RtlRaiseCustomSystemEventTrigger(&triggerConfig);
```

Within the code sample above, the GUID passed as a parameter to the **RtlRaiseCustomSystemEventTrigger** function defines the identifier of the trigger that the app will register for when creating the background task. This identifier must be unique.

### Creating a background task

Creating a background task and registering it for a custom trigger is very similar to the process used for background tasks that work with the standard system triggers.

1. Begin by creating a UWP app.

1. Define the background task in the app manifest file as shown in the following example. Note that the **Type** attribute of the **Task** element is set to `"systemEvent"`

    ```xml
    <Applications>
      <Application Id="MyBackgroundTaskSample.App" Executable="$targetnametoken$.exe" EntryPoint=" MyBackgroundTaskSample.App">
        <Extensions>
          <Extension Category="windows.backgroundTasks" EntryPoint="MyBackgroundTask.SampleBackgroundTask">
            <BackgroundTasks>
              <Task Type="systemEvent" />
            </BackgroundTasks>
          </Extension>
        </Extensions>
      </Application>
    </Applications>
    ```

1. Register the app to listen for the custom trigger you created as shown in the following code excerpt. Note that the string used when instantiating the **CustomSystemEventTrigger** must match the GUID used when creating the trigger in your native service or device driver.

    ```cpp
    public void InitBackgroundTask()
    {
       // Create a new background task builder.
       BackgroundTaskBuilder taskBuilder = new BackgroundTaskBuilder();

       // Create a new CustomSystemEvent trigger.
       var myTrigger = new CustomSystemEventTrigger(
                            "{9118718B-FF80-4AFE-BAF1-D88A4525F3AB}", //Trigger Identifier
                            CustomSystemEventTriggerRecurrence.Once); //OneShot 

       // Associate the CustomSystemEvent trigger with the background task builder.
       taskBuilder.SetTrigger(myTrigger);

       // Specify the background task to run when the trigger fires.
       taskBuilder.TaskEntryPoint = MyBackgroundTask.SampleBackgroundTask;

       // Name the background task.
       taskBuilder.Name = "fabrikam.audio-jack.connected Task";

       // Register the background task.
       BackgroundTaskRegistration taskRegistration = taskBuilder.Register();

       // Associate completed event handler with the new background task.
       taskRegistration.Completed += new BackgroundTaskCompletedEventHandler(OnCompleted); 
    }
    ```

1. Create the background task as shown in the following code excerpt.

    ```cpp
    namespace MyBackgroundTask
    {
       public sealed class SampleBackgroundTask : IBackgroundTask
       {
          // Called by the system when it's time to run our task
          public void Run(IBackgroundTaskInstance instance)
          {
             DoWork();
          }
       }
    }
    ```

For additional guidance about creating, configuring, and working with background tasks and triggers, see [Quickstart: Create and register a background task](/previous-versions/windows/apps/hh977055(v=win.10)).
