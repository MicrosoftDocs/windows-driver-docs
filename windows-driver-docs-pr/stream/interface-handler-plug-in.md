---
title: Interface Handler Plug-in
author: windows-driver-content
description: Interface Handler Plug-in
MS-HAID:
- 'ksproxy\_dg\_2cf82267-7e9c-4e88-9887-59399c29c654.xml'
- 'stream.interface\_handler\_plug\_in'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cd81f622-d11c-4b40-ac78-9324716e0a2c
keywords: ["Kernel Streaming Proxy WDK AVStream , interface handler", "interface handler WDK AVStream"]
---

# Interface Handler Plug-in


You can write an interface handler plug-in to provide programmatic user-mode access to a driver-specific property set that is exposed by a KS minidriver. First, register your object as described in [Registering KS Proxy Plug-ins](registering-ks-proxy-plug-ins.md).

Your interface plug-in class could derive from [CUnknown](http://go.microsoft.com/fwlink/p/?linkid=106451):

```
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

```
hResult = piOuterUnknown->QueryInterface(
                __uuidof( piKsPropertySet ),
                 &piKsPropertySet );
```

Then, from **CreateInstance**, invoke the constructor of your interface to create an instance of your interface handler object.

Provide the pointer to **IKsPropertySet** as a parameter in the invocation of the constructor. The constructor then retains the pointer to iKsPropertySet as the m\_piKsPropertySet member in the previous declaration.

Now you can implement Get and Set methods in your class that call [**IKsPropertySet::Get**](https://msdn.microsoft.com/library/windows/hardware/ff560719) and [**IKsPropertySet::Set**](https://msdn.microsoft.com/library/windows/hardware/ff560721) respectively to manipulate properties that are exposed by the driver.

Alternatively, you can query the outer unknown for a pointer to its **IKsObject** interface. Then call [**IKsObject::KsGetObjectHandle**](https://msdn.microsoft.com/library/windows/hardware/ff559890) to obtain a file handle. Now you manipulate device properties by calling [**KsSynchronousIoControlDevice**](https://msdn.microsoft.com/library/windows/hardware/ff567143) with this file handle.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Interface%20Handler%20Plug-in%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


