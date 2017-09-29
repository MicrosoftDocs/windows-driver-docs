---
title: Hardware notifications design guide
author: windows-driver-content
description: Describes support for key buttons (Power, Windows, volume and rotation lock) and other indicators in a standardized way, together with associated corresponding Windows Engineering Guidance (WEG).
ms.assetid: E18DAA6C-C64D-40B3-A112-682A935655D0
---

# Hardware notifications design guide


Describes support for key buttons (Power, Windows, volume and rotation lock) and other indicators in a standardized way, together with associated corresponding Windows Engineering Guidance (WEG).

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[GPIO buttons and indicators implementation guide](gpio-buttons-and-indicators-implementation-guide-for-windows-8-1.md)</p></td>
<td align="left"><p>Windows 8 introduced support for general-purpose I/O (GPIO) buttons and indicators by using a HID miniport class driver. The goal was to provide support for key buttons (Power, Windows, volume and rotation lock) in a standardized way, together with associated corresponding Windows Engineering Guidance (WEG). Windows 8.1 is focused on enhancing the quality of the end-to-end user experience and unifying the behavior across various innovative form factors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[GPIO buttons and indicators supplemental testing](gpio-buttons-and-indicators-supplemental-certification-testing-for-windows-8-1.md)</p></td>
<td align="left"><p>This topic describes Windows 8.1 test scenarios for hardware buttons and indicators, to ensure an optimal user experience for various form factors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Hardware notifications support](hardware-notifications-support)</p></td>
<td align="left"><p>Windows 10, version 1709 provides an infrastructure for the hardware-agnostic support of notification components such as LEDs and vibration mechanisms. This support is delivered through the introduction of a Kernel-Mode Driver Framework (KMDF) class extension specifically for hardware notification components that allows for the rapid development of client drivers. A KMDF class extension is essentially a KMDF driver that provides a defined set of functionality for a given class of devices, similar to a port driver in the Windows Driver Model (WDM). This section provides an overview of the architecture of the hardware notification class extension. For additional information about the KMDF, see [Using WDF to Develop a Driver](https://docs.microsoft.com/windows-hardware/drivers/wdf/using-the-framework-to-develop-a-driver).</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics
[Hardware notifications reference](https://msdn.microsoft.com/en-us/library/windows/hardware/dn789336)

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Hardware%20notifications%20design%20guide%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


