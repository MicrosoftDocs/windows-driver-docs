---
title: Roadmap for Windows 2000 Display Driver Model (XDDM)
description: Roadmap for Developing Drivers for the Windows 2000 Display Driver Model (XDDM)
ms.assetid: 5f34d0ad-ab31-4361-9a42-83930aef267b
---

# Roadmap for Developing Drivers for the Windows 2000 Display Driver Model (XDDM)


![figure of a roadmap with the text "wdk" superimposed on a highway](images/wdkroadmap-th.png)The Windows 2000 display driver model (XDDM) requires that a graphics hardware vendor supply a paired display driver and video miniport driver. Both of these drivers for display run in kernel mode.

**Note**  XDDM and VGA drivers will not compile on Windows 8 and later versions. If display hardware is attached to a Windows 8 computer without a driver that is certified to support Windows Display Driver Model (WDDM) 1.2 or later, the system defaults to running the Microsoft Basic Display Driver.

 

To create XDDM display drivers on Windows 7 and earlier versions of Windows, download and install the Windows 7 Windows Driver Kit (WDK) (build 7600), open the WDK Help documentation from the **Start** menu, and follow the recommended steps in the topic, [Roadmap for Developing Drivers for the Windows Display Driver Model (WDDM)](roadmap-for-developing-drivers-for-the-windows-vista-display-driver-mo.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Roadmap%20for%20Developing%20Drivers%20for%20the%20Windows%202000%20Display%20Driver%20Model%20%28XDDM%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




