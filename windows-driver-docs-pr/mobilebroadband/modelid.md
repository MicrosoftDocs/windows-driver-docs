---
title: ModelID
description: ModelID
ms.assetid: 6873f5b6-453e-4f8e-b534-0bc805865905
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ModelID


The ModelID element specifies the GUID of a physical device.

**Caution**  
The [ModelIDList](modelidlist.md) and ModelID elements are not supported for service metadata packages. You must use the [HardwareIDList](hardwareidlist.md) and [HardwareID](hardwareid.md) elements instead.

 

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


``` syntax
<ModelID>
  text
</ModelID>
```

## <span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes


There are no attributes.

## <span id="Text_value"></span><span id="text_value"></span><span id="TEXT_VALUE"></span>Text value


A value formatted as a [GUIDType](guidtype-packageinfo.md) XML simple type.

## <span id="Child_elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child elements


There are no child elements.

## <span id="Parent_elements"></span><span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent elements


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[ModelIDList](modelidlist.md)</p></td>
<td><p>The [ModelIDList](modelidlist.md) element specifies the GUID of each hardware model supported by the device specified within the device metadata package.</p></td>
</tr>
</tbody>
</table>

 

## <span id="XSD"></span><span id="xsd"></span>XSD


## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The ModelID element specifies a model ID for a hardware model supported by a device. Each model ID is specified through a GUID.

**Caution**  
The [ModelIDList](modelidlist.md) and ModelID elements are not supported for service metadata packages. You must use the [HardwareIDList](hardwareidlist.md) and [HardwareID](hardwareid.md) elements instead.

 

Model IDs are based on the business definition or SKU of the physical device. Each model ID must be unique for all makes and models of the physical device.

The following list describes the differences between hardware and model IDs for a physical device:

-   Hardware IDs, specified through the [HardwareID](hardwareid.md) element, identify a hardware function based on a bus-specific value. Hardware IDs could map device drivers to device instances. For example, two devices with the same hardware ID share a functional interface that is used by the same driver.

-   Model IDs, specified through the ModelID element, enable the OEM or independent hardware vendor (IHV) to uniquely identify the physical device independent of bus or interface technologies. For example, two devices with different model IDs may have the same hardware IDs for their components.

-   Hardware IDs map device metadata packages to device instances on a specific bus or interface.

-   Model IDs map device metadata packages to physical devices, regardless of how the device is connected to the computer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20ModelID%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




