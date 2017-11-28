---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE
description: The focus mode property controls the auto, manual, and preset focus modes of the camera.
ms.assetid: FA014A4B-0CD3-4288-B721-4A73CDD28551
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE


The focus mode property controls the auto, manual, and preset focus modes of the camera.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567563)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) structure and a [**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING**](https://msdn.microsoft.com/library/windows/hardware/dn567566) structure.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) is set to this total property data size.

The **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) contains a bitwise OR combination of one or more of the following video processing options.

| Processing and focus mode                        | Description                                                                  |
|--------------------------------------------------|------------------------------------------------------------------------------|
| KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO      | Camera driver uses its own processing logic for video.                       |
| KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL    | Camera driver uses a preset processing method or a temperature based method. |
| KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_LOCK      | The current video processing method is locked.                               |
| KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS        | No converging focal point set.                                               |
| KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_MACRO      | Macro range focal convergence.                                               |
| KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_NORMAL     | Normal range focal convergence.                                              |
| KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_FULLRANGE  | Full range focal convergence.                                                |
| KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_INFINITY   | Infinite range focal convergence.                                            |
| KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_HYPERFOCAL | Hyperfocal range.                                                            |

 

The **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) contains the video processing flag currently set for the camera. If KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO setting may be combined with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_LOCK.

This property control is asynchronous.

Remarks
-------

### <span id="Processing_modes"></span><span id="processing_modes"></span><span id="PROCESSING_MODES"></span>Processing modes

<span id="KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_AUTO"></span><span id="kscamera_extendedprop_videoprocflag_auto"></span>KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO  
This flag indicates that the auto focus operation has converged when the completion event is triggered. Upon completion, and when this flag is not a combined with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_LOCK, the focus may diverge and the camera driver may continue to attempt convergence. If the KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_LOCK flag is included, the focus is locked to the first convergence and does not change until a new focus command is received.

Locking, without combining Auto mode, an already locked control should be treated as a no-op by the camera driver. Locking, in combination with Auto mode, an already locked control should trigger a new convergence.

This flag is mutually exclusive with the KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL and KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS flags.

<span id="KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_MANUAL"></span><span id="kscamera_extendedprop_videoprocflag_manual"></span>KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL  
Manual indicates that for this video processing, the specific values are provided. Specific values are provided to the driver.

This flag must not be combined with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO, KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_LOCK, or KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS.

<span id="KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_LOCK"></span><span id="kscamera_extendedprop_videoprocflag_lock"></span>KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_LOCK  
When this flag is set without a corresponding KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO flag, the camera driver is expected to lock the current focus state and trigger the completion event once the focus is locked. Camera driver must not vary the focus state until a new focus command is received. If KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO combined this flag, the camera driver will converge on auto-focus and lock the focus to that converged point and then trigger the completion event. This flag is must not be combined with KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS or KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL.

This flag may not be specified with a range flag for the focus control unless it is combined with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO. In that case, the focus is performed using the range flag to determine where to attempt the auto-focus scan. Then, upon convergence, the focus setting locks and the completion event fires.

<span id="KSCAMERA_EXTENDEDPROP_FOCUS_CONTINUOUS"></span><span id="kscamera_extendedprop_focus_continuous"></span>KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS  
This flag indicates that the focus is continuous. There is no single convergence point for focus control in this case. The driver must accept this request and complete the asynchronous operation immediately.

This flag must not be combined with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO, KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_LOCK, or KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL.

This mode is required for all drivers.

<span id="KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_MACRO"></span><span id="kscamera_extendedprop_focus_range_macro"></span>KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_MACRO  
This flag indicates that focus convergence should be performed for the macro range. The exact focal range is determined by the driver. This flag may be combined with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO and KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS.

<span id="KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_NORMAL"></span><span id="kscamera_extendedprop_focus_range_normal"></span>KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_NORMAL  
This flag indicates that focus convergence should be performed for the normal range. The exact focal range is determined by the driver. This flag may be combined with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO and KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS.

<span id="KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_FULLRANGE"></span><span id="kscamera_extendedprop_focus_range_fullrange"></span>KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_FULLRANGE  
This flag indicates that focus convergence should be performed for the full range. The exact focal range is determined by the driver. This flag may be combined with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO and KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS.

This mode is required for all drivers.

<span id="KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_INFINITY"></span><span id="kscamera_extendedprop_focus_range_infinity"></span>KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_INFINITY  
This flag indicates that focus convergence should be performed for the infinite range. The exact focal range is determined by the driver. This flag may be combined with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO and KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS.

<span id="KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_HYPERFOCAL"></span><span id="kscamera_extendedprop_focus_range_hyperfocal"></span>KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_HYPERFOCAL  
This flag indicates that focus convergence should be performed for the hyperfocal range. The exact focal range is determined by the driver. This flag may be combined with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO and KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS.

### <span id="Getting_the_property"></span><span id="getting_the_property"></span><span id="GETTING_THE_PROPERTY"></span>Getting the property

When responding to a KSPROPERTY\_TYPE\_GET request, the driver sets the members of the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) to the following.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Version</td>
<td>1</td>
</tr>
<tr class="even">
<td>PinId</td>
<td>KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF).</td>
</tr>
<tr class="odd">
<td>Size</td>
<td><p>sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING)</p></td>
</tr>
<tr class="even">
<td>Result</td>
<td>0</td>
</tr>
<tr class="odd">
<td>Capability</td>
<td><p>KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL | KSCAMERA_EXTENDEDPROP_CAPS_CANCELLABLE |</p>
<p>(Video processing and focus modes supported)</p></td>
</tr>
<tr class="even">
<td>Flags</td>
<td>The current video processing and focus mode.</td>
</tr>
</tbody>
</table>

 

If no focus range flag previously set, then the driver sets **Flags** to KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_FULLRANGE along with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO (default). The members of the [**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING**](https://msdn.microsoft.com/library/windows/hardware/dn567566) structure that follows [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) are set according to the requirements of the focus mode.

Alt**Capability**

The **VideoProp.Value.ull** value must contain the current exposure setting when the mode is KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO.

### <span id="Setting_the_property"></span><span id="setting_the_property"></span><span id="SETTING_THE_PROPERTY"></span>Setting the property

When the property is set, a KSPROPERTY\_TYPE\_SET request, the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) will contain the focus mode to set. The **VideoProc.Value** member of [**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING**](https://msdn.microsoft.com/library/windows/hardware/dn567566) must be ignored when **Flags** contains the KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO, KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_LOCK, KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS flags.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available starting with Windows 8.1.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563)

[**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING**](https://msdn.microsoft.com/library/windows/hardware/dn567566)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





