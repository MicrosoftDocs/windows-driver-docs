---
title: Device-specific methods (\_DSM)
author: windows-driver-content
description: To support increased functionality and extension to select technology stacks, Windows define Device-Specific Methods (\_DSM) for the device.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: E49BE897-28A5-42FE-875C-A8EB56EABF8B
---

# Device-specific methods (\_DSM)


To support increased functionality and extension to select technology stacks, Windows define Device-Specific Methods (\_DSM) for the device.

The [ACPI 5.0 specification](http://www.acpi.info) introduces several device-specific methods that are used by Windows to support hardware platforms that use System on a Chip (SoC) integrated circuits. The topics in this section describe the arguments and return values that are defined for these methods.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[GPIO controller Device-Specific Method (_DSM)](gpio-controller-device-specific-method---dsm-.md)</p></td>
<td><p>To support a variety of device-class-specific communications between the general-purpose I/O (GPIO) driver stack in Windows and the platform firmware, Microsoft defines a Device-Specific Method (_DSM) that can be included under a GPIO controller in the ACPI namespace.</p></td>
</tr>
<tr class="even">
<td><p>[Battery Device-Specific Method](battery-device-specific-method.md)</p></td>
<td><p>To support the passive thermal management of the battery by the platform, Microsoft defines a _DSM method to communicate to the platform firmware the thermal throttling limit set by the battery's thermal zone.</p></td>
</tr>
<tr class="odd">
<td><p>[Device-Specific Method for Microsoft thermal extensions](device-specific-method-for-microsoft-thermal-extensions.md)</p></td>
<td><p>To support more flexible design of thermal zones and thermal sensors, Windows supports extensions to the ACPI thermal zone model. Specifically, Windows supports a thermal minimum throttle limit (MTL) for each thermal zone, and also supports sharing a temperature sensor between thermal zones.</p></td>
</tr>
<tr class="even">
<td><p>[USB Device-Specific Method (_DSM)](usb-device-specific-method---dsm-.md)</p></td>
<td><p>To support device-class-specific configuration of the USB subsystem, Windows defines a Device-Specific Method (_DSM) that has the functions that are described in this article.</p></td>
</tr>
<tr class="odd">
<td><p>[HIDI2C Device-Specific Method (_DSM)](hidi2c-device-specific-method---dsm-.md)</p></td>
<td><p>The _DSM method is defined in section 9.14.1, &quot;_DSM (Device Specific Method)&quot;, in the [ACPI 5.0 specification](http://www.acpi.info). This method provides for individual, device-specific data and control functions that can be called by a device driver without conflicting with other such device-specific methods.</p></td>
</tr>
<tr class="even">
<td><p>[Windows button array Device-Specific Method (_DSM)](windows-button-array-device-specific-method---dsm-.md)</p></td>
<td><p>To support evolution of the Windows Button user interface (UI), Windows defines a Device-Specific Method (_DSM) for the Windows button array device with the function that is described in this article.</p></td>
</tr>
</tbody>
</table>

 

## <a href="" id="other--dsms-defined-for-windows"></a>Other \_DSMs defined for Windows


To support device-class-specific communications between the driver stack in Windows and the platform firmware, Microsoft defines Device-Specific Methods (\_DSM) to be used with drivers.

|                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Topic                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](https://msdn.microsoft.com/library/windows/hardware/mt604741) | The \_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1) is designed to map to the JEDEC Byte Addressable Energy Backed Interface standard in order to minimize BIOS complexity. It provides a common basis of reporting device functions & capabilities, such that OS software can interact with various implementations through the same mechanisms. Further, it allows support for vendor-specific functionality through access to I2C registers. |
| [\_DSM (Device Specific Method) for SATA](https://msdn.microsoft.com/library/windows/hardware/dn613874)                                                                               | This method enables management of each port of a SATA controller separate from the host controller as a whole.                                                                                                                                                                                                                                                                                                                                                                           |

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Device-specific%20methods%20%28_DSM%29%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


