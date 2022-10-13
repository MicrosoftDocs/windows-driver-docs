---
title: Creating an INF file
description: Creating an INF file
keywords:
- joysticks WDK HID , INF files
- virtual joystick drivers WDK HID , INF files
- VJoyD WDK HID , INF files
- INF files WDK joysticks
- INF files WDK joysticks , creating
ms.date: 10/11/2022
---

# Creating an INF file

All minidrivers and OEM-defined joysticks should be installed using an INF file to provide all the necessary information to the system. An INF file describes a device installation in terms of the class of the device, the files that need to be copied, any compatible devices, any system resources the device requires, and changes to the registry. INF files for customizing the standard analog driver don't need to copy any files, state compatible devices, or specify system resources. The INF file can specify other actions, such as modifying the Autoexec.bat file, but this isn't necessary for a joystick minidriver.

The INF file contains the elements described below:

## Setting the device class

Joysticks fall under the MEDIA class, the one titled "Sound, video and game controllers" under the Add New Hardware control panel. The class-related sections should be copied from either the examples or the Joystick.inf file.

## Selecting source files

The "SourceDisksFiles" section of the INF file specifies which files to copy. This includes all necessary drivers, and any other files, such as documentation and setup applications. As this may be the first joystick driver to be installed on a user's system, the system joystick drivers Vjoyd.vxd and Msjstrick.drv should be copied, in addition to the specific drivers for this device. The source of these two drivers should be established by reference to Layout.inf (causing the user to be prompted for the Windows 95/98/Me installation disc) and not distributed on the OEM disc. The drivers should be copied to the user's system directory, which is destination code 11.

## Setting the manufacturer-specific data

