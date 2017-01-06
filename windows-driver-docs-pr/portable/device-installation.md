---
Description: Device Installation
MS-HAID: 'wpddk.device\_installation'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Device Installation
---

# Device Installation


WPD drivers are UMDF (Windows Driver Frameworks (WDF)-User-Mode Driver Framework) compliant drivers. Therefore they will use the Windows Plug and Play (PnP) infrastructure for installation.

There are also various ways to create a PnP experience on buses that are not traditionally PnP—for example, using PnP-X for network devices. This enables discovery of the devices over arbitrary buses and lets the PnP component perform the installation as before.

Once the driver for the device is installed on the system, clients will use WPD APIs to enumerate all installed and currently active WPD Devices.

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Device%20Installation%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




