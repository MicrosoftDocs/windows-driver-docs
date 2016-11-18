---
title: Selecting Source Files
author: windows-driver-content
description: Selecting Source Files
MS-HAID:
- 'di\_7bb057d0-47bd-4108-aff7-ac64bb2b60bd.xml'
- 'hid.selecting\_source\_files'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 259a7092-1197-4521-853a-6064aaa0c037
keywords: ["INF files WDK joysticks , source files"]
---

# Selecting Source Files


## <a href="" id="ddk-selecting-source-files-di"></a>


The "SourceDisksFiles" section of the INF file specifies which files to copy. This includes all necessary drivers, as well as any other files, such as documentation and setup applications. As this may be the first joystick driver to be installed on a user's system, the system joystick drivers Vjoyd.vxd and Msjstrick.drv should be copied, in addition to the specific drivers for this device. The source of these two drivers should be established by reference to Layout.inf (causing the user to be prompted for the Windows 95/98/Me installation disc) and not distributed on the OEM disc. The drivers should be copied to the user's system directory, which is destination code 11.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Selecting%20Source%20Files%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


