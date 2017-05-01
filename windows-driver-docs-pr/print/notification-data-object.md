---
title: Notification Data Object
author: windows-driver-content
description: Notification Data Object
ms.assetid: 6ba8840d-a693-485c-81da-81205e511120
keywords:
- spooler notification WDK print , data object
- print spooler notification WDK , data object
- notification data object WDK print spooler
- IPrintAsyncNotifyDataObject
- data object WDK spooler notification
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Notification Data Object


## <a href="" id="ddk-notification-data-object-gg"></a>


The notification data is handled as an object that exposes the [IPrintAsyncNotifyDataObject](http://go.microsoft.com/fwlink/p/?linkid=124761) interface. Clients of the spooler notification pipe can define their own data schema and can send any data type back and forth. However, the spooler queries the notification data object for a BYTE\* pointer, the length of the data, and the notification type. The notification type is a GUID, as described in [Notification Types](notification-filtering-and-communication-styles.md#notification-types).

```
#define INTERFACE IPrintAsyncNotifyDataObject
DECLARE_INTERFACE_(IPrintAsyncNotifyDataObject, IUnknown)
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
 
    STDMETHOD(AcquireData)(
         THIS_
         OUT BYTE**,
         OUT ULONG*,
         OUT PrintAsyncNotificationType**
         ) PURE;
 
    STDMETHOD(ReleaseData)(
        THIS
        ) PURE;
};
```

The notification sender must pack the data in an **IPrintAsyncNotifyDataObject** object. The sender must implement the [IUnknown](http://go.microsoft.com/fwlink/p/?linkid=124716) interface.

The listening client calls the [IPrintAsyncNotifyDataObject::AcquireData](http://go.microsoft.com/fwlink/p/?linkid=124762) method to obtain a raw pointer to the notification data, the size of the notification data, and the notification type.

When the listening client is finished with the data, it must call the [IPrintAsyncNotifyDataObject::ReleaseData](http://go.microsoft.com/fwlink/p/?linkid=124763) method. The clients of the spooler notification pipe must implement the **IPrintAsyncNotifyDataObject** interface in such a way that if the **IPrintAsyncNotifyDataObject::Release** method is called before the **IPrintAsyncNotifyDataObject::ReleaseData** method is called, the object is not released. It is recommended that a call to the **IPrintAsyncNotifyDataObject::AcquireData** method should increment the object's reference count, and that a call to the **ReleaseData** method should decrement object's reference count.

The spooler defines a special notification type GUID named NOTIFICATION\_RELEASE. When either the spooler or the listening application dies, the rundown code announces the "still alive" end of the channel by calling the [IPrintAsyncNotifyChannel::CloseChannel](http://go.microsoft.com/fwlink/p/?linkid=124759) method.

A call to the **IPrintAsyncNotifyDataObject::AcquireData** method against this notification returns with the BYTE\*\* parameter set to **NULL**, the ULONG\* parameter set to 0, and the GUID\* parameter set to NOTIFICATION\_RELEASE.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Notification%20Data%20Object%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


