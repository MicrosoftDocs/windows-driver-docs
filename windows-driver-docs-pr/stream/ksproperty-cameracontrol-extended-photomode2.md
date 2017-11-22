---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE property allows a submode to be configured.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: B5BE7B11-66FD-476C-8141-C2210B21133C
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE


The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE property allows a submode to be configured.

## <span id="Usage_summary"></span><span id="usage_summary"></span><span id="USAGE_SUMMARY"></span>Usage summary


The following submodes are defined as follows.

``` syntax
#define KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE_SUB_NONE       0x00000000
#define KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE_SUB_VARIABLE   0x00000001
```

KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_SEQUENCE\_SUB\_NONE is used by a regular photo sequence.

KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_SEQUENCE\_SUB\_VARIABLE is used to indicate a photo sequence is variable. If per-frame settings are specified, the KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_SEQUENCE\_SUB\_VARIABLE flag will be specified in the submode field of the KSCAMERA\_EXTENDEDPROP\_PHOTOMODE structure to indicate a variable photo sequence, even if no item settings are specified (item count is 0 for all frames). When the frame count is 1 and the item count is 0, the variable photo sequence reduces to one frame variable photo sequence using global settings.

The following is a definition of the KSCAMERA\_EXTENDEDPROP\_PHOTOMODE structure defined in ksmedia.h

``` syntax
typedef struct tagKSCAMERA_EXTENDEDPROP_PHOTOMODE {  
    ULONG       RequestedHistoryFrames;  
    ULONG       MaxHistoryFrames;  
    ULONG       SubMode;  
    ULONG       Reserved;  
} KSCAMERA_EXTENDEDPROP_PHOTOMODE, *PKSCAMERA_EXTENDEDPROP_PHOTOMODE;
```

Variable photo sequence mode has the following unique characteristics on a photo sequence.

-   Always use a finite photo sequence.

-   Per frame settings are applied when the frame count is greater than 0.

-   The driver will automatically stop the photo sequence at the end without the need for the KS\_VideoControlFlag\_StopPhotoSequenceCapture trigger when a loop count of greater than 0 is specified.

-   The last sample must be marked with the KSSTREAM\_HEADER\_OPTIONSF\_ENDOFPHOTOSEQUENCE flag.

-   The capture pipeline will not drop any sample from the driver.

-   Neither the pipeline nor the driver\\MFT0 generates any photo thumbnail.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




