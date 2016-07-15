---
Description: 'Preferred Voice-Communications Device ID'
MS-HAID: 'audio.preferred\_voice\_communications\_device\_id'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Preferred Voice-Communications Device ID'
---

# Preferred Voice-Communications Device ID


## <span id="preferred_voice_communications_device_id"></span><span id="PREFERRED_VOICE_COMMUNICATIONS_DEVICE_ID"></span>


In Windows Me, and Windows 2000 and later, the Windows multimedia functions **waveInMessage** and **waveOutMessage** can retrieve the device ID of the preferred device for voice communications. These two functions get the preferred voice-communication device IDs for wave input and wave output, respectively. Each device ID identifies the wave device that is preferred specifically for voice communications, in contrast to the wave device that is preferred for general wave audio usage. For information about obtaining the device ID of the preferred device for general wave audio, see [Accessing the Preferred Device ID](accessing-the-preferred-device-id.md).

Knowing the preferred voice-communications device can be helpful to application programs that, for example, allow users to select a device to open from a list of two or more devices. Such an application typically needs to indicate which among the devices in the list is the preferred device.

To retrieve the device ID of the current preferred voice-communications device, an application calls the wave *Xxx*Message function with the message parameter set to the constant [**DRVM\_MAPPER\_CONSOLEVOICECOM\_GET**](audio.drvm_mapper_consolevoicecom_get).

When calling the **waveInMessage** or **waveOutMessage** function with the DRVM\_MAPPER\_CONSOLEVOICECOM\_GET message, specify the value of the device handle as WAVE\_MAPPER and cast this value to the appropriate handle type, HWAVEIN or HWAVEOUT. The wave *Xxx*Message functions accept this value in place of a valid device handle so that an application can query for the default device ID without first having to open a device. For more information about the wave *Xxx*Message functions, see [System-Intercepted Device Messages](system-intercepted-device-messages.md).

The DRVM\_MAPPER\_PREFERRED\_GET message is intercepted by the mapper for the target device (waveIn or waveOut). For information about mappers for wave devices, see the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Preferred%20Voice-Communications%20Device%20ID%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


