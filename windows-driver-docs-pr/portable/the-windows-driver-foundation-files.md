---
Description: The Windows Driver Frameworks Files
MS-HAID: 'wpddk.the\_windows\_driver\_foundation\_files'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: The Windows Driver Frameworks Files
---

# The Windows Driver Frameworks Files


The WpdHelloWorldDriver project contains the following Windows user-mode driver framework (UMDF) files.

| Filename   | Description                                                                                                                                                                   |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device.cpp | Contains an implementation of the CDevice member functions. These functions handle Plug and Play and Power-Management events.                                                 |
| Device.h   | Contains a definition for the CDevice class.                                                                                                                                  |
| Driver.cpp | Contains an implementation of the CDriver member functions. These functions handle device initialization and cleanup.                                                         |
| Driver.h   | Contains a definition for the CDriver class.                                                                                                                                  |
| Queue.cpp  | Contains an implementation of the CQueue member functions.                                                                                                                    |
| Queue.h    | Contains a definition for the CQueue class as well as definitions for the Windows Driver Foundation (WDF) callbacks. These functions handle device control and file creation. |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20The%20Windows%20Driver%20Frameworks%20Files%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



