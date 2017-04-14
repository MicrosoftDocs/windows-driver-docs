---
title: Creating Standard Resource Maps
author: windows-driver-content
description: Creating Standard Resource Maps
ms.assetid: 97d95481-5290-41d3-a6e6-7cc142d4c2e8
keywords: ["standard resource maps WDK multifunction devices"]
---

# Creating Standard Resource Maps


## <a href="" id="ddk-creating-standard-resource-maps-dg"></a>


If a multifunction device's INF contains an [**INF DDInstall.LogConfigOverride section**](https://msdn.microsoft.com/library/windows/hardware/ff547339), the parent resources are implicitly numbered 00 through *nn* as they appear in the INF's *log-config-section* sections (see [**INF LogConfig Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547448)). For example, consider a multifunction PC Card with the following INF *DDInstall*.**LogConfigOverride** section:

```
[DDInstall.LogConfigOverride]
LogConfig = DDInstall.Override0
 
[DDInstall.Override0]    ;com2
IOConfig=2f8-2ff                      ; resource 00
IOConfig=20@100-FFFF%FFE0             ; resource 01
IRQConfig=3,4,5,7,9,10,11             ; resource 02
MemConfig=4000@0-FFFFFFFF%FFFFC000    ; resource 03
PcCardConfig=41:100000(W)             ; resource 04
```

The device in this example has five resources, which are numbered 00 through 04. If there is more than one *DDInstall*.**LogConfigOverride** section, the resources must be listed in the same order in each section.

If one child function (Child0000) requires the first and third resources listed above, the resource map for this child would be: 00,02. If another child function (Child00001) requires all five resources, then its resource map would be: 00,01,02,03,04. In this example, resources 00 (**IoConfig=2f8-2ff**) and 02 (**IRQConfig=3,4,5,7,9,10,11**) are shared. These resource maps would be specified in the INF as follows:

```
[DDInstall.RegHW]
    ; for each "child" function list hardware ID and resource map
HKR,Child0000,HardwareID,,child0000-hardware-ID
HKR,Child0000,ResourceMap,1,00,02                 ; map for Child0000
HKR,Child0001,HardwareID,,child0001-hardware-ID
HKR,Child0001,ResourceMap,1,00,01,02,03,04        ; map for Child0001
```

The "1" following the **ResourceMap** parameter specifies that the registry entry is a REG\_BINARY data type. The numbers following the "1" are the resource map values.

If there are no *DDInstall*.**LogConfigOverride** sections in the INF, the parent resources are numbered in the order that the resource requirements are constructed by the driver for the underlying bus. For PC Cards, the bus driver reports resources in this order: IRQ, I/O ports, memory addresses. For multiple I/O and memory requirements, they are numbered in the same order as the tuples on the card. Other bus drivers might list resources in other orders.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bmultifunc\multifunc%5D:%20Creating%20Standard%20Resource%20Maps%20%20RELEASE:%20%288/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


