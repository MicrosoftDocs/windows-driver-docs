---
title: Property Sheet Extensions
author: windows-driver-content
description: Property Sheet Extensions
ms.assetid: 36254759-882c-45af-92df-e0769b65ec55
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Property Sheet Extensions


## <a href="" id="ddk-property-sheet-extensions-si"></a>


The Properties context menu item provides access to scanner or camera property sheets in either the Scanners and Cameras Control Panel folder for devices (root items) or the My Computer folder.

Property sheet extensions for cameras and scanners also can provide a user interface for specific image acquisition sessions, that is, non-root **IWiaItem** objects (see the Microsoft Windows SDK documentation), that are active when the user is using the default scanning dialog. These extensions are accessed through an advanced properties or advanced settings link on the image acquisition dialog. When an action is chosen from the context menu for a property, WIA constructs the property sheet using the vendor-supplied implementation of the **IShellExtInit** and **IShellPropSheetExt** interfaces (see the Windows SDK documentation).

For both property sheet and context menu UI extensions, the **IDataObject** interface (described in the Windows SDK documentation) describing the selected items uses either the WIAItemNames format, or the WIAItemPointer format. These formats and their format names are defined in *wiadevd.h*.

The WIAItemNames format, whose format name is CFSTR\_WIAITEMNAMES, returns an HGLOBAL pointing to a double-null-terminated list of **IWiaItem** identifiers. Each identifier is of the form &lt;device id&gt;::&lt;full path name&gt;. For root items, the full path name portion is empty.

The WIAItemPointer format is supported in versions of Microsoft Windows XP and later. The format name is CFSTR\_WIAITEMPTR. The WIAItemPointer format returns an STGMEDIUM structure (declared in the Windows SDK documentation) whose **tymed** member is set to TYMED\_ISTREAM. This format can be used when the user selects only a single item. The property sheet or context extension can call **CoUnmarshalInterface** on the **IStream** object stored in the STGMEDIUM structure to retrieve an **IWiaItem** interface. (See the Windows SDK documentation for descriptions of the **CoUnmarshalInterface** function, and the **IStream** and **IWiaItem** interfaces.) Using this format, every page on the property sheet can share a properly marshaled **IWiaItem** interface, which is important during scans.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Property%20Sheet%20Extensions%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


