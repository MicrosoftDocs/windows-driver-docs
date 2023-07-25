---
title: Notification errors
description: Notification errors
keywords:
- spooler notification WDK print , errors
- print spooler notification WDK , errors
- notification errors WDK print spooler
- errors WDK spooler notification
ms.date: 07/18/2023
---

# Notification errors

The members of the **PrintAsyncNotifyError** enumerated type are used to signify the type of error that occurred. The following table describes the possible error codes.

| Error code | Value | Communication type | Applies to | Description |
|--|--|--|--|--|
| CHANNEL_CLOSED_BY_SERVER | 0x01 |  |  | **SendNotification** and **CloseChannel** return this value when the print spooler closed the channel prior to the call. |
| CHANNEL_CLOSED_BY_ANOTHER_LISTENER | 0x02 | Bidirectional | Listener | SendNotification and **CloseChannel** return this value when another listener closed the channel prior to the call. |
| CHANNEL_CLOSED_BY_SAME_LISTENER | 0x03 | Bidirectional | Sender | **CloseChannel** returns this value when the same listener closed the channel prior to the call. |
| CHANNEL_RELEASED_BY_LISTENER | 0x04 |  |  | **SendNotification** and **CloseChannel** return this value when another listener released the channel prior to the call. |
| UNIRECTIONAL_NOTIFICATION_LOST | 0x05 | Unidirectional | Sender | **SendNotification** returns this value to the sender when one or more of the present listeners did not receive the notification. This can occur when the sender sends notifications faster than the listeners can process. |
| ASYNC_NOTIFICATION_FAILURE | 0x06 | Unidirectional | Sender | **SendNotification** returns this value to the sender when none of the present listeners receive the notification. This situation can occur in some limited system resource conditions.. |
| NO_LISTENERS | 0x07 | Unidirectional | Sender | **SendNotification** returns this value to the sender as a non-error to indicate that no listeners are registered. |
| CHANNEL_ALREADY_CLOSED | 0x08 | Bidirectional | Sender and Listener | **SendNotification** returns this value when the channel was already closed. |
| CHANNEL_ALREADY_OPENED | 0x09 | Bidirectional and Unidirectional | Sender and Listener | **CreateNotificationChannel** returns this value when the channel is already open. |
| CHANNEL_WAITING_FOR_CLIENT_NOTIFICATION | 0x0a | Bidirectional | Sender | **SendNotification** returns this value when the channel is waiting for a client notification. |
| CHANNEL_NOT_OPENED | 0x0b | Bidirectional and Unidirectional | Sender | **CreateNotificationChannel** returns this value when the channel has not been opened. |
| ASYNC_CALL_ALREADY_PARKED | 0x0c | Bidirectional and Unidirectional | Sender (Internal) | A call has already been placed on this channel. More than one call per channel at a time is not allowed. |
| NOT_REGISTERED | 0x0d |  |  | **UnregisterForNotifications** returns this value when the registration object has not been registered. |
| ALREADY_UNREGISTERED | 0x0e | Bidirectional and Unidirectional | Listener | **UnregisterForNotifications** returns this value when the registration object has already been unregistered. |
| ALREADY_REGISTERED | 0x0f | Bidirectional and Unidirectional | Listener | **RegisterForNotifications** returns this value when the registration object has already been registered. |
| CHANNEL_ACQUIRED | 0x10 | Bidirectional | Sender | **SendNotification** and **CloseChannel** return this value when another listener acquires the channel. |
| ASYNC_CALL_IN_PROGRESS | 0x11 | Bidirectional | Sender | **SendNotification** returns this value when a call is already in progress. Only one call per channel is allowed at a time. |
| MAX_NOTIFICATION_SIZE_EXCEEDED | 0x12 | Bidirectional and Unidirectional | Sender | **SendNotification** returns this value when the notification data size exceeds the maximum allowed. |
| INTERNAL_NOTIFICATION_QUEUE_IS_FULL | 0x13 | Bidirectional and Unidirectional | Sender | **OnEventNotify** returns this value when the notification queue is full. |
| INVALID_NOTIFICATION_TYPE | 0x14 | Bidirectional and Unidirectional | Sender | **SendNotification** returns this value when the notification's type is different than the channel's type. |
| MAX_REGISTRATION_COUNT_EXCEEDED | 0x15 | Bidirectional and Unidirectional | Listener | **RegisterForNotifications** returns this value when the number of registrations exceeds the maximum number that is allowed. |
| MAX_CHANNEL_COUNT_EXCEEDED | 0x16 | Bidirectional and Unidirectional | Sender | **CreatePrintNotificationChannel** returns this value when the number of channels exceeds the maximum number that is allowed. |
