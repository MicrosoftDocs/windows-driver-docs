---
title: Run new SMS received background events
description: Run new SMS received background events
ms.assetid: 57534569-3678-4e2c-b55a-7dc6f057fb7d
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Run new SMS received background events


The Mobile Broadband SMS platform provides separate system events for new SMS data that is received, depending on whether it’s an administrative SMS notification from a mobile network operator or a general SMS message. The background system event for a new administrative SMS notification that is received from a mobile network operator is only accessible by a mobile broadband app.

Apps must have already received user consent to use SMS to read new received SMS messages in a background tasks. Apps cannot read the contents of a new received SMS message from a background task if they are accessing SMS for the first time, because the app cannot trigger the system SMS device consent prompt from a background task.

The following code examples demonstrate a background task that is designed to run when a new SMS message is received.

**C# background task code**

``` syntax
namespace SmsBackgroundSample
{
  public sealed class SmsBackgroundTask : IBackgroundTask
  { 
    // The Run method is the entry point of a background task.

    public void Run(IBackgroundTaskInstance taskInstance)
    {
      // Associate a cancellation handler with the background task.

      taskInstance.Canceled += new BackgroundTaskCanceledEventHandler(OnCanceled);

      ManualResetEvent manualEventWaiter = new ManualResetEvent(false);
      manualEventWaiter.Reset();

      // Do the background task activity.

      DisplayToastAsync(taskInstance, manualEventWaiter);

      // Wait until the async operation is done. We need to do this else the background process will exit.
      manualEventWaiter.WaitOne(5000);

            Debug.Print("Background " + taskInstance.Task.Name + (" process ran"));

  }

  async void DisplayToastAsync(IBackgroundTaskInstance taskInstance, ManualResetEvent manualEventWaiter)
  {
    SmsReceivedEventDetails smsDetails = (SmsReceivedEventDetails)taskInstance.TriggerDetails;
    SmsBinaryMessage smsEncodedmsg = (SmsBinaryMessage) smsDetails.BinaryMessageMessage;
    SmsTextMessage smsTextMessage = Windows.Devices.Sms.SmsTextMessage.FromBinaryMessage(smsEncodedmsg);

    XmlDocument toastXml = ToastNotificationManager.GetTemplateContent(ToastTemplateType.ToastText02);
    XmlNodeList stringElements = toastXml.GetElementsByTagName("text");

    stringElements.Item(0).AppendChild(toastXml.CreateTextNode(smsTextMessage.From));
    stringElements.Item(1).AppendChild(toastXml.CreateTextNode(smsTextMessage.Body));

    ToastNotification notification = new ToastNotification(toastXml);
    ToastNotificationManager.CreateToastNotifier().Show(notification);

    manualEventWaiter.Set();
  }

}
```

**JavaScript app code to register background task**

``` syntax
var triggerAway = new Windows.ApplicationModel.Background.SystemTrigger(Windows.ApplicationModel.Background.SystemTriggerType.smsReceived, false);
var builderAway = new Windows.ApplicationModel.Background.BackgroundTaskBuilder();

builderAway.setTrigger(triggerAway);
builderAway.taskEntryPoint = "HelloWorldBackground.BackgroundTask1";
builderAway.name = "Sms";

var taskAway = builderAway.register();
taskAway.addEventListener("progress", new ProgressHandler(taskAway).onProgress);
taskAway.addEventListener("completed", new CompleteHandler(taskAway).onCompleted);
```

## <span id="related_topics"></span>Related topics


[Developing SMS apps](developing-sms-apps.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Run%20new%20SMS%20received%20background%20events%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