The manufacturer-specific section that the INF file points to contains one entry for each device that can be installed. Each entry contains the name of the device followed by the name of the install section, the device ID, and any compatible devices. If the device has been registered as Plug and Play compatible, then the Plug and Play ID (starting with an asterisk) should be used for the device ID. If the device hasn't been registered, then a device ID that isn't Plug and Play compatible (that is, one not starting with an asterisk) should be used. When registering this type of device, avoid choosing an ID that conflicts with other device IDs ("Joystick," for example, wouldn't be a good ID).

## Setting up LogConfig entries

Devices requiring system resources such as input/output (I/O) ports use a LogConfig entry in the install section to specify which configurations they can use. Some devices don't use resources of their own. Instead, they use another driver, such as the serial port driver, to communicate with the device. The DirectX 3.0 VJoyD differs from previous versions in its handling of analog game port I/O port requirements. Older versions worked only if at least one device had been configured with I/O port allocations in the standard game port range 0x200 to 0x20f. In addition, the second I/O range had to be a single port. The newer VJoyD works if no game ports are configured to allow systems that have no game ports to use devices operated through minidrivers. The second I/O range can now be more than one port.

Devices using ports in the range 0x200 to 0x20f are interpreted to be analog game ports by VJoyD, and may therefore be considered conflicting devices by the configuration manager. Any other sets of game port I/O ports are ignored; if a machine has game ports on two cards, only the ports on one card are polled. If the device needs to use a standard game port in a nonstandard way, things get even more interesting. Requesting the standard ports in LogConfig entries of the installation section for the device can work but usually results in much reconfiguring and rebooting to swap joysticks. An alternative is to share the resources with VJoyD by using any set of I/O ranges passed through the configuration manager callback that fits the game port criteria. As long as the user doesn't configure joysticks to both the standard analog driver and the OEM driver, then run an application that tries to poll them both, this works.

In DirectX 3.0, changes were implemented to allow an OEM VxD to be called in place of the standard analog polling by setting the JOY_HWS_ISGAMEPORTDRIVER flag. Control Panel allows such a device to be set up as a global driver, meaning that it, rather than the internal analog polling, gets called for any joysticks that have no minidriver associated with them. This ensures that VJoyD doesn't interfere with the polling of the OEM device.

If the first four devices during boot are all handled by minidrivers (which may be an OEM global driver), VJoyD doesn't check for and is not able to use any game ports, even if these devices are no longer handled by minidrivers. If VJoyD can't use its ports (or if no game ports exist), returning JOY_OEMPOLLRC_YOUPOLL to a poll request doesn't cause the standard polling to be used. Reconfiguring back to devices using this polling takes effect only after the game port resources have been reallocated (probably not until a reboot).

## Setting up AddReg entries

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

Values that describe this joystick are put into the registry under an OEM-defined key, starting with the path REGSTR_PATH_JOYOEM (found under HKEY_LOCAL_MACHINE). Under this key, an OEM can place a number of static values that customize the way an OEM joystick appears in the joystick calibration program and to applications for Windows 95/98/Me. The names of the values are defined in Regstr.h, so it is the names of these constants that are discussed below, rather than the names that appear in the registry. Every OEM-defined device must at least have its basic properties defined and a name that the user can see in the joystick selection box under Control Panel. For a minidriver to be loaded, the value must contain the name of the minidriver VxD (including the .vxd extension). The OEM name value (REGSTR_VAL_JOYOEMNAME), and the minidriver file name(REGSTR_VAL_JOYOEMCALLOUT) values are simple strings. The basic properties REGSTR_VAL_JOYOEMDATA value is binary data, whose meaning is detailed in the following passages.

There are two doublewords; the first contains a set of flags, the second is the number of buttons the device has.

The flags specify what kind of device it is, which axes are present, and how they should be interpreted.

Most of the flags are defined in Mmddk.h. The two new flags added in DirectX 3.0 are defined in Dinput.h. The following flags are used only to remap the axes of an OEM-defined analog joystick that is polled directly by VJoyD. They change the default behavior of VJoyD when doing analog polling, but have no effect on the data returned by minidrivers.

| Flag | Description |
|--|--|
| JOY_HWS_XISJ1Y | X is on the J1 Y axis. |
| JOY_HWS_XISJ2X | X is on the J2 X axis. |
| JOY_HWS_XISJ2Y | X is on the J2 Y axis. |
| JOY_HWS_YISJ1X | Y is on the J1 X axis. |
| JOY_HWS_YISJ2X | Y is on the J2 X axis. |
| JOY_HWS_YISJ2Y | Y is on the J2 Y axis. |
| JOY_HWS_RISJ1X | R is on the J1 X axis. |
| JOY_HWS_RISJ1Y | R is on the J1 Y axis. |
| JOY_HWS_RISJ2Y | R is on the J2 Y axis. |
| JOY_HWS_ZISJ1X | Z is on the J1 X axis. |
| JOY_HWS_ZISJ1Y | Z is on the J1 Y axis. |
| JOY_HWS_ZISJ2X | Z is on the J2 X axis. |
| JOY_HWS_POVISJ1X | Polled POV is on the J1 X axis. |
| JOY_HWS_POVISJ1Y | Polled POV is on the J1 Y axis. |
| JOY_HWS_POVISJ2X | Polled POV is on the J2 X axis. |

The default behavior is:

- X defaults to the J1 X axis.
- Y defaults to the J1 Y axis.
- R (rudder) defaults to the J2 X axis.
- Z defaults to the J2 Y axis.
- POV hat (if implemented as polling) defaults to the J2 Y axis.

Flags are also defined to determine whether POV data comes from an axis or from a button combination. If the described device is being polled by VJoyD, JOY_HWS_POVISBUTTONCOMBOS causes VJoyD to interpret button combinations to produce the POV, otherwise an axis is used to find it. If the described device is polled through a minidriver, then a value in **dwPOV** other than POV_UNDEFINED causes an override of any other POV calculation. However, if JOY_HWS_POVISBUTTONCOMBOS is set, VJoyD interprets the buttons as it would for an analog joystick. Otherwise the POV is taken from the Z axis value if JOY_HWS_HASZ isn't set, from R otherwise. When possible, minidrivers should avoid having the generic VJoyD interpret POV information, as a minidriver usually has more information about the hardware implementation.

The following flags are used to describe which features the device has:

| Flag | Description |
|--|--|
| JOY_HWS_HASZ | Joystick has Z (third axis) information. |
| JOY_HWS_HASR | Joystick has R (fourth axis) information. |
| JOY_HWS_HASU | Joystick has R (fourth axis) information. |
| JOY_HWS_HASV | Joystick has R (fourth axis) information. |
| JOY_HWS_HASPOV | Joystick has a POV hat. |

The following flags are used to describe the device type:

| Flag | Device type |
|--|--|
| JOY_HWS_ISYOKE | Flight yoke |
| JOY_HWS_ISGAMEPAD | Game pad |
| JOY_HWS_ISCARCTRL | Race car controller |
| JOY_HWS_ISHEADTRACKER | Head tracker (defined in DirectX 3.0). |

Finally, the JOY_HWS_ISGAMEPORTDRIVER flag that was added in DirectX 3.0 indicates that this minidriver replaces the standard polling of a game port.

For example, if you have a digital joystick that has eight buttons and returns values for X, Y, Z, R, and POV, then you need to set the bits JOY_HWS_HASZ, JOY_HWS_HASPOV, and JOY_HWS_HASR. This gives you the following:

| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|--|--|--|--|
| &nbsp; | 0x00000001 | JOY_HWS_HASZ | 01,00,00,00 |
| &vert; | 0x00000002 | JOY_HWS_HASPOV | 02,00,00,00 |
| &vert; | 0x00080000 | JOY_HWS_HASR | 00,00,08,00 |
| = | 0x00080003 | combination | 03,00,08,00 |

Putting this **DWORD** in little-endian format, followed by a **DWORD** for the number of buttons, gives you 03,00,08,00,08,00,00,00, which is the series of bytes required in your INF file.

All of the remaining registry settings supplied in the INF file customize the instructions for calibration given by the standard control panel, and are as follows:

| Registry setting | Description |
|--|--|
| REGSTR_VAL_JOYOEMXYLABEL | This string is displayed below the XY position control found in the test and calibrate dialogs of the joystick CPL. |
| REGSTR_VAL_JOYOEMZLABEL | This string is displayed below the Z position control found in the test and calibrate dialogs of the joystick CPL. |
| REGSTR_VAL_JOYOEMRLABEL | This string is displayed below the R position control found in the test and calibrate dialogs of the joystick CPL. |
| REGSTR_VAL_JOYOEMPOVLABEL | This string is displayed below the POV hat control found in the test and calibrate dialogs of the joystick CPL. |
| REGSTR_VAL_JOYOEMULABEL | This string is displayed below the U position control found in the test and calibrate dialogs of the joystick CPL. |
| REGSTR_VAL_JOYOEMVLABEL | This string is displayed below the V position control found in the test and calibrate dialogs of the joystick CPL. |
| REGSTR_VAL_JOYOEMTESTMOVEDESC | This string is displayed in the movement section of the test dialog. It describes to the user how to test the joystick. |
| REGSTR_VAL_JOYOEMTESTBUTTONDESC | This string is displayed in the button section of the test dialog. It describes to the user how to test the buttons. |
| REGSTR_VAL_JOYOEMTESTMOVECAP | This string is displayed as the caption of the group box surrounding the movement section of the test dialog. |
| REGSTR_VAL_JOYOEMTESTBUTTONCAP | This string is displayed as the caption of the group box surrounding the button section of the test dialog. |
| REGSTR_VAL_JOYOEMTESTWINCAP | This string is displayed as the caption of the test dialog. |
| REGSTR_VAL_JOYOEMCALCAP | This string will be displayed as the caption of the calibration dialog. |
| REGSTR_VAL_JOYOEMCALWINCAP | This string is displayed as the caption of the calibration dialog. |
| REGSTR_VAL_JOYOEMCAL1 | This string instructs the user how to center the XY portion of the joystick for calibration. |
| REGSTR_VAL_JOYOEMCAL2 | This string instructs the user how to move the XY portion of the joystick for calibration. |
| REGSTR_VAL_JOYOEMCAL3 | This string instructs the user how to recenter the XY portion of the joystick for calibration. |
| REGSTR_VAL_JOYOEMCAL4 | This string instructs the user how to move the Z portion of the joystick for calibration. |
| REGSTR_VAL_JOYOEMCAL5 | This string instructs the user how to move the R portion of the joystick for calibration. |
| REGSTR_VAL_JOYOEMCAL6 | This string instructs the user how to move the U portion of the joystick for calibration. |
| REGSTR_VAL_JOYOEMCAL7 | This string instructs the user how to move the V portion of the joystick for calibration. |
| REGSTR_VAL_JOYOEMCAL8 | This string instructs the user how to move the POV hat up for calibration. |
| REGSTR_VAL_JOYOEMCAL9 | This string instructs the user how to move the POV hat right for calibration. |
| REGSTR_VAL_JOYOEMCAL10 | This string instructs the user how to move the POV hat down for calibration. |
| REGSTR_VAL_JOYOEMCAL11 | This string instructs the user how to move the POV hat left for calibration. |
| REGSTR_VAL_JOYOEMCAL12 | This string consists of a message that informs the user that the calibration process is finished. |
