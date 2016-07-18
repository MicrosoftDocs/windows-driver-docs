---
title: Vendor's GFX User Interface
description: Vendor's GFX User Interface
ms.assetid: 853c7df4-6292-44c1-b104-7c62cbc36b3a
keywords: ["GFX filters WDK audio , user interfaces", "user interface WDK GFX filters", "ISpecifyPropertyPages interface", "IPropertyPage interface", "property page objects WDK GFX filters", "COM user interfaces WDK GFX filters"]
---

# Vendor's GFX User Interface


## <span id="vendor_s_gfx_user_interface"></span><span id="VENDOR_S_GFX_USER_INTERFACE"></span>


A vendor who provides a GFX filter should also provide a COM-based user interface that supports the [**ISpecifyPropertyPages**](https://msdn.microsoft.com/library/windows/desktop/ms695217) interface. For information about this interface, see the [ISpecifyPropertyPages](http://go.microsoft.com/fwlink/p/?linkid=106291) page on the MSDN website.

The CLSID of this COM object is specified in the GFX driver's installation INF file. For more information, see the description of the **UserInterface/CLSID** subkey in the [Installing a Device-Specific GFX Filter](installing-a-device-specific-gfx-filter.md) topic.

In addition to providing the user interface, the vendor should provide property page COM objects that implement the [**IPropertyPage**](https://msdn.microsoft.com/library/windows/desktop/ms691246) interface for each property page CLSID that is returned by the UI object's [**ISpecifyPropertyPages**](https://msdn.microsoft.com/library/windows/desktop/ms695217) interface. Vendors can choose appropriate ways to implement, install, and register these COM objects. For information about the **IPropertyPage** interface, see the Windows SDK documentation.

The Multimedia applet in Control Panel passes a data object to the property pages by calling [**IPropertyPage::SetObjects**](https://msdn.microsoft.com/library/windows/desktop/ms678529). The vendor's property page object can call [**IDataObject::GetData**](https://msdn.microsoft.com/library/windows/desktop/ms678431) with the medium type specified as TYMED\_HGLOBAL. This call creates a new handle to the vendor's GFX filter. The vendor's property page objects can use this handle to access the GFX filter's [KS properties, events, and methods](https://msdn.microsoft.com/library/windows/hardware/ff567673). The property page object must make sure that the handle is eventually closed by calling [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211). For more information about **IDataObject::GetData** and **CloseHandle**, see the Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Vendor's%20GFX%20User%20Interface%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




