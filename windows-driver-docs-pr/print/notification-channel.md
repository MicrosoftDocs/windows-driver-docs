---
title: Notification Channel
author: windows-driver-content
description: Notification Channel
MS-HAID:
- 'splarch\_b3435e38-1470-4664-80bf-14045befff3c.xml'
- 'print.notification\_channel'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3161342a-0737-4f3b-bb16-32d6949bceea
keywords: ["spooler notification WDK print , channel", "print spooler notification WDK , channel", "notification channel WDK print spooler", "CreatePrintAsyncNotifyChannel", "channel notification WDK print spooler", "data channels WDK spooler notification", "IPrintAsyncNotifyChannel"]
---

# Notification Channel


## <a href="" id="ddk-notification-channel-gg"></a>


This section contains information about the [CreatePrintAsyncNotifyChannel](http://go.microsoft.com/fwlink/p/?linkid=124750) function and the [IPrintAsyncNotifyChannel](http://go.microsoft.com/fwlink/p/?linkid=124758) interface.

```
HRESULT
 CreatePrintAsyncNotifyChannel(
    IN LPCWSTR,
    IN PrintAsyncNotificationType*,
    IN PrintAsyncNotifyUserFilter,
    IN PrintAsyncNotifyConversationStyle,
    IN IPrintAsyncNotifyCallback*,
 OUT IPrintAsyncNotifyChannel**
    );
```

Printing components call the **CreatePrintAsyncNotifyChannel** function to create a notification channel. The channel can be per-printer or per-server.

The printing component can open a notification channel only if the component is loaded by the spooler. Winspool.drv disables this capability if the caller runs inside applications--and not in the spooler service. For example, when the application loads the driver to perform rendering, a call to **CreatePrintAsyncNotifyChannel** fails. However, the same call succeeds if the driver is loaded by the spooler service.

Spoolss.lib provides this functionality so that port monitors can open channels. Components that run inside the spooler and that are linked to Spoolss.lib can call the **CreatePrintAsyncNotifyChannel** function. The following procedure explains the purpose of each input parameter in a call to this function. The first step in the procedure applies to the first parameter in this function, the second step applies to the second parameter, and so on.

To create a notification channel, specify the following items:

1.  The name of the printer or server.

2.  The notification channel type. The caller can specify the type of notifications that are to be sent though this channel.

3.  The user filter. The caller can specify the users that are to receive notifications, either the same user as the notification sender, or all users.

4.  The conversation filter. The caller must specify whether this is a unidirectional or a bidirectional channel. To mark the channel as unidirectional, set the last parameter (of type **IPrintAsyncNotifyChannel**\*\*) of **CreatePrintAsyncNotifyChannel** to **NULL**.

5.  The **IPrintAsyncNotifyCallback** interface to be called when a notification comes back from the other end of the channel. This can be **NULL**, if the caller is not interested in receiving responses.

When **CreatePrintAsyncNotifyChannel** returns, the sixth parameter (of type **IPrintAsyncNotifyChannel**\*\*) points to a memory location that contains the address of an **IPrintAsyncNotifyChannel** object. This object identifies the channel, and is used to send notifications and to close the channel.

### IPrintAsyncNotifyChannel Interface

The **IPrintAsyncNotifyChannel** interface identifies a channel and is used to send notifications and to close the channel. When a printing component calls the **CreatePrintAsyncNotifyChannel** function to create a notification channel, the spooler service responds by providing an object that exposes the **IPrintAsyncNotifyChannel** interface.

This interface inherits from the **IUnknown** interface so that the clients of the spooler notification mechanism can implement either a COM or a C++ object. The interface declaration in the following code example shows this inheritance:

```
#define INTERFACE IPrintAsyncNotifyChannel
DECLARE_INTERFACE_(IPrintAsyncNotifyChannel, IUnknown)
{
    STDMETHOD(QueryInterface)(
        THIS_ 
        REFIID riid, 
        void** ppvObj
        ) PURE;
 
    STDMETHOD_(ULONG, AddRef)(
        THIS
        ) PURE;
 
    STDMETHOD_(ULONG, Release)(
        THIS
        ) PURE;
 
    STDMETHOD(SendNotification)(
         THIS_
         IN IPrintAsyncNotifyDataObject*
         ) PURE;
 
    STDMETHOD(CloseChannel)(
         THIS_
         IN IPrintAsyncNotifyDataObject*
         ) PURE;
};
```

To send a notification, the sender calls the [IPrintAsyncNotifyChannel::SendNotification](http://go.microsoft.com/fwlink/p/?linkid=124760) method. The sender can be either the printing component that opens the channel and sends notifications or a listening client when it has to respond to a notification. This method behaves asynchronously. When the method returns a success code, the spooler tries to send the notification to listeners. But there is no guarantee that any listeners receive the notification.

To close the channel, the sender or a listener can call the [IPrintAsyncNotifyChannel::CloseChannel](http://go.microsoft.com/fwlink/p/?linkid=124759) method. The caller can pass in a notification that gives the reason for closing the channel or can pass a **NULL** pointer. When the channel is closed, all queued notifications are discarded.

You must be careful in calling [Release](http://go.microsoft.com/fwlink/p/?linkid=98433) on a channel object, because it does not follow all the general COM programming invariants. You should call **Release** on **IPrintAsyncNotifyChannel** only if the following conditions occur:

-   If you called [AddRef](http://go.microsoft.com/fwlink/p/?linkid=98432) explicitly, and you must match it with a call to **Release**.

-   If you created the channel as unidirectional, and you must call **Release** one time on the pointer that you received as an output parameter. You should call **Release** after you have sent the desired notifications and closed the channel.

-   If you created the channel as bidirectional, you might have to call **Release** one time on the pointer that you received as an output parameter. You should call **Release** only if you do one or more of the following:
    -   Before you call **Release** for a bidirectional channel, you must always call **CloseChannel** and receive a success result. You must not call **Release** if the call to **CloseChannel** fails, because the channel might have already been released on your behalf.
    -   You must not call **Release** while entering the **ChannelClosed** event. To avoid this situation, check for a call to **CloseChannel** that has failed with the error CHANNEL\_ALREADY\_CLOSED. You do not have to call **Release** in this case, because the channel has already been released on your behalf.
    -   You must not call **CloseChannel**, **Release**, or any other member function on the channel if your **ChannelClosed** callback function has finished running. In this case, the channel has already been released, so any further calls might cause undefined behavior. This restriction might require coordination between your foreground thread and callback object.
    -   You must make sure that your foreground thread and callback object coordinate the call to **CloseChannel** and **Release**. Your foreground thread and your callback object cannot begin a call to **CloseChannel** if the other is about to call or has completed calling **Release**. You can implement this restriction by using the [**InterlockedCompareExchange**](https://msdn.microsoft.com/library/windows/hardware/ff547853) routine. If you do not use **InterlockedCompareExchange**, you might cause undefined behavior.
-   If you registered as a listener on the channel, you can call **CloseChannel** and then call **Release** in your [IPrintAsyncNotifyCallback::OnEventNotify](http://go.microsoft.com/fwlink/p/?linkid=124757) callback function to end the bidirectional communication. However, you must not call **CloseChannel** or **Release** in your **ChannelClosed** callback.

If you meet one of these conditions, you must call **Release**. If you do not meet one of these conditions, you must not call **Release**.

**Note**   Calling **Release** under any of the preceding conditions but the first, in which you call **AddRef** explicitly, is an exception to general COM programming patterns. **IPrintAsyncNotifyChannel** differs from standard COM practice in this situation.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Notification%20Channel%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


