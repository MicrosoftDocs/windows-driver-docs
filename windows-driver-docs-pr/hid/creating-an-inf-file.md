---
title: Creating an INF File
description: Creating an INF File
keywords:
- joysticks WDK HID , INF files
- virtual joystick drivers WDK HID , INF files
- VJoyD WDK HID , INF files
- INF files WDK joysticks
- INF files WDK joysticks , creating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating an INF File

All minidrivers and OEM-defined joysticks should be installed using an INF file to provide all the necessary information to the system. An INF file describes a device installation in terms of the class of the device, the files that need to be copied, any compatible devices, any system resources the device requires, and changes to the registry. INF files for customizing the standard analog driver do not need to copy any files, state compatible devices, or specify system resources. The INF file can specify other actions, such as modifying the Autoexec.bat file, but this is not usually necessary for a joystick minidriver.

The INF file contains the elements described below:

## Setting the Device Class

Joysticks fall under the MEDIA class, the one titled "Sound, video and game controllers" under the Add New Hardware control panel. The class-related sections should be copied from either the examples or the Joystick.inf file.

## Selecting Source Files

The "SourceDisksFiles" section of the INF file specifies which files to copy. This includes all necessary drivers, as well as any other files, such as documentation and setup applications. As this may be the first joystick driver to be installed on a user's system, the system joystick drivers Vjoyd.vxd and Msjstrick.drv should be copied, in addition to the specific drivers for this device. The source of these two drivers should be established by reference to Layout.inf (causing the user to be prompted for the Windows 95/98/Me installation disc) and not distributed on the OEM disc. The drivers should be copied to the user's system directory, which is destination code 11.

## Setting the Manufacturer-Specific Data

The manufacturer-specific section that the INF file points to contains one entry for each device that can be installed. Each entry contains the name of the device followed by the name of the install section, the device ID, and any compatible devices. If the device has been registered as Plug and Play compatible, then the Plug and Play ID (starting with an asterisk) should be used for the device ID. If the device has not been registered, then a device ID that is not Plug and Play compatible (that is, one not starting with an asterisk) should be used. When registering this type of device, avoid choosing an ID that conflicts with other device IDs ("Joystick," for example, would not be a good ID).

## Setting Up LogConfig Entries

Devices requiring system resources such as input/output (I/O) ports use a LogConfig entry in the install section to specify which configurations they can use. Some devices do not use resources of their own. Instead, they use another driver, such as the serial port driver, to communicate with the device. The DirectX 3.0 VJoyD differs from previous versions in its handling of analog game port I/O port requirements. Older versions worked only if at least one device had been configured with either one or two I/O port allocations with ports in the standard game port range 0x200 to 0x20f. (In addition, the second I/O range had to be a single port.) The newer VJoyD works if no game ports are configured to allow systems that have no game ports to use devices operated through minidrivers. (The second I/O range can now be more than one port.)

Devices using ports in the range 0x200 to 0x20f are interpreted to be analog game ports by VJoyD, and may therefore be considered conflicting devices by the configuration manager. Any other sets of game port I/O ports are ignored; if a machine has game ports on two cards, only the ports on one card are polled. If the device needs to use a standard game port in a nonstandard way, things get even more interesting. Requesting the standard ports in LogConfig entries of the installation section for the device can work, but it usually results in a lot of reconfiguring and rebooting to swap joysticks. An alternative is to share the resources with VJoyD by using any set of I/O ranges passed through the configuration manager callback that fit the game port criteria. As long as the user does not configure joysticks to both the standard analog driver and the OEM driver, then run an application that tries to poll them both, this works well enough.

In DirectX 3.0, changes were implemented to allow an OEM VxD to be called in place of the standard analog polling by setting the JOY\_HWS\_ISGAMEPORTDRIVER flag. Control Panel allows such a device to be set up as a global driver, meaning that it, rather than the internal analog polling, gets called for any joysticks that have no minidriver associated with them. This ensures that VJoyD does not interfere with the polling of the OEM device.

If the first four devices during boot are all handled by minidrivers (which may be an OEM global driver), VJoyD does not check for -- and is not able to use -- any game ports, even if these devices are no longer handled by minidrivers. If VJoyD cannot use its ports (or if no game ports exist), returning JOY\_OEMPOLLRC\_YOUPOLL to a poll request does not cause the standard polling to be used. Reconfiguring back to devices using this polling takes effect only after the game port resources have been reallocated (probably not until a reboot).

