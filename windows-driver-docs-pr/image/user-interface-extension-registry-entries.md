---
title: User Interface Extension Registry Entries
description: User Interface Extension Registry Entries
ms.assetid: 1ddf12a1-50e9-4f6e-9394-5bb1afb67798
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# User Interface Extension Registry Entries





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

 

 




