---
title: Creating a WIA Microdriver
author: windows-driver-content
description: Creating a WIA Microdriver
MS-HAID:
- 'WIA\_db\_hello\_9d3d469a-5d10-47cc-883d-fdd2a2c9a890.xml'
- 'image.creating\_a\_wia\_microdriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4f453569-d768-47fb-9b70-ebb51e303cf0
---

# Creating a WIA Microdriver


## <a href="" id="ddk-creating-a-wia-microdriver-si"></a>


Many flatbed scanners are controlled in a similar manner. The common behavior between models has been abstracted into a Microsoft-provided common driver called the WIA Flatbed Driver. This driver calls a DLL, called a microdriver, provided by the scanner vendor, that implements any needed device-specific behavior. The WIA Flatbed Driver together with the microdriver can then be used as a WIA minidriver. The advantage of using a microdriver is that it is very easy to implement and debug. Not all scanners can be supported by a microdriver. It is most appropriate for simple devices (without a duplexer or other advanced features), or when a base-functionality driver is desired.

**Note**  The WIA microdrivers described in this section are WIA 1.0. Currently there is no corresponding WIA microdriver model for WIA 2.0. If you develop a WIA microdriver to run on a computer that has a Windows version that supports WIA 2.0 (Windows Vista or newer), this WIA microdriver will work like any other WIA 1.0 device, and will be used by WIA 2.0 applications in WIA 1.0 compatibility mode.

 

The following diagram shows the components in the WIA microdriver architecture.

![diagram illustrating the components in the wia microdriver architecture](images/art-6.png)

The WIA Flatbed Driver handles requests from the WIA service by calling the WIA microdriver functions in the microdriver. The microdriver must implement each of these functions. A [**SCANINFO**](https://msdn.microsoft.com/library/windows/hardware/ff547361) structure is passed to the microdriver to store and communicate scanning parameters such as the scan window and resolution. The WIA Flatbed Driver reads values from the SCANINFO structure, but never writes them. It is the microdriver's responsibility to set the SCANINFO members.

The microdriver should not store any parameters for a scan, but should rely on the values stored in the [**SCANINFO**](https://msdn.microsoft.com/library/windows/hardware/ff547361) structure. This is important for supporting multiple application access to the device. If two applications are setting up a scan on the same device at the same time, there is only one copy of the microdriver running. In this situation the microdriver is called with one of two different SCANINFO structures depending on which application is trying to access the device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Creating%20a%20WIA%20Microdriver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


