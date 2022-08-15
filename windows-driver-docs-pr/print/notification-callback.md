---
title: Notification Callback
description: Notification Callback
keywords:
- spooler notification WDK print , callback
- print spooler notification WDK , callback
- notification callback WDK print spooler
- IPrintAsyncNotifyCallback
- callbacks WDK spooler notification
ms.date: 06/08/2020
---

# Notification Callback

Any print component or listening application that is interested in receiving notifications must provide objects that expose the [IPrintAsyncNotifyCallback](/windows/win32/api/prnasnot/nn-prnasnot-iprintasyncnotifycallback) interface. The interface inherits from **IUnknown** so that the clients of the spooler notification mechanism can implement either a COM or a C++ object.

A listening application must provide a pointer to an **IPrintAsyncNotifyCallback** interface when it registers to receive notifications. The notification sender must provide a pointer to an **IPrintAsyncNotifyCallback** interface if it is interested in a response and it creates a bidirectional channel.

```cpp
#define INTERFACE IPrintAsyncNotifyCallback
DECLARE_INTERFACE_(IPrintAsyncNotifyCallback, IUnknown)
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

    STDMETHOD(OnEventNotify)(
         THIS_
 IN IPrintAsyncNotifyChannel*,
         IN IPrintAsyncNotifyDataObject*
         ) PURE;

 STDMETHOD(ChannelClosed)(
         THIS_
         IN IPrintAsyncNotifyChannel*,
         IN IPrintAsyncNotifyDataObject*
         ) PURE;
};
```

When a notification is sent from one end of the channel, the spooler service calls the [IPrintAsyncNotifyCallback::OnEventNotify](/windows/win32/api/prnasnot/nf-prnasnot-iprintasyncnotifycallback-oneventnotify) method at the other end of the channel to deliver the notification.

When the notification channel is closed at one end, the spooler service calls the [IPrintAsyncNotifyCallback::ChannelClosed](/windows/win32/api/prnasnot/nf-prnasnot-iprintasyncnotifycallback-channelclosed) method at the other end to announce that the channel is closed. The reason for closing the channel is delivered as a notification.

If either the server or the listening application dies, the spooler rundown code detects this condition and the "still alive" end of the channel that is still alive is notified by a **IPrintAsyncNotifyCallback::ChannelClosed** call, in which a NOTIFICATION\_RELEASE message is delivered.