## Setting Up AddReg Entries

The INF file also needs to set up registry entries in the section selected by the AddReg entry of the install section. For devices requiring a minidriver, the following need to be set up to make sure that the driver is properly associated with the multimedia system drivers:

```cpp
HKR,,DevLoader,,mmdevldr.vxd
HKR,Drivers,,,
HKR,Drivers,MIGRATED,,0
HKR,Drivers\joystick,,,
HKR,,Driver,,vjoyd.vxd
HKR,Drivers\joystick\msjstick.drv,,,
HKR,Drivers\joystick\msjstick.drv,Description,,%OEMJoy.DeviceDesc%
HKR,Drivers\joystick\msjstick.drv,Driver,,msjstick.drv
```

The %OEMJoy.DeviceDesc% string is replaced by whatever the device name string has been called.

Values that describe this joystick are put into the registry under an OEM-defined key, starting with the path REGSTR\_PATH\_JOYOEM (found under HKEY\_LOCAL\_MACHINE). Under this key, an OEM can place a number of static values that customize the way an OEM joystick appears in the joystick calibration program and to applications for Windows 95/98/Me. The names of the values are defined in Regstr.h, so it is the names of these constants that are discussed below, rather than the names that appear in the registry. Every OEM-defined device must at least have its basic properties defined and a name that the user can see in the joystick selection box under Control Panel. For a minidriver to be loaded, the value must contain the name of the minidriver VxD (including the .vxd extension). The OEM name value (REGSTR\_VAL\_JOYOEMNAME), and the minidriver file name(REGSTR\_VAL\_JOYOEMCALLOUT) values are simple strings. The basic properties REGSTR\_VAL\_JOYOEMDATA value is binary data, whose meaning is detailed in the following passages.

There are two doublewords; the first contains a set of flags, the second is the number of buttons the device has.

The flags specify what kind of device it is, which axes are present, and how they should be interpreted.

Most of the flags are defined in Mmddk.h. The two new flags added in DirectX 3.0 are defined in Dinput.h. The following flags are used only to remap the axes of an OEM-defined analog joystick that is polled directly by VJoyD. They change the default behavior of VJoyD when doing analog polling, but have no effect on the data returned by minidrivers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>JOY_HWS_XISJ1Y</p></td>
<td><p>X is on the J1 Y axis.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_XISJ2X</p></td>
<td><p>X is on the J2 X axis.</p></td>
</tr>
<tr class="odd">
<td><p>JOY_HWS_XISJ2Y</p></td>
<td><p>X is on the J2 Y axis.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_YISJ1X</p></td>
<td><p>Y is on the J1 X axis.</p></td>
</tr>
<tr class="odd">
<td><p>JOY_HWS_YISJ2X</p></td>
<td><p>Y is on the J2 X axis.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_YISJ2Y</p></td>
<td><p>Y is on the J2 Y axis.</p></td>
</tr>
<tr class="odd">
<td><p>JOY_HWS_RISJ1X</p></td>
<td><p>R is on the J1 X axis.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_RISJ1Y</p></td>
<td><p>R is on the J1 Y axis.</p></td>
</tr>
<tr class="odd">
<td><p>JOY_HWS_RISJ2Y</p></td>
<td><p>R is on the J2 Y axis.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_ZISJ1X</p></td>
<td><p>Z is on the J1 X axis.</p></td>
</tr>
<tr class="odd">
<td><p>JOY_HWS_ZISJ1Y</p></td>
<td><p>Z is on the J1 Y axis.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_ZISJ2X</p></td>
<td><p>Z is on the J2 X axis.</p></td>
</tr>
<tr class="odd">
<td><p>JOY_HWS_POVISJ1X</p></td>
<td><p>Polled POV is on the J1 X axis.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_POVISJ1Y</p></td>
<td><p>Polled POV is on the J1 Y axis.</p></td>
</tr>
<tr class="odd">
<td><p>JOY_HWS_POVISJ2X</p></td>
<td><p>Polled POV is on the J2 X axis.</p></td>
</tr>
</tbody>
</table>

The default behavior is:

- X defaults to the J1 X axis.

- Y defaults to the J1 Y axis.

