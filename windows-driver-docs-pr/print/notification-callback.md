---
title: Notification Callback
author: windows-driver-content
description: Notification Callback
ms.assetid: cf884097-45a4-4ef3-8ebb-64c006838235
keywords: ["spooler notification WDK print , callback", "print spooler notification WDK , callback", "notification callback WDK print spooler", "IPrintAsyncNotifyCallback", "callbacks WDK spooler notification"]
---

# Notification Callback


## <a href="" id="ddk-notification-callback-gg"></a>


Any print component or listening application that is interested in receiving notifications must provide objects that expose the [IPrintAsyncNotifyCallback](http://go.microsoft.com/fwlink/p/?linkid=124755) interface. The interface inherits from **IUnknown** so that the clients of the spooler notification mechanism can implement either a COM or a C++ object.

A listening application must provide a pointer to an **IPrintAsyncNotifyCallback** interface when it registers to receive notifications. The notification sender must provide a pointer to an **IPrintAsyncNotifyCallback** interface if it is interested in a response and it creates a bidirectional channel.

```
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

When a notification is sent from one end of the channel, the spooler service calls the [IPrintAsyncNotifyCallback::OnEventNotify](http://go.microsoft.com/fwlink/p/?linkid=124757) method at the other end of the channel to deliver the notification.

When the notification channel is closed at one end, the spooler service calls the [IPrintAsyncNotifyCallback::ChannelClosed](http://go.microsoft.com/fwlink/p/?linkid=124756) method at the other end to announce that the channel is closed. The reason for closing the channel is delivered as a notification.

If either the server or the listening application dies, the spooler rundown code detects this condition and the "still alive" end of the channel that is still alive is notified by a **IPrintAsyncNotifyCallback::ChannelClosed** call, in which a NOTIFICATION\_RELEASE message is delivered.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Notification%20Callback%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


