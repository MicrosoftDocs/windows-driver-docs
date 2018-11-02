---
title: Mirror Drivers
description: Mirror Drivers
ms.assetid: 7231375a-969b-4c55-83d4-96ba5caade20
keywords:
- display drivers WDK Windows 2000 , mirror drivers
- mirror drivers WDK Windows 2000 display
- virtual desktop WDK Windows 2000 display
- global desktop mirroring WDK Windows 2000 display
- GDI virtual desktop WDK Windows 2000 display
- virtual device mirroring WDK Windows 2000 display
- video miniport drivers WDK Windows 2000 , mirror drivers
- assistive technologies and mirror drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mirror Drivers


## <span id="in_this_section"></span>In this section


-   [Remote Display Drivers](remote-display-drivers.md)
-   [Video Port DDI Support](video-port-ddi-support.md)
-   [Mirror Driver INF File](mirror-driver-inf-file.md)
-   [Mirror Driver Installation](mirror-driver-installation.md)

## <span id="Mirror_drivers_in_Windows_8"></span><span id="mirror_drivers_in_windows_8"></span><span id="MIRROR_DRIVERS_IN_WINDOWS_8"></span>Mirror drivers in Windows 8


Starting with Windows 8, mirror drivers will not install on the system. Mirror drivers described in this section will install and run only on earlier versions of Windows.

However, a special GDI accessibility driver model is available starting with Windows 8 to developers who want to provide mirror driver capabilities in [*assistive technologies*](http://go.microsoft.com/fwlink/p/?linkid=248209) for customers with disabilities or impairments. To learn more about this special driver model, please contact <acc_driver@microsoft.com>.

A *remote display driver* model that is based on the mirror driver architecture can also run starting with Windows 8. For more information, see [Remote Display Drivers](remote-display-drivers.md).

## <span id="ddk_mirror_drivers_gg"></span><span id="DDK_MIRROR_DRIVERS_GG"></span>Mirror driver description


A [*mirror driver*](https://msdn.microsoft.com/library/windows/hardware/ff556308#wdkgloss-mirror-driver) is a display driver for a virtual device that mirrors the drawing operations of one or more additional physical display devices. It is implemented and behaves much like any other display driver; however, its paired video miniport driver is minimal in comparison to a typical miniport driver. See [Mirror Driver Support in Video Miniport Drivers (Windows 2000 Model)](mirror-driver-support-in-video-miniport-drivers--windows-2000-model-.md) for more information about miniport drivers in mirroring systems. The Windows Driver Kit (WDK) through the Windows 7 edition (Version 7600) contains a sample mirror driver which includes component source files that are contained in three directories.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Directory</th>
<th align="left">Contains Source Files For</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>\src\video\displays\mirror\disp</p></td>
<td align="left"><p>The mirror driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>\src\video\miniport\mirror\mini</p></td>
<td align="left"><p>The miniport driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>\src\video\displays\mirror\app</p></td>
<td align="left"><p>The user-mode service. Also contains <em>mirror.inf.</em></p></td>
</tr>
</tbody>
</table>

 

GDI supports a *virtual desktop* and provides the ability to replicate a portion of the virtual desktop on a mirror device. GDI implements the virtual desktop as a graphics layer above the physical display driver layer. All drawing operations start in this virtual desktop space; GDI clips and renders them on the appropriate physical display devices that exist in the virtual desktop.

A mirror device can specify an arbitrary [*clip region*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-clip-region) in the virtual desktop, including one that spans more than one physical display device. GDI then sends the mirror device all drawing operations that intersect that driver's clip region. A mirror device can set a clip region that exactly matches a particular physical device; therefore, it can effectively mirror that device.

**Note**   In Windows 2000 and later, the mirror driver's clip region must include the primary display device.

 

**Note**   In Windows Vista and later, the Desktop Windows Manager (DWM) will be turned off when the mirror driver is loaded.

 

The *mirror* driver code sample illustrates how to implement a mirror driver. For more information that will help you understand the sample:

-   Use the sample INF file, *mirror.inf*, as a template. See [Mirror Driver INF File](mirror-driver-inf-file.md) for details.

-   See the *mirror.exe* application, which demonstrates how the mirror driver is attached to the virtual desktop. See [Mirror Driver Installation](mirror-driver-installation.md) for details.

-   Refer to the Windows SDK documentation for information about using the Win32 **EnumDisplayDevices** function. You use this function to determine the **\\\\.\\Display\#** name associated with your mirrored display device. This number is required to change the settings for your mirrored device. For multiple instances, **\#** is a different number for each instance; therefore you must determine this number by iterating through the available display devices.

**To attach the mirrored device to the global desktop**

1.  Add the REG\_DWORD registry entry **Attach.ToDesktop** to your driver's services keys.

2.  Set this key's entry to 1 (one).

To disable the mirror driver, set this entry to 0 (zero).

As mentioned previously, the driver is installed and operates in a drawing layer that resides above the device layer. Because the mirror driver's coordinate space is the desktop coordinate space, it can span more than one device. If the mirror driver is intended to mirror the primary display, its display coordinates should coincide with the primary display's desktop coordinates.

-   After the mirror driver is installed, it will be called for all rendering operations that intersect the driver's display region. On a [multiple-monitor system](multiple-monitor-support-in-the-display-driver.md), this might not include all drawing operations if the mirror driver overlaps only the primary display device.

-   It is recommended that a user-mode service be used to maintain the mirror driver's settings. This application can ensure that the driver is loaded correctly at boot time and it can respond appropriately to changes to the desktop by getting notifications of display changes via the WM\_DISPLAYCHANGE message.

-   GDI calls the mirror driver for any 2D graphics DDI drawing operation that intersects the driver's bounding rectangle. Note that GDI does not perform a bounding rectangle check if the surface is a device format bitmap; that is, if the [**SURFOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff569901) has an **iType** of STYPE\_DEVBITMAP.

-   As always, the mirror driver must be implemented without the use of global variables. All state must exist in the [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) for that particular driver. GDI will call [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) for every hardware device extension created by the video miniport driver.

-   The mirror driver should not support DirectDraw.

-   A mirror driver must set the GCAPS\_LAYERED flag to **TRUE** in the **flGraphicsCaps** member of the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure.

-   An accessibility mirror driver must set the GCAPS2\_EXCLUDELAYERED and GCAPS2\_INCLUDEAPIBITMAPS flags to **TRUE** in the **flGraphicsCaps2** member of the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure.

-   A mirror driver can optionally support brush realizations by implementing [**DrvRealizeBrush**](https://msdn.microsoft.com/library/windows/hardware/ff556273).

GDI allows the same driver to run on both a single and multiple-monitor system. A driver in a multiple-monitor system need only track its position within the global desktop. GDI provides this position to the driver whenever a Win32 **ChangeDisplaySettings** call occurs, such as when a user dynamically changes the monitor's position in the desktop by using the Display program in Control Panel. GDI updates the **dmPosition** member of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure accordingly when such a change occurs. A driver can receive notification of such a change by implementing [**DrvNotify**](https://msdn.microsoft.com/library/windows/hardware/ff556252). See [Mirror Driver Installation](mirror-driver-installation.md) for more information.

**Note**   Mirror drivers are not required to render with pixel-perfect accuracy when rendering on the client side with such accuracy may be difficult. For example, the adapter/monitor receiving the mirrored image is not required to render [Grid Intersect Quantization](cosmetic-lines.md) (GIQ) line drawing and polygon fills with the same precision as the adapter/monitor being mirrored.

 

 

 





