---
title: Property Page Plug-in
description: Property Page Plug-in
ms.assetid: cf5f5861-1670-413c-9c42-c1b6eb6d719a
keywords:
- Kernel Streaming Proxy WDK AVStream , property page
- property page WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Property Page Plug-in


You can provide a user interface to device properties by writing a property page as a plug-in for KS proxy. This topic explains how to write such a plug-in. First, register your object as described in [Registering KS Proxy Plug-ins](registering-ks-proxy-plug-ins.md).

Next, declare the factory template for your filter. A factory template is a C++ class that contains information for the class factory.

In your DLL, declare a global array of [CFactoryTemplate](http://go.microsoft.com/fwlink/p/?linkid=106450)objects, one for each filter or COM component in your DLL. If you only have one property page, create only one object in the array.

For each object, generate a GUID for the class identifier (CLSID) and provide an entry in the declaration.

The array must be named g\_Templates:

```cpp
CFactoryTemplate g_Templates[] =
{
    {
        L"My Property Page",
        &CLSID_MyPropPage),
        CMyPropPage::CreateInstance,
        NULL,
        NULL
    },
};
```

Your property page should derive from the class [CBasePropertyPage](http://go.microsoft.com/fwlink/p/?linkid=106449) and should override several of the methods of **CBasePropertyPage**:

```cpp
class CMyPropPage: public CBasePropertyPage
{
public:
    // creation routine returns ptr to new prop pg as a CUnknown
    static CUnknown* CreateInstance( LPUNKNOWN piOuterUnknown, HRESULT* phResult );

    // overridden methods:
    HRESULT OnConnect( IUnknown *punk);
    HRESULT OnDisconnect();
    HRESULT OnApplyChanges();
    HRESULT OnActivate();
    HRESULT OnDeactivate();
    INT_PTR OnReceiveMessage( HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam );
private:
    CMyPropPage ( LPUNKNOWN piOuterUnknown );
};
```

To initialize the property page, the hosting property sheet calls [IPropertyPage::SetPageSite](http://go.microsoft.com/fwlink/p/?linkid=106442). This call results in a call of the plug-in's **OnConnect** method. At the time of this call, the property page has been connected to the filter, but the property page has not yet been displayed.

The parameter provided in the call to **OnConnect** is the interface to KS proxy, which can then be queried for a pointer to **IKsPropertySet**. You can then call [**IKsPropertySet::Get**](https://msdn.microsoft.com/library/windows/hardware/ff560719) and [**IKsPropertySet::Set**](https://msdn.microsoft.com/library/windows/hardware/ff560721) to manipulate the exposed properties of the driver.

You must also provide a **CreateInstance** method. The system invokes a property page's method to create an instance of the property page. This method should call the constructor of your class to instantiate it.

The constructor receives a pointer to the outer unknown interface, which in this case is KS proxy.

The property page's **OnDisconnect** method is called when the property page should release the associated object. This callback should decrement the reference count on the pointer to the interface to KS proxy by calling its **Release** method.

 

 




