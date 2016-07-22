---
title: CM\_PROB\_PARTIAL\_LOG\_CONF
description: CM\_PROB\_PARTIAL\_LOG\_CONF
ms.assetid: 1e8b10e8-c2c6-4a71-9af5-575206098148
keywords: ["CM_PROB_PARTIAL_LOG_CONF"]
---

# CM\_PROB\_PARTIAL\_LOG\_CONF


## <a href="" id="ddk-cm-prob-partial-log-conf-dg"></a>


The device is only partially configured.

### Error Code

16

### Display Message (Windows 2000 and later versions of Windows)

"Windows cannot identify all the resources this device uses. (Code 16)"

"To specify additional resources for this device, click the Resources tab and fill in the missing settings. Check your hardware documentation to find out what settings to use."

### Recommended Resolution (Windows 2000 and later versions of Windows)

Manually configure the resources that the device requires.

To configure device resources, follow these steps:

1.  [Open Device Manager](using-device-manager.md).

2.  Double-click the icon that represents the device in the Device Manager window.

3.  On the device properties sheet that appears, click the **Resources** tab. The device resources are listed in the **resource settings** list on the **Resources** page.

4.  If a resource in the **resource settings** list has a question mark next to it, select that resource to assign it to the device.

5.  If a resource cannot be changed, click **Change Settings**. If **Change Settings** is unavailable, try to clear the **Use automatic settings** check box to make it available.

If the device is not a Plug and Play device, look in the device documentation for more information about how to configure resources for the device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_PARTIAL_LOG_CONF%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




