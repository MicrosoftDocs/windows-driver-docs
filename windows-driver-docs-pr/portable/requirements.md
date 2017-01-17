---
Description: Requirements
MS-HAID: 'wpddk.requirements'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Requirements
---

# Requirements


To create a Windows Portable Devices (WPD) driver, you must have the latest [Windows Driver Kit (WDK)](http://go.microsoft.com/fwlink/p/?linkid=178709) installed on your computer. The required header and library files are shown in the following list and are included in the WDK:

-   *PortableDeviceGuids.lib*
-   *PortableDeviceClassExtension.h*
-   *PortableDeviceTypes.h*
-   *PortableDevice.h*
-   Any other required library or header files that are required by the User-Mode Driver Framework (UMDF).

If your driver supports the new Device Services model, it will also include one or more of the following header files:

-   *AnchorSyncDeviceService.h*
-   *BridgeDeviceService.h*
-   *CalendarDeviceService.h*
-   *ContactDeviceService.h*
-   *DeviceServices.h*
-   *FullEnumSyncDeviceService.h*
-   *HintsDeviceService.h*
-   *MessageDeviceService.h*
-   *MetadataDeviceService.h*
-   *NotesDeviceService.h*
-   *RingtoneDeviceService.h*
-   *StatusDeviceService.h*
-   *SyncDeviceService.h*
-   *TaskDeviceService.h*

Of these files, *BridgeDeviceService.h* and *DeviceService.h* are required for all service applications. Other applications must include one or more of these other files to support a particular device.

## <span id="related_topics"></span>Related topics


[**WPD Drivers**](wpd-drivers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Requirements%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




