---
title: Adding UI to a WIA Minidriver
description: Adding UI to a WIA Minidriver
ms.assetid: 70440de2-0554-4f5b-9ce4-fe060d3077a4
ms.date: 07/18/2018
ms.localizationpriority: medium
---

# Adding UI to a WIA Minidriver

You can add extended UI or replace UI components for a WIA minidriver by installing a separate DLL with the WIA minidriver. Unlike a TWAIN driver, a WIA driver's UI component is separate from the actual WIA minidriver. The UI components run in the application's process, while the WIA minidriver runs in the WIA service's process. So, a WIA driver might not directly show UI; only the WIA UI extension modules of the driver might show UI.

WIA allows you to add property pages to the system-provided dialog boxes, provide custom icon images, or completely replace the system-provided dialog box. The property page extension mechanism is based on the shell definition of the **IShellPropSheetExt** COM interface (described in the Microsoft Windows SDK documentation). This mechanism is registered under the property sheet handlers (**HKCR\\Clsid\\**&lt;*Clsid of the device UI*&gt;**\\shellex\\PropertySheetHandlers**).

All device dialog box extensions, except property pages, require that the [IWiaUIExtension Interface](https://msdn.microsoft.com/library/windows/hardware/ff545078) be implemented.

If you implement the **IWiaUIExtension** interface and do not wish to replace the system UI, you must return E\_NOTIMPL for the [**IWiaUIExtension::DeviceDialog**](https://msdn.microsoft.com/library/windows/hardware/ff545069) method. Any other return value suppresses the device dialog box for the device.

The device dialog box must be implemented as a modal dialog in an in-process COM server, passing *pDeviceDialogData* -&gt;*hwndParent* for the parent to the **DialogBoxParam** function (described in the Windows SDK documentation). The device dialog box must return S\_OK for success, S\_FALSE if the user cancels the dialog box, or a COM error HRESULT for other errors.

The [**DEVICEDIALOGDATA**](https://msdn.microsoft.com/library/windows/hardware/ff540560) structure contains all of the data needed to implement a custom device dialog.

To provide a custom icon for a device, implement the [**IWiaUIExtension::GetDeviceIcon**](https://msdn.microsoft.com/library/windows/hardware/ff545075) method. The icon is destroyed by the caller using **DestroyIcon** (described in the Windows SDK documentation).

**Note**   WIA has very limited scripting support. So, while it is possible to replace the UI, it is not possible to merely suppress it in a script.

The rest of this section includes:

[Creating a "Hello World" WIA Minidriver UI Extension](creating-a--hello-world--wia-minidriver-ui-extension.md), a complete example of how to implement your own custom UI.
