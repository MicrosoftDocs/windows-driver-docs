---
title: Sending Notifications
description: Sending Notifications
keywords:
- notifications WDK Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
---

# Sending Notifications




 

The IHV Extensions DLL calls the [**Dot11ExtSendNotification**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_notification) function to send notifications to any service or application that has registered for the notification. In order to receive the notification, the service or application must register with the Auto Configuration Manager (ACM) by calling the [**WlanRegisterNotification**](/windows/win32/api/wlanapi/nf-wlanapi-wlanregisternotification) function.

**Note**  The service or application must register for notifications with a source value of L2\_NOTIFICATION\_SOURCE\_WLAN\_IHV in order to receive notifications through calls to the [**Dot11ExtSendNotification**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_notification) function.

 

When calling [**Dot11ExtSendNotification**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_notification), the IHV Extensions DLL passes a pointer to a [**L2\_NOTIFICATION\_DATA**](/windows/win32/api/l2cmn/ns-l2cmn-l2_notification_data) structure to the *pNotificationData* parameter. The L2\_NOTIFICATION\_DATA defines the type of the notification and can provide additional data about the notification to the IHV Extensions DLL.

 

 
