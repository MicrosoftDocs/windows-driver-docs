---
title: Property Page Callback Function
description: Property Page Callback Function
ms.assetid: 3f4d7247-2a12-4889-9fc0-a28f58046c7b
keywords: ["device property pages WDK device installations , callback functions", "property pages WDK device installations , callback functions", "custom property pages WDK device installations , callback functions", "callback functions WDK property page", "PSPCB_CREATE", "PSPCB_RELEASE"]
---

# Property Page Callback Function


## <a href="" id="ddk-property-page-callback-function-dg"></a>


When a provider creates a property page for its device or device class, it supplies a pointer to a callback function. The callback function is called one time when the property page is created and again when it is about to be destroyed.

The callback is a **PropSheetPageProc** function that is described in the Windows SDK documentation. This function must be able to handle the PSPCB\_CREATE and PSPCB\_RELEASE actions.

The callback is called with a PSPCB\_CREATE message when a property page is being created. In response to this message, the callback can allocate memory for data that is associated with the page. The function should return **TRUE** to continue to create the page or **FALSE** if the page should not be created.

Property pages for a device are destroyed when the user clicks **OK** or **Cancel** on the page's dialog box or clicks **Uninstall** on the **Drivers** tab.

When a property page is destroyed, the callback is called with a PSPCB\_RELEASE message. The function should free any data that was allocated when the property page was created. Typically, this involves freeing the data referenced by the **lParam** member of the PROPSHEETPAGE structure. The return value is ignored when the page is being destroyed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Property%20Page%20Callback%20Function%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




