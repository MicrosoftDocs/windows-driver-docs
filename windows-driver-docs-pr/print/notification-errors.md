---
title: Notification Errors
description: Notification Errors
ms.assetid: ffead40c-5c1c-45f6-83d2-48e4af357255
keywords:
- spooler notification WDK print , errors
- print spooler notification WDK , errors
- notification errors WDK print spooler
- errors WDK spooler notification
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Notification Errors





The members of the **PrintAsyncNotifyError** enumerated type are used to signify the type of error that occurred. The following table describes the possible error codes.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Error code</th>
<th>Value</th>
<th>Communication type</th>
<th>Applies to</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHANNEL_CLOSED_BY_SERVER</p></td>
<td><p>0x01</p></td>
<td></td>
<td></td>
<td><p><strong>SendNotification</strong> and <strong>CloseChannel</strong> return this value when the print spooler closed the channel prior to the call.</p></td>
</tr>
<tr class="even">
<td><p>CHANNEL_CLOSED_BY_ANOTHER_LISTENER</p></td>
<td><p>0x02</p></td>
<td><p>Bidirectional</p></td>
<td><p>Listener</p></td>
<td><p>SendNotification and <strong>CloseChannel</strong> return this value when another listener closed the channel prior to the call.</p></td>
</tr>
<tr class="odd">
<td><p>CHANNEL_CLOSED_BY_SAME_LISTENER</p></td>
<td><p>0x03</p></td>
<td><p>Bidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>CloseChannel</strong> returns this value when the same listener closed the channel prior to the call.</p></td>
</tr>
<tr class="even">
<td><p>CHANNEL_RELEASED_BY_LISTENER</p></td>
<td><p>0x04</p></td>
<td></td>
<td></td>
<td><p><strong>SendNotification</strong> and <strong>CloseChannel</strong> return this value when another listener released the channel prior to the call.</p></td>
</tr>
<tr class="odd">
<td><p>UNIRECTIONAL_NOTIFICATION_LOST</p></td>
<td><p>0x05</p></td>
<td><p>Unidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>SendNotification</strong> returns this value to the sender when one or more of the present listeners did not receive the notification. This can occur when the sender sends notifications faster than the listeners can process.</p></td>
</tr>
<tr class="even">
<td><p>ASYNC_NOTIFICATION_FAILURE</p></td>
<td><p>0x06</p></td>
<td><p>Unidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>SendNotification</strong> returns this value to the sender when none of the present listeners receive the notification. This situation can occur in some limited system resource conditions..</p></td>
</tr>
<tr class="odd">
<td><p>NO_LISTENERS</p></td>
<td><p>0x07</p></td>
<td><p>Unidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>SendNotification</strong> returns this value to the sender as a non-error to indicate that no listeners are registered.</p></td>
</tr>
<tr class="even">
<td><p>CHANNEL_ALREADY_CLOSED</p></td>
<td><p>0x08</p></td>
<td><p>Bidirectional</p></td>
<td><p>Sender and Listener</p></td>
<td><p><strong>SendNotification</strong> returns this value when the channel was already closed.</p></td>
</tr>
<tr class="odd">
<td><p>CHANNEL_ALREADY_OPENED</p></td>
<td><p>0x09</p></td>
<td><p>Bidirectional and Unidirectional</p></td>
<td><p>Sender and Listener</p></td>
<td><p><strong>CreateNotificationChannel</strong> returns this value when the channel is already open.</p></td>
</tr>
<tr class="even">
<td><p>CHANNEL_WAITING_FOR_CLIENT_NOTIFICATION</p></td>
<td><p>0x0a</p></td>
<td><p>Bidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>SendNotification</strong> returns this value when the channel is waiting for a client notification.</p></td>
</tr>
<tr class="odd">
<td><p>CHANNEL_NOT_OPENED</p></td>
<td><p>0x0b</p></td>
<td><p>Bidirectional and Unidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>CreateNotificationChannel</strong> returns this value when the channel has not been opened.</p></td>
</tr>
<tr class="even">
<td><p>ASYNC_CALL_ALREADY_PARKED</p></td>
<td><p>0x0c</p></td>
<td><p>Bidirectional and Unidirectional</p></td>
<td><p></p>
Sender
(Internal)</td>
<td><p>A call has already been placed on this channel. More than one call per channel at a time is not allowed.</p></td>
</tr>
<tr class="odd">
<td><p>NOT_REGISTERED</p></td>
<td><p>0x0d</p></td>
<td></td>
<td></td>
<td><p><strong>UnregisterForNotifications</strong> returns this value when the registration object has not been registered.</p></td>
</tr>
<tr class="even">
<td><p>ALREADY_UNREGISTERED</p></td>
<td><p>0x0e</p></td>
<td><p>Bidirectional and Unidirectional</p></td>
<td><p>Listener</p></td>
<td><p><strong>UnregisterForNotifications</strong> returns this value when the registration object has already been unregistered.</p></td>
</tr>
<tr class="odd">
<td><p>ALREADY_REGISTERED</p></td>
<td><p>0x0f</p></td>
<td><p>Bidirectional and Unidirectional</p></td>
<td><p>Listener</p></td>
<td><p><strong>RegisterForNotifications</strong> returns this value when the registration object has already been registered.</p></td>
</tr>
<tr class="even">
<td><p>CHANNEL_ACQUIRED</p></td>
<td><p>0x10</p></td>
<td><p>Bidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>SendNotification</strong> and <strong>CloseChannel</strong> return this value when another listener acquires the channel.</p></td>
</tr>
<tr class="odd">
<td><p>ASYNC_CALL_IN_PROGRESS</p></td>
<td><p>0x11</p></td>
<td><p>Bidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>SendNotification</strong> returns this value when a call is already in progress. Only one call per channel is allowed at a time.</p></td>
</tr>
<tr class="even">
<td><p>MAX_NOTIFICATION_SIZE_EXCEEDED</p></td>
<td><p>0x12</p></td>
<td><p>Bidirectional and Unidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>SendNotification</strong> returns this value when the notification data size exceeds the maximum allowed.</p></td>
</tr>
<tr class="odd">
<td><p>INTERNAL_NOTIFICATION_QUEUE_IS_FULL</p></td>
<td><p>0x13</p></td>
<td><p>Bidirectional and Unidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>OnEventNotify</strong> returns this value when the notification queue is full.</p></td>
</tr>
<tr class="even">
<td><p>INVALID_NOTIFICATION_TYPE</p></td>
<td><p>0x14</p></td>
<td><p>Bidirectional and Unidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>SendNotification</strong> returns this value when the notification&#39;s type is different than the channel&#39;s type.</p></td>
</tr>
<tr class="odd">
<td><p>MAX_REGISTRATION_COUNT_EXCEEDED</p></td>
<td><p>0x15</p></td>
<td><p>Bidirectional and Unidirectional</p></td>
<td><p>Listener</p></td>
<td><p><strong>RegisterForNotifications</strong> returns this value when the number of registrations exceeds the maximum number that is allowed.</p></td>
</tr>
<tr class="even">
<td><p>MAX_CHANNEL_COUNT_EXCEEDED</p></td>
<td><p>0x16</p></td>
<td><p>Bidirectional and Unidirectional</p></td>
<td><p>Sender</p></td>
<td><p><strong>CreatePrintNotificationChannel</strong> returns this value when the number of channels exceeds the maximum number that is allowed.</p></td>
</tr>
</tbody>
</table>

 

 

 




