---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE extended property is extended to support advanced focus scenarios as follows
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2A55CA7C-2EC0-4D88-8499-E05BF68DA97C
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


The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE extended property is extended to support advanced focus scenarios as follows:

-   Focus unlock

-   Continuous focus and lock

-   Driver fallback control in the event of a focus search failure

-   Focus search on preconfigured regions

-   Predefined manual positions

## <span id="Usage_summary_table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage summary table


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Scope</th>
<th>Control</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Version 1</p></td>
<td><p>Filter</p></td>
<td><p>Asynchronous, Cancellable</p></td>
</tr>
</tbody>
</table>

 

The following new capability flags are defined in ksmedia\_phone.h for these new scenarios.

``` syntax
#define KSCAMERA_EXTENDEDPROP_FOCUS_CONTINUOUSLOCK                     0x0000000000000200
#define KSCAMERA_EXTENDEDPROP_FOCUS_UNLOCK                             0x0000000000000400
#define KSCAMERA_EXTENDEDPROP_FOCUS_DRIVERFALLBACK_OFF                 0x0000000000000800
#define KSCAMERA_EXTENDEDPROP_FOCUS_REGIONBASED                        0x0000000000001000

#define KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_INFINITY                  0x0000000000200000
#define KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_HYPERFOCAL                0x0000000000400000
#define KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_NEAREST                   0x0000000000800000
```

**KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUSLOCK**

When this flag is specified, it locks the continuous auto focus after ensuring focus convergence. The driver sends a completion event after the focus is locked. This flag can only be used when KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS is specified. If KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS is advertised by the driver, KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUSLOCK must also be supported.

**KSCAMERA\_EXTENDEDPROP\_FOCUS\_UNLOCK**

When this flag is specified, it unlocks the focus. For single focus, this releases focus and immediately moves the lens to a driver determined default position without initiating any focus search. For continuous auto focus, this releases focus and resumes continuous auto focus. The driver sends a completion event after focus is unlocked. If focus is not locked, the driver should accept this command and send a completion event immediately. This flag is not sticky and must not overwrite the focus mode which is defined as KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO, KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS, KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL.

**KSCAMERA\_EXTENDEDPROP\_FOCUS\_DRIVERFALLBACK\_OFF**

When this flag is specified, the driver must not decide a lens fallback position. If the focus search fails, the lens position must be kept at where the search ended. This flag can only be set along with the KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO flag or the KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUSLOCK flag.

**KSCAMERA\_EXTENDEDPROP\_FOCUS\_REGIONBASED**

When this flag is specified, the focus search is based on the regions preconfigured by ROI control. If no regions have been configured, focus search is based on the default region determined by the driver. This flag can only be set when KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO or KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS is also specified at the same time.

**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO**

This flag indicates that the focus is a single auto focus. The driver sends a completion event after the focus has converged. This flag is mutually exclusive of the KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL and KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS flags.

**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL**

This flag indicates that the focus is manual. The driver sends a completion event after the manual focus has completed. The lens position to use is determined by VideoProc.Value.ul if the DISTANCE\_XXX flag is not present. If the DISTANCE\_XXX flag is present, the DISTANCE\_XXX takes precedence over VideoProc.Value.ul and moves the lens to a predefined manual position as determined by the DISTANCE\_XXX flag.

**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_LOCK**

This flag indicates that the focus is locked on the spot after it receives the LOCK command. The driver sends a completion event after the focus is locked. This flag must not overwrite the focus mode which is defined as KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO, KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS, KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL.

**KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS**

This flag indicates that the focus is continuous. The driver must accept this command and complete the asynchronous operation immediately. This flag is mutually exclusive of the KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL, KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO and LOCK flags. This mode is optional and may not be supported on all devices.

**KSCAMERA\_EXTENDEDPROP\_FOCUS\_RANGE\_MACRO\\NORMAL\\FULLRANGE**

The range serves only as a hint and the exact focal search range is up to driver. These flags can only be used with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO and KSCAMERA\_EXTENDEDPROP\_FOCUS\_CONTINUOUS.

**KSCAMERA\_EXTENDEDPROP\_FOCUS\_DISTANCE\_NEAREST**

When this flag is specified with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL, the driver immediately moves the lens to a predefined nearest position and keeps the lens in that position.

**KSCAMERA\_EXTENDEDPROP\_FOCUS\_DISTANCE\_INFINITY**

When this flag is specified with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL, the driver immediately moves the lens to a predefined infinity position and keeps the lens in that position.

**KSCAMERA\_EXTENDEDPROP\_FOCUS\_DISTANCE\_HYPERFOCAL**

When this flag is specified with KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL, the driver immediately moves the lens to a predefined hyper focal position and keeps the lens in that position.

The following capabilities are mandatory for Windows Phone 8.1 and later camera drivers.

-   KSCAMERA\_EXTENDEDPROP\_FOCUS\_UNLOCK

-   KSCAMERA\_EXTENDEDPROP\_FOCUS\_REGIONBASED

-   KSCAMERA\_EXTENDEDPROP\_FOCUS\_DRIVERFALLBACK\_OFF

-   KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_AUTO

-   KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_MANUAL

-   KSCAMERA\_EXTENDEDPROP\_VIDEOPROCFLAG\_LOCK

The descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136) structure fields when using the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE property are the same as the Windows 8.1 DDI.

The following table contains the descriptions and requirements for the KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING structure fields when using the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE property. This structure is defined in ksmedia.h

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Mode</p></td>
<td><p>This is unused and must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Min/Max/Step</p></td>
<td><p>The Min/Max/Step contains the minimum/maximum/increment of the manual lens position supported by the camera driver. These values are logical ranges and are unitless. The driver must return these values for GET operations if manual focus is supported.</p></td>
</tr>
<tr class="odd">
<td><p>VideoProc</p></td>
<td><p>If KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_MANUAL is specified in the Flags field of the KSCAMERA_EXTENDEDPROP_HEADER, the VideoProc.Value.ul must specify the lens position within the range described by the Min/Max/Step parameter.</p>
<p>If Flags other than Manual is specified, for SET operations, the VideoProc field is ignored. For GET operations, the driver must always return the current lens position regardless.</p></td>
</tr>
<tr class="even">
<td><p>Reserved</p></td>
<td><p>This is unused. This must be ignored by the driver</p></td>
</tr>
</tbody>
</table>

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




