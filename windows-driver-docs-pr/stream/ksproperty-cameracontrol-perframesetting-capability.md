---
title: KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CAPABILITY
description: The KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CAPABILITY property ID that is defined in KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY is used to get the per-frame capabilities from the driver.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9EB8AB4C-56C0-4F70-AFFE-76444FAADFF8
keywords: ["KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CAPABILITY


The **KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CAPABILITY** property ID that is defined in [**KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/dn936802) is used to get the per-frame capabilities from the driver. This is a GET only control; the driver must fail any SET calls.

## <span id="Usage_summary"></span><span id="usage_summary"></span><span id="USAGE_SUMMARY"></span>Usage summary


To query per frame setting capability with the driver, the **KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CAPABILITY** property control is sent to the driver along with a data buffer. In a GET call, the driver fills the per frame setting capability payload in the data buffer provided using the format layout specified below.

-   Capability header ([**KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925190))

-   Item header ([**KSCAMERA\_PERFRAMESETTING\_CAP\_ITEM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925193))

-   Item header ([**KSCAMERA\_PERFRAMESETTING\_CAP\_ITEM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925193))

-   Item payload ([**KSPROPERTY\_STEPPING\_LONG**](https://msdn.microsoft.com/library/windows/hardware/dn936838) or [**KSPROPERTY\_STEPPING\_LONGLONG**](https://msdn.microsoft.com/library/windows/hardware/dn936841))

The capability payload must start with a capability header. Each capability item must start with an item header. If a capability item has a payload, the item header must be followed by a corresponding item payload.

In a GET call, a zero length buffer is sent to the driver first to find out the required data buffer size to hold the entire capability payload. In response to the call, the driver must return **STATUS\_BUFFER\_OVERFLOW** with the required capability buffer size that must be at least the size of [**KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925190).

The following are the descriptions of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** fields in context of the item types defined in the **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE** enumeration. The payload field represents the item payload structures after the **KSCAMERA\_PERFRAMESETTING\_CAP\_ITEM\_HEADER** structure.

<span id="Exposure_time_item"></span><span id="exposure_time_item"></span><span id="EXPOSURE_TIME_ITEM"></span>**Exposure time item**  
**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure + the size of a **KSPROPERTY\_STEPPING\_LONGLONG** structure if manual mode is supported.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_EXPOSURE\_TIME**.

**Flags**

This contains the available flags. This field must contain the flags available by doing a bit-wise OR of the flags defined in ksmedia.h.

``` syntax
#define KSCAMERA_PERFRAMESETTING_AUTO                           0x0000000100000000
#define KSCAMERA_PERFRAMESETTING_MANUAL                         0x0000000200000000
```

**Payload**

If the driver supports manual mode, a range payload must be specified in KSPROPERTY\_STEPPING\_LONGLONG.Bounds.SignedMinimum\\SignedMaxmum and KSPROPERTY\_STEPPING\_LONGLONG.SteppingDelta

<span id="Flash_item"></span><span id="flash_item"></span><span id="FLASH_ITEM"></span>**Flash item**  
**Size**

This is the size of the [**KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925190) structure.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_FLASH**

**Flags**

This contains the available flags. This field must contain the flags available by doing a bit-wise OR of the FLASH flags defined below in ksmedia.h.

``` syntax
#define KSCAMERA_EXTENDEDPROP_FLASH_OFF                                 0x0000000000000000  
#define KSCAMERA_EXTENDEDPROP_FLASH_ON                                  0x0000000000000001  
#define KSCAMERA_EXTENDEDPROP_FLASH_ON_ADJUSTABLEPOWER                  0x0000000000000002  
#define KSCAMERA_EXTENDEDPROP_FLASH_AUTO                                0x0000000000000004  
#define KSCAMERA_EXTENDEDPROP_FLASH_AUTO_ADJUSTABLEPOWER                0x0000000000000008  
#define KSCAMERA_EXTENDEDPROP_FLASH_REDEYEREDUCTION                     0x0000000000000010




```

**Payload**

The flash item does not have a payload. If KSCAMERA\_EXTENDEDPROP\_FLASH\_ON\_ADJUSTABLEPOWER or KSCAMERA\_EXTENDEDPROP\_FLASH\_AUTO\_ADJUSTABLEPOWER is specified in the flags, the power parameter is in the range from 0 to 100.

<span id="Exposure_compensation_item"></span><span id="exposure_compensation_item"></span><span id="EXPOSURE_COMPENSATION_ITEM"></span>**Exposure compensation item**  
**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure + the size of a **KSPROPERTY\_STEPPING\_LONG** structure if steps are supported.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_EXPOSURE\_COMPENSATION**

**Flags**

This contains the available flags. This field must contain the flags available by doing a bit-wise OR of the EVCOMP flags defined below in ksmedia.h or the AUTO flag defined below in ksmedia\_phone.h.

``` syntax
#define KSCAMERA_PERFRAMESETTING_AUTO                          0x0000000100000000
#define KSCAMERA_EXTENDEDPROP_EVCOMP_SIXTHSTEP                          0x0000000000000001  
#define KSCAMERA_EXTENDEDPROP_EVCOMP_QUARTERSTEP                        0x0000000000000002  
#define KSCAMERA_EXTENDEDPROP_EVCOMP_THIRDSTEP                          0x0000000000000004  
#define KSCAMERA_EXTENDEDPROP_EVCOMP_HALFSTEP                           0x0000000000000008  
#define KSCAMERA_EXTENDEDPROP_EVCOMP_FULLSTEP                           0x0000000000000010
```

**Payload**

If a driver supports only auto mode, a payload is not included. Otherwise, a range payload must be specified in a [**KSPROPERTY\_STEPPING\_LONG**](https://msdn.microsoft.com/library/windows/hardware/dn936838) structure. The min and max of EV compensation are absolute EV compensation values and are determined from **KSPROPERTY\_STEPPING\_LONG.Bounds.SignedMinimum** and KSPROPERTY\_STEPPING\_LONG.Bounds.SignedMaximum. The step of EV compensation is determined by the step size of the lowest EVCOMP step flag that corresponds to a float (for example, 1/6 for KSCAMERA\_EXTENDEDPROP\_EVCOMP\_SIXTHSTEP).

<span id="ISO_speed_item"></span><span id="iso_speed_item"></span><span id="ISO_SPEED_ITEM"></span>**ISO speed item**  
**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure + the size of a **KSPROPERTY\_STEPPING\_LONG** structure if manual mode is supported.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_ISO**

**Flags**

This field contains the available flags. This field must contain the flags available by doing a bit-wise OR of the ISO flags defined below in ksmedia.h and ksmedia\_phone.h. If per-frame ISO is supported, the driver must support at least one of the following capabilities, ISO\_AUTO and ISO\_MANUAL, in which ISO\_AUTO is mandatory. If ISO\_MANUAL is advertised, the driver must further advertise the supported ISO speed min\\max\\step in **KSPROPERTY\_STEPPING\_LONG.ISO\_MANUAL** must be supported if manual ISO is desired.

``` syntax
#define KSCAMERA_EXTENDEDPROP_ISO_MANUAL                                0x0080000000000000
```

``` syntax
#define KSCAMERA_EXTENDEDPROP_ISO_AUTO                                  0x0000000000000001
```

**Payload**

If a driver supports only auto mode, a payload is not included. Otherwise, a range payload must be specified in a **KSPROPERTY\_STEPPING\_LONG** structure. The min, max, and step of ISO speeds are determined from **KSPROPERTY\_STEPPING\_LONG.Bounds.UnsignedMinimum**, K**SPROPERTY\_STEPPING\_LONG.Bounds.UnsignedMaximum**, and **KSPROPERTY\_STEPPING\_LONG.Bounds.SteppingDelta**. Drivers supporting integer manual ISO should only advertise ISO\_MANUAL with supported ISO speed ranges (min/max/step). Numeric ISO\_Xxx presets are not supported for per-frame ISO.

<span id="Focus_item"></span><span id="focus_item"></span><span id="FOCUS_ITEM"></span>**Focus item**  
**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure + the size of a **KSPROPERTY\_STEPPING\_LONG** structure.

**Type**

This must be [**KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_FOCUS**](https://msdn.microsoft.com/library/windows/hardware/dn925212#kscamera-perframesetting-item-focus).

**Flags**

This contains the available flags. This field must be set by doing a bit-wise OR of the flag defined below in ksmedis.h.

``` syntax
#define KSCAMERA_PERFRAMESETTING_MANUAL                         0x0000000200000000
```

**Payload**

A range payload must be specified in a KSPROPERTY\_STEPPING\_LONG structure. The min, max, and step of lens position are determined from **KSPROPERTY\_STEPPING\_LONG.Bounds.UnsignedMinimum**, **KSPROPERTY\_STEPPING\_LONG.Bounds.UnsignedMaximum**, and **KSPROPERTY\_STEPPING\_LONG.SteppingDelta**. The behavior of per-frame setting focus and how it interworks with global focus settings is defined as follows.

1.  Lens position is sticky; but focus commands are not. If continuous auto focus (CAF) has been selected in the global settings, the CAF operation is overridden only for the specified frames and CAF will likely move the lens position (likely after a full sweep) after provided manual focus.

2.  The global focus setting is always assumed unless explicitly overridden with a manual setting in PFS.

3.  The global AF is one-shot and only applies to the first frame, if no manual override was specified.

4.  The global CAF applies to all frames unless explicitly overridden by a PFS.

5.  The global manual focus settings do not revert after a manual PFS (the lens position remains).

<span id="Confirmation_image_type"></span><span id="confirmation_image_type"></span><span id="CONFIRMATION_IMAGE_TYPE"></span>**Confirmation image type**  
**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_PHOTOCONFIRMATION**.

**Flags**

The flags field is not used.

**Payload**

There is no payload for this item.

<span id="Custom_property_item"></span><span id="custom_property_item"></span><span id="CUSTOM_PROPERTY_ITEM"></span>**Custom property item**  
**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure + the size of the GUID.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_CUSTOM**.

**Flags**

The flags field is not used.

**Payload**

This is the custom property GUID.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




