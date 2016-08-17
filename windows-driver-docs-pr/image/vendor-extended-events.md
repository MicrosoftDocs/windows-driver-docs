---
title: Vendor-Extended Events
description: Vendor-Extended Events
MS-HAID:
- 'WIA\_drv\_cam\_563bb5a2-6e90-4c8a-851f-2d9038ae420b.xml'
- 'image.vendor\_extended\_events'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 00131b75-3b15-46f8-b4da-1e1593afb3c0
---

# Vendor-Extended Events


## <a href="" id="ddk-vendor-extended-events-si"></a>


Vendor-extended events are defined in the **DeviceData** and **Events** INF file sections (see the example in [Vendor-Extended Features](vendor-extended-features.md)). An **EventCode** entry lists all the event codes, separated by commas. For each event code, an entry of the form **EventCode***XXXX* should exist, where XXXX is the PTP event code in uppercase hexadecimal. The entry should list the WIA GUID code to send when the event code is received by the driver.

Display names of events should be declared in the **Events** section. For each event, there must be an **EventCode***XXXX* entry, containing the event name in quotes, the event GUID, and the application to be launched when the event occurs, all separated by commas. If an asterisk is used in place of the application name, the registered application name is used. See [INF Files for WIA Devices](inf-files-for-wia-devices.md) for more information. An application can use the **IWiaDevMgr::RegisterEventCallback***Xxx* methods (described in the Microsoft Windows SDK documentation) to receive the events. Currently, the parameters from the event cannot be passed to the application.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Vendor-Extended%20Events%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




