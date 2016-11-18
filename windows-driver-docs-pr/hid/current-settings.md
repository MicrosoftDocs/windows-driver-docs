---
title: Current Settings
author: windows-driver-content
description: Current Settings
MS-HAID:
- 'di\_fbd5430e-8518-4971-b4ca-6ceafaa7e133.xml'
- 'hid.current\_settings'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4de99ad0-fcd9-4f8d-8125-8f622443a0c6
keywords: ["current registry settings WDK joysticks"]
---

# Current Settings


## <a href="" id="ddk-current-settings-di"></a>


There are two parts to the current registry settings: a value to store, which is a replacement for the standard polling, and a key under which the capabilities, calibrated values, and minidriver data are stored.

A minidriver that is used to poll devices that do not have an associated minidriver to replace the standard polling can be defined in the key named REGSTR\_VAL\_JOYCALLOUT. This feature was new for DirectX 3.0. The values are set by Control Panel from the advanced settings page when the user selects a new global driver from the list that contains all minidrivers that have the JOY\_HWS\_ISGAMEPORTDRIVER flag set.

The remaining settings are stored under the REGSTR\_KEY\_JOYCURR key. When a device is first configured to a particular joystick ID, Control Panel copies values from the relevant OEM key under REGSTR\_PATH\_JOYOEM to the REGSTR\_KEY\_JOYCURR key. Each of the key value names under this key contains the joystick ID as a part of the name so each joystick has its own settings. The REGSTR\_VAL\_JOYOEMNAME value is copied to the relevant REGSTR\_VAL\_JOYNOEMNAME and, if present, the REGSTR\_VAL\_JOYOEMCALLOUT value is copied to REGSTR\_VAL\_JOYNOEMCALLOUT. The REGSTR\_VAL\_JOYOEMDATA value is used as the first two doublewords of the REGSTR\_VAL\_JOYNCONFIG value, with the whole of that value defined (when expanded) as follows:

```
struct {
    /* usage settings, copied from REGSTR_VAL_JOYOEMNAME */
    struct {
        DWORD   dwFlags;
        DWORD   dwNumButtons;
    } hws;
 
    /* usage flags, described below */
    DWORD    dwUsageSettings;
 
    struct {
        /* values returned by hardware during calibration */
        struct { 
            /* minimums for each axis */
            struct {
                DWORD    dwX;
                DWORD    dwY;
                DWORD    dwZ;
                DWORD    dwR;
                DWORD    dwU;
                DWORD    dwV;
            } jpMin;
            /* maximums for each axis */
            struct {
                DWORD    dwX;
                DWORD    dwY;
                DWORD    dwZ;
                DWORD    dwR;
                DWORD    dwU;
                DWORD    dwV;
            } jpMax;
            /* center positions for each axis */
            struct
            {
                DWORD    dwX;
                DWORD    dwY;
                DWORD    dwZ;
                DWORD    dwR;
                DWORD    dwU;
                DWORD    dwV;
            } jpCenter;
        } jrvHardware;
 
        /* POV values returned by hardware during calibration */
        DWORD   dwPOVValues[JOY_POV_NUMDIRS];
 
        /* calibration flags, described below */
        DWORD   dwCalFlags;
    } hwv; 
 
    /* type of joystick, described below */
    DWORD   dwType;
 
    /* reserved for OEM drivers */
    DWORD   dwReserved; 
};
```

The usage settings are a combination of the following values:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>JOY_US_HASRUDDER</p></td>
<td><p>0x00000001l</p></td>
<td><p>/* joystick configured with rudder */</p></td>
</tr>
<tr class="even">
<td><p>JOY_US_PRESENT</p></td>
<td><p>0x00000002l</p></td>
<td><p>/* is joystick actually present? */</p></td>
</tr>
<tr class="odd">
<td><p>JOY_US_ISOEM</p></td>
<td><p>0x00000004l</p></td>
<td><p>/* joystick is an OEM-defined type */</p></td>
</tr>
<tr class="even">
<td><p>JOY_US_RESERVED</p></td>
<td><p>0x80000000l</p></td>
<td><p>/* reserved */</p></td>
</tr>
</tbody>
</table>

 

The calibration flags are a combination of the following values:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>JOY_ISCAL_XY</p></td>
<td><p>0x00000001l</p></td>
<td><p>/* XY are calibrated */</p></td>
</tr>
<tr class="even">
<td><p>JOY_ISCAL_Z</p></td>
<td><p>0x00000002l</p></td>
<td><p>/* Z is calibrated */</p></td>
</tr>
<tr class="odd">
<td><p>JOY_ISCAL_R</p></td>
<td><p>0x00000004l</p></td>
<td><p>/* R is calibrated */</p></td>
</tr>
<tr class="even">
<td><p>JOY_ISCAL_U</p></td>
<td><p>0x00000008l</p></td>
<td><p>/* U is calibrated */</p></td>
</tr>
<tr class="odd">
<td><p>JOY_ISCAL_V</p></td>
<td><p>0x00000010l</p></td>
<td><p>/* V is calibrated */</p></td>
</tr>
<tr class="even">
<td><p>JOY_ISCAL_POV</p></td>
<td><p>0x00000020l</p></td>
<td><p>/* POV is calibrated */</p></td>
</tr>
</tbody>
</table>

 

The **dwType** member holds a number representing the type of a predefined joystick. If an OEM calibration utility sets up this value, it should set a value outside the range of values defined in Mmddk.h. The exact value is unimportant as it is reset by the standard control panel.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Current%20Settings%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


