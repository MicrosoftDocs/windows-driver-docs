---
title: Develop an app to handle the MobileOperatorNotification event
description: Develop an app to handle the MobileOperatorNotification event
ms.assetid: 3c483888-8ec4-4270-af3e-ef1efc995171
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Develop an app to handle the MobileOperatorNotification event


This topic explains how to develop a mobile broadband app that handles the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event.

-   [Best practices](#bp)

-   [Step 1: Background task contract declaration](#stepone)

-   [Step 2: Background task handler](#steptwo)

-   [Step 3: Handle the Activation event](#stepthree)

-   [Step 4: Handle background task completion handlers](#stepfour)

-   [Troubleshooting](#ts)

-   [Sample backgroundtask.js file](#samp)

## <span id="bp"></span><span id="BP"></span>Best practices


For background event handling, you should use the following best practices:

-   Do not register for background events on which you can’t take action. Processing these events will needlessly consume the app quota.

-   Do not perform large amounts of processing on receipt of a background event.

-   Consider deferring processing to the next time the app is launched.

-   Consider showing a toast notification and updating tile in response to a background event. Your mobile broadband app can process the background event payload.

For more info on background tasks, see [Introduction to Background Tasks](http://go.microsoft.com/fwlink/p/?linkid=313924).

## <span id="stepone"></span><span id="STEPONE"></span>Step 1: Background task contract declaration


For Windows to recognize the background task experiences that are supplied by a mobile broadband app, the app must declare that it is providing an extension to system functionality.

To make the declaration in the package.appxmanifest file for your Visual Studio project, perform the following steps:

**To declare a background task contract**

1.  In **Solution Explorer**, double-click the package.appxmanifest file for your project.

2.  On the **Declarations** tab, from **Available Declarations**, select **Background Tasks** and then click **Add**.

3.  Under the **Properties** heading, enter the following app info:

    -   In the **Start page** box under **App settings**, for a mobile broadband app that uses JavaScript and HTML, enter the file name that handles the background task in the app (for example, **backgroundtask.js**).

    -   Under the **Supported task types** heading, click the **System event** check box.

If this is done correctly, you should have an extension element similar to the following in the package.appxmanifest file.

``` syntax
<Extension Category="windows.backgroundTasks" StartPage="backgroundtask.js">
  <BackgroundTasks>
    <Task Type="systemEvent" />
  </BackgroundTasks>
</Extension>
```

## <span id="steptwo"></span><span id="STEPTWO"></span>Step 2: Background task handler


If your app provides a mobile operator notifications declaration, it must supply a handler for the background task activation. The handler will get the mobile operator network account ID and event data from [**Windows.Networking.NetworkOperators.NetworkOperatorNotificationEventDetails**](https://msdn.microsoft.com/library/windows/apps/br207377).

Because the only UI that is supported by background task is **Toast**, the background task handler can show Toast or save [**NetworkOperatorNotificationEventDetails**](https://msdn.microsoft.com/library/windows/apps/br207377) to local storage.

The following code examples demonstrate a background task that is designed to run when a new administrative SMS notification is received.

**C#**

``` syntax
using Windows.Networking.NetworkOperators;

namespace MNOMessageBackground
{
    public sealed class MNOBackgroundTask : IBackgroundTask
    {
       public void Run(Windows.ApplicationModel.Background.IBackgroundTaskInstance taskInstance)
       {
         NetworkOperatorNotificationEventDetails notifyData = (NetworkOperatorNotificationEventDetails)taskInstance.TriggerDetails;

         //The network account ID is stored in notifyData.NetworkAccountId

            switch (notifyData.NotificationType)
            {
                case NetworkOperatorEventMessageType.Gsm: // 0
                    break;
                case NetworkOperatorEventMessageType.Cdma: // 1
                    break;
                case NetworkOperatorEventMessageType.Ussd: // 2
                    break;
                case NetworkOperatorEventMessageType.DataPlanThresholdReached: // 3
                    break;
                case NetworkOperatorEventMessageType.DataPlanReset: //4 
                    break;
                case NetworkOperatorEventMessageType.DataPlanDeleted: //5
                    break;
                case NetworkOperatorEventMessageType.ProfileConnected: //6
                    break;
                case NetworkOperatorEventMessageType.ProfileDisconnected: //7
                    break;
                case NetworkOperatorEventMessageType.RegisteredRoaming: //8
                    break;
                case NetworkOperatorEventMessageType.RegisteredHome: ///9
                    break;
                case NetworkOperatorEventMessageType.TetheringEntitlementCheck: //10
                    break;

                default:
                    break;
             }

            // Add code to save the message to app local storage, and optionally show toast notification and tile updates.
        }
    }
}
```

**JavaScript**

``` syntax
(function () {
    "use strict";

    //
    // The background task instance's activation parameters are available via
    // Windows.UI.WebUI.WebUIBackgroundTaskInstance.current.
    //
    var backgroundTaskInstance = Windows.UI.WebUI.WebUIBackgroundTaskInstance.current,
        networkOperatorEventType = Windows.Networking.NetworkOperators.NetworkOperatorEventMessageType,
        key = null,
        settings = Windows.Storage.ApplicationData.current.localSettings;

    try {

        
        var details = backgroundTaskInstance.triggerDetails;

// The network account ID is stored in details.networkAccountId.

        switch (details.notificationType) {
            case networkOperatorEventType.gsm:
                showToast("Mobile Broadband message", details.message);
                break;
            case networkOperatorEventType.cdma:
                showToast("Mobile Broadband message", details.message);
                break;
            case networkOperatorEventType.ussd:
                showToast("Mobile Broadband message", details.message);
                break;
            case networkOperatorEventType.dataPlanThresholdReached:
                showToast("Mobile Broadband message", "Data plan threshold reached");
                break;
            case networkOperatorEventType.dataPlanReset:
                showToast("Mobile Broadband message", "Data plan reset");
                break;
            case networkOperatorEventType.dataPlanDeleted:
                showToast("Mobile Broadband message", "Data plan deleted");
                break;
            case networkOperatorEventType.profileConnected:
                showToast("Mobile Broadband message", "Profile connected");
                break;
            case networkOperatorEventType.profileDisconnected:
                showToast("Mobile Broadband message", "Profile disconnected");
                break;
            case networkOperatorEventType.registeredRoaming:
                showToast("Mobile Broadband message", "Registered roaming");
                break;
            case networkOperatorEventType.registeredHome:
                showToast("Mobile Broadband message", "Registered home");
                break;
            case networkOperatorEventType.tetheringEntitlementCheck:
                showToast("Mobile Broadband message", "Entitlement check completed");
                break;
            default:
                showToast("Mobile Broadband message", "Unknown message");
                break;
        }

        //
        // A JavaScript background task must call close when it is done.
        //
 close();
    }
    catch (exception) {
// Display error message.
close();
    }
```

### <span id="Show_tile_and_toast_notifications"></span><span id="show_tile_and_toast_notifications"></span><span id="SHOW_TILE_AND_TOAST_NOTIFICATIONS"></span>Show tile and toast notifications

We recommend that you show both toast and tile notifications in your mobile broadband app because a user can miss a toast notification due to its transient nature. For toast notification and tile update experience design guidelines, see [Designing the user experience of a mobile broadband app](designing-the-user-experience-of-a-mobile-broadband-app.md).

**To enable toast notifications**

1.  In **Solution Explorer**, double-click the package.appxmanifest file for your project.

2.  On the **Application UI** tab, under the **Notifications** heading, set **Toast capable** to **Yes**.

If this is done correctly, you should have an extension element similar to the following in the package.appxmanifest file.

``` syntax
<VisualElements … ToastCapable="true"… />
```

The following code shows how to display a toast notification in a background task handle:

**JavaScript**

``` syntax
function showToast(title, body) {
        var notifications = Windows.UI.Notifications;
        var toastNotificationManager = Windows.UI.Notifications.ToastNotificationManager;
        var toastXml = toastNotificationManager.getTemplateContent(notifications.ToastTemplateType.toastText02);

        var temp = "the parameter will pass to app when app activated from tap Toast ";
        toastXml.selectSingleNode("/toast").setAttribute("launch", temp);

        var textNodes = toastXml.getElementsByTagName("text");
        textNodes[0].appendChild(toastXml.createTextNode(title));
        textNodes[1].appendChild(toastXml.createTextNode(body));

        var toast = new notifications.ToastNotification(toastXml);
        toastNotificationManager.createToastNotifier().show(toast);
    }
```

### <span id="Get_SMS_text_message"></span><span id="get_sms_text_message"></span><span id="GET_SMS_TEXT_MESSAGE"></span>Get SMS text message

If the background task was triggered by an incoming SMS message, the background task details will carry the SMS object in its payload.

**JavaScript**

``` syntax
(function () {
    "use strict";

    //
    // The background task instance's activation parameters are available via
    // Windows.UI.WebUI.WebUIBackgroundTaskInstance.current.
    //
    var backgroundTaskInstance = Windows.UI.WebUI.WebUIBackgroundTaskInstance.current,

    try {
        
        var details = backgroundTaskInstance.triggerDetails;
        if (details.notificationType === networkOperatorEventType.gsm
        || details.notificationType === networkOperatorEventType.cdma)
        {
     var textMessage = new Windows.Devices.Sms.SmsTextMessage.fromBinaryMessage(details.smsMessage);
            
         // textMessage can be used to get other SmsMessage properties    
         // like sender number, timestamp, message part count etc.
         showToast("From: " + textMessage.from + "; TimeStamp: " + textMessage.timestamp, details.message);
        }
```

### <span id="Use_local_storage"></span><span id="use_local_storage"></span><span id="USE_LOCAL_STORAGE"></span>Use local storage

The background task can use local storage to save the message that you get from the background event, so that the app can use that information later.

**JavaScript**

``` syntax
    //
    // Save the message 
    //
    var settings = Windows.Storage.ApplicationData.current.localSettings;
    var keyMessage = "BA5857FA-DE2C-4A4A-BEF2-49D8B4130A39";


    //
    // The background task instance's activation parameters are available via
    // Windows.UI.WebUI.WebUIBackgroundTaskInstance.current
    //
    var backgroundTaskInstance = Windows.UI.WebUI.WebUIBackgroundTaskInstance.current;

    var details = backgroundTaskInstance.triggerDetails;
    settings.values[keyMessage] = details.message;
```

The following code demonstrates how to retrieve the message stored by the background task handler in the app:

**JavaScript**

``` syntax
var settings = Windows.Storage.ApplicationData.current.localSettings;
    var keyMessage = "BA5857FA-DE2C-4A4A-BEF2-49D8B4130A39";
    var operatorMessage = settings.values[keyMessage];
```

## <span id="stepthree"></span><span id="STEPTHREE"></span>Step 3: Handle the Activation event


If the toast sets a parameter, it will be passed to app through **detail.arguments**.

In JavaScript or C#, you handle the [**WinJS.Application.onactivated**](https://msdn.microsoft.com/library/windows/apps/br212679) event, and then examine the event arguments that are passed to the event handler. Activation from toast passes the event argument of type [**Windows.UI.WebUI.WebUILaunchActivatedEventArgs**](https://msdn.microsoft.com/library/windows/apps/hh701841). If the event argument’s **detail.kind** property is [**Windows.ApplicationModel.Activation.ctivationKind**](https://msdn.microsoft.com/library/windows/apps/br224693).**launch**, the app provides either the Start experience or the Notification experience, depending on whether the event argument’s **detail.argument** property is set to **null**.

**JavaScript**

``` syntax
WinJS.Application.addEventListener("activated", activated; false);

function activated(eventArgs)
{
  if (eventArgs.detail.kind == Windows.ApplicationModel.Activation.ActivationKind.launch)
  {
    if (!eventArgs.detail.arguments)
    {
      // Initialize logic for the Start experience here.
    }
    else
    {
      // Initialize logic for the Notification experience here.
    }
  }
}
```

## <span id="stepfour"></span><span id="STEPFOUR"></span>Step 4: Handle background task completion handlers


The foreground app can also register a completion handler to be notified when the background task completes. The completion status or any exception that occurs in the **Run** method of the background task is passed to the completion handler in the foreground app. If the app was suspended when the task completed, it receives the completion notification next time that the app is resumed. If the app was in the **Terminated** state, it does not receive the completion notification. If the background task needs to preserve the information that it ran successfully, it must persist the information by using State Manager or another means, such as a file that the app can read when it returns to the **Running** state.

**Important**  
Although the mobile operator background event is registered automatically by the system to the app, the app still needs to run at least one time to register to the background completion or progress handlers.

 

**C#**

``` syntax
foreach (var cur in BackgroundTaskRegistration.AllTasks)
{
   if(cur.Value.Name == “MobileOperatorNotificationHandler”)
   {
       cur.Value.Progress += new BackgroundTaskProgressEventHandler(OnProgress);
       cur.Value.Completed += new BackgroundTaskCompletedEventHandler(OnCompleted);
   }
}

//
// Handle background task completion.
private void OnCompleted(IBackgroundTaskRegistration sender, BackgroundTaskCompletedEventArgs e)
{
   var taskCompletion = task as IBackgroundTaskRegistration;
   var completionArgs = args.Context as BackgroundTaskCompletedEventArgs;
   
  //
  // If the background task threw an exception, display the exception in the error text box.
  if (completionArgs.Status != null)
  {
    throw completionArgs.Status;
  }
}

// Handle background task progress.
private void OnProgress(IBackgroundTaskRegistration sender, BackgroundTaskProgressEventArgs e)
{
  var taskRegistration = task as IBackgroundTaskRegistration;
  var progressArgs = args.Context as BackgroundTaskProgressEventArgs;
  // progressArgs.Progress has the progress percentage
}
```

**JavaScript**

``` syntax
var iter = Windows.ApplicationModel.Background.BackgroundTaskRegistration.allTasks.first();
var hascur = iter.hasCurrent;
while (hascur) {
    var cur = iter.current.value;
    if (cur.name === “MobileOperatorNotificationHandler”) {
        cur.addEventListener("progress", new ProgressHandler(cur).onProgress);
        cur.addEventListener("completed", new CompleteHandler(cur).onCompleted);
    }
    hascur = iter.moveNext();
}

//
// Handle background task progress.
//
function ProgressHandler(task) {
    this.onProgress = function (args) {
       try {
           var progress = "Progress: " + args.progress + "%";
       } catch (ex) {
           displayError(ex);
       }
   };
}

//
// Handle background task completion.
//
function CompleteHandler(task) {
    this.onCompleted = function (args) {
        try {
            var key = task.taskId;
        } catch (ex) {
            displayError(ex);
        }
    };
}
```

## <span id="ts"></span><span id="TS"></span>Troubleshooting


Use these sections to help troubleshoot issues that may come up.

### <span id="Trigger_metadata_parsing_to_register_background_tasks"></span><span id="trigger_metadata_parsing_to_register_background_tasks"></span><span id="TRIGGER_METADATA_PARSING_TO_REGISTER_BACKGROUND_TASKS"></span>Trigger metadata parsing to register background tasks

For users, when the mobile broadband device is connected, Windows 8, Windows 8.1, and Windows 10 automatically installs the mobile broadband app and associated service metadata and registers background tasks that are defined in the service metadata. However, in Windows 8.1, the app is not automatically pinned to the Start screen.

Developers can manually trigger Windows 8, Windows 8.1, and Windows 10 to parse service metadata and register background tasks by pressing the **F5** key (or right-click and select **Refresh**) in the **Devices and Printers** window on the desktop. Background task registration through service metadata parsing succeeds only when the app is deployed.

### <span id="Verify_that_background_tasks_are_correctly_registered_"></span><span id="verify_that_background_tasks_are_correctly_registered_"></span><span id="VERIFY_THAT_BACKGROUND_TASKS_ARE_CORRECTLY_REGISTERED_"></span>Verify that background tasks are correctly registered

Developers can verify that the Device Setup Manager (DSM) has properly parsed the service metadata by viewing the event logs under **Application and Services Logs\\Microsoft\\Windows\\DeviceSetupManager**.

1.  Open Event Viewer.

2.  On the **Menu** tab, select **View**, and then click **Show Analytic and Debug Logs**.

3.  Browse to **Applications and Services Logs\\Microsoft\\Windows\\DeviceSetupManager**.

Events of interest include Event ID 220 that indicates that DSM has successfully registered the background task for the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event, and Event ID 7900, which indicates any errors that are found in the metadata package.

### <span id="Verify_that_provisioning_metadata_is_successfully_applied"></span><span id="verify_that_provisioning_metadata_is_successfully_applied"></span><span id="VERIFY_THAT_PROVISIONING_METADATA_IS_SUCCESSFULLY_APPLIED"></span>Verify that provisioning metadata is successfully applied

When applying provisioning metadata, verify that [**ProvisionFromXmlDocumentResults.AllElementsProvisioned**](https://msdn.microsoft.com/library/windows/apps/br212047) is true. If not, check the ProvisionResultsXml for more details about the error. Common mobile broadband errors include the following:

-   A mismatch between the SIM in the PC and the provisioning file (profile fails with ERROR\_NOT\_FOUND).

-   A mismatch between the CarrierId in the provisioning file and the service number in the experience metadata.

### <span id="Verify_that_background_tasks_are_being_run_by_the_System_Event_Broker"></span><span id="verify_that_background_tasks_are_being_run_by_the_system_event_broker"></span><span id="VERIFY_THAT_BACKGROUND_TASKS_ARE_BEING_RUN_BY_THE_SYSTEM_EVENT_BROKER"></span>Verify that background tasks are being run by the System Event Broker

You can verify that Windows is generating the [MobileOperatorNotification](mobile-operator-notification-event-technical-details.md) event and that the app’s background task is being run by the event broker by checking the Event Viewer. Logging for these events is off by default and can be enabled by performing the following steps:

1.  Open Event Viewer.

2.  On the **Menu** tab, select **View**, and then click **Show Analytic and Debug Logs**.

3.  Browse to **Applications and Services Logs\\Microsoft\\Windows\\BackgroundTaskInfrastructure**.

4.  Right-click **Diagnostic log** and select **Enable Log**.

After you enable the logs, a successful execution of the background task results in an event of **Event ID = 1** that has the following description: “An instance of a background task with entry point &lt;background\_task\_namespace\_name&gt;.&lt;background\_task\_class\_name&gt; and name MobileOperatorNotificationHandler has been created in session 1 and given an ID of {11111111-1111-1111-1111-111111111111}.”

If the background task is not being run, first verify that the names of your background tasks that are specified in the service metadata match the names in the AppXManifest.xml file of your package. Verify that after deploying the app, parsing the service metadata is triggered and inserts the mobile broadband device.

### <span id="Verify_that_Windows_receives_SMS_and_USSD_notifications"></span><span id="verify_that_windows_receives_sms_and_ussd_notifications"></span><span id="VERIFY_THAT_WINDOWS_RECEIVES_SMS_AND_USSD_NOTIFICATIONS"></span>Verify that Windows receives SMS and USSD notifications

You can verify that Windows is receiving SMS and USSD notifications by checking for SmsRouter events in Event Viewer.

In Event Viewer, under **Application and Services Logs\\Microsoft\\Windows \\Mobile-Broadband-Experience-SmsRouter\\Microsoft-Windows-SMSRouter**, are entries such as “The SMSRouter received a SMS Operator Notification message” and “The SMSRouter received a Text message”. Under **Application and Services Logs\\Microsoft\\Windows \\Mobile-Broadband-Experience-SmsApi\\SMSApi** are entries such as “App: Microsoft.SDKSamples.SmsSendReceive sent SMS text message on mobile broadband device: {11111111-1111-1111-1111-111111111111}”.

### <span id="Received_SMS_messages_are_not_detected_as_operator_notifications"></span><span id="received_sms_messages_are_not_detected_as_operator_notifications"></span><span id="RECEIVED_SMS_MESSAGES_ARE_NOT_DETECTED_AS_OPERATOR_NOTIFICATIONS"></span>Received SMS messages are not detected as operator notifications

If received SMS are not detected as operator notifications, verify the custom filtering rules for administrative SMS notifications in the account provisioning metadata. For more info about provisioning metadata, see [Account provisioning](account-provisioning.md).

In particular, if account provisioning metadata specifies the sender phone number, verify that the number formatting specified matches that in the received message by using the SMS APIs. To verify that this is matching correctly, temporarily change the Pattern to **\[^\]\\*** to match all messages from this sender.

## <span id="samp"></span><span id="SAMP"></span>Sample backgroundtask.js file


``` syntax
//
// A JavaScript background task runs a specified JavaScript file.
//
(function () {
    "use strict";

    //
    // The background task instance's activation parameters are available via Windows.UI.WebUI.WebUIBackgroundTaskInstance.current.
    //
    var backgroundTaskInstance = Windows.UI.WebUI.WebUIBackgroundTaskInstance.current,
        networkOperatorEventType = Windows.Networking.NetworkOperators.NetworkOperatorEventMessageType,
        key = null,
        settings = Windows.Storage.ApplicationData.current.localSettings;

    try {       
        var details = backgroundTaskInstance.triggerDetails;

        switch (details.notificationType) {
            case networkOperatorEventType.gsm:
                var textMessage = new Windows.Devices.Sms.SmsTextMessage.fromBinaryMessage(details.smsMessage);
                showToast("Gsm Msg From: " + textMessage.from + "; TimeStamp: " + textMessage.timestamp, details.message);
                
                break;
            case networkOperatorEventType.cdma:
                showToast("Mobile Broadband message", details.message);
                break;
            case networkOperatorEventType.ussd:
                showToast("Mobile Broadband message", details.message);
                break;
            case networkOperatorEventType.dataPlanThresholdReached:
                showToast("Mobile Broadband message", "Data plan threshold reached");
                break;
            case networkOperatorEventType.dataPlanReset:
                showToast("Mobile Broadband message", "Data plan reset");
                break;
            case networkOperatorEventType.dataPlanDeleted:
                showToast("Mobile Broadband message", "Data plan deleted");
                break;
            case networkOperatorEventType.profileConnected:
                showToast("Mobile Broadband message", "Profile connected");
                break;
            case networkOperatorEventType.profileDisconnected:
                showToast("Mobile Broadband message", "Profile disconnected");
                break;
            case networkOperatorEventType.registeredRoaming:
                showToast("Mobile Broadband message", "Registered roaming");
                break;
            case networkOperatorEventType.registeredHome:
                showToast("Mobile Broadband message", "Registered home");
                break;
            case networkOperatorEventType.tetheringEntitlementCheck:
                showToast("Mobile Broadband message", "Entitlement check completed");
                break;
            default:
                showToast("Mobile Broadband message", "Unknown message");
                break;
        }
        taskSucceeded();
    }
    catch (exception) {
        taskFailed();
    }

    function showToast(title, body) {

        var notifications = Windows.UI.Notifications;
        var toastNotificationManager = Windows.UI.Notifications.ToastNotificationManager;
        var toastXml = toastNotificationManager.getTemplateContent(notifications.ToastTemplateType.toastText02);

        //
        // Pass to app through eventArguments.arguments.
        //
        var temp = "\"Title\"" + ":" + "\"" + title + "\"" + "," + "\"Message\"" + ":" + "\"" + body + "\"";
        if (temp.length > 251) {
            temp = temp.substring(0, 251);
        }
        toastXml.selectSingleNode("/toast").setAttribute("launch", "'{" + temp + "}'");

        var textNodes = toastXml.getElementsByTagName("text");
        textNodes[0].appendChild(toastXml.createTextNode(title));
        textNodes[1].appendChild(toastXml.createTextNode(body));

        var toast = new notifications.ToastNotification(toastXml);
        toastNotificationManager.createToastNotifier().show(toast);        
    }

    //
    // This function is called when the background task is completed successfully.
    //
    function taskSucceeded() {
        //
        // Use the succeeded property to indicate that this background task completed successfully.
        //
        backgroundTaskInstance.succeeded = true;
        backgroundTask.taskInstance.progress = 100;
        console.log("Background " + backgroundTask.taskInstance.task.name + " Completed");

        //
        // Write to localSettings to indicate that this background task completed.
        //
        key = backgroundTaskInstance.task.taskId.toString();
        settings.values[key] = "Completed";

        //
        // A JavaScript background task must call close when it is done.
        //
        close();
    }

    //
    // If the task was canceled or failed, stop the background task.
    //
    function taskFailed() {
        console.log("Background " + backgroundTask.taskInstance.task.name + " Failed");
        backgroundTaskInstance.succeeded = false;

        key = backgroundTaskInstance.task.taskId.toString();
        settings.values[key] = "Failed";

        close();
    }
})();
```

## <span id="related_topics"></span>Related topics


[Enabling mobile operator notifications and system events](enabling-mobile-operator-notifications-and-system-events.md)

[Creating and configuring Internet Sharing experiences](creating-and-configuring-internet-sharing-experiences.md)

 

 






