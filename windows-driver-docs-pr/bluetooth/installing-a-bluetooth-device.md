---
title: Installing a Bluetooth Device
description: Installing a Bluetooth Device
ms.assetid: 2bf2b2df-260c-42a5-9ee9-6db91f304036
keywords:
- Bluetooth WDK , installations
- client-side profile drivers WDK Bluetooth
- server-side profile drivers WDK Bluetooth
- INF files WDK Bluetooth
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Bluetooth Device


There are two installation types for Bluetooth profile drivers

1.  Client-side installation

2.  Server-side installation

Client-side installations are for remote devices where the remote device advertises its services and the computer connects to it. Examples include: mouse devices, keyboards, and printers.

Server-side installations are where the computer advertises services and remote devices can connect to the computer to use those services. For example, a vendor could author a server-side installation to enable a PDA to print to a printer attached to the computer.

These two installation types require different installation procedures.

### <span id="installing_a_client_side_profile_driver"></span><span id="INSTALLING_A_CLIENT_SIDE_PROFILE_DRIVER"></span>**Installing a Client-side Profile Driver**

When a user wants to use a Bluetooth-enabled device, the user should bring the device within range of the computer and initiate a connection from the computer to the remote device. The following is the installation sequence for a client-side profile driver installation.

**To Install a Client-side Profile Driver**

1.  Launch Bluetooth Devices in **Control Panel** to find all devices within range of the computer.

2.  Select the device to pair with.

3.  Pair (or bond) the device with the local radio. This may or may not involve a PIN exchange.

4.  The local radio issues an SDP inquiry to identify the services supported on the remote device.

5.  The **Found New Hardware Wizard** searches for appropriate drivers on the local hard disk drive, and/or on Windows Update.

6.  If the **Found New Hardware Wizard** does not find an appropriate driver for the device, it prompts the user to insert the profile driver installation media that contains the profile driver's device setup information file (INF file).

### <span id="installing_a_server_side_profile_driver"></span><span id="INSTALLING_A_SERVER_SIDE_PROFILE_DRIVER"></span>**Installing a Server-side Profile Driver**

The Bluetooth driver stack supports service GUIDs as defined by the Bluetooth SIG, as well as custom GUIDs (that is, GUIDs that are not defined by the Bluetooth SIG).

**Note**  You can use the *Guidgen.exe* tool that is provided with the Microsoft Windows SDK to create custom GUIDs.

 

To expose computer functionality that remote Bluetooth devices can use, you must write a user-mode installation application.

The installation application must communicate with the Bluetooth driver stack to create a service GUID for the functionality to expose. Vendors specify the service GUID in the application and in their device installation INF file.

The installation application must call the user-mode API **BluetoothSetLocalServiceInfo**. However, before the application can call this API, the application must have the SE\_LOAD\_DRIVER\_NAME security privilege. The following code example demonstrates how to obtain this privilege. Note, the example does not demonstrate error handling.

```cpp
HANDLE procToken;
LUID luid;
TOKEN_PRIVILEGES tp;

OpenProcessToken(GetCurrentProcess(), TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &procToken);

LookupPrivilegeValue(NULL, SE_LOAD_DRIVER_NAME, &luid);

Tp.PrivilegeCount = 1;
Tp.privileges[0].Luid = luid;
Tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;

AdjustTokenPrivileges(procToken, FALSE, &tp, sizeof(TOKEN_PRIVILEGES), (PTOKEN_PRIVILEGES) NULL, (PDWORD)NULL)
```

### <span id="profile_driver_inf_file"></span><span id="PROFILE_DRIVER_INF_FILE"></span>**Profile Driver INF file**

A profile driver's INF file contains information about a Bluetooth device for client-side installation. For a server-side installation, the INF file specifies a device ID that corresponds to the service GUID created by the installation application. All Bluetooth devices are members of the **Bluetooth** class. The Bluetooth class installer ( *Bthci.dll*) assists in installing profile drivers.

For more information about creating and distributing INF files and installing drivers, see [Creating an INF File](https://msdn.microsoft.com/library/windows/hardware/ff549520) and [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

### <span id="plug_and_play_ids"></span><span id="PLUG_AND_PLAY_IDS"></span>**Plug and Play IDs**

The Bluetooth driver stack generates hardware IDs according to the following templates:

-   BTHENUM\\{ *ServiceGUID*}\_VID& *nnnnnnnn*

-   BTHENUM\\{ *ServiceGUID*}\_VID& *nnnnnnnn*\_PID& *nnnn*

-   BTHENUM\\{ *ServiceGUID*}\_LOCALMFG& *nnnn*

The Bluetooth driver stack generates compatible IDs according to the following template:

-   BTHENUM\\{ *ServiceGUID*}

*ServiceGUID* is a 16-bit GUID expanded into a 128-bit GUID, as defined by the Bluetooth specification. For example, {00001124-0000-1000-8000-00805F9B34FB} corresponds to an HID device.

The 8 digits following *VID&* correspond to the vendor ID code.

The 4 digits following *PID&* correspond to the product ID code.

The 4 digits following *LOCALMFG&* correspond to the manufacturer of the local Bluetooth radio.

The VID/PID and LOCALMFG tags are independent of each other.

The most generic device ID is a *ServiceGUID* by itself. For example:

BTHENUM\\{00001124-0000-1000-8000-00805F9B34FB}

You can restrict the Bluetooth driver stack to load your profile driver and software to run only on a specific release of a remote device by using Plug and Play IDs in both the remote device and the INF file. Note that the Bluetooth driver stack generates a VID/PID pair only if the device publishes a Plug and Play ID that the stack can detect using SDP. For example:

BTHENUM\\{00001124-0000-1000-8000-00805F9B34FB}\_VID& *nnnnnnnn*\_PID& *nnnn*

You can restrict the Bluetooth driver stack to load profile driver and software to run only on a specific local Bluetooth radio by specifying the LOCALMFG tag in the device ID in your INF file. For example:

BTHENUM\\{00001124-0000-1000-8000-00805F9B34FB}\_LOCALMFG& *nnnn*

 

 





