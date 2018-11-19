---
title: Interface Handler Plug-in
description: Interface Handler Plug-in
ms.assetid: cd81f622-d11c-4b40-ac78-9324716e0a2c
keywords:
- Kernel Streaming Proxy WDK AVStream , interface handler
- interface handler WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Interface Handler Plug-in


You can write an interface handler plug-in to provide programmatic user-mode access to a driver-specific property set that is exposed by a KS minidriver. First, register your object as described in [Registering KS Proxy Plug-ins](registering-ks-proxy-plug-ins.md).

Your interface plug-in class could derive from [CUnknown](http://go.microsoft.com/fwlink/p/?linkid=106451):

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

You can then query this outer object for a pointer to the MS-provided [IKsPropertySet](https://msdn.microsoft.com/library/windows/hardware/ff560718) interface:

```cpp
hResult = piOuterUnknown->QueryInterface(
                __uuidof( piKsPropertySet ),
                 &piKsPropertySet );
```

Then, from **CreateInstance**, invoke the constructor of your interface to create an instance of your interface handler object.

Provide the pointer to **IKsPropertySet** as a parameter in the invocation of the constructor. The constructor then retains the pointer to iKsPropertySet as the m\_piKsPropertySet member in the previous declaration.

Now you can implement Get and Set methods in your class that call [**IKsPropertySet::Get**](https://msdn.microsoft.com/library/windows/hardware/ff560719) and [**IKsPropertySet::Set**](https://msdn.microsoft.com/library/windows/hardware/ff560721) respectively to manipulate properties that are exposed by the driver.

Alternatively, you can query the outer unknown for a pointer to its **IKsObject** interface. Then call [**IKsObject::KsGetObjectHandle**](https://msdn.microsoft.com/library/windows/hardware/ff559890) to obtain a file handle. Now you manipulate device properties by calling [**KsSynchronousIoControlDevice**](https://msdn.microsoft.com/library/windows/hardware/ff567143) with this file handle.

 

 




