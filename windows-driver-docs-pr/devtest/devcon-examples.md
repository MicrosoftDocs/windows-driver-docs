---
title: Device Console (DevCon.exe) Examples
description: Explore examples for Device Console (DevCon.exe) commands, including hardware IDs, classes, driver files, installing and scanning, and more.
keywords:
- DevCon WDK , examples
- Device Console WDK , examples
- examples WDK DevCon
- DevCon WDK , commands
- Device Console WDK , commands
- commands WDK DevCon
- Example 44 Forcibly update the HAL
- HAL update example
ms.date: 07/16/2025
ms.topic: example-scenario
---

# Device Console (DevCon.exe) examples

This article provides examples to demonstrate various Device Console (*DevCon.exe*) commands, including hardware identifiers (IDs), classes, driver files, installing and scanning, and more.

> [!IMPORTANT]
> Administrators are recommended to use the [PnPUtil](pnputil.md) command line tool rather than the Device Console sample. The PnPUtil tool ships with every release of Windows and makes use of the most reliable and secure APIs available. For more information on using PnPutil instead of Device Console, see [Replacing Device Console](devcon-migration.md).

## Example categories

The article provides examples for the following categories of Device Console commands, or _DevCon_ for short.

| Category | Examples |
|----------|----------|
| **HwIDs**| [Example 1: Find all hardware IDs](#example-1-find-all-hardware-ids) </br>[Example 2: Find hardware IDs by using a pattern](#example-2-find-hardware-ids-by-using-a-pattern) </br>[Example 3: Find hardware IDs by using a class](#example-3-find-hardware-ids-by-using-a-class) |
| **Classes**| [Example 4: List classes on the local computer](#example-4-list-classes-on-the-local-computer) |
| **ListClass** | [Example 6: List the devices in a device setup class](#example-6-list-the-devices-in-a-device-setup-class) </br>[Example 7: List the devices in multiple classes](#example-7-list-the-devices-in-multiple-classes) |
| **DriverFiles**| [Example 8: List all driver files](#example-8-list-all-driver-files) </br>[Example 9: List the driver files of a particular device](#example-9-list-the-driver-files-of-a-particular-device) |
| **DriverNodes**| [Example 10: List driver packages by hardware ID pattern](#example-10-list-driver-packages-by-hardware-id-pattern) </br>[Example 11: List driver packages by device instance ID pattern](#example-11-list-driver-packages-by-device-instance-id-pattern) |
| **Resources**| [Example 12: List resources of a class of devices](#example-12-list-resources-of-a-class-of-devices) </br>[Example 13: List resources of a device by ID](#example-13-list-resources-of-device-by-id) |
| **Stack**| [Example 14: Display the driver stack for storage devices](#example-14-display-the-driver-stack-for-storage-devices) </br>[Example 15: Find the setup class of a device](#example-15-find-the-setup-class-of-a-device) </br>[Example 16: Display the stack for related devices](#example-16-display-the-stack-for-related-devices) |
| **Status**| [Example 17: Display the status of all devices on the local computer](#example-17-display-the-status-of-all-devices) </br>[Example 18: Display the status of a device by device instance ID](#example-18-display-the-status-of-a-device-by-device-instance-id) </br>[Example 19: Display the status of related devices](#example-19-display-the-status-of-related-devices) |
| **Find**| [Example 20: Find devices by hardware ID pattern](#example-20-find-devices-by-hardware-id-pattern) </br>[Example 21: Find devices by device instance ID or class](#example-21-find-devices-by-device-instance-id-or-class) |
| **FindAll**| [Example 22: Find (and find all) devices in a setup class](#example-22-find-and-find-all-devices-in-a-setup-class) |
| **ClassFilter**| [Example 23: Display the filter drivers for a setup class](#example-23-display-the-filter-drivers-for-a-setup-class) </br>[Example 24: Add a filter driver to a setup class](#example-24-add-a-filter-driver-to-a-setup-class) </br>[Example 25: Insert a filter driver in the class list](#example-25-insert-a-filter-driver-in-the-class-list) </br>[Example 26: Replace a filter driver](#example-26-replace-a-filter-driver) </br>[Example 27: Change the order of filter drivers](#example-27-change-the-order-of-filter-drivers) |
| **Enable**| [Example 28: Enable a particular device](#example-28-enable-a-particular-device) </br>[Example 29: Enable devices by class](#example-29-enable-devices-by-class) |
| **Disable**| [Example 30: Disable devices by an ID pattern](#example-30-disable-devices-by-an-id-pattern) </br>[Example 31: Disable devices by device instance ID](#example-31-disable-devices-by-device-instance-id) |
| **Update and UpdateNI**| [Example 32: Update the driver for communication ports](#example-32-update-the-driver-for-communication-ports) </br>[Example 44: Forcibly update the hardware abstraction layer (HAL)](#example-44-forcibly-update-the-hal) |
| **Install**| [Example 33: Install a device](#example-33-install-a-device) </br>[Example 34: Install a device by using unattended setup](#example-34-install-a-device-by-using-unattended-setup) |
| **Remove**| [Example 35: Remove devices by device instance ID pattern](#example-35-remove-devices-by-device-instance-id-pattern) </br>[Example 36: Remove a particular network device](#example-36-remove-a-particular-network-device) |
| **Rescan**| [Example 37: Scan the computer for new devices](#example-37-scan-the-computer-for-new-devices) |
| **Restart**| [Example 38: Restart a device](#example-38-restart-a-device) |
| **Reboot**| [Example 39: Reboot the local computer](#example-39-reboot-the-local-computer) |
| **SetHwID** | [Example 40: Assign a hardware ID to a legacy device](#example-40-assign-a-hardware-id-to-a-legacy-device) </br>[Example 41: Add a hardware ID to all legacy devices](#example-41-add-a-hardware-id-to-all-legacy-devices) </br>[Example 42: Delete a hardware ID from all legacy devices](#example-42-delete-a-hardware-id-from-all-legacy-devices) </br>[Example 43: Add, delete, and replace hardware IDs](#example-43-add-delete-and-replace-hardware-ids) </br>[Example 44: Forcibly update the HAL](#example-44-forcibly-update-the-hal) |
| **dp_add, dp_deleted, dp_enum** | [Example 45: Add and remove driver packages](#example-45-add-and-remove-driver-packages) |

## Example details

The full DevCon examples are provided in the following sections.

### Example 1: Find all hardware IDs

DevCon operations use IDs and ID patterns to identify devices. As a result, a common first step for using DevCon is to create a hardware ID reference file for devices on the computer.

The following command uses the **[DevCon HwIDs](devcon-hwids.md)** operation, which returns the IDs and the device description. The command uses the asterisk (`*`) wildcard character to represent all devices on the local computer.

```console
devcon hwids *
```

Because the output is lengthy and used repeatedly, save the output in a text file for reference.

The following command extends the previous command with the redirection character (`>`). The redirection saves the command output in the specified file, *hwids.txt*.

```console
devcon hwids * > hwids.txt
```

### Example 2: Find hardware IDs by using a pattern

To find the hardware IDs of a particular device, enter one of the following values with the command:

- Hardware ID or pattern
- Compatible ID or pattern
- Device instance ID or pattern
- Name of the device setup class

The following command uses the **DevCon HwIDs** operation and a pattern to find the hardware IDs of the floppy disk drive on the computer. (The user assumes that the pattern appears in one of the device IDs.) The command uses the wildcard character (`*`) to represent all characters that might precede or follow the word `floppy` in any of the IDs.

```console
devcon hwids *floppy*
```

In response, DevCon displays the device instance ID, hardware ID, and compatible ID of the floppy disk drive on the computer. You can use these IDs in subsequent DevCon commands.

```console
FDC\GENERIC_FLOPPY_DRIVE\5&39194F6D&0&0
    Name: Floppy disk drive
    Hardware ID's:
        FDC\GENERIC_FLOPPY_DRIVE
    Compatible ID's:
        GenFloppyDisk
1 matching device(s) found.
```

In this example, the phrase "floppy" occurs in the hardware ID or compatible ID of only one device on the computer. If the phrase occurs in the ID of more than one device, all devices with the phrase "floppy" in their IDs appear in the output.

### Example 3: Find hardware IDs by using a class

The following command uses the **[DevCon HwIDs](devcon-hwids.md)** operation and a device setup class to find the hardware IDs of all devices in the Ports device setup class. The equals symbol (`=`) that precedes the class name indicates that the specified value is a class and not an ID.

```console
devcon hwids =ports
```

In response, DevCon displays the hardware IDs and compatible IDs of the three devices in the Ports setup class:

```console
ACPI\PNP0401\4&B4063F4&0
    Name: ECP Printer Port (LPT1)
    Hardware ID's:
        ACPI\PNP0401
        *PNP0401
ACPI\PNP0501\1
    Name: Communications Port (COM1)
    Hardware ID's:
        ACPI\PNP0501
        *PNP0501
ACPI\PNP0501\2
    Name: Communications Port (COM2)
    Hardware ID's:
        ACPI\PNP0501
        *PNP0501
3 matching device(s) found.
```

### Example 4: List classes on the local computer

Because DevCon operations can use the device setup class to identify devices, it's helpful to create a reference file of the device setup classes of devices on the computer.

The following command uses the **[DevCon Classes](devcon-classes.md)** operation, which returns a list and description of all classes on the computer.

```console
devcon classes
```

Because the output is lengthy and used repeatedly, save the output in a text file for reference.

The following command displays all device classes on the computer. It uses the redirection character (`>`) to save the command output in the specified file, *classes.txt*.

```console
devcon classes > classes.txt
```

### Example 6: List the devices in a device setup class

The following command uses the **[DevCon ListClass](devcon-listclass.md)** operation to list the devices in Net, the device setup class for network adapters.

```console
devcon listclass net
```

In response, DevCon displays the device instance ID and description of each device in the Net setup class:

```console
Listing 6 device(s) for setup class "Net" (Network adapters).
PCI\VEN_10B7&DEV_9200&SUBSYS_00BE1028&REV_78\4&BB7B4AE&0&60F0: 3Com 3C920 Integrated Fast Ethernet Controller (3C905C-TX Compatible)
ROOT\MS_L2TPMINIPORT\0000                                   : WAN Miniport (L2TP)
ROOT\MS_NDISWANIP\0000                                      : WAN Miniport (IP)
ROOT\MS_PPPOEMINIPORT\0000                                  : WAN Miniport (PPPOE)
ROOT\MS_PPTPMINIPORT\0000                                   : WAN Miniport (PPTP)
ROOT\MS_PTIMINIPORT\0000                                    : Direct Parallel
```

Although the command response is interesting, it doesn't provide the hardware IDs of the devices in the Net setup class.

The following command uses the **[DevCon HwIDs](devcon-hwids.md)** operation to list the devices in the Net setup class. In a **DevCon HwIDs** command, the equals symbol (`=`) precedes the value to indicate that the value is a class and not an ID.

```console
devcon hwids =net
```

The resulting display lists the devices in the Net class and includes the device instance ID, hardware IDs, and compatible IDs of devices in the class.

```console
PCI\VEN_10B7&DEV_9200&SUBSYS_00BE1028&REV_78\4&BB7B4AE&0&60F0
    Name: 3Com 3C920 Integrated Fast Ethernet Controller (3C905C-TX Compatible)
    Hardware ID's:
        PCI\VEN_10B7&DEV_9200&SUBSYS_00BE1028&REV_78
        PCI\VEN_10B7&DEV_9200&SUBSYS_00BE1028
        PCI\VEN_10B7&DEV_9200&CC_020000
        PCI\VEN_10B7&DEV_9200&CC_0200
    Compatible ID's:
        PCI\VEN_10B7&DEV_9200&REV_78
        PCI\VEN_10B7&DEV_9200
        PCI\VEN_10B7&CC_020000
        PCI\VEN_10B7&CC_0200
 PCI\VEN_10B7
        PCI\CC_020000
 PCI\CC_0200
ROOT\MS_L2TPMINIPORT\0000
    Name: WAN Miniport (L2TP)
    Hardware ID's:
        ms_l2tpminiport
ROOT\MS_NDISWANIP\0000
    Name: WAN Miniport (IP)
    Hardware ID's:
        ms_ndiswanip
ROOT\MS_PPPOEMINIPORT\0000
    Name: WAN Miniport (PPPOE)
    Hardware ID's:
        ms_pppoeminiport
ROOT\MS_PPTPMINIPORT\0000
    Name: WAN Miniport (PPTP)
    Hardware ID's:
        ms_pptpminiport
ROOT\MS_PTIMINIPORT\0000
    Name: Direct Parallel
    Hardware ID's:
        ms_ptiminiport
6 matching device(s) found.
```

### Example 7: List the devices in multiple classes

The following command uses the **[DevCon ListClass](devcon-listclass.md)** operation to list the devices in the DiskDrive, CDROM, and TapeDrive classes.

```console
devcon listclass diskdrive cdrom tapedrive
```

In response, DevCon displays the devices in those classes:

```console
Listing 1 device(s) for setup class "DiskDrive" (Disk drives).
IDE\DISKWDC_WD204BA_____________________________16.13M16\4457572D414D3730323136333938203120202020: WDC WD204BA
Listing 1 device(s) for setup class "CDROM" (DVD/CD-ROM drives).
IDE\CDROMSAMSUNG_DVD-ROM_SD-608__________________2.2_____\4&13B4AFD&0&0.0.0: SAMSUNG DVD-ROM SD-608
No devices for setup class "TapeDrive" (Tape drives).
```

### Example 8: List all driver files

The following command uses the **[DevCon DriverFiles](devcon-driverfiles.md)** operation to list the file names of drivers that devices on the system use. The command uses the wildcard character (`*`) to represent all devices on the system. Because the output is extensive, it uses the redirection character (`>`) to save the command output in the specified file, *driverfiles.txt*.

```console
devcon driverfiles * > driverfiles.txt
```

### Example 9: List the driver files of a particular device

The following command uses the **[DevCon DriverFiles](devcon-driverfiles.md)** operation to search for the device driver used by the mouse device on the local computer. The command identifies the device by one of its hardware IDs, `HID\Vid_045e&Pid_0039&Rev_0121`. The hardware ID is enclosed in quotes (`" "`) because it includes the ampersand (`&`) symbol.

```console
devcon driverfiles "HID\Vid_045e&Pid_0039&Rev_0121"
```

In response, DevCon displays the two device drivers that support the mouse device:

```console
HID\VID_045E&PID_0039\6&DC36FDE&0&0000
    Name: Microsoft USB IntelliMouse Optical
    Driver installed from c:\windows\inf\msmouse.inf [HID_Mouse_Inst]. 2 file(s)
 used by driver:
        C:\WINDOWS\System32\DRIVERS\mouhid.sys
        C:\WINDOWS\System32\DRIVERS\mouclass.sys
1 matching device(s) found.
```

### Example 10: List driver packages by hardware ID pattern

The following command uses the **[DevCon DriverNodes](devcon-drivernodes.md)** command and an ID pattern to list the driver nodes of software-enumerated devices. Patterns are useful for finding information about similar devices that might not be in the same setup class.

The following command uses the ID pattern `sw*` to specify devices with hardware IDs or compatible IDs that begin with "sw" for  _software-enumerated_ devices.

```console
devcon drivernodes sw*
```

In response, DevCon displays the driver nodes of software-enumerated devices on the system:

```console
SW\{A7C7A5B0-5AF3-11D1-9CED-00A024BF0407}\{9B365890-165F-11D0-A195-0020AFD156E4}

 Name: Microsoft Kernel System Audio Device
DriverNode #0:
    Inf file is c:\windows\inf\wdmaudio.inf
    Inf section is WDM_SYSAUDIO
    Driver description is Microsoft Kernel System Audio Device
    Manufacturer name is Microsoft
    Provider name is Microsoft
    Driver date is 7/1/2001
    Driver version is 5.1.2535.0
    Driver node rank is 0
    Driver node flags are 00002244
        Inf is digitally signed
SW\{B7EAFDC0-A680-11D0-96D8-00AA0051E51D}\{9B365890-165F-11D0-A195-0020AFD156E4}

    Name: Microsoft Kernel Wave Audio Mixer
DriverNode #0:
    Inf file is c:\windows\inf\wdmaudio.inf
    Inf section is WDM_KMIXER
    Driver description is Microsoft Kernel Wave Audio Mixer
    Manufacturer name is Microsoft
    Provider name is Microsoft
    Driver date is 7/1/2001
    Driver version is 5.1.2535.0
    Driver node rank is 0
    Driver node flags are 00002244
        Inf is digitally signed
SW\{CD171DE3-69E5-11D2-B56D-0000F8754380}\{9B365890-165F-11D0-A195-0020AFD156E4}

    Name: Microsoft WINMM WDM Audio Compatibility Driver
DriverNode #0:
    Inf file is c:\windows\inf\wdmaudio.inf
    Inf section is WDM_WDMAUD
    Driver description is Microsoft WINMM WDM Audio Compatibility Driver
    Manufacturer name is Microsoft
    Provider name is Microsoft
    Driver date is 7/1/2001
    Driver version is 5.1.2535.0
    Driver node rank is 0
    Driver node flags are 00002244
        Inf is digitally signed
3 matching device(s) found.
```

### Example 11: List driver packages by device instance ID pattern

The following command uses the **[DevCon DriverNodes](devcon-drivernodes.md)** operation to list the driver packages of all devices with device instance IDs that begin with `ROOT\MEDIA` for devices in the _Enum\Root\Media_ registry subkey. The command uses the **at** symbol (`@`) to indicate that the phrase is in the device instance ID.

```console
devcon drivernodes @ROOT\MEDIA*
```

In response, DevCon displays the driver nodes of devices with a device instance ID that begins with `ROOT\MEDIA`:

```console
ROOT\MEDIA\MS_MMACM
    Name: Audio Codecs
DriverNode #0:
    Inf file is c:\windows\inf\wave.inf
    Inf section is MS_MMACM
    Driver description is Audio Codecs
    Manufacturer name is (Standard system devices)
    Provider name is Microsoft
    Driver date is 7/1/2001
    Driver version is 5.1.2535.0
    Driver node rank is 0
    Driver node flags are 00002240
        Inf is digitally signed
ROOT\MEDIA\MS_MMDRV
    Name: Legacy Audio Drivers
DriverNode #0:
    Inf file is c:\windows\inf\wave.inf
    Inf section is MS_MMDRV
    Driver description is Legacy Audio Drivers
    Manufacturer name is (Standard system devices)
    Provider name is Microsoft
    Driver date is 7/1/2001
    Driver version is 5.1.2535.0
    Driver node rank is 0
    Driver node flags are 00002240
        Inf is digitally signed
ROOT\MEDIA\MS_MMMCI
    Name: Media Control Devices
DriverNode #0:
    Inf file is c:\windows\inf\wave.inf
    Inf section is MS_MMMCI
    Driver description is Media Control Devices
    Manufacturer name is (Standard system devices)
    Provider name is Microsoft
    Driver date is 7/1/2001
    Driver version is 5.1.2535.0
    Driver node rank is 0
    Driver node flags are 00002240
        Inf is digitally signed
ROOT\MEDIA\MS_MMVCD
    Name: Legacy Video Capture Devices
DriverNode #0:
    Inf file is c:\windows\inf\wave.inf
    Inf section is MS_MMVCD
    Driver description is Legacy Video Capture Devices
    Manufacturer name is (Standard system devices)
    Provider name is Microsoft
    Driver date is 7/1/2001
    Driver version is 5.1.2535.0
    Driver node rank is 0
    Driver node flags are 00002240
        Inf is digitally signed
ROOT\MEDIA\MS_MMVID
    Name: Video Codecs
DriverNode #0:
    Inf file is c:\windows\inf\wave.inf
    Inf section is MS_MMVID
    Driver description is Video Codecs
    Manufacturer name is (Standard system devices)
    Provider name is Microsoft
    Driver date is 7/1/2001
    Driver version is 5.1.2535.0
    Driver node rank is 0
    Driver node flags are 00002240
        Inf is digitally signed
5 matching device(s) found.
```

### Example 12: List resources of a class of devices

The following command uses the **[DevCon Resources](devcon-resources.md)** operation to display the resources allocated to devices in the Hdc device setup class. This class includes IDE controllers. The syntax precedes the class name `hdc` with the equals symbol (`=`) to indicate that the specified value is a class and not an ID.

```console
devcon resources =hdc
```

In response, DevCon lists the resources allocated to IDE controllers on the local computer:

```console
PCI\VEN_8086&DEV_244B&SUBSYS_00000000&REV_02\3&29E81982&0&F9
    Name: Intel(r) 82801BA Bus Master IDE Controller
    Device is currently using the following resources:
        IO  : ffa0-ffaf
PCIIDE\IDECHANNEL\4&37E53584&0&0
    Name: Primary IDE Channel
    Device is currently using the following resources:
        IO  : 01f0-01f7
        IO  : 03f6-03f6
        IRQ : 14
PCIIDE\IDECHANNEL\4&37E53584&0&1
    Name: Secondary IDE Channel
    Device is currently using the following resources:
        IO  : 0170-0177
        IO  : 0376-0376
        IRQ : 15
3 matching device(s) found.
```

### Example 13: List resources of device by ID

The following command uses the **[DevCon Resources](devcon-resources.md)** operation to list the resources allocated to the system timer. The command uses the hardware ID of the system timer, `ACPI\PNP0100`, to specify the device.

```console
devcon resources *PNP0100
```

In response, DevCon displays the resources of the system timer:

```console
ROOT\*PNP0100\PNPBIOS_8
    Name: System timer
    Device has the following resources reserved:
        IO  : 0040-005f
        IRQ : 0
1 matching device(s) found.
```

The following command uses the device instance ID of the system timer in the DevCon `resources` command. The command uses the **at** symbol (`@`) to indicate that the string is a device instance ID and not a hardware ID or compatible ID.

```console
devcon resources "@ACPI\PNP0100\4&b4063f4&0"
```

### Example 14: Display the driver stack for storage devices

The following command uses the **[DevCon Stack](devcon-stack.md)** operation to search for devices in the Volume setup class and display the expected driver stack for those devices. The equals symbol (`=`) precedes the string to indicate that the value is a class and not an ID.

```console
devcon stack =Volume
```

In response, DevCon displays the expected stack for the devices in the Volume class. The returned data includes the following information:

- Device instance ID and description of each device
- GUID and name of the device setup class
- Names of upper and lower filter drivers
- Controlling services (if any)

```console
STORAGE\VOLUME\1&30A96598&0&SIGNATURE32323533OFFSET271167600LENGTH6E00D0C00
    Name: Generic volume
    Setup Class: {71A27CDD-812A-11D0-BEC7-08002BE2092F} Volume
    Class upper filters:
        VolSnap
    Controlling service:
        (none)
STORAGE\VOLUME\1&30A96598&0&SIGNATURE32323533OFFSET7E00LENGTH27115F800
    Name: Generic volume
    Setup Class: {71A27CDD-812A-11D0-BEC7-08002BE2092F} Volume
    Class upper filters:
        VolSnap
    Controlling service:
        (none)
2 matching device(s) found.
```

### Example 15: Find the setup class of a device

The **[DevCon Stack](devcon-stack.md)** operation returns the setup class of a device in addition to the upper and lower filter drivers. The following commands find the setup class of the printer port interface by locating its device instance ID and then using the device instance ID to find its setup class.

The following command uses the **[DevCon HwIDs](devcon-hwids.md)** operation to find the device instance ID of the printer port interface. It searches on the "LPT" phrase within the printer port hardware ID:

```console
devcon hwids *lpt*
```

In response, DevCon returns the device instance ID (displayed in bold text) and the hardware ID of the printer port interface:

```console
LPTENUM\MICROSOFTRAWPORT\5&CA97D7E&0&LPT1
    Name: Printer Port Logical Interface
    Hardware ID's:
        LPTENUM\MicrosoftRawPort958A
        MicrosoftRawPort958A
1 matching device(s) found.
```

The next command uses the **[DevCon Stack](devcon-stack.md)** operation to find the device setup class of the device represented by the device instance ID. The command uses the **at** symbol (`@`) to identify the ID as a device instance ID. The ID is enclosed in quotes (`" "`) because it includes the ampersand (`&`) symbol.

```console
devcon stack "@LPTENUM\MICROSOFTRAWPORT\5&CA97D7E&0&LPT1"
```

In response, DevCon displays the driver stack for the printer port interface, including the class. The display reveals that the printer port is in the System class:

```console
LPTENUM\MICROSOFTRAWPORT\5&CA97D7E&0&LPT1
    Name: Printer Port Logical Interface
    Setup Class: {4D36E97D-E325-11CE-BFC1-08002BE10318} System
    Controlling service:
        (none)
1 matching device(s) found.
```

### Example 16: Display the stack for related devices

The following command uses the **[DevCon Stack](devcon-stack.md)** operation to display the expected stack for miniport driver devices. It searches for devices in the Net setup class that have "miniport" in their hardware ID or compatible ID.

This command first limits the search to the Net setup class and then finds the "miniport" string. It doesn't find devices other than the items in the Net setup class.

```console
devcon stack =net *miniport*
```

In response, DevCon displays the expected stack for miniport drivers:

```console
ROOT\MS_L2TPMINIPORT\0000
    Name: WAN Miniport (L2TP)
    Setup Class: {4D36E972-E325-11CE-BFC1-08002BE10318} Net
    Controlling service:
        Rasl2tp
ROOT\MS_PPPOEMINIPORT\0000
    Name: WAN Miniport (PPPOE)
    Setup Class: {4D36E972-E325-11CE-BFC1-08002BE10318} Net
    Controlling service:
        RasPppoe
    Lower filters:
        NdisTapi
ROOT\MS_PPTPMINIPORT\0000
    Name: WAN Miniport (PPTP)
    Setup Class: {4D36E972-E325-11CE-BFC1-08002BE10318} Net
    Controlling service:
        PptpMiniport
    Lower filters:
        NdisTapi
ROOT\MS_PTIMINIPORT\0000
    Name: Direct Parallel
    Setup Class: {4D36E972-E325-11CE-BFC1-08002BE10318} Net
    Controlling service:
        Raspti
    Lower filters:
        PtiLink
4 matching device(s) found.
```

### Example 17: Display the status of all devices

The following command uses the **[DevCon Status](devcon-status.md)** operation to find the status of all devices on the local computer. It then saves the status in the *status.txt* file for logging or later review. The command uses the wildcard character (`*`) to represent all devices. It uses the redirection character (`>`) to save the command output in the specified file, *status.txt*.

```console
devcon status * > status.txt
```

### Example 18: Display the status of a device by device instance ID

The most reliable way to find the status of a particular device is to use the device instance ID of the device.

The following command uses the device instance ID of the I/O controller on the local computer in a **[DevCon Status](devcon-status.md)** command. The command includes the device instance ID of the device, `PCI\VEN_8086&DEV_1130&SUBSYS_00000000&REV_02\3&29E81982&0&00`. The command uses the **at** symbol (`@`) to identify the string as a device instance ID. The ID is enclosed in quotes (`" "`) because it includes the ampersand (`&`) symbol.

```console
devcon status "@PCI\VEN_8086&DEV_1130&SUBSYS_00000000&REV_02\3&29E81982&0&00"
```

In response, DevCon displays the status of the I/O controller:

```console
PCI\VEN_8086&DEV_1130&SUBSYS_00000000&REV_02\3&29E81982&0&00
    Name: Intel(R) 82815 Processor to I/O Controller - 1130
    Driver is running.
1 matching device(s) found.
```

### Example 19: Display the status of related devices

The following command uses the **[DevCon Status](devcon-status.md)** operation to display the status of particular storage-related devices. It searches for the following devices:

- Disk drive, `GenDisk`
- CD-ROM drive, `GenCdRom`
- Floppy disk drive, `FDC\GENERIC_FLOPPY_DRIVE`
- Volumes, `STORAGE\Volume`
- Logical disk manager, `ROOT\DMIO`
- Volume manager, `ROOT\FTDISK`
- Floppy disk controller, `ACPI\PNP0700`

In the command, each ID is separated from the others by spaces. Notice that `GenDisk` and `GenCdRom` are compatible IDs, whereas the other IDs are hardware IDs.

```console
devcon status GenDisk GenCdRom FDC\GENERIC_FLOPPY_DRIVE STORAGE\Volume ROOT\DMIO ROOT\FTDISK ACPI\PNP0700
```

In response, DevCon displays the status of each device:

```console
FDC\GENERIC_FLOPPY_DRIVE\1&3A2146F1&0&0
    Name: Floppy disk drive
    Driver is running.
IDE\CDROMSAMSUNG_DVD-ROM_SD-608__________________2.2_____\4&13B4AFD&0&0.0.0
    Name: SAMSUNG DVD-ROM SD-608
    Driver is running.
IDE\DISKWDC_WD204BA_____________________________16.13M16\4457572D414D373032313633393820312
0202020
    Name: WDC WD204BA
    Driver is running.
ROOT\DMIO\0000
    Name: Logical Disk Manager
    Driver is running.
ROOT\FLOPPYDISK\0000
    Device has a problem: 28.
ROOT\FLOPPYDISK\0002
    Device has a problem: 01.
ROOT\FLOPPYDISK\0003
    Device has a problem: 01.
ROOT\FLOPPYDISK\0004
    Device is currently stopped.
ROOT\FTDISK\0000
    Name: Volume Manager
    Driver is running.
STORAGE\VOLUME\1&30A96598&0&SIGNATUREEA1AA9C7OFFSET1770DF800LENGTH3494AEA00
    Name: Generic volume
    Driver is running.
STORAGE\VOLUME\1&30A96598&0&SIGNATUREEA1AA9C7OFFSET7E00LENGTH1770CFC00
    Name: Generic volume
    Driver is running.
11 matching device(s) found.
```

### Example 20: Find devices by hardware ID pattern

The following command uses the **[DevCon Find](devcon-find.md)** operation to search for mouse devices. Specifically, the command searches the computer for devices with hardware IDs or compatible IDs that include the phrase "mou":

```console
devcon find *mou*
```

In response, DevCon discovers two mouse devices:

```console
ROOT\*PNP0F03\1_0_21_0_31_0                                 : Microsoft PS/2 Mouse
ROOT\RDP_MOU\0000                                           : Terminal Server Mouse Driver
```

Because all DevCon display operations also find hardware IDs, you can use any display operation to search for hardware IDs. Select the operation based on the content that you need in the output. For example, to find the device drivers for mouse-related devices on a local computer, submit the following command:

```console
devcon driverfiles *mou*
```

In response, DevCon finds the devices and lists their drivers:

```console
HID\VID_045E&PID_0039\6&DC36FDE&0&0000
    Name: Microsoft USB IntelliMouse Optical
    Driver installed from c:\windows\inf\msmouse.inf [HID_Mouse_Inst]. 2 file(s) used by d
river:
        C:\WINDOWS\System32\DRIVERS\mouhid.sys
        C:\WINDOWS\System32\DRIVERS\mouclass.sys
ROOT\RDP_MOU\0000
    Name: Terminal Server Mouse Driver
    Driver installed from c:\windows\inf\machine.inf [RDP_MOU]. 2 file(s) used by driver:
        C:\WINDOWS\System32\DRIVERS\termdd.sys
        C:\WINDOWS\System32\DRIVERS\mouclass.sys
2 matching device(s) found.
```

### Example 21: Find devices by device instance ID or class

The following commands use the **[DevCon Find](devcon-find.md)** operation to display all legacy devices on the local computer. Because legacy devices don't have a hardware ID, you must search for them by their device instance ID (registry path), `ROOT\LEGACY`, or their setup class, `LegacyDriver`.

The first command finds legacy drivers by a device instance ID pattern. The **at** symbol (`@`) precedes the ID pattern to indicate that the value is a device instance ID. The value is followed by the wildcard character (`*`) to instruct the command to find all devices in the specified ID, the _ROOT\Legacy_ subkey:

```console
devcon find @root\legacy*
```

The second command finds legacy devices by searching for all devices in the LegacyDriver class:

```console
devcon find =legacydriver
```

Both commands produce the same output, in this case, finding the same 27 legacy devices:

```console
ROOT\LEGACY_AFD\0000                                        : AFD Networking Support Environment
ROOT\LEGACY_BEEP\0000                                       : Beep
ROOT\LEGACY_DMBOOT\0000                                     : dmboot
ROOT\LEGACY_DMLOAD\0000                                     : dmload
ROOT\LEGACY_FIPS\0000                                       : Fips
ROOT\LEGACY_GPC\0000                                        : Generic Packet Classifier
ROOT\LEGACY_IPSEC\0000                                      : ipsec
ROOT\LEGACY_KSECDD\0000                                     : ksecdd
ROOT\LEGACY_MNMDD\0000                                      : mnmdd
ROOT\LEGACY_MOUNTMGR\0000                                   : mountmgr
ROOT\LEGACY_NDIS\0000                                       : ndis
ROOT\LEGACY_NDISTAPI\0000                                   : Remote Access NDIS TAPI Driver
ROOT\LEGACY_NDISUIO\0000                                    : NDIS Usermode I/O Protocol
ROOT\LEGACY_NDPROXY\0000                                    : NDProxy
ROOT\LEGACY_NETBT\0000                                      : netbt
ROOT\LEGACY_NULL\0000                                       : Null
ROOT\LEGACY_PARTMGR\0000                                    : PartMgr
ROOT\LEGACY_PARVDM\0000                                     : ParVdm
ROOT\LEGACY_RASACD\0000                                     : Remote Access Auto Connection Driver
ROOT\LEGACY_RDPCDD\0000                                     : RDPCDD
ROOT\LEGACY_RDPWD\0000                                      : RDPWD
ROOT\LEGACY_TCPIP\0000                                      : tcpip
ROOT\LEGACY_TDPIPE\0000                                     : TDPIPE
ROOT\LEGACY_TDTCP\0000                                      : TDTCP
ROOT\LEGACY_VGASAVE\0000                                    : VgaSave
ROOT\LEGACY_VOLSNAP\0000                                    : VolSnap
ROOT\LEGACY_WANARP\0000                                     : Remote Access IP ARP Driver
27 matching device(s) found.
```

### Example 22: Find (and find all) devices in a setup class

The following command uses the **[DevCon FindAll](devcon-findall.md)** operation to find all devices on the computer in the Net setup class. The equals symbol (`=`) precedes the class name "Net" to indicate that the specified value is a class and not an ID.

```console
devcon findall =net
```

In response, DevCon lists the following seven devices in the Net setup class. The first six are standard miniport driver devices. The seventh device, the RAS async adapter, is a software-enumerated device (`SW\*`) installed only as needed.

```console
PCI\VEN_10B7&DEV_9200&SUBSYS_00BE1028&REV_78\4&BB7B4AE&0&60F0: 3Com 3C920 Integrated Fast
Ethernet Controller (3C905C-TX Compatible)
ROOT\MS_L2TPMINIPORT\0000                                   : WAN Miniport (L2TP)
ROOT\MS_NDISWANIP\0000                                      : WAN Miniport (IP)
ROOT\MS_PPPOEMINIPORT\0000                                  : WAN Miniport (PPPOE)
ROOT\MS_PPTPMINIPORT\0000                                   : WAN Miniport (PPTP)
ROOT\MS_PTIMINIPORT\0000                                    : Direct Parallel
SW\{EEAB7790-C514-11D1-B42B-00805FC1270E}\ASYNCMAC          : RAS Async Adapter
7 matching device(s) found.
```

The following command compares the output from the **[DevCon Find](devcon-find.md)** and **DevCon FindAll** operations by running a **DevCon Find** command with the same parameters as the previous **DevCon FindAll** command:

```console
devcon find =net
```

In response, DevCon lists the following six devices in the Net setup class:

```console
PCI\VEN_10B7&DEV_9200&SUBSYS_00BE1028&REV_78\4&BB7B4AE&0&60F0: 3Com 3C920 Integrated Fast
Ethernet Controller (3C905C-TX Compatible)
ROOT\MS_L2TPMINIPORT\0000                                   : WAN Miniport (L2TP)
ROOT\MS_NDISWANIP\0000                                      : WAN Miniport (IP)
ROOT\MS_PPPOEMINIPORT\0000                                  : WAN Miniport (PPPOE)
ROOT\MS_PPTPMINIPORT\0000                                   : WAN Miniport (PPTP)
ROOT\MS_PTIMINIPORT\0000                                    : Direct Parallel
6 matching device(s) found.
```

Predictably, the **DevCon Find** command, which returns only currently installed devices, doesn't list the software-enumerated device because the device isn't installed.

### Example 23: Display the filter drivers for a setup class

The following command uses the **[DevCon ClassFilter](devcon-classfilter.md)** operation to display the upper filter drivers for the DiskDrive setup class. Because this command includes no classfilter operators, DevCon displays the filter drivers for the class, but doesn't change them.

```console
devcon classfilter DiskDrive upper
```

In response, DevCon displays the upper filter drivers for the DiskDrive class and confirms the filter drivers aren't changed. In this case, the display shows that devices in the DiskDrive setup class use the *PartMgr.sys* upper filter driver:

```console
Class filters unchanged.
    PartMgr
```

### Example 24: Add a filter driver to a setup class

The following command uses the **[DevCon ClassFilter](devcon-classfilter.md)** operation to add a fictitious filter, *Disklog.sys*, to the list of upper filter drivers for the DiskDrive setup class.

This command uses the add-after (`+`, the plus symbol) ClassFilter operator to load the Disklog driver after the PartMgr driver so it receives data that *PartMgr.sys* already processed.

When the command starts, the virtual cursor is positioned before the first filter driver. Because it isn't positioned on a particular driver, DevCon adds the Disklog driver to the end of the filter driver list.

The command also uses the `/r` parameter, which reboots the system as necessary to make the class filter change effective.

```console
devcon /r classfilter DiskDrive upper +Disklog
```

In response, DevCon displays the current upper filter drivers for the DiskDrive class:

```console
Class filters changed. Class devices must be restarted for changes to take effect.
    PartMgr
    Disklog
```

If you misspell the driver name, or try to add a driver that isn't installed on the system, the command fails. DevCon doesn't add a driver unless the driver is registered as a service. That is, DevCon only adds the driver if it has a subkey in the Services registry _HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services_ subkey.

The following command tests this safeguard feature. It attempts to add "Disklgg" (instead of "Disklog") to the list of upper filters for the DiskDrive class. The output demonstrates that the command fails:

```console
devcon /r classfilter DiskDrive upper +Disklgg
devcon failed.
```

### Example 25: Insert a filter driver in the class list

The following command uses the **[DevCon ClassFilter](devcon-classfilter.md)** operation to add a fictitious filter driver, *MyFilter.sys*, to the list of upper filter drivers for the DiskDrive setup class. The command places *MyFilter.sys* between *PartMgr.sys* and *Disklog.sys* in the load order:

```console
devcon /r classfilter DiskDrive upper @Disklog -MyFilter
```

The following list shows the filter drivers for the DiskDrive class before the command is submitted:

```console
    PartMgr
    Disklog
```

The first subcommand, `@Disklog`, uses the positioning operator (`@`, the **at** symbol) to place the virtual cursor on the Disklog filter driver. The second subcommand, `-MyFilter`, uses the add-before operator (`-`, the minus symbol) to add *MyFilter.sys* before *Disklog.sys*.

The command also uses the `/r` parameter, which reboots the system as necessary to make the class filter change effective.

The positioning operator is essential in this example. Before DevCon processes any classfilter subcommands, the virtual cursor is at the beginning of the list and isn't positioned on any filter drivers. If you use the add-before (`+`) operator when the cursor isn't positioned on a driver, DevCon adds the driver to the beginning of the list. If you use the add-after (`-`) operator when the cursor isn't positioned on a driver, it adds the driver to the end of the list.

In response, DevCon displays the current upper filter drivers for the DiskDrive class:

```console
Class filters changed. Class devices must be restarted for changes to take effect.
    PartMgr
    MyFilter
    Disklog
```

You can also use the following command to add the MyFilter driver and place it between PartMgr and Disklog. In this example, the first subcommand, `@PartMgr`, positions the virtual cursor on the PartMgr filter driver. The second subcommand, `+MyFilter`, uses the add-after operator (`+`) to add *MyFilter.sys* after PartMgr:

```console
devcon /r classfilter DiskDrive upper @PartMgr +MyFilter
```

### Example 26: Replace a filter driver

The following command uses the **[DevCon ClassFilter](devcon-classfilter.md)** operation to replace the original copy of *MyFilter.sys* with a new and improved version, *MyNewFilter.sys*, in the list of filter drivers for the DiskDrive setup class:

```console
devcon /r classfilter DiskDrive upper !MyFilter +MyNewFilter
```

The following list shows the filter drivers for the DiskDrive class before the command is submitted:

```console
    PartMgr
    MyFilter
    Disklog
```

The first subcommand uses the delete operator (`!`, the exclamation mark) to delete MyFilter from the list of upper filter drivers for the DiskDrive class. (It doesn't affect the *MyFilter.sys* file in the _C:\Windows\System32\Drivers directory_ location.)

The second subcommand uses the add-after operator (`+`) to place the new filter driver in the position previously occupied by the deleted driver. Because the delete operator leaves the cursor in the position that the deleted filter occupied, the add-before (`-`) and add-after (`+`) operators have the same effect.

The command also uses the `/r` parameter, which reboots the system as necessary to make the class filter change effective.

In response, DevCon shows the new class filter configuration for the DiskDrive class:

```console
Class filters changed. Class devices must be restarted for changes to take effect.
    PartMgr
    MyNewFilter
    Disklog
```

### Example 27: Change the order of filter drivers

The following command uses the **[DevCon ClassFilter](devcon-classfilter.md)** operation to change the order of filter drivers for the DiskDrive setup class. Specifically, it reverses the order of the second and third filter drivers.

```console
devcon /r classfilter DiskDrive upper !Disklog =@PartMgr +Disklog
```

The following list shows the filter drivers for the DiskDrive class before the command is submitted. It also shows the intended result of the command.

| Before | After |
|--|--|
| PartMgr | PartMgr |
| MyNewFilter | Disklog |
| Disklog | MyNewFilter |

The first subcommand uses the delete operator (`!`) to delete Disklog from the list. The second subcommand uses the start operator (`=`, the equals symbol) to move the virtual cursor back to the starting position and the positioning operator (`@`, the **at** symbol) to place the cursor on the PartMgr driver. The start operator is necessary because the virtual cursor moves only forward through the list. The final subcommand uses the add-after operator (`+`) to add Disklog after PartMgr.

In response, DevCon shows the new class filter configuration for the DiskDrive class:

```console
Class filters changed. Class devices must be restarted for changes to take effect.
    PartMgr
    Disklog
    MyNewFilter
```

### Example 28: Enable a particular device

The following command uses the **[DevCon Enable](devcon-enable.md)** operation to enable a previously disabled programmable interrupt controller. The controlled is disabled and then reenabled to correct a system problem. Because the controller hardware ID in this example includes an asterisk (`*PNP0000`), the command uses the single quote character (`'`) to direct DevCon to find the hardware ID precisely as specified in the command. If the command didn't use the quote character (`'`) in this instance, DevCon interprets the asterisk (`*`) in the value as a wildcard character.

```console
devcon enable '*PNP0000
```

In response, DevCon displays the device instance ID of the device and explains that you must reboot the system to enable the device:

```console
ACPI\PNP0000\4&B4063F4&0                                    : Enabled on reboot
Not all of 1 device(s) enabled, at least one requires reboot to complete the operation.
```

You can respond by rebooting the system manually, or by using the **[DevCon Reboot](devcon-reboot.md)** operation.

The following command adds the `/r` parameter to the previous command. The `/r` parameter reboots the system as necessary to complete an operation.

```console
devcon /r enable '*PNP0000
```

In response, DevCon enables the device and then reboots the system to make the enable operation effective.

When the system starts, use a DevCon `status` command to confirm that the device is enabled:

```console
devcon status '*PNP0000

ACPI\PNP0000\4&B4063F4&0
    Name: Programmable interrupt controller
    Driver is running.
```

### Example 29: Enable devices by class

The following command enables all printer devices on the computer by specifying the Printer setup class in a **[DevCon Enable](devcon-enable.md)** command. The command includes the `/r` parameter, which reboots the system as necessary to make the enable operation effective.

```console
devcon /r enable =Printer
```

In response, DevCon displays the device instance ID of the printer that it found in the Printer class and reports that the printer is enabled. Although the command includes the `/r` parameter, the system doesn't reboot because a reboot isn't required to enable the printer.

```console
LPTENUM\HEWLETT-PACKARDDESKJET_1120C\1&7530F08&0&LPT1.4        : Enabled
1 device(s) enabled.
```

### Example 30: Disable devices by an ID pattern

The following command uses the **[DevCon Disable](devcon-disable.md)** operation to disable the USB devices on the local computer. It identifies the devices by a hardware ID pattern (`USB*`). This pattern matches any device with a hardware ID or compatible ID that begins with "USB." The command includes the `/r` parameter, which reboots the system as necessary to make the disable operation effective.

> [!NOTE]
> Before you use an ID pattern to disable a device, determine which devices might be affected. Use the pattern in a display command, such as `devcon status USB*` or `devcon hwids USB*`.

```console
devcon /r disable USB*
```

In response, DevCon displays the device instance IDs of the USB devices and reports they're disabled. Although the command includes the `/r` parameter, the system doesn't reboot because a reboot isn't required to disable the devices.

```console
USB\ROOT_HUB\4&2A40B465&0
: Disabled
USB\ROOT_HUB\4&7EFA360&0
: Disabled
USB\VID_045E&PID_0039\5&29F428A4&0&2
: Disabled
3 device(s) disabled.
```

### Example 31: Disable devices by device instance ID

The following command uses the **[DevCon Disable](devcon-disable.md)** operation to disable the USB devices on the local computer. The command uses the **at** symbol (`@`) to identify the devices by their device instance IDs. Each device instance ID is separated from the others by a space.

When the device ID includes the ampersand (`&`) symbol, the value is enclosed in quotes (`" "`). The command includes the `/r` parameter, which reboots the system as necessary to make the disable operation effective.

```console
devcon /r disable "@USB\ROOT_HUB\4&2A40B465&0" "@USB\ROOT_HUB\4&7EFA360&0" "@USB\VID_045E&PID_0039\5&29F428A4&0&2"
```

In response, DevCon displays the device instance IDs of the USB devices and reports they're disabled. Although the command includes the `/r` parameter, the system doesn't reboot because a reboot isn't required to disable the devices.

```console
USB\ROOT_HUB\4&2A40B465&0
: Disabled
USB\ROOT_HUB\4&7EFA360&0
: Disabled
USB\VID_045E&PID_0039\5&29F428A4&0&2
: Disabled
3 device(s) disabled.
```

### Example 32: Update the driver for communication ports

The following command uses the **[DevCon Update](devcon-update.md)** operation to replace the current device driver for communication ports on the system with a test driver specified in the *test.inf* file. The command affects only devices whose entire hardware ID is `*PNP0501` (including the asterisk `*`).

You can use this command to replace signed drivers on the system with alternate drivers for testing or troubleshooting, or to associate the devices with the newest version of the same drivers.

```console
devcon update c:\windows\inf\test.inf *PNP0501
```

In response, DevCon displays a **Hardware Installation** warning explaining that the driver didn't pass Windows Logo testing. If you select the **Continue Anyway** option on the dialog, the installation continues.

Then, DevCon displays the following success message:

```console
Updating drivers for *PNP0501 from c:\windows\inf\test.inf.
Drivers updated successfully.
```

You can also use the **[DevCon UpdateNI](devcon-updateni.md)** operation, the noninteractive version of the **DevCon Update** operation, to update drivers. The **DevCon UpdateNI** operation is identical to the **DevCon Update** operation except it suppresses all user prompts that require a response and assumes the default response to the prompt.

The following command uses the **DevCon UpdateNI** operation to install the test driver:

```console
devcon updateni c:\windows\inf\test.inf *PNP0501
```

In this case, DevCon doesn't display the **Hardware Installation** warning. Instead, it assumes the default response, **Stop Installation**. As a result, DevCon can't update the drivers and displays a failure message:

```console
Updating drivers for *PNP0501 from c:\windows\inf\test.inf.
devcon failed.
```

### Example 33: Install a device

The following command uses the **[DevCon Install](devcon-install.md)** operation to install a keyboard device on the local computer. The command includes the full path to the setup information (INF) file *keyboard.inf* for the device and a hardware ID `*PNP030b`:

```console
devcon /r install c:\windows\inf\keyboard.inf *PNP030b
```

In response, DevCon reports it installed the device. That is, DevCon creates a device node for the new device and updates the driver files for the device.

```console
Device node created. Install is complete when drivers files are updated...
Updating drivers for *PNPO30b from c:\windows\inf\keyboard.inf
Drivers updated successfully.
```

### Example 34: Install a device by using unattended setup

The following example shows how to install the Microsoft Loopback Adapter during an unattended installation of Microsoft Windows XP.

To install this device during an unattended setup, begin by adding the following files to a floppy disk: *devcon.exe* and *netloop.inf* (*C:\Windows\inf\netloop.inf*).

Then add the following DevCon command in the `[GUIRunOnce]` section of the unattended setup file:

```console
a:\devcon /r install a:\Netloop.inf '*MSLOOP
```

This command identifies the loopback adapter by using its hardware ID, `*MSLOOP`. The single quote character (`'`) that precedes the value `\*MSLOOP` informs DevCon to interpret the string literally. As a result, DevCon interprets the asterisk (`*`) as part of the hardware ID and not as a wildcard character.

The command also specifies that DevCon use the *Netloop.inf* file (on the floppy disk) in the installation. The `/r` parameter reboots the computer as necessary to complete the installation.

Finally, add network configuration settings to the unattended setup file and run the unattended setup.

### Example 35: Remove devices by device instance ID pattern

The following command uses the **[DevCon Remove](devcon-remove.md)** operation to remove all USB devices from the computer. It identifies the devices by a device instance ID pattern that matches any device instance ID (registry path) that begins with the "USB\" string. The command uses the **at** symbol (`@`) to distinguish the device instance ID from a hardware ID or compatible ID. The command also includes the `/r` parameter that reboots the system as necessary to make the removal effective.

> [!WARNING]
> Before you use an ID pattern to remove a device, determine which devices might be affected. Use the pattern in a display command, such as `devcon status @usb\*` or `devcon hwids @usb\*`.

```console
devcon /r remove @usb\*
```

In response, DevCon displays the device instance ID of the removed devices:

```console
USB\ROOT_HUB\4&2A40B465&0                             : Removed
USB\ROOT_HUB\4&7EFA360&0                              : Removed
USB\VID_045E&PID_0039\5&29F428A4&0&2                  : Removed
3 device(s) removed.
```

### Example 36: Remove a particular network device

The following command uses the **[DevCon Remove](devcon-remove.md)** operation to uninstall the NDISWAN miniport driver from the local computer. The command specifies the Net class and then refines the search by specifying devices in the class whose hardware ID or compatible ID include "ndiswan." The command also includes the `/r` parameter, which reboots the system as necessary to make the removal effective.

> [!WARNING]
> Before you use an ID pattern to remove a device, determine which devices might be affected. Use the pattern in a display command, such as `devcon status =net *ndiswan` or `devcon hwids =net *ndiswan*`.

```console
devcon /r remove =net *ndiswan*
```

In response, DevCon displays the device instance ID of the removed device:

```console
ROOT\MS_NDISWANIP\0000 : Removed 1 device(s) removed.
```

### Example 37: Scan the computer for new devices

The following command uses the **[DevCon Rescan](devcon-rescan.md)** operation to scan the local computer for new devices.

```console
devcon rescan
```

In response, DevCon reports that it scanned the system but found no new devices:

```console
Scanning for new hardware.
Scanning completed.
```

### Example 38: Restart a device

The following command uses the **[DevCon Restart](devcon-restart.md)** operation to restart the loopback adapter on the local computer. The command limits the search to the Net setup class and, within that class, specifies the device instance ID of the loopback adapter, `@'ROOT\*MSLOOP\0000`. 

The **at** symbol (`@`) identifies the string value as a device instance ID. The single quote character (`'`) informs DevCon to interpret the string literally. As a result, DevCon interprets the asterisk (`*`) as part of the ID and not as a wildcard character.

```console
devcon restart =net @'ROOT\*MSLOOP\0000
```

In response, DevCon displays the device instance ID of the device and reports the result:

```console
ROOT\*MSLOOP\0000                                              : Restarted
1 device(s) restarted.
```

### Example 39: Reboot the local computer

The following command uses the **[DevCon Reboot](devcon-reboot.md)** operation to reboot the operating system on the local computer and to associate the reboot with a hardware installation. Unlike the `/r` parameter, the **DevCon Reboot** operation doesn't depend on the return code from another operation.

You can include this command in scripts and batch files that require the system to reboot.

```console
devcon reboot
```

In response, DevCon displays a message indicating that it's restarting the computer (_Rebooting local machine_).

DevCon uses the standard **ExitWindowsEx** function to reboot. If the user has open files on the computer or a program doesn't close, the system doesn't reboot. It waits until the user responds to system prompts to close the files or end the process.

### Example 40: Assign a hardware ID to a legacy device

The following command uses the **[DevCon SetHwID](devcon-sethwid.md)** operation to assign the hardware ID `beep` to the legacy beep device.

The command uses the device instance ID of the device `ROOT\LEGACY_BEEP\0000` because the beep legacy device has no hardware IDs or compatible IDs. The command uses the **at** symbol (`@`) to indicate that the string is a device instance ID.

The command doesn't use any symbol parameters to position the ID. By default, DevCon adds new hardware IDs to the end of a hardware ID list. In this case, because the device has no other hardware IDs, the ID placement is irrelevant.

```console
devcon sethwid @ROOT\LEGACY_BEEP\0000 := beep
```

In response, DevCon displays a message indicating that it added `beep` to the hardware ID list for the device. It also displays the resulting hardware ID list. In this case, only one hardware ID is in the list:

```console
ROOT\LEGACY_BEEP\0000                              : beep
Modified 1 hardware ID(s).
```

### Example 41: Add a hardware ID to all legacy devices

The following command uses the **[DevCon SetHwID](devcon-sethwid.md)** operation to add the hardware ID, legacy, to the list of hardware IDs for all legacy devices.

The command uses the minus symbol (`-`) parameter to add the new hardware ID to the end of the hardware ID list for the device, in case a preferred hardware ID exists for one of the devices. It also uses a device instance ID pattern, `@ROOT\LEGACY*`, to identify the legacy devices on the computer, that is, all devices that have a device instance ID that begins with `ROOT\LEGACY*`.

```console
devcon sethwid @ROOT\LEGACY* := -legacy
```

In response, DevCon displays the resulting hardware ID lists for all affected devices:

```console
ROOT\LEGACY_AFD\0000                                        : legacy
ROOT\LEGACY_BEEP\0000                                    : beep,legacy
ROOT\LEGACY_CRCDISK\0000                                    : legacy
ROOT\LEGACY_DMBOOT\0000                                     : legacy
ROOT\LEGACY_DMLOAD\0000                                     : legacy
ROOT\LEGACY_FIPS\0000                                       : legacy
...
ROOT\LEGACY_WANARP\0000                                     : legacy
Modified 27 hardware ID(s).
```

After you assign the same hardware ID to a group of devices, you can use the other DevCon operations to view and change the devices in a single command.

For example, the following command displays the status of all legacy devices:

```console
devcon status legacy
```

### Example 42: Delete a hardware ID from all legacy devices

The following command uses the **[DevCon SetHwID](devcon-sethwid.md)** operation to delete the hardware ID `legacy` from the list of hardware IDs for all legacy devices.

The command uses the hardware ID `legacy` to identify all devices that have that hardware ID. It uses the delete operator (`!`) to delete the `legacy` hardware ID.

```console
devcon sethwid legacy := !legacy
```

In response, DevCon displays the resulting hardware ID lists for all affected devices:

```console
ROOT\LEGACY_AFD\0000                                        :
ROOT\LEGACY_BEEP\0000                                    : beep
ROOT\LEGACY_CRCDISK\0000                                    :
ROOT\LEGACY_DMBOOT\0000                                     :
ROOT\LEGACY_DMLOAD\0000                                     :
ROOT\LEGACY_FIPS\0000                                       :
...
ROOT\LEGACY_WANARP\0000                                     :
Modified 27 hardware ID(s).
```

### Example 43: Add, delete, and replace hardware IDs

The following examples show how to use the various features of the **[DevCon SetHwID](devcon-sethwid.md)** operation.

This series of examples uses a fictitious device, **DeviceX**, with the device instance ID, `ROOT\DeviceX\0000`. Before DevCon commands run for the device, the device has the following list of hardware IDs:

```console
Hw3 Hw4
```

The following command uses the plus symbol (`+`) to add the ID values `Hw1` and `Hw2` to the beginning of a list of hardware IDs for DeviceX. Because the `Hw2` ID already appears in the list, the ID value is moved, not added. The command uses the **at** symbol (`@`) to identify the device by its device instance ID.

```console
devcon sethwid @ROOT\DEVICEX\0000 := +Hw1 Hw2
```

In response, DevCon displays the new hardware ID list for the device. The `Hw1` and `Hw2` ID values appear at the beginning of the ID list in the specified order:

```console
ROOT\DEVICEX\0000                         : Hw1,Hw2,Hw3,Hw4
Modified 1 hardware ID(s).
```

Also, DevCon reports that it modified one hardware ID list, that is, the hardware ID list of a single device.

The following command uses the delete operator (`!`) to delete the `Hw1` hardware ID. It then lists the hardware ID `Hw5` without a symbol parameter. Without symbol parameters, **SetHwID** adds the hardware ID to the end of the hardware ID list for the device.

This command demonstrates that unlike the other symbol parameters for the **DevCon SetHwID** operation, the delete operator (`!`) applies only to the hardware ID that it prefixes.

```console
devcon sethwid @ROOT\DeviceX\0000 := !Hw1 Hw5
```

In response, DevCon displays the resulting hardware ID list for DeviceX:

```console
ROOT\DEVICEX\0000                         : Hw2,Hw3,Hw4,Hw5
Modified 1 hardware ID(s).
```

The following command uses the equals (`=`) parameter to replace all hardware IDs in the list for DeviceX with a single hardware ID, `DevX`.

```console
devcon sethwid @ROOT\DeviceX\0000 := =DevX
```

In response, DevCon displays the resulting hardware ID list for DeviceX:

```console
ROOT\DEVICEX\0000                         : DevX
Modified 1 hardware ID(s).
```

The success message indicates that DevCon modified the hardware ID of one device.

### Example 44: Forcibly update the HAL

The following example shows how to use DevCon to update the HAL on the computer. The current HAL is a uniprocessor (`_up`) built with the [Advanced Configuration and Power Interface (ACPI)](../acpi/index.md) and the [Advanced Programmable Interrupt Controller (APIC)](https://en.wikipedia.org/wiki/Advanced_Programmable_Interrupt_Controller), as appropriate for the computer. A tester wants to change the type to a multiprocessor (`_mp`) ACPI APIC HAL for testing purposes.

The first command uses the **[DevCon SetHwID](devcon-sethwid.md)** operation to change the hardware ID of the HAL from `acpiapic_up`, the hardware ID for uniprocessor HALs, to `acpiapic_mp`, the hardware ID for multiprocessor HALs.

You must change the hardware ID because the INF file (*.inf*) for the HAL includes drivers for both uniprocessor and multiprocessor HALs. The system selects the most appropriate driver from the INF file (*.inf*) based on the hardware ID of the device. If you don't change the hardware ID, the **DevCon Update** command reinstalls the same uniprocessor HAL driver.

In the following example, the command identifies the HAL by its instance ID, `ROOT\ACPI_HAL\0000`, as indicated by the **at** symbol (`@`) preceding the ID. The command uses the plus symbol (`+`) to specify `acpiapic_mp` as the first hardware ID in the list for the HAL. The command uses the delete operator (`!`) to delete the `acpiapic_up` hardware ID from the list of IDs for the HAL.

```console
devcon sethwid @ROOT\ACPI_HAL\0000 := +acpiapic_mp !acpiapic_up
```

In response, DevCon displays the following new hardware ID list for the HAL:

```console
ROOT\ACPI_HAL\0000                         : acpiapic_mp
Modified 1 hardware ID(s).
```

The following command uses the **[DevCon Update](devcon-update.md)** operation to update the driver for the HAL:

```console
devcon update c:\windows\inf\hal.inf acpiapic_mp
```

Then, DevCon displays the following success message:

```console
Updating drivers for acpiapic_mp from c:\windows\inf\hal.inf.
Drivers updated successfully.
```

### Example 45: Add and remove driver packages

The following examples show how to use DevCon to add, delete, and display third-party (OEM) driver packages in the driver store.

The first command, a **[DevCon Dp_add](devcon-dp-add.md)** operation, copies the INF file (*.inf*) for the Toaster sample driver in the Windows Driver Kit (WDK) to the driver store, that is, to the _%Windir%\inf_ directory. The command includes the fully qualified path to the INF file for the Toaster sample driver.

This command is intended for third-party (OEM) drivers and devices, but you can use the Toaster sample to test the commands.

```console
devcon dp_add C:\WinDDK\5322\src\general\toaster\inf\i386\toaster.inf
```

In response, DevCon reports that it added the Toaster INF file to the driver store and named it *Oem2.inf*:

```console
Driver Package 'oem2.inf' added.
```

Before the INF file is copied to the driver store, Windows compares the binary version of the file to the similar files in the driver store. It checks to confirm there are no binary files with the same INF name. For example, if you repeat the command to add the *Toaster.inf* file to the driver store, DevCon doesn't create a new _OEM*.inf_ file. It only reports the name of the existing file, as shown in the following DevCon output:

```console
devcon dp_add C:\WinDDK\5322\src\general\toaster\inf\i386\toaster.inf
Driver Package 'oem2.inf' added.

devcon dp_add C:\WinDDK\5322\src\general\toaster\inf\i386\toaster.inf
Driver Package 'oem2.inf' added.
```

To remove the driver package for the Toaster driver from the driver store, you must use the _OEM*.inf_ file name for the driver. To find the file name for the driver, use the **[DevCon Dp_enum](devcon-dp-enum.md)** operation.

The following command lists all of the OEM driver packages and a few of their properties:

```console
devcon dp_enum
```

In response, DevCon generates the following output:

```console
c:\WinDDK\5322\tools\devcon\i386>devcon dp_enum
The following 3rd party Driver Packages are on this machine:
oem2.inf
    Provider: Microsoft
    Class: unknown
```

The output indicates that the driver package supplied by Microsoft with the unspecified device class (Toaster) is named *OEM2.inf*. You can use this information to delete the driver package associated with the file.

The following command deletes the *OEM2.inf* file from the driver store, along with its associated precompiled INF (*.pnf*) and catalog (*.cat*) files. The command uses the *OEM2.inf* file name:

```console
devcon dp_delete oem2.inf
```

In response, DevCon displays a message that indicates the command success:

```console
Driver Package 'oem2.inf' deleted.
```

The *OEM*.inf* file name is required in the **[DevCon Dp_delete](devcon-dp-delete.md)** operation. If you try to use the original name of the INF file, the command fails, as shown in the following DevCon output:

```console
devcon dp_delete C:\WinDDK\5322\src\general\toaster.inf
Deleting the specified Driver Package from the machine failed.
devcon failed.
```
