---
title: Notification Data Object
description: Notification Data Object
keywords:
- spooler notification WDK print , data object
- print spooler notification WDK , data object
- notification data object WDK print spooler
- IPrintAsyncNotifyDataObject
- data object WDK spooler notification
ms.date: 06/08/2020
---

# Notification Data Object

The notification data is handled as an object that exposes the [IPrintAsyncNotifyDataObject](/windows/win32/api/prnasnot/nn-prnasnot-iprintasyncnotifydataobject) interface. Clients of the spooler notification pipe can define their own data schema and can send any data type back and forth. However, the spooler queries the notification data object for a BYTE\* pointer, the length of the data, and the notification type. The notification type is a GUID, as described in [Notification Types](notification-filtering-and-communication-styles.md#notification-types).

```cpp
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

The notification sender must pack the data in an **IPrintAsyncNotifyDataObject** object. The sender must implement the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface.

The listening client calls the [IPrintAsyncNotifyDataObject::AcquireData](/windows/win32/api/prnasnot/nf-prnasnot-iprintasyncnotifydataobject-acquiredata) method to obtain a raw pointer to the notification data, the size of the notification data, and the notification type.

When the listening client is finished with the data, it must call the [IPrintAsyncNotifyDataObject::ReleaseData](/windows/win32/api/prnasnot/nf-prnasnot-iprintasyncnotifydataobject-releasedata) method. The clients of the spooler notification pipe must implement the **IPrintAsyncNotifyDataObject** interface in such a way that if the **IPrintAsyncNotifyDataObject::Release** method is called before the **IPrintAsyncNotifyDataObject::ReleaseData** method is called, the object is not released. It is recommended that a call to the **IPrintAsyncNotifyDataObject::AcquireData** method should increment the object's reference count, and that a call to the **ReleaseData** method should decrement object's reference count.

The spooler defines a special notification type GUID named NOTIFICATION\_RELEASE. When either the spooler or the listening application dies, the rundown code announces the "still alive" end of the channel by calling the [IPrintAsyncNotifyChannel::CloseChannel](/windows/win32/api/prnasnot/nf-prnasnot-iprintasyncnotifychannel-closechannel) method.

A call to the **IPrintAsyncNotifyDataObject::AcquireData** method against this notification returns with the BYTE\*\* parameter set to **NULL**, the ULONG\* parameter set to 0, and the GUID\* parameter set to NOTIFICATION\_RELEASE.
