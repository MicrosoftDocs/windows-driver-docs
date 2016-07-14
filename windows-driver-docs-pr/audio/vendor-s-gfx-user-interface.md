---
Description: 'Vendor''s GFX User Interface'
MS-HAID: 'audio.vendor\_s\_gfx\_user\_interface'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Vendor''s GFX User Interface'
---

# Vendor's GFX User Interface


## <span id="vendor_s_gfx_user_interface"></span><span id="VENDOR_S_GFX_USER_INTERFACE"></span>


A vendor who provides a GFX filter should also provide a COM-based user interface that supports the [**ISpecifyPropertyPages**](com.ispecifypropertypages) interface. For information about this interface, see the [ISpecifyPropertyPages](http://go.microsoft.com/fwlink/p/?linkid=106291) page on the MSDN website.

The CLSID of this COM object is specified in the GFX driver's installation INF file. For more information, see the description of the **UserInterface/CLSID** subkey in the [Installing a Device-Specific GFX Filter](installing-a-device-specific-gfx-filter.md) topic.

In addition to providing the user interface, the vendor should provide property page COM objects that implement the [**IPropertyPage**](com.ipropertypage) interface for each property page CLSID that is returned by the UI object's [**ISpecifyPropertyPages**](com.ispecifypropertypages) interface. Vendors can choose appropriate ways to implement, install, and register these COM objects. For information about the **IPropertyPage** interface, see the Windows SDK documentation.

The Multimedia applet in Control Panel passes a data object to the property pages by calling [**IPropertyPage::SetObjects**](com.ipropertypage_setobjects). The vendor's property page object can call [**IDataObject::GetData**](com.idataobject_getdata) with the medium type specified as TYMED\_HGLOBAL. This call creates a new handle to the vendor's GFX filter. The vendor's property page objects can use this handle to access the GFX filter's [KS properties, events, and methods](stream.ks_properties__events__and_methods). The property page object must make sure that the handle is eventually closed by calling [**CloseHandle**](base.closehandle). For more information about **IDataObject::GetData** and **CloseHandle**, see the Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Vendor's%20GFX%20User%20Interface%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



