---
Description: WPD Driver Development Tools
MS-HAID: 'wpddk.familiarizing\_yourself\_with\_the\_sample\_driver'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: WPD Driver Development Tools
---

# WPD Driver Development Tools


Windows Portable Devices (WPD) supplies three tools with the Windows Driver Kit, which you can use to develop a WPD device driver. These tools are described in the following table.

| Tool                     | Description                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *WpdDeviceInspector.exe* | This tool is designed to query a WPD driver and generate a comprehensive HTML report that describes your device and its capabilities. For example, you can use the tool to retrieve a list of supported device commands and objects. It will also generate a list of all properties that are supported by each object.                                                   |
| *WpdInfo.exe*            | This tool performs common WPD operations such as opening and closing a device, creating or deleting objects on a device, and issuing device commands. This tool can also show supported properties, commands, content types, events, and formats at the device level, service level, or both. In addition, it can show the properties for each object on a given device. |
| *NetMon.exe*             | This tool logs the traffic between a WPD application and a WPD driver.                                                                                                                                                                                                                                                                                                   |

 

In addition to the tools that are supplied with the Windows Driver Kit, you might also want to install the Windows SDK and use two WPD sample applications found in this kit to explore and test WPD drivers. These sample applications are described in the following table.

| Application                | Description                                                                                                                                                                                    |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *WpdApiSample.exe*         | You can use this application to perform common WPD operations on a WPD device, such as enumerating devices, listing content on a device, and transferring content to or from the device.       |
| *WpdServicesApiSample.exe* | You can use this application to perform WPD operations on a WPD device that implements a Contacts device service. (Be aware that this application only works with the WpdServiceSampleDriver.) |

 

## <span id="related_topics"></span>Related topics


****
[Using the WpdInfo Tool](using-the-wpdinfo-tool.md)

[Using the WpdDeviceInspector Tool](using-the-wpddeviceinspector-tool.md)

[Using the NetMon Tool](using-the-netmon-tool.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20WPD%20Driver%20Development%20Tools%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




