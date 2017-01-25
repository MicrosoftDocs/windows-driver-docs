---
Description: The WpdServiceSampleDriver Sample
MS-HAID: 'wpddk.the\_wpdservicesampledriver\_sample'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: The WpdServiceSampleDriver Sample
---

# The WpdServiceSampleDriver Sample


A device service is an extension of a functional object. In addition to logically grouping device capabilities, a device service provides applications that can programmatically discover those capabilities.

The WpdServiceSampleDriver shows how to extend the WpdHelloWorldDriver sample so that it supports a simulated device with a Contacts device service. By using this device service, an application can discover events, methods, and properties that operate on Contacts that are stored on the device. And, the application can use the Contacts device service to handle these events, invoke these methods, or retrieve these properties. For example, the application might invoke methods to synchronize the Contacts that are found on the device with the contacts that are stored on a computer or to read the Name property for a given Contact.

## <span id="Limitation"></span><span id="limitation"></span><span id="LIMITATION"></span>Limitation


This driver was written in the simplest way to demonstrate concepts. Therefore, the sample driver might perform operations or be structured in a way that are inefficient in a production driver. Additionally, this sample does not use real hardware. Instead, it simulates a device by using data structures in memory. Therefore the driver might be implemented in a way that is unrealistic for production hardware.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20The%20WpdServiceSampleDriver%20Sample%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



