---
Description: The COM Component Files
MS-HAID: 'wpddk.the\_com\_component\_files'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: The COM Component Files
---

# The COM Component Files


The WpdHelloWorldDriver project contains the following COM component files.

| Filename                | Description                                                                                                                                               |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| resource.h              | Contains a single definition for the driver's identifier.                                                                                                 |
| stdafx.h                | Includes standard system files.                                                                                                                           |
| WpdHelloWorldDriver.cpp | Contains the basic COM methods that handle server registration, returning a class factory, and the DLL entry point.                                       |
| WpdHelloWorldDriver.def | Declares the module parameters.                                                                                                                           |
| WpdHelloWorldDriver.idl | Contains the necessary definitions for the driver's COM component.                                                                                        |
| WpdHelloWorldDriver.rc  | Contains definitions for resources required by the driver. These resources include the file type, the file description string, and the original filename. |
| WpdHelloWorldDriver.rgs | Contains the registration script for the driver's COM component.                                                                                          |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20The%20COM%20Component%20Files%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



