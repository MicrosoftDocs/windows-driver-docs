---
Description: The WPD Driver Samples
MS-HAID: 'wpddk.the\_wpd\_driver\_samples'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: The WPD Driver Samples
---

# The WPD Driver Samples


The Windows Portable Devices Driver Kit includes five sample WPD drivers. These drivers are briefly described in the following table. A more detailed description of these drivers appears later in the documentation.

**Note**  If you are not familiar with the WPD driver model, begin with the WpdHelloWorldDriver.

 

| Sample                                                            | Description                                                                                                                                                                                    |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [WpdHelloWorldDriver](the-sample-driver-architecture.md)         | A basic sample driver that supports a single device object and multiple read-only properties. This driver simulates hardware interaction.                                                      |
| [WpdBasicHardwareDriver](the-wpdbasichardwaredriver-sample.md)   | A sample driver that interacts with simple sensors. This driver allows WPD applications to receive sensor data and to set the interval at which that data arrives.                             |
| [WpdMultiTransportDriver](the-wpdmultitransportdriver-sample.md) | A sample driver that demonstrates the creation of a single access point for devices that support multiple transports. This driver simulates hardware interaction.                              |
| [WpdWudfSampleDriver](the-wpdwudfsampledriver-sample.md)         | A comprehensive sample driver that demonstrates the WPD device driver interface (DDI). This sample driver simulates hardware interaction.                                                      |
| [WpdServiceSampleDriver](the-wpdservicesampledriver-sample.md)   | A sample driver that demonstrates support for a Contacts service. (Services are an extension of the functional objects that are supported by WPD.) This driver simulates hardware interaction. |

 

## <span id="related_topics"></span>Related topics


[WPD HelloWorld Driver download page](http://go.microsoft.com/fwlink/p/?linkid=257508)

[WPD Basic Hardware Driver download page](http://go.microsoft.com/fwlink/p/?linkid=256221)

[WPD Multi-Transport Driver download page](http://go.microsoft.com/fwlink/p/?linkid=256222)

[WPD Service Sample Driver download page](http://go.microsoft.com/fwlink/p/?linkid=256223)

[WPD WUDF Sample Driver download page](http://go.microsoft.com/fwlink/p/?linkid=256224)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20The%20WPD%20Driver%20Samples%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




