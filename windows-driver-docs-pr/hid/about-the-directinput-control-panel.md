---
title: About the DirectInput Control Panel
author: windows-driver-content
description: About the DirectInput Control Panel
MS-HAID:
- 'di\_1d8d3ee2-c1cf-4f8e-809c-81d1dca41a3a.xml'
- 'hid.about\_the\_directinput\_control\_panel'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d6845778-1203-4b5a-8a7b-7d4eecbcc59e
keywords: ["property sheets WDK DirectInput , about control panel", "game controllers WDK DirectInput , about control panel", "control panels WDK DirectInput , about control panel", "Joy.cpl"]
---

# About the DirectInput Control Panel


## <a href="" id="ddk-about-the-directinput-control-panel-di"></a>


DirectInput provides support for game controllers such as game pads, joysticks, and force-feedback devices. In Microsoft DirectX 5.0 and later versions, DirectInput provides a new game controller control panel called Joy.cpl. This version of Control Panel is the first to allow extensibility in that the property sheets that are displayed for each controller can be replaced with property pages that are specific to that controller. This is done through the creation of a DLL that contains information about these property sheets. This DLL exposes a COM interface that is called into by the DirectInput control panel.

Game controller hardware vendors are encouraged to use this extensibility feature to provide customized property sheets for their game controllers instead of creating a separate control panel. This allows the user to open a single control panel to configure and test their game controllers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20About%20the%20DirectInput%20Control%20Panel%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