- R (rudder) defaults to the J2 X axis.

- Z defaults to the J2 Y axis.

- POV hat (if implemented as polling) defaults to the J2 Y axis.

Flags are also defined to determine whether POV data comes from an axis or from a button combination. If the described device is being polled by VJoyD, JOY\_HWS\_POVISBUTTONCOMBOS causes VJoyD to interpret button combinations to produce the POV, otherwise an axis is used to find it. If the described device is polled through a minidriver, then a value in **dwPOV** other than POV\_UNDEFINED causes an override of any other POV calculation. However, if JOY\_HWS\_POVISBUTTONCOMBOS is set, VJoyD interprets the buttons as it would for an analog joystick. Otherwise the POV is taken from the Z axis value if JOY\_HWS\_HASZ is not set, from R otherwise. When possible, minidrivers should avoid having the generic VJoyD interpret POV information, as a minidriver usually has more information about the hardware implementation.

The following flags are used to describe which features the device has:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>JOY_HWS_HASZ</p></td>
<td><p>Joystick has Z (3rd axis) information.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_HASR</p></td>
<td><p>Joystick has R (4th axis) information.</p></td>
</tr>
<tr class="odd">
<td><p>JOY_HWS_HASU</p></td>
<td><p>Joystick has R (4th axis) information.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_HASV</p></td>
<td><p>Joystick has R (4th axis) information.</p></td>
</tr>
<tr class="odd">
<td><p>JOY_HWS_HASPOV</p></td>
<td><p>Joystick has a POV hat.</p></td>
</tr>
</tbody>
</table>

The following flags are used to describe the device type:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>JOY_HWS_ISYOKE</p></td>
<td><p>Device is a flight yoke.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_ISGAMEPAD</p></td>
<td><p>Device is a game pad.</p></td>
</tr>
<tr class="odd">
<td><p>JOY_HWS_ISCARCTRL</p></td>
<td><p>Device is a race car controller.</p></td>
</tr>
<tr class="even">
<td><p>JOY_HWS_ISHEADTRACKER</p></td>
<td><p>Device is a head tracker (defined in DirectX 3.0).</p></td>
</tr>
</tbody>
</table>

Finally, the JOY\_HWS\_ISGAMEPORTDRIVER flag that was added in DirectX 3.0 indicates that this minidriver replaces the standard polling of a game port.

For example, if you have a digital joystick that has eight buttons and returns values for X, Y, Z, R, and POV, then you need to set the bits JOY\_HWS\_HASZ, JOY\_HWS\_HASPOV, and JOY\_HWS\_HASR. This gives you the following:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><p>0x00000001</p></td>
<td><p>JOY_HWS_HASZ</p></td>
<td><p>01,00,00,00</p></td>
</tr>
<tr class="even">
<td><p>|</p></td>
<td><p>0x00000002</p></td>
<td><p>JOY_HWS_HASPOV</p></td>
<td><p>02,00,00,00</p></td>
</tr>
<tr class="odd">
<td><p>|</p></td>
<td><p>0x00080000</p></td>
<td><p>JOY_HWS_HASR</p></td>
<td><p>00,00,08,00</p></td>
</tr>
<tr class="even">
<td><p>=</p></td>
<td><p>0x00080003</p></td>
<td><p>combination</p></td>
<td><p>03,00,08,00</p></td>
</tr>
</tbody>
</table>

Putting this **DWORD** in little-endian format, followed by a **DWORD** for the number of buttons, gives you 03,00,08,00,08,00,00,00, which is the series of bytes required in your INF file.

All of the remaining registry settings supplied in the INF file customize the instructions for calibration given by the standard control panel, and are as follows:

<a href="" id="regstr-val-joyoemxylabel-"></a>REGSTR\_VAL\_JOYOEMXYLABEL
This string is displayed below the XY position control found in the test and calibrate dialogs of the joystick CPL.

<a href="" id="regstr-val-joyoemzlabel-"></a>REGSTR\_VAL\_JOYOEMZLABEL
This string is displayed below the Z position control found in the test and calibrate dialogs of the joystick CPL.

<a href="" id="regstr-val-joyoemrlabel-"></a>REGSTR\_VAL\_JOYOEMRLABEL
This string is displayed below the R position control found in the test and calibrate dialogs of the joystick CPL.

