---
Description: WPD Driver Development Tools
title: WPD Driver Development Tools
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





