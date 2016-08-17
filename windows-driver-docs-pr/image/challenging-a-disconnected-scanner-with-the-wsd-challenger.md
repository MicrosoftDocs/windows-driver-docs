---
title: Challenging a Disconnected Scanner with the WSD Challenger
description: Challenging a Disconnected Scanner with the WSD Challenger
MS-HAID:
- 'WIA\_wsd\_scan\_3e0ced98-6bcd-41cb-872d-d202dc45a435.xml'
- 'image.challenging\_a\_disconnected\_scanner\_with\_the\_wsd\_challenger'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f938a235-0360-43f9-9f84-6b9cb6ca9245
---

# Challenging a Disconnected Scanner with the WSD Challenger


A web services scanner driver can challenge a disconnected scanner to reestablish communication with the device when the scanner comes back online. To challenge a disconnected scanner, the driver uses the WSD Challenger DLL (*WSDCHNGR.DLL*) that is provided with Windows Vista. The Windows Image Acquisition (WIA) Service also uses *WSDCHNGR.DLL* to actively monitor all WSDScan scanner devices and enable drivers to respond to a challenge following a device communication failure.

The challenge for a class of devices is initiated by the **WSDCHNGRChallengeDeviceClass** WSD Challenge function. A WIA driver typically does not have to directly call this function because the WIA service calls it for all WIA devices.

Because a WIA driver is unloaded shortly after the device that it supports is disconnected, the driver itself cannot keep *WSDCHNGR.DLL* loaded. The driver, therefore, cannot continue monitoring WSD challenging and cannot reconnect to the device when it comes back online. Instead, WIA drivers that are installed by using the *WSDScan.sys* kernel-mode driver can use the WIA service to challenge the device class and enable the challenging of monitoring to continue after the driver is unloaded.

Typically, a WIA driver that is using *WSDScan.sys* uses only the following WSD Challenger functions:

<a href="" id="wsdchngrinitialize"></a>**WSDCHNGRInitialize**  
Initializes the WSD Challenger interface that the WIA driver client uses. Call this function when the driver is loaded.

<a href="" id="wsdchngrshutdown"></a>**WSDCHNGRShutdown**  
Shuts down the WSD Challenger interface that the WIA driver client uses. Call this function when the driver is unloaded.

**Note**   When this shutdown happens, if the device is a WSDScan-class device, the WIA service continues to run WSD challenge monitoring for the device after the driver has been unloaded and terminated its web services Challenge interface.

 

<a href="" id="wsdchngrregisterdevicetochallenge"></a>**WSDCHNGRRegisterDeviceToChallenge**  
Registers the device to be challenged. Call this function after the driver encounters any potential communication failure. The same device can be registered for a challenge more than once. **WSDCHNGRRegisterDeviceToChallenge** returns S\_OK if the first device is registered successfully. This function returns S\_FALSE when it is called for a device that is already registered to be challenged.

The following code examples show how to use these WSD Challenge functions to initialize the WSD Challenger and how to register the scanner device for challenging after potential communication failures:

[Macro Example to Filter Error Codes](macro-example-to-filter-error-codes.md)

[Code Example for Challenging a Potentially Disconnected Device](code-example-for-challenging-a-potentially-disconnected-device.md)

[Code Example for Implementing Helper Methods](code-example-for-implementing-helper-methods.md)

For more information about the definitions and variables that are used in these examples, see [Definitions and Variables Used in the Examples](definitions-and-variables-used-in-the-examples.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Challenging%20a%20Disconnected%20Scanner%20with%20the%20WSD%20Challenger%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




