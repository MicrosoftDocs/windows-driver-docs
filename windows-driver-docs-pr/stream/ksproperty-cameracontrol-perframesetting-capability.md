---
title: KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CAPABILITY
description: The KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CAPABILITY property ID that is defined in KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY is used to get the per-frame capabilities from the driver.
keywords: ["KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/11/2018
---

# KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CAPABILITY

The **KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CAPABILITY** property ID that is defined in [**KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_cameracontrol_perframesetting_property) is used to get the per-frame capabilities from the driver. This is a GET only control; the driver must fail any SET calls.

## Usage summary

To query per frame setting capability with the driver, the **KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CAPABILITY** property control is sent to the driver along with a data buffer. In a GET call, the driver fills the per frame setting capability payload in the data buffer provided using the format layout specified below.

-   Capability header ([**KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_cap_header))

-   Item header ([**KSCAMERA\_PERFRAMESETTING\_CAP\_ITEM\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_cap_header))

-   Item header ([**KSCAMERA\_PERFRAMESETTING\_CAP\_ITEM\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_cap_header))

-   Item payload ([**KSPROPERTY\_STEPPING\_LONG**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_stepping_long) or [**KSPROPERTY\_STEPPING\_LONGLONG**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_stepping_longlong))

The capability payload must start with a capability header. Each capability item must start with an item header. If a capability item has a payload, the item header must be followed by a corresponding item payload.

In a GET call, a zero length buffer is sent to the driver first to find out the required data buffer size to hold the entire capability payload. In response to the call, the driver must return **STATUS\_BUFFER\_OVERFLOW** with the required capability buffer size that must be at least the size of [**KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_cap_header).

The following are the descriptions of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** fields in context of the item types defined in the **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE** enumeration. The payload field represents the item payload structures after the **KSCAMERA\_PERFRAMESETTING\_CAP\_ITEM\_HEADER** structure.


**Exposure time item**  

**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure + the size of a **KSPROPERTY\_STEPPING\_LONGLONG** structure if manual mode is supported.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_EXPOSURE\_TIME**.

**Flags**

This contains the available flags. This field must contain the flags available by doing a bit-wise OR of the flags defined in ksmedia.h.

```cpp
#define KSCAMERA_PERFRAMESETTING_AUTO       0x0000000100000000
#define KSCAMERA_PERFRAMESETTING_MANUAL     0x0000000200000000
```

**Payload**

If the driver supports manual mode, a range payload must be specified in KSPROPERTY\_STEPPING\_LONGLONG.Bounds.SignedMinimum\\SignedMaxmum and KSPROPERTY\_STEPPING\_LONGLONG.SteppingDelta

**Flash item**  

**Size**

This is the size of the [**KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_cap_header) structure.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_FLASH**

**Flags**

This contains the available flags. This field must contain the flags available by doing a bit-wise OR of the FLASH flags defined below in ksmedia.h.

```cpp
#define KSCAMERA_EXTENDEDPROP_FLASH_OFF                                 0x0000000000000000  
#define KSCAMERA_EXTENDEDPROP_FLASH_ON                                  0x0000000000000001  
#define KSCAMERA_EXTENDEDPROP_FLASH_ON_ADJUSTABLEPOWER                  0x0000000000000002  
#define KSCAMERA_EXTENDEDPROP_FLASH_AUTO                                0x0000000000000004  
#define KSCAMERA_EXTENDEDPROP_FLASH_AUTO_ADJUSTABLEPOWER                0x0000000000000008  
#define KSCAMERA_EXTENDEDPROP_FLASH_REDEYEREDUCTION                     0x0000000000000010
```

**Payload**

The flash item does not have a payload. If KSCAMERA\_EXTENDEDPROP\_FLASH\_ON\_ADJUSTABLEPOWER or KSCAMERA\_EXTENDEDPROP\_FLASH\_AUTO\_ADJUSTABLEPOWER is specified in the flags, the power parameter is in the range from 0 to 100.

**Exposure compensation item**  

**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure + the size of a **KSPROPERTY\_STEPPING\_LONG** structure if steps are supported.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_EXPOSURE\_COMPENSATION**

**Flags**

This contains the available flags. This field must contain the flags available by doing a bit-wise OR of the EVCOMP flags defined below in ksmedia.h or the AUTO flag defined below in ksmedia\_phone.h.

```cpp
#define KSCAMERA_PERFRAMESETTING_AUTO               0x0000000100000000
#define KSCAMERA_EXTENDEDPROP_EVCOMP_SIXTHSTEP      0x0000000000000001  
#define KSCAMERA_EXTENDEDPROP_EVCOMP_QUARTERSTEP    0x0000000000000002  
#define KSCAMERA_EXTENDEDPROP_EVCOMP_THIRDSTEP      0x0000000000000004  
#define KSCAMERA_EXTENDEDPROP_EVCOMP_HALFSTEP       0x0000000000000008  
#define KSCAMERA_EXTENDEDPROP_EVCOMP_FULLSTEP       0x0000000000000010
```

**Payload**

If a driver supports only auto mode, a payload is not included. Otherwise, a range payload must be specified in a [**KSPROPERTY\_STEPPING\_LONG**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_stepping_long) structure. The min and max of EV compensation are absolute EV compensation values and are determined from **KSPROPERTY\_STEPPING\_LONG.Bounds.SignedMinimum** and KSPROPERTY\_STEPPING\_LONG.Bounds.SignedMaximum. The step of EV compensation is determined by the step size of the lowest EVCOMP step flag that corresponds to a float (for example, 1/6 for KSCAMERA\_EXTENDEDPROP\_EVCOMP\_SIXTHSTEP).

**ISO speed item**  

**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure + the size of a **KSPROPERTY\_STEPPING\_LONG** structure if manual mode is supported.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_ISO**

**Flags**

This field contains the available flags. This field must contain the flags available by doing a bit-wise OR of the ISO flags defined below in ksmedia.h and ksmedia\_phone.h. If per-frame ISO is supported, the driver must support at least one of the following capabilities, ISO\_AUTO and ISO\_MANUAL, in which ISO\_AUTO is mandatory. If ISO\_MANUAL is advertised, the driver must further advertise the supported ISO speed min\\max\\step in **KSPROPERTY\_STEPPING\_LONG.ISO\_MANUAL** must be supported if manual ISO is desired.

```cpp
#define KSCAMERA_EXTENDEDPROP_ISO_MANUAL    0x0080000000000000
```

```cpp
#define KSCAMERA_EXTENDEDPROP_ISO_AUTO      0x0000000000000001
```

**Payload**

If a driver supports only auto mode, a payload is not included. Otherwise, a range payload must be specified in a **KSPROPERTY\_STEPPING\_LONG** structure. The min, max, and step of ISO speeds are determined from **KSPROPERTY\_STEPPING\_LONG.Bounds.UnsignedMinimum**, K**SPROPERTY\_STEPPING\_LONG.Bounds.UnsignedMaximum**, and **KSPROPERTY\_STEPPING\_LONG.Bounds.SteppingDelta**. Drivers supporting integer manual ISO should only advertise ISO\_MANUAL with supported ISO speed ranges (min/max/step). Numeric ISO\_Xxx presets are not supported for per-frame ISO.

**Focus item**  

**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure + the size of a **KSPROPERTY\_STEPPING\_LONG** structure.

**Type**

This must be [**KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_FOCUS**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-kscamera_perframesetting_item_type#kscamera-perframesetting-item-focus).

**Flags**

This contains the available flags. This field must be set by doing a bit-wise OR of the flag defined below in ksmedis.h.

```cpp
#define KSCAMERA_PERFRAMESETTING_MANUAL     0x0000000200000000
```

**Payload**

A range payload must be specified in a KSPROPERTY\_STEPPING\_LONG structure. The min, max, and step of lens position are determined from **KSPROPERTY\_STEPPING\_LONG.Bounds.UnsignedMinimum**, **KSPROPERTY\_STEPPING\_LONG.Bounds.UnsignedMaximum**, and **KSPROPERTY\_STEPPING\_LONG.SteppingDelta**. The behavior of per-frame setting focus and how it interworks with global focus settings is defined as follows.

1.  Lens position is sticky; but focus commands are not. If continuous auto focus (CAF) has been selected in the global settings, the CAF operation is overridden only for the specified frames and CAF will likely move the lens position (likely after a full sweep) after provided manual focus.

2.  The global focus setting is always assumed unless explicitly overridden with a manual setting in PFS.

3.  The global AF is one-shot and only applies to the first frame, if no manual override was specified.

4.  The global CAF applies to all frames unless explicitly overridden by a PFS.

5.  The global manual focus settings do not revert after a manual PFS (the lens position remains).

**Confirmation image type** 

**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_PHOTOCONFIRMATION**.

**Flags**

The flags field is not used.

**Payload**

There is no payload for this item.


**Custom property item**  

**Size**

This is the size of the **KSCAMERA\_PERFRAMESETTING\_CAP\_HEADER** structure + the size of the GUID.

**Type**

This must be **KSCAMERA\_PERFRAMESETTING\_ITEM\_TYPE.KSCAMERA\_PERFRAMESETTING\_ITEM\_CUSTOM**.

**Flags**

The flags field is not used.

**Payload**

This is the custom property GUID.

## Requirements

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
