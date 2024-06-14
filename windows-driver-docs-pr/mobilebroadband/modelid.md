---
title: ModelID
description: ModelID
ms.date: 04/20/2017
---

# ModelID

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

The ModelID element specifies the GUID of a physical device.

**Caution**  
The [ModelIDList](modelidlist.md) and ModelID elements are not supported for service metadata packages. You must use the [HardwareIDList](hardwareidlist.md) and [HardwareID](hardwareid.md) elements instead.

 

## Usage


``` syntax
<ModelID>
  text
</ModelID>
```

## Attributes


There are no attributes.

## Text value


A value formatted as a [GUIDType](guidtype-packageinfo.md) XML simple type.

## Child elements


There are no child elements.

## Parent elements


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

 

## XSD


## Remarks


The ModelID element specifies a model ID for a hardware model supported by a device. Each model ID is specified through a GUID.

**Caution**  
The [ModelIDList](modelidlist.md) and ModelID elements are not supported for service metadata packages. You must use the [HardwareIDList](hardwareidlist.md) and [HardwareID](hardwareid.md) elements instead.

 

Model IDs are based on the business definition or SKU of the physical device. Each model ID must be unique for all makes and models of the physical device.

The following list describes the differences between hardware and model IDs for a physical device:

-   Hardware IDs, specified through the [HardwareID](hardwareid.md) element, identify a hardware function based on a bus-specific value. Hardware IDs could map device drivers to device instances. For example, two devices with the same hardware ID share a functional interface that is used by the same driver.

-   Model IDs, specified through the ModelID element, enable the OEM or independent hardware vendor (IHV) to uniquely identify the physical device independent of bus or interface technologies. For example, two devices with different model IDs may have the same hardware IDs for their components.

-   Hardware IDs map device metadata packages to device instances on a specific bus or interface.

-   Model IDs map device metadata packages to physical devices, regardless of how the device is connected to the computer.

 

 





