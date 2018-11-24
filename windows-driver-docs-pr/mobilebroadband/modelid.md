---
title: ModelID
description: ModelID
ms.assetid: 6873f5b6-453e-4f8e-b534-0bc805865905
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ModelID

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

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
<td><p><a href="modelidlist.md" data-raw-source="[ModelIDList](modelidlist.md)">ModelIDList</a></p></td>
<td><p>The <a href="modelidlist.md" data-raw-source="[ModelIDList](modelidlist.md)">ModelIDList</a> element specifies the GUID of each hardware model supported by the device specified within the device metadata package.</p></td>
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

 

 





