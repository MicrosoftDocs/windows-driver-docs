---
title: Device Manager Details Tab
description: Device Manager Details Tab
ms.assetid: 5f1e345f-72c6-4bd4-a0fa-304e5d0d91be
keywords: ["Device Manager WDK , Details tab", "firmware revision numbers WDK Device Manager", "revision numbers WDK Device Manager", "Details tab WDK Device Manager"]
---

# Device Manager Details Tab


## <a href="" id="ddk-device-manager-details-tab-dg"></a>


For Windows XP and later versions of Windows, Device Manager provides a **Details** tab for each device. This tab displays lots of information useful to driver developers and testers, and aids Microsoft Customer Support Services (CSS) in diagnosing customer problems. The tab's page displays [device identification strings](device-identification-strings.md), together with device and driver configuration information that can be useful when you debug drivers.

### <a href="" id="ddk-viewing-a-device-s-details-tab-dg"></a>Viewing a Device's Details Tab

Starting with Windows Server 2003 SP1 and Windows XP SP2, the details tab is enabled by default.

On Windows Server 2003, Windows XP SP1, Windows XP, and Windows 2000, the details tab is disabled by default.

To enable this tab, set the user environment variable DEVMGR\_SHOW\_DETAILS to 1. After you set this environment variable, the **Details** tab of the device will be available in Device Manager. To permanently set a user environment variable, use the **Advanced** tab of the system property sheet. For information about how to set environment variables, see "Setting environment variables" in the Help and Support Center.

### <a href="" id="ddk-providing-firmware-revision-numbers-for-the-details-tab-dg"></a>Providing Firmware Revision Numbers for the Details Tab

Device Manager's **Details** tab can display a device's firmware revision number, if available. A driver can supply a firmware revision number by responding to a WMI request. Specifically, the driver's [**DpWmiQueryDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine should support **MSDeviceUI\_FirmwareRevision\_GUID** by returning a DEVICE\_UI\_FIRMWARE\_REVISION structure (defined in Wmidata.h). The structure must contain the firmware revision number as a NULL-terminated WCHAR string, preceded by a USHORT value that contains the string length (including the **NULL**).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Manager%20Details%20Tab%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




