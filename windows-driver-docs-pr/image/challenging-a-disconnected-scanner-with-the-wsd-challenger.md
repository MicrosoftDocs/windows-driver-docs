---
title: Challenging a Disconnected Scanner with the WSD Challenger
description: Challenging a Disconnected Scanner with the WSD Challenger
ms.assetid: f938a235-0360-43f9-9f84-6b9cb6ca9245
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Challenging a Disconnected Scanner with the WSD Challenger

> [!IMPORTANT] 
> WSD Challenger functionality has been deprecated and all WSD Challenger-related documentation will be removed in 2018.

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

 

 




