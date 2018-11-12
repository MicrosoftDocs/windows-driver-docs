---
title: Notifications
description: Notifications
ms.assetid: 55292cae-9255-4dae-9f60-93ce22253e60
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Notifications


You can keep your users informed through service notifications such as plan activation status, approaching data cap, and currently roaming. Windows supports existing channels such as SMS, USSD, and Windows Notification Service to trigger notifications.

Your mobile broadband app should communicate time-critical events to the user through toast notifications whether the user is in another app, on the **Start** screen, or on the desktop.

![toast notification](images/mb-fig3-toast.png)

Your app can receive background events to process SMS or USSD notifications. For info about background notifications that are associated with mobile broadband apps, see these API pages under the [Windows.ApplicationModel.Background](https://docs.microsoft.com/uwp/api/windows.applicationmodel.background) namespace:

- [MobileBroadbandDeviceServiceNotificationTrigger](https://docs.microsoft.com/uwp/api/windows.applicationmodel.background.mobilebroadbanddeviceservicenotificationtrigger)
- [MobileBroadbandPcoDataChangeTrigger](https://docs.microsoft.com/uwp/api/windows.applicationmodel.background.mobilebroadbandpcodatachangetrigger)
- [NetworkOperatorNotificationTrigger](https://docs.microsoft.com/uwp/api/windows.applicationmodel.background.networkoperatornotificationtrigger)
- [SmsMessageReceivedTrigger](https://docs.microsoft.com/uwp/api/windows.applicationmodel.background.smsmessagereceivedtrigger)

## <span id="related_topics"></span>Related topics


[Mobile broadband app scenarios](mobile-broadband-app-scenarios.md)

 

 






