---
Description: Multifunction Device Limits
MS-HAID: 'audio.multifunction\_device\_limits'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Multifunction Device Limits
---

# Multifunction Device Limits


## <span id="multifunction_device_limits"></span><span id="MULTIFUNCTION_DEVICE_LIMITS"></span>


The number of audio functions per multifunction device is limited by the following factors:

-   When the adapter driver calls [**PcAddAdapterDevice**](audio.pcaddadapterdevice), the function's fourth parameter, *MaxObjects*, specifies the maximum number of miniport driver objects that the driver can support. The sample adapter drivers in the Microsoft Windows Driver Kit (WDK) set this parameter to the integer constant MAX\_MINIPORTS, which is typically defined to be a small value (five or less). You might need to increase this value if you plan to support multiple stereo pairs or other types of audio subdevices.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Multifunction%20Device%20Limits%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