<a href="" id="regstr-val-joyoempovlabel-"></a>REGSTR\_VAL\_JOYOEMPOVLABEL
This string is displayed below the POV hat control found in the test and calibrate dialogs of the joystick CPL.

<a href="" id="regstr-val-joyoemulabel-"></a>REGSTR\_VAL\_JOYOEMULABEL
This string is displayed below the U position control found in the test and calibrate dialogs of the joystick CPL.

<a href="" id="regstr-val-joyoemvlabel-"></a>REGSTR\_VAL\_JOYOEMVLABEL
This string is displayed below the V position control found in the test and calibrate dialogs of the joystick CPL.

<a href="" id="regstr-val-joyoemtestmovedesc-"></a>REGSTR\_VAL\_JOYOEMTESTMOVEDESC
This string is displayed in the movement section of the test dialog. It describes to the user how to test the joystick.

<a href="" id="regstr-val-joyoemtestbuttondesc-"></a>REGSTR\_VAL\_JOYOEMTESTBUTTONDESC
This string is displayed in the button section of the test dialog. It describes to the user how to test the buttons.

<a href="" id="regstr-val-joyoemtestmovecap-"></a>REGSTR\_VAL\_JOYOEMTESTMOVECAP
This string is displayed as the caption of the group box surrounding the movement section of the test dialog.

<a href="" id="regstr-val-joyoemtestbuttoncap-"></a>REGSTR\_VAL\_JOYOEMTESTBUTTONCAP
This string is displayed as the caption of the group box surrounding the button section of the test dialog.

<a href="" id="regstr-val-joyoemtestwincap-"></a>REGSTR\_VAL\_JOYOEMTESTWINCAP
This string is displayed as the caption of the test dialog.

<a href="" id="regstr-val-joyoemcalcap-"></a>REGSTR\_VAL\_JOYOEMCALCAP
This string will be displayed as the caption of the calibration dialog.

<a href="" id="regstr-val-joyoemcalwincap-"></a>REGSTR\_VAL\_JOYOEMCALWINCAP
This string is displayed as the caption of the calibration dialog.

<a href="" id="regstr-val-joyoemcal1-"></a>REGSTR\_VAL\_JOYOEMCAL1
This string instructs the user how to center the XY portion of the joystick for calibration.

<a href="" id="regstr-val-joyoemcal2-"></a>REGSTR\_VAL\_JOYOEMCAL2
This string instructs the user how to move the XY portion of the joystick for calibration.

<a href="" id="regstr-val-joyoemcal3-"></a>REGSTR\_VAL\_JOYOEMCAL3
This string instructs the user how to recenter the XY portion of the joystick for calibration.

<a href="" id="regstr-val-joyoemcal4-"></a>REGSTR\_VAL\_JOYOEMCAL4
This string instructs the user how to move the Z portion of the joystick for calibration.

<a href="" id="regstr-val-joyoemcal5-"></a>REGSTR\_VAL\_JOYOEMCAL5
This string instructs the user how to move the R portion of the joystick for calibration.

<a href="" id="regstr-val-joyoemcal6-"></a>REGSTR\_VAL\_JOYOEMCAL6
This string instructs the user how to move the U portion of the joystick for calibration.

<a href="" id="regstr-val-joyoemcal7-"></a>REGSTR\_VAL\_JOYOEMCAL7
This string instructs the user how to move the V portion of the joystick for calibration.

<a href="" id="regstr-val-joyoemcal8-"></a>REGSTR\_VAL\_JOYOEMCAL8
This string instructs the user how to move the POV hat up for calibration.

<a href="" id="regstr-val-joyoemcal9-"></a>REGSTR\_VAL\_JOYOEMCAL9
This string instructs the user how to move the POV hat right for calibration.

<a href="" id="regstr-val-joyoemcal10-"></a>REGSTR\_VAL\_JOYOEMCAL10
This string instructs the user how to move the POV hat down for calibration.

<a href="" id="regstr-val-joyoemcal11-"></a>REGSTR\_VAL\_JOYOEMCAL11
This string instructs the user how to move the POV hat left for calibration.

<a href="" id="regstr-val-joyoemcal12-"></a>REGSTR\_VAL\_JOYOEMCAL12
This string consists of a message that informs the user that the calibration process is finished.
