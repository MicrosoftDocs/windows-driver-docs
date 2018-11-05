---
title: Vendor's GFX User Interface
description: Vendor's GFX User Interface
ms.assetid: 853c7df4-6292-44c1-b104-7c62cbc36b3a
keywords:
- GFX filters WDK audio , user interfaces
- user interface WDK GFX filters
- ISpecifyPropertyPages interface
- IPropertyPage interface
- property page objects WDK GFX filters
- COM user interfaces WDK GFX filters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vendor's GFX User Interface


## <span id="vendor_s_gfx_user_interface"></span><span id="VENDOR_S_GFX_USER_INTERFACE"></span>


A vendor who provides a GFX filter should also provide a COM-based user interface that supports the [**ISpecifyPropertyPages**](https://msdn.microsoft.com/library/windows/desktop/ms695217) interface. For information about this interface, see [ISpecifyPropertyPages](https://go.microsoft.com/fwlink/p/?linkid=106291).

The CLSID of this COM object is specified in the GFX driver's installation INF file. For more information, see the description of the **UserInterface/CLSID** subkey in the [Installing a Device-Specific GFX Filter](installing-a-device-specific-gfx-filter.md) topic.

In addition to providing the user interface, the vendor should provide property page COM objects that implement the [**IPropertyPage**](https://msdn.microsoft.com/library/windows/desktop/ms691246) interface for each property page CLSID that is returned by the UI object's [**ISpecifyPropertyPages**](https://msdn.microsoft.com/library/windows/desktop/ms695217) interface. Vendors can choose appropriate ways to implement, install, and register these COM objects. For information about the **IPropertyPage** interface, see the Windows SDK documentation.

The Multimedia applet in Control Panel passes a data object to the property pages by calling [**IPropertyPage::SetObjects**](https://msdn.microsoft.com/library/windows/desktop/ms678529). The vendor's property page object can call [**IDataObject::GetData**](https://msdn.microsoft.com/library/windows/desktop/ms678431) with the medium type specified as TYMED\_HGLOBAL. This call creates a new handle to the vendor's GFX filter. The vendor's property page objects can use this handle to access the GFX filter's [KS properties, events, and methods](https://msdn.microsoft.com/library/windows/hardware/ff567673). The property page object must make sure that the handle is eventually closed by calling [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211). For more information about **IDataObject::GetData** and **CloseHandle**, see the Windows SDK documentation.

 

 




