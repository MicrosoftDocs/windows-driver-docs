---
title: Child Devices of the Display Adapter
description: Child Devices of the Display Adapter
ms.assetid: 9fd20e1a-db98-4571-8fc4-6d33fd0e2f16
keywords:
- video present networks WDK display , display adapter child devices
- VidPN WDK display , display adapter child devices
- child devices WDK video present network
- display adapter child devices WDK video present network
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Child Devices of the Display Adapter


A child device of the display adapter is a device on the display adapter that is enumerated as a child by the display miniport driver. All child devices of the display adapter are on-board; monitors and other external devices that connect to the display adapter are not considered child devices.

The display miniport driver's [**DxgkDdiQueryChildRelations**](https://msdn.microsoft.com/library/windows/hardware/ff559750) function is responsible for enumerating child devices of the display adapter. During the enumeration, the display miniport driver assigns each child device a type and a hot-plug detection (HPD) awareness value. The type is one of the [**DXGK\_CHILD\_DEVICE\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff561008) enumerators:

-   **TypeVideoOutput**

-   **TypeOther**

The HPD awareness value is one of the [**DXGK\_CHILD\_DEVICE\_HPD\_AWARENESS**](https://msdn.microsoft.com/library/windows/hardware/ff561006) enumerators:

-   **HpdAwarenessAlwaysConnected**

-   **HpdAwarenessInterruptible**

-   **HpdAwarenessPolled**

The following table gives some examples of devices that have various types and HPD awareness values.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">HpdAwareness</th>
<th align="left">VideoOutput</th>
<th align="left">Other</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>AlwaysConnected</strong></p></td>
<td align="left"><p>Output for integrated LCD panel on a desktop computer</p></td>
<td align="left"><p>TV tuner</p>
<p>cross bar switch</p>
<p>MPEG2 codec</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Interruptible</strong></p></td>
<td align="left"><p>DVI</p>
<p>HDMI</p>
<p>Output for integrated LCD panel on a portable computer</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Polled</strong></p></td>
<td align="left"><p>S-video</p>
<p>HD15</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

The operating system uses one of several strategies, depending on the HPD awareness value, to determine whether an external device is connected to a child device. The following table briefly describes how the operating system determines the connection status of devices with various HPD awareness values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">HpdAwareness</th>
<th align="left">How operating system determines connection status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>AlwaysConnected</p></td>
<td align="left"><p>The operating system knows the child device is always present. No external device is ever connected to or disconnected from the child device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Interruptible</p></td>
<td align="left"><p>The operating system is notified when an external display device is connected to or disconnected from the child device. (The display panel on a portable computer is considered connected when the lid is open and disconnected when the lid is closed.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Polled</p></td>
<td align="left"><p>The operating system asks whether an external display device is connected to the child device.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Child%20Devices%20of%20the%20Display%20Adapter%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




