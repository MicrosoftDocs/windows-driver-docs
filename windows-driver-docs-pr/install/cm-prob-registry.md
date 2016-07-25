---
title: CM\_PROB\_REGISTRY
description: CM\_PROB\_REGISTRY
ms.assetid: 162586c4-f67f-40e8-bbbb-2b5c574732f4
keywords: ["CM_PROB_REGISTRY"]
---

# CM\_PROB\_REGISTRY


## <a href="" id="ddk-cm-prob-registry-dg"></a>


A registry problem was detected.

### Error Code

19

### Display Message (Windows 2000 and later versions of Windows)

"Windows cannot start this hardware device because its configuration information (in the registry) is incomplete or damaged. (Code 19)"

### Recommended Resolution (Windows 2000 and later versions of Windows)

This error can result if more than one service is defined for a device, there is a failure opening the service key, or the driver name cannot be obtained from the service key.

Try either uninstalling and reinstalling the driver or rolling back the system to the most recent successful configuration of the registry.

To uninstall and reinstall a device driver, follow these steps:

1.  [Open Device Manager](using-device-manager.md).

2.  Right-click the icon that represents the device in the Device Manager window.

3.  On the menu that appears, click **Uninstall** to uninstall the device driver.

4.  Click **Action** on the Device Manager menu bar.

5.  On the **Action** menu, click **Scan for hardware changes** to reinstall the device driver.

To roll a system back to the most recent successful configuration of the registry, restart the computer in Safe Mode and select the Last Known Good Configuration option.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_REGISTRY%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




