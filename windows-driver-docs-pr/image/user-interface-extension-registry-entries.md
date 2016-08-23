---
title: User Interface Extension Registry Entries
author: windows-driver-content
description: User Interface Extension Registry Entries
MS-HAID:
- 'WIA\_drv\_cus\_f15095c2-cfca-4489-b410-a83b19c88c9a.xml'
- 'image.user\_interface\_extension\_registry\_entries'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1ddf12a1-50e9-4f6e-9394-5bb1afb67798
---

# User Interface Extension Registry Entries


## <a href="" id="ddk-user-interface-extension-registry-entries-si"></a>


You must provide the COM server class ID for each extension. Note that the class ID of the COM server for each extension is listed as a registry key (not a value) under CLSID\\{WIA\_DIP\_UI\_CLSID}\\shellex, where WIA\_DIP\_UI\_CLSID is the actual GUID returned when the application requests this property. The application uses it as part of the look-up key in the registry. Each extensibility interface can refer to a different class ID. There is no requirement that the same object implement them all. List only those extensions that are implemented. It is not required to list all four.

Because the class ID GUID identifies which driver to use, if all models of your device use the same driver, they can all have the same class ID GUID. If different models use different drivers, then they must have different GUIDs.

<a href="" id="clsid--wia-dip-ui-clsid--shellex-contextmenuhandlers--clsid-of-com-in-process-server-"></a>CLSID\\{WIA\_DIP\_UI\_CLSID}\\shellex\\ContextMenuHandlers\\&lt;CLSID of COM in-process server&gt;  
Vendor-supplied COM DLL that implements context menu UI extensions.

<a href="" id="clsid--wia-dip-ui-clsid--shellex-propertysheethandlers--clsid-of-com-in-process-server-"></a>CLSID\\{WIA\_DIP\_UI\_CLSID}\\shellex\\PropertySheetHandlers\\&lt;CLSID of COM in-process server&gt;  
Vendor-supplied COM DLL that implements property sheet UI extensions.

<a href="" id="clsid--wia-dip-ui-clsid--shellex-wiadialogextensionhandlers--clsid-of-com-in-process-server-"></a>CLSID\\{WIA\_DIP\_UI\_CLSID}\\shellex\\WiaDialogExtensionHandlers\\&lt;CLSID of COM in-process server&gt;  
Vendor-supplied COM DLL that implements application dialog UI extensions.

<a href="" id="clsid--clsid-of-the-com-in-process-server--inprocserver32-default-value"></a>CLSID\\&lt;CLSID of the COM in-process server&gt;\\InProcServer32\\Default Value  
REG\_SZ type containing the name of the vendor-supplied COM server implementing the extensibility interfaces.

<a href="" id="clsid--clsid-of-the-com-in-process-server--inprocserver32-threadingmodel"></a>CLSID\\&lt;CLSID of the COM in-process server&gt;\\InProcServer32\\ThreadingModel  
REG\_SZ type containing the name of the threading model of the vendor-supplied COM server. Set this key to Apartment.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20User%20Interface%20Extension%20Registry%20Entries%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


