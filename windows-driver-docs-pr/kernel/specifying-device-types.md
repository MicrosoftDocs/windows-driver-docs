---
title: Specifying Device Types
description: Provides information about specifying device types.
keywords: ["device objects WDK kernel , device types", "device types WDK device objects"]
ms.date: 02/21/2025
---

# Specifying device types

Each device object has a *device type*, which is stored in the **DeviceType** member of its [**DEVICE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) structure. The device type represents the type of underlying hardware for the driver.

Every kernel-mode driver that creates a device object must specify an appropriate device type value when calling [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice). The **IoCreateDevice** routine uses the supplied device type to initialize the **DeviceType** member of the **DEVICE_OBJECT** structure.

The system defines the following device type values, listed in alphabetical order:

```cpp
#define FILE_DEVICE_BEEP                    0x00000001
#define FILE_DEVICE_CD_ROM                  0x00000002
#define FILE_DEVICE_CD_ROM_FILE_SYSTEM      0x00000003
#define FILE_DEVICE_CONTROLLER              0x00000004
#define FILE_DEVICE_DATALINK                0x00000005
#define FILE_DEVICE_DFS                     0x00000006
#define FILE_DEVICE_DISK                    0x00000007
#define FILE_DEVICE_DISK_FILE_SYSTEM        0x00000008
#define FILE_DEVICE_FILE_SYSTEM             0x00000009
#define FILE_DEVICE_INPORT_PORT             0x0000000a
#define FILE_DEVICE_KEYBOARD                0x0000000b
#define FILE_DEVICE_MAILSLOT                0x0000000c
#define FILE_DEVICE_MIDI_IN                 0x0000000d
#define FILE_DEVICE_MIDI_OUT                0x0000000e
#define FILE_DEVICE_MOUSE                   0x0000000f
#define FILE_DEVICE_MULTI_UNC_PROVIDER      0x00000010
#define FILE_DEVICE_NAMED_PIPE              0x00000011
#define FILE_DEVICE_NETWORK                 0x00000012
#define FILE_DEVICE_NETWORK_BROWSER         0x00000013
#define FILE_DEVICE_NETWORK_FILE_SYSTEM     0x00000014
#define FILE_DEVICE_NULL                    0x00000015
#define FILE_DEVICE_PARALLEL_PORT           0x00000016
#define FILE_DEVICE_PHYSICAL_NETCARD        0x00000017
#define FILE_DEVICE_PRINTER                 0x00000018
#define FILE_DEVICE_SCANNER                 0x00000019
#define FILE_DEVICE_SERIAL_MOUSE_PORT       0x0000001a
#define FILE_DEVICE_SERIAL_PORT             0x0000001b
#define FILE_DEVICE_SCREEN                  0x0000001c
#define FILE_DEVICE_SOUND                   0x0000001d
#define FILE_DEVICE_STREAMS                 0x0000001e
#define FILE_DEVICE_TAPE                    0x0000001f
#define FILE_DEVICE_TAPE_FILE_SYSTEM        0x00000020
#define FILE_DEVICE_TRANSPORT               0x00000021
#define FILE_DEVICE_UNKNOWN                 0x00000022
#define FILE_DEVICE_VIDEO                   0x00000023
#define FILE_DEVICE_VIRTUAL_DISK            0x00000024
#define FILE_DEVICE_WAVE_IN                 0x00000025
#define FILE_DEVICE_WAVE_OUT                0x00000026
#define FILE_DEVICE_8042_PORT               0x00000027
#define FILE_DEVICE_NETWORK_REDIRECTOR      0x00000028
#define FILE_DEVICE_BATTERY                 0x00000029
#define FILE_DEVICE_BUS_EXTENDER            0x0000002a
#define FILE_DEVICE_MODEM                   0x0000002b
#define FILE_DEVICE_VDM                     0x0000002c
#define FILE_DEVICE_MASS_STORAGE            0x0000002d
#define FILE_DEVICE_SMB                     0x0000002e
#define FILE_DEVICE_KS                      0x0000002f
#define FILE_DEVICE_CHANGER                 0x00000030
#define FILE_DEVICE_SMARTCARD               0x00000031
#define FILE_DEVICE_ACPI                    0x00000032
#define FILE_DEVICE_DVD                     0x00000033
#define FILE_DEVICE_FULLSCREEN_VIDEO        0x00000034
#define FILE_DEVICE_DFS_FILE_SYSTEM         0x00000035
#define FILE_DEVICE_DFS_VOLUME              0x00000036
#define FILE_DEVICE_SERENUM                 0x00000037
#define FILE_DEVICE_TERMSRV                 0x00000038
#define FILE_DEVICE_KSEC                    0x00000039
#define FILE_DEVICE_FIPS                    0x0000003A
#define FILE_DEVICE_INFINIBAND              0x0000003B
#define FILE_DEVICE_VMBUS                   0x0000003E
#define FILE_DEVICE_CRYPT_PROVIDER          0x0000003F
#define FILE_DEVICE_WPD                     0x00000040
#define FILE_DEVICE_BLUETOOTH               0x00000041
#define FILE_DEVICE_MT_COMPOSITE            0x00000042
#define FILE_DEVICE_MT_TRANSPORT            0x00000043
#define FILE_DEVICE_BIOMETRIC               0x00000044
#define FILE_DEVICE_PMI                     0x00000045
#define FILE_DEVICE_EHSTOR                  0x00000046
#define FILE_DEVICE_DEVAPI                  0x00000047
#define FILE_DEVICE_GPIO                    0x00000048
#define FILE_DEVICE_USBEX                   0x00000049
#define FILE_DEVICE_CONSOLE                 0x00000050
#define FILE_DEVICE_NFP                     0x00000051
#define FILE_DEVICE_SYSENV                  0x00000052
#define FILE_DEVICE_VIRTUAL_BLOCK           0x00000053
#define FILE_DEVICE_POINT_OF_SERVICE        0x00000054
#define FILE_DEVICE_STORAGE_REPLICATION     0x00000055
#define FILE_DEVICE_TRUST_ENV               0x00000056
#define FILE_DEVICE_UCM                     0x00000057
#define FILE_DEVICE_UCMTCPCI                0x00000058
#define FILE_DEVICE_PERSISTENT_MEMORY       0x00000059
#define FILE_DEVICE_NVDIMM                  0x0000005a
#define FILE_DEVICE_HOLOGRAPHIC             0x0000005b
#define FILE_DEVICE_SDFXHCI                 0x0000005c
#define FILE_DEVICE_UCMUCSI                 0x0000005d
#define FILE_DEVICE_PRM                     0x0000005e
#define FILE_DEVICE_EVENT_COLLECTOR         0x0000005f
#define FILE_DEVICE_USB4                    0x00000060
#define FILE_DEVICE_SOUNDWIRE               0x00000061
#define FILE_DEVICE_FABRIC_NVME             0x00000062
#define FILE_DEVICE_SVM                     0x00000063
#define FILE_DEVICE_HARDWARE_ACCELERATOR    0x00000064
#define FILE_DEVICE_I3C                     0x00000065
```

These constants are defined in Ntddk.h and Wdm.h. Check these files to see whether additional device types have been defined.

The FILE_DEVICE_DISK specification covers disk partitions and any object that appears as a disk.

Intermediate drivers usually specify device types that represent the underlying device. For example, the system-supplied fault-tolerant disk driver, *ftdisk*, creates device objects of type FILE_DEVICE_DISK; it does not define new device types for the mirror sets, stripe sets, and volume sets it manages.

FILE_DEVICE_*XXX* values in the range of 0 through 32767 are reserved for Microsoft. All driver writers must use these system-defined constants for devices belonging to the system-defined device types.

If a type of hardware does not match any of the defined types, specify a value of either FILE_DEVICE_UNKNOWN, or a value within the range of 32768 through 65535.
