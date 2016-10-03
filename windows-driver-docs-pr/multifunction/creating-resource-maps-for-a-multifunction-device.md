---
title: Creating Resource Maps for a Multifunction Device
author: windows-driver-content
description: Creating Resource Maps for a Multifunction Device
MS-HAID:
- 'mf-supp\_412d6527-52b3-4e22-93ff-e84a25d11fce.xml'
- 'multifunc.creating\_resource\_maps\_for\_a\_multifunction\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 332eef11-4056-4fe0-87ed-4305c091bab1
keywords: ["multifunction devices WDK , resource maps", "resource maps WDK multifunction devices", "child function resource maps WDK"]
---

# Creating Resource Maps for a Multifunction Device


## <a href="" id="ddk-creating-resource-maps-for-a-multifunction-device-dg"></a>


A *resource map* identifies the resources of a multifunction device that are used by a child function. Resource maps are specified using an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320). If a multifunction device requires resource maps, the INF for the device typically contains a resource map for each function of the device.

There are two types of resource maps − *standard* resource maps and *varying* resource maps. This section describes how to construct resource maps and includes the following topics:

[Creating Standard Resource Maps](creating-standard-resource-maps.md)

[Creating Varying Resource Maps](creating-varying-resource-maps.md)

Some multifunction devices can be described using only standard resource maps. Others require varying resource maps, or a combination of standard and varying maps. Still others require no resource maps at all. See [Supporting Multifunction PC Card Devices](supporting-multifunction-pc-card-devices.md) to determine which multifunction devices require resource maps.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bmultifunc\multifunc%5D:%20Creating%20Resource%20Maps%20for%20a%20Multifunction%20Device%20%20RELEASE:%20%288/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


