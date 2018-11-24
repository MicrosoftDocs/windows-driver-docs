---
title: Property Sheet Extensions
description: Property Sheet Extensions
ms.assetid: 36254759-882c-45af-92df-e0769b65ec55
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Property Sheet Extensions





The Properties context menu item provides access to scanner or camera property sheets in either the Scanners and Cameras Control Panel folder for devices (root items) or the My Computer folder.

Property sheet extensions for cameras and scanners also can provide a user interface for specific image acquisition sessions, that is, non-root **IWiaItem** objects (see the Microsoft Windows SDK documentation), that are active when the user is using the default scanning dialog. These extensions are accessed through an advanced properties or advanced settings link on the image acquisition dialog. When an action is chosen from the context menu for a property, WIA constructs the property sheet using the vendor-supplied implementation of the **IShellExtInit** and **IShellPropSheetExt** interfaces (see the Windows SDK documentation).

For both property sheet and context menu UI extensions, the **IDataObject** interface (described in the Windows SDK documentation) describing the selected items uses either the WIAItemNames format, or the WIAItemPointer format. These formats and their format names are defined in *wiadevd.h*.

The WIAItemNames format, whose format name is CFSTR\_WIAITEMNAMES, returns an HGLOBAL pointing to a double-null-terminated list of **IWiaItem** identifiers. Each identifier is of the form &lt;device id&gt;::&lt;full path name&gt;. For root items, the full path name portion is empty.

The WIAItemPointer format is supported in versions of Microsoft Windows XP and later. The format name is CFSTR\_WIAITEMPTR. The WIAItemPointer format returns an STGMEDIUM structure (declared in the Windows SDK documentation) whose **tymed** member is set to TYMED\_ISTREAM. This format can be used when the user selects only a single item. The property sheet or context extension can call **CoUnmarshalInterface** on the **IStream** object stored in the STGMEDIUM structure to retrieve an **IWiaItem** interface. (See the Windows SDK documentation for descriptions of the **CoUnmarshalInterface** function, and the **IStream** and **IWiaItem** interfaces.) Using this format, every page on the property sheet can share a properly marshaled **IWiaItem** interface, which is important during scans.

 

 




