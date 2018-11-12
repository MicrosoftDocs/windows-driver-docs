---
title: Supported Ethernet NICs for Network Kernel Debugging in Windows 8
description: You can do kernel debugging over an Ethernet network cable when the target computer is running Windows 8. The target computer must have a supported network interface card (NIC) or network adapter.
ms.assetid: 92FEEBAF-9978-4BDE-BB4F-81454D84A7E7
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Supported Ethernet NICs for Network Kernel Debugging in Windows 8


You can do kernel debugging over an Ethernet network cable when the target computer is running Windows 8. The target computer must have a supported network interface card (NIC) or network adapter.

During kernel debugging, the computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. To do [kernel debugging over a network cable](setting-up-a-network-debugging-connection.md), the target computer must have a supported network adapter. When the target computer is running Windows 8, the network adapters listed here are supported for kernel debugging.

**Note**  For a list of network adapters supported by Windows 8.1 for kernel debugging, see [Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md).

 

## <span id="System_Requirements"></span><span id="system_requirements"></span><span id="SYSTEM_REQUIREMENTS"></span>System Requirements


Kernel debugging through Ethernet NICs requires certain low-level platform support. Windows requires that these NICs be attached via PCI/PCIe for this debugging solution. In most cases, simply plugging in one of these supported NICs will allow a robust kernel debugging experience. However, there may be cases where BIOS configuration details hinder the Windows debug path. The following set of platform requirements should be considered:

-   System firmware should discover and configure the NIC device such that its resources do not conflict with any other devices that have been BIOS-configured.
-   System firmware should place the NIC’s resources under address windows that are not marked prefetchable.

## <span id="Finding_the_vendor_ID_and_device_ID"></span><span id="finding_the_vendor_id_and_device_id"></span><span id="FINDING_THE_VENDOR_ID_AND_DEVICE_ID"></span>Finding the vendor ID and device ID


First find the vendor ID and device ID of the network adapter on your target computer.

-   On the target computer, open Device Manager (enter **devmgmt** in a Command Prompt window).
-   In Device Manager, locate the network adapter that you want to use for debugging.
-   Right click the network adapter node, and choose **Properties**.
-   In the **Details** tab, under **Property**, select **Hardware Ids**.

The vendor and device IDs are shown as VEN\_*VendorID* and DEV\_*DeviceID*. For example, if you see PCI\\VEN\_8086&DEV\_104B, the vendor ID is 8086, and the device ID is 104B.

## <span id="Vendor_ID_8086__Intel_Corporation"></span><span id="vendor_id_8086__intel_corporation"></span><span id="VENDOR_ID_8086__INTEL_CORPORATION"></span>Vendor ID 8086, Intel Corporation


For vendor ID 8086, these device IDs are supported:

1000
1001
1004
1008
1009
100C
100D
100E
100F
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
101A
101D
101E
1026
1027
1028
1049
104A
104B
104C
104D
105E
105F
1060
1075
1076
1077
1078
1079
107A
107B
107C
107D
107E
107F
108A
108B
108C
1096
1098
1099
109A
10A4
10A5
10A7
10A9
10B5
10B9
10BA
10BB
10BC
10BD
10BF
10C9
10CB
10CC
10CD
10CE
10D3
10D5
10D6
10D9
10DA
10E5
10E6
10E7
10E8
10EA
10EB
10EF
10F0
10F5
10F6
1501
1502
1503
150A
150C
150D
150E
150F
1510
1511
1516
1518
1521
1522
1523
1524
1526
294C
## <span id="vendor_id_10ec__realtek_semiconductor_corp."></span><span id="VENDOR_ID_10EC__REALTEK_SEMICONDUCTOR_CORP."></span>Vendor ID 10EC, Realtek Semiconductor Corp.


For vendor ID 10EC, these device IDs are supported:

8136
8137
8167
8168
8169
## <span id="Vendor_ID_14E4__Broadcom"></span><span id="vendor_id_14e4__broadcom"></span><span id="VENDOR_ID_14E4__BROADCOM"></span>Vendor ID 14E4, Broadcom


For vendor ID 14E4, these device IDs are supported:

1600
1601
1639
163A
163B
163C
1644
1645
1646
1647
1648
164A
164C
164D
1653
1654
1655
1656
1657
1658
1659
165A
165B
165C
165D
165E
165F
1668
1669
166A
166B
166D
166E
1672
1673
1674
1676
1677
1678
1679
167A
167B
167C
167D
167F
1680
1681
1684
1688
1690
1691
1692
1693
1694
1696
1698
1699
169A
169B
169D
16A0
16A6
16A7
16A8
16AA
16AC
16B0
16B1
16B2
16B4
16B5
16B6
16C6
16C7
16DD
16F7
16FD
16FE
16FF
170D
170E
170F
## <span id="Vendor_ID_1969__Atheros_Communications"></span><span id="vendor_id_1969__atheros_communications"></span><span id="VENDOR_ID_1969__ATHEROS_COMMUNICATIONS"></span>Vendor ID 1969, Atheros Communications


Support for Atheros network adapters is provided by a separate module that is available from Qualcomm. These device IDs are supported.

1062
1063
1073
1083
1090
1091
10A0
10A1
10B0
10B1
10C0
10C1
10D0
10D1
10E0
10E1
10F0
10F1
2060
2062
E091
E0A1
E0B1
E0C1
E0D1
E0E1
E0F1
## <span id="related_topics"></span>Related topics



[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)

 

 






