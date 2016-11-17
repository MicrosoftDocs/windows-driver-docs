---
title: Property Page Plug-in
author: windows-driver-content
description: Property Page Plug-in
MS-HAID:
- 'ksproxy\_dg\_d4f175b1-2966-46ba-98f0-78266a5947a8.xml'
- 'stream.property\_page\_plug\_in'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cf5f5861-1670-413c-9c42-c1b6eb6d719a
keywords: ["Kernel Streaming Proxy WDK AVStream , property page", "property page WDK AVStream"]
---

# Property Page Plug-in


You can provide a user interface to device properties by writing a property page as a plug-in for KS proxy. This topic explains how to write such a plug-in. First, register your object as described in [Registering KS Proxy Plug-ins](registering-ks-proxy-plug-ins.md).

Next, declare the factory template for your filter. A factory template is a C++ class that contains information for the class factory.

In your DLL, declare a global array of [CFactoryTemplate](http://go.microsoft.com/fwlink/p/?linkid=106450)objects, one for each filter or COM component in your DLL. If you only have one property page, create only one object in the array.

For each object, generate a GUID for the class identifier (CLSID) and provide an entry in the declaration.

The array must be named g\_Templates:

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Property%20Page%20Plug-in%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


