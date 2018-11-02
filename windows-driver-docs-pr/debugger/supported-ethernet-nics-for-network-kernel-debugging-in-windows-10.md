---
title: Supported Ethernet NICs for Network Kernel Debugging in Windows 10
description: You can do kernel debugging over an Ethernet network cable when the target computer is running Windows. The target computer must have a supported network interface card (NIC) or network adapter.
ms.assetid: F98A7ACE-DD04-423C-A438-89E21363C693
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Supported Ethernet NICs for Network Kernel Debugging in Windows 10


You can do kernel debugging over an Ethernet network cable when the target computer is running Windows. The target computer must have a supported network interface card (NIC) or network adapter.

During kernel debugging, the computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. To do [kernel debugging over a network cable](setting-up-a-network-debugging-connection.md), the target computer must have a supported network adapter. When the target computer is running Windows, the network adapters listed here are supported for kernel debugging.

**Note**  
The list of supported adapters is for the following versions of Windows

-   Windows 10, version 1703
-   Windows Server 2016

 

## <span id="Finding_the_vendor_ID_and_device_ID"></span><span id="finding_the_vendor_id_and_device_id"></span><span id="FINDING_THE_VENDOR_ID_AND_DEVICE_ID"></span>Finding the vendor ID and device ID


First find the vendor ID and device ID of the network adapter on your target computer.

-   On the target computer, open Device Manager (enter **devmgmt** in a Command Prompt window).
-   In Device Manager, locate the network adapter that you want to use for debugging.
-   Right click the network adapter node, and choose **Properties**.
-   In the **Details** tab, under **Property**, select **Hardware Ids**.

The vendor and device IDs are shown as VEN\_*VendorID* and DEV\_*DeviceID*. For example, if you see PCI\\VEN\_8086&DEV\_104B, the vendor ID is 8086, and the device ID is 104B.

## <span id="Vendor_ID_8086__Intel_Corporation"></span><span id="vendor_id_8086__intel_corporation"></span><span id="VENDOR_ID_8086__INTEL_CORPORATION"></span>Vendor ID 8086, Intel Corporation


For vendor ID 8086, these device IDs are supported:

0001
0008
000C
000D
0438
043A
043C
0440
0470
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
1071
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
10C0
10C2
10C3
10C4
10C5
10C6
10C7
10C8
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
10DB
10DD
10DE
10DF
10E1
10E5
10E6
10E7
10E8
10EA
10EB
10EC
10EF
10F0
10F1
10F4
10F5
10F6
10F7
10F8
10F9
10FB
10FC
11A9
1501
1502
1503
1507
150A
150B
150C
150D
150E
150F
1510
1511
1514
1516
1517
1518
151C
1521
1522
1523
1524
1525
1526
1527
1528
1529
152A
1533
1534
1535
1536
1537
1538
1539
153A
153B
1546
154A
154D
1557
1558
1559
155A
1560
1563
156F
1570
157B
157C
15A0
15A1
15A2
15A3
15AA
15AB
15AC
15AD
15AE
15B7
15B8
17D0
1F40
1F41
1F45
1F63
1F72
211B
2159
294C
8976
## <span id="vendor_id_10ec__realtek_semiconductor_corp."></span><span id="VENDOR_ID_10EC__REALTEK_SEMICONDUCTOR_CORP."></span>Vendor ID 10EC, Realtek Semiconductor Corp.


For vendor ID 10EC, these device IDs are supported:

8136
8137
8166
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
163D
163E
1641
1642
1643
1644
1645
1646
1647
1648
164A
164C
164D
164E
164F
1650
1653
1654
1655
1656
1657
1659
165A
165B
165C
165D
165E
165F
1662
1663
1665
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
168A
168D
168E
1680
1681
1682
1683
1684
1686
1687
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
16A1
16A2
16A4
16A5
16A6
16A7
16A8
16AA
16AC
16AE
16B0
16B1
16B2
16B3
16B4
16B5
16B6
16B7
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


For vendor ID 1969, these device IDs are supported:

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
## <span id="Vendor_ID_19A2__ServerEngines__Emulex_"></span><span id="vendor_id_19a2__serverengines__emulex_"></span><span id="VENDOR_ID_19A2__SERVERENGINES__EMULEX_"></span>Vendor ID 19A2, ServerEngines (Emulex)


For vendor ID 19A2, these device IDs are supported:

0211
0215
0221
0700
0710
## <span id="Vendor_ID_10DF__Emulex_Corporation"></span><span id="vendor_id_10df__emulex_corporation"></span><span id="VENDOR_ID_10DF__EMULEX_CORPORATION"></span>Vendor ID 10DF, Emulex Corporation


For vendor ID 10DF, these device IDs are supported:

0720
E220
## <span id="Vendor_ID_15B3__Mellanox_Technology"></span><span id="vendor_id_15b3__mellanox_technology"></span><span id="VENDOR_ID_15B3__MELLANOX_TECHNOLOGY"></span>Vendor ID 15B3, Mellanox Technology


For vendor ID 15B3, these device IDs are supported:

1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
100A
100B
100C
100D
100E
100F
1010
1013
1015
1017
1019
101B
101D
101F
1021
1023
1025
1027
1029
102B
102F
6340
6341
634A
634B
6354
6368
6369
6372
6732
6733
673C
673D
6746
6750
6751
675A
6764
6765
676E
6778

## <span id="Vendor_ID_1137__Cisco_Systems_Inc"></span><span id="vendor_id_1137__cisco_systems_inc"></span><span id="VENDOR_ID_1137__CISCO_SYSTEMS_INC"></span>Vendor ID 1137, Cisco Systems Inc


For vendor ID 1137, these device IDs are supported:

0043
## <span id="related_topics"></span>Related topics


[Setting Up Kernel-Mode Debugging over a Network Cable in Visual Studio](setting-up-a-network-debugging-connection-in-visual-studio.md)

[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)

[Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 8](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)

 

 






