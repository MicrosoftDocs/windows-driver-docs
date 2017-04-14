---
title: Camera Driver UI Extension Sample
author: windows-driver-content
description: Camera Driver UI Extension Sample
ms.assetid: 21ddf804-fff5-4cdc-adb5-f85d769ccc1f
---

# Camera Driver UI Extension Sample


## <a href="" id="ddk-camera-driver-ui-extension-sample-si"></a>


The *extend* directory in the WDK contains a sample user interface extension for WIA digital still camera drivers.

This sample shows how to write WIA user interface (UI) extensions. It adds tabs to the device properties dialog (accessible from Windows Explorer) and adds commands to the context menu for the sample camera device's icon. These extensions are applied to the WIA sample camera from the WDK by providing implementations of the **IShellPropSheetExt** and **IContextMenu** COM interfaces (described in the Microsoft Windows SDK documentation).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Camera%20Driver%20UI%20Extension%20Sample%20%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


