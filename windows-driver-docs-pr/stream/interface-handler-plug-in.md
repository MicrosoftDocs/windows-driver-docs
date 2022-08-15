---
title: Interface Handler Plug-in
description: Interface handler plug-in
keywords:
- Kernel Streaming Proxy WDK AVStream , interface handler
- interface handler WDK AVStream
ms.date: 06/18/2020
---

# Interface handler plug-in

You can write an interface handler plug-in to provide programmatic user-mode access to a driver-specific property set that is exposed by a KS minidriver. First, register your object as described in [Registering KS Proxy Plug-ins](registering-ks-proxy-plug-ins.md).

Your interface plug-in class could derive from [CUnknown](/previous-versions//ms783086(v=vs.85)):

```cpp
class CMyPluginInterface : public CUnknown
{
public:
    // creation method
    static CUnknown* CALLBACK CreateInstance( LPUNKNOWN piOuterUnknown, HRESULT* phResult );
private:
 CMyPluginInterface( IKsPropertySet* piKsPropertySet );
    IKsPropertySet* m_piKsPropertySet;
};
```

The interface plug-in is a vendor-supplied COM interface that aggregates with the MS-provided KS proxy at create time.

Specifically, the **CreateInstance** method of the plug-in receives a pointer to KS proxy as an outer unknown.

You can then query this outer object for a pointer to the MS-provided [IKsPropertySet](/windows-hardware/drivers/ddi/dsound/nn-dsound-ikspropertyset) interface:

```cpp
hResult = piOuterUnknown->QueryInterface(
                __uuidof( piKsPropertySet ),
                 &piKsPropertySet );
```

Then, from **CreateInstance**, invoke the constructor of your interface to create an instance of your interface handler object.

Provide the pointer to **IKsPropertySet** as a parameter in the invocation of the constructor. The constructor then retains the pointer to iKsPropertySet as the m\_piKsPropertySet member in the previous declaration.

Now you can implement Get and Set methods in your class that call [**IKsPropertySet::Get**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-ikspropertyset-get) and [**IKsPropertySet::Set**](/windows-hardware/drivers/ddi/dsound/nf-dsound-ikspropertyset-set) respectively to manipulate properties that are exposed by the driver.

Alternatively, you can query the outer unknown for a pointer to its **IKsObject** interface. Then call [**IKsObject::KsGetObjectHandle**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-iksobject-ksgetobjecthandle) to obtain a file handle. Now you manipulate device properties by calling [**KsSynchronousIoControlDevice**](/windows-hardware/drivers/ddi/ks/nf-ks-kssynchronousiocontroldevice) with this file handle.
