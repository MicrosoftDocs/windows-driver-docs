---
Description: Obtaining a Device Interface Name
MS-HAID: 'audio.obtaining\_a\_device\_interface\_name'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Obtaining a Device Interface Name
---

# Obtaining a Device Interface Name


## <span id="obtaining_a_device_interface_name"></span><span id="OBTAINING_A_DEVICE_INTERFACE_NAME"></span>


In Windows Me, and Windows 2000 and later, the Windows multimedia functions **waveInMessage**, **waveOutMessage**, **midiInMessage**, **midiOutMessage**, and **mixerMessage** can retrieve the device interface name of a device. This information is useful to application programs that need to identify the device outside of the waveIn, waveOut, midiIn, midiOut, or mixer API. Within one of these APIs, a device ID is sufficient.

The Plug and Play manager generates a device interface name to uniquely identify each device that it enumerates. An application should treat the string containing a device interface name as opaque. For more information about device interfaces, see [Introduction to Device Interfaces](devinst.overview_of_device_interface_classes).

The header file Mmddk.h defines two message constants for the purpose of obtaining device interface names:

[**DRV\_QUERYDEVICEINTERFACESIZE**](audio.drv_querydeviceinterfacesize)

[**DRV\_QUERYDEVICEINTERFACE**](audio.drv_querydeviceinterface)

The first message obtains the size in bytes of the buffer needed to hold the string containing the device interface name. The second message retrieves the name string in a buffer of the required size.

The system intercepts and handles the DRV\_QUERYDEVICEINTERFACESIZE and DRV\_QUERYDEVICEINTERFACE messages without sending the messages to the device driver.

The first parameter to the *xxx*Message function is the device ID, which the caller must cast to the appropriate handle type: HWAVEIN, HWAVEOUT, HMIDIIN, HMIDIOUT, or HMIXER. For more information about the *xxx*Message functions, see [System-Intercepted Device Messages](system-intercepted-device-messages.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Obtaining%20a%20Device%20Interface%20Name%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



