---
title: Registry settings
description: Registry settings
keywords:
- joysticks WDK HID , registry settings
- virtual joystick drivers WDK HID , registry settings
- VJoyD WDK HID , registry settings
- registry WDK joysticks
ms.date: 10/12/2022
---

# Registry settings

The registry is used by the joystick interface to store configuration, calibration, and user preference information. It is also used to store customized text for the calibration program. The Windows 95/98/Me joystick calibration program can be customized through the registry to provide instructions to the user during calibration that are specific to the joystick.

The values fall into five groups:

Original data supplied by the OEM and installed from an INF file (described above).

## User values

There are two parts to the current registry settings: a value to store, which is a replacement for the standard polling, and a key under which the capabilities, calibrated values, and minidriver data are stored.

A minidriver that is used to poll devices that do not have an associated minidriver to replace the standard polling can be defined in the key named REGSTR_VAL_JOYCALLOUT. This feature was new for DirectX 3.0. The values are set by Control Panel from the advanced settings page when the user selects a new global driver from the list that contains all minidrivers that have the JOY_HWS_ISGAMEPORTDRIVER flag set.

The remaining settings are stored under the REGSTR_KEY_JOYCURR key. When a device is first configured to a particular joystick ID, Control Panel copies values from the relevant OEM key under REGSTR_PATH_JOYOEM to the REGSTR_KEY_JOYCURR key. Each of the key value names under this key contains the joystick ID as a part of the name so each joystick has its own settings. The REGSTR_VAL_JOYOEMNAME value is copied to the relevant REGSTR_VAL_JOYNOEMNAME and, if present, the REGSTR_VAL_JOYOEMCALLOUT value is copied to REGSTR_VAL_JOYNOEMCALLOUT. The REGSTR_VAL_JOYOEMDATA value is used as the first two doublewords of the REGSTR_VAL_JOYNCONFIG value, with the whole of that value defined (when expanded) as follows:

```cpp
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

| Setting | Value | Description |
|--|--|--|
| JOY_US_HASRUDDER | 0x00000001 | Joystick configured with rudder |
| JOY_US_PRESENT | 0x00000002 | Is joystick actually present? |
| JOY_US_ISOEM | 0x00000004 | Joystick is an OEM-defined type |
| JOY_US_RESERVED | 0x80000000 | Reserved |

The calibration flags are a combination of the following values:

| Flag | Value | Description |
|--|--|--|
| JOY_ISCAL_XY | 0x00000001 | XY are calibrated |
| JOY_ISCAL_Z | 0x00000002 | Z is calibrated |
| JOY_ISCAL_R | 0x00000004 | R is calibrated |
| JOY_ISCAL_U | 0x00000008 | U is calibrated |
| JOY_ISCAL_V | 0x00000010 | V is calibrated |
| JOY_ISCAL_POV | 0x00000020 | POV is calibrated |

The **dwType** member holds a number representing the type of a predefined joystick. If an OEM calibration utility sets up this value, it should set a value outside the range of values defined in Mmddk.h. The exact value is unimportant as it is reset by the standard control panel.

## Current settings

These registry settings are set up during installation from the INF file, as described in [Creating an INF File](creating-an-inf-file.md), and during the device enumeration at boot time.

## Saved settings

When the current joystick settings are saved, the REGSTR_VAL_JOYNCONFIG saved under the REGSTR_KEY_JOYCURR key is also written under the REGSTR_KEY_JOYSETTINGS key in a subkey with the same name as that from which the OEM-defined settings are taken (non-OEM settings are saved in a subkey "predef" plus the type number). When a joystick is replaced, the saved settings remain so that if the joystick is restored, the saved settings are put back into the current settings. These registry values are used only by Control Panel.

## Driver settings

A single value named REGSTR_VAL_JOYUSERVALUES stores the structure described below. This structure specifies how data should be manipulated by VJoyD when an application requests that data be scaled, centered, or have a dead zone defined.

```cpp
struct {
  /* value at which to time-out internal joystick polling */
  DWORD   dwTimeOut;

  /* range of values app wants returned for axes */
  struct {
    /* minimums for each axis */
    struct {
      DWORD  dwX;
      DWORD  dwY;
      DWORD  dwZ;
      DWORD  dwR;
      DWORD  dwU;
      DWORD  dwV;
    } jpMin;
    /* maximums for each axis */
    struct {
      DWORD  dwX;
      DWORD  dwY;
      DWORD  dwZ;
      DWORD  dwR;
      DWORD  dwU;
      DWORD  dwV;
    } jpMax;
    /* center positions for each axis */
    struct {
      DWORD  dwX;
      DWORD  dwY;
      DWORD  dwZ;
      DWORD  dwR;
      DWORD  dwU;
      DWORD  dwV;
    } jpCenter;
  } jrvRanges;

  /* area around center to be considered as "dead". specified as */
  /* a percentage (0-100). Only X & Y handled by system driver */
  struct {
    DWORD  dwX;
    DWORD  dwY;
    DWORD  dwZ;
    DWORD  dwR;
    DWORD  dwU;
    DWORD  dwV;
  } jpDeadZone;
}
```

The user values, current settings, and saved settings are all stored in the registry under the path belonging to the "current" joystick driver. Each of the joystick devices for which a driver is installed has a key under the path REGSTR_PATH_JOYCONFIG that has the form Msjstick.drv&lt;*xxxx*&gt;, where the *xxxx* is a four-digit number used to keep the key name unique. The number relates to the number of multimedia (sound, video and game controller) drivers that have been installed. At boot time, Msjstick.drv is initialized to the configuration for each of the game controller drivers. Since it can only deal with one configuration at a time, each one replaces the last and the "current" driver is the last one to be initialized. This means that the user is likely to lose all the current settings when a new driver is installed, and a minidriver cannot be structured on the assumption that the path to these registry values will always be the same.
