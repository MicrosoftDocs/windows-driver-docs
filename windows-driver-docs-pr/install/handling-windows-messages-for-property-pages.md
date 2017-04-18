---
title: Handling Windows Messages for Property Pages
description: Handling Windows Messages for Property Pages
ms.assetid: 4920a003-59b5-41dc-a8ee-5e034087006a
keywords: ["device property pages WDK device installations , Windows messages", "property pages WDK device installations , Windows messages", "custom property pages WDK device installations , Windows messages", "WM_INITDIALOG", "Windows messages WDK property pages", "SendDlgItemMessage", "friendly names WDK property pages", "WM_NOTIFY", "PSN_APPLY"]
---

# Handling Windows Messages for Property Pages


## <a href="" id="ddk-handling-windows-messages-for-property-pages-dg"></a>


When a [device property page provider](types-of-device-property-page-providers.md) handles a request to create a property page for its device or device class, it returns the address of a dialog box procedure for the property page. The dialog box procedure must initialize the property page when it gets a WM\_INITDIALOG message, and it must be prepared to handle changes to device properties when it gets a WM\_NOTIFY message. The procedure can also handle any other such messages it may require, as described in the Microsoft Windows SDK documentation.

In response to a WM\_INITDIALOG message, the dialog box procedure initializes information in the property page. Such information might include an icon that represents the device, the friendly name of the device, and its PnP device description.

[**SetupDiLoadClassIcon**](https://msdn.microsoft.com/library/windows/hardware/ff552053) loads the icons for a specified device class and returns a handle to the loaded large icon that can be used in a subsequent call to **SendDlgItemMessage**. For example:

```
if (SetupDiLoadClassIcon(
        &pTestPropPageData->DeviceInfoData->ClassGuid, &ClassIcon, 
        NULL)) {
    OldIcon = (HICON)SendDlgItemMessage(
                        hDlg, 
                        IDC_TEST_ICON,
                        STM_SETICON, (WPARAM)ClassIcon, 0);
    if (OldIcon) {
                DestroyIcon(OldIcon);
    }
}
```

The handle returned in ClassIcon can be cast to the WPARAM that is required by the SendDlgItemMessage function. In the example, IDC\_TEST\_ICON identifies the control in the dialog box that receives the STM\_SETICON message. The value of IDC\_TEST\_ICON must be defined in the provider. For additional functions that manipulate icons and bitmaps see [Device Installation Functions](https://msdn.microsoft.com/library/windows/hardware/ff541299). For more information about **SendDlgItemMessage**, **DestroyIcon**, and using icons in dialog boxes, see the Windows SDK documentation.

In addition to an icon that represents the device, a typical device property page includes a description or "friendly name" of the device and shows the current settings of device properties. The Plug and Play (PnP) manager stores the PnP properties of each device in the registry. A property page provider can call [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967) to get the value of any such property. If device- or class-specific configuration information has also been stored in the registry as part of the installation process, a property page provider can use other **SetupDiXxx** functions to extract that information for display. For more information, see [Device Installation Functions](https://msdn.microsoft.com/library/windows/hardware/ff541299).

When certain types of changes occur on the page, the property sheet sends a [WM\_NOTIFY](http://go.microsoft.com/fwlink/p/?linkid=181554) message to the dialog box procedure. The dialog box procedure should be prepared to extract the notification code from the message parameters and respond appropriately.

For more information about the notifications that a dialog box procedure might encounter, such as the PSN\_APPLY or PSN\_HELP notifications, and how the procedure should handle them, see [Notifications](http://go.microsoft.com/fwlink/p/?linkid=181555) in the Windows SDK documentation.

### <a href="" id="psn-apply-notifications"></a>PSN\_APPLY Notifications

The property sheet sends a PSN\_APPLY notification message when the user clicks **OK**, **Close**, or **Apply**. In response to this message, the dialog box procedure should validate and apply the changes that were made by the user.

When it receives the PSN\_APPLY notification, the provider must do the following:

1.  If it has not already done so, get a pointer to the device install parameters ([**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346) structure) for the device. This structure is available by calling [**SetupDiGetDeviceInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff551104), passing the saved *DeviceInfoSet* and *DeviceInfoData* that were passed in the area referenced by the **lParam** member of the PROPSHEETPAGE structure.

2.  Ensure that the user's changes are valid.

3.  If the provider allows a user to set a property that requires Windows to remove and restart the device, the provider must set the DI\_FLAGSEX\_PROPCHANGE\_PENDING flag in the **FlagsEx** field of the returned SP\_DEVINSTALL\_PARAMS structure.

    However, if the provider can ensure that the changes do not require the device's drivers to be stopped and then restarted, it does not have to set this flag.

4.  Call [**SetupDiSetDeviceInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff552141) with the changed [**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346) structure to set the new parameters.

### <a href="" id="psn-reset-notifications"></a>PSN\_RESET Notifications

The property sheet sends a PSN\_RESET notification message when the user clicks **Cancel**. In response to this message, the dialog box procedure should discard any changes that were made by the user.

 

 





