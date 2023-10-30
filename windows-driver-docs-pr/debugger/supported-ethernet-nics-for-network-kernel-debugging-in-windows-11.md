---
title: Supported Ethernet NICs for Network Kernel Debugging in Windows 11
description: Learn about kernel debugging over an Ethernet network cable when the target computer is running Windows 11.
ms.date: 10/06/2021
---

# Supported Ethernet NICs for Network Kernel Debugging in Windows 11

To do kernel debugging over an Ethernet network cable, the target computer must have a supported network interface card (NIC).

During kernel debugging, the computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. For more information, see [Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md).

To do kernel debugging over a network cable, the target computer must have a supported network adapter. When the target computer is running Windows, the network adapters listed here are supported for kernel debugging.

## Version Information

This topic lists the supported adapters for the following versions of Windows

- Windows 11, Build 22000

**Determining NIC support using VerifiedNicList.xml**  

To determine which set of NICs is supported for any particular release of Windows, examine the `VerifiedNicList.xml` file that is in the debuggers directory installed by the WDK or SDK that shipped with that particular release of Windows. For 64 bit Windows, by default, it will be installed in this directory:

`C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\VerifiedNicList.xml`

Checking the VerifiedNicList.xml that ships for a particular release, is required because additional hardware support is added to new releases of Windows that is not present in previous releases.  So you must check the VerifiedNicLIst.xml file for that particular release.

## Finding the vendor ID and device ID

To find the vendor ID and device ID of the network adapter on your target computer.

- On the target computer, open Device Manager (enter **devmgmt** in a Command Prompt window).
- In Device Manager, locate the network adapter that you want to use for debugging.
- Select and hold (or right-click) the network adapter node, and choose **Properties**.
- In the **Details** tab, under **Property**, select **Hardware Ids**.

The vendor and device IDs are shown as VEN\_*VendorID* and DEV\_*DeviceID*. For example, if you see PCI\\VEN\_8086&DEV\_104B, the vendor ID is 8086, and the device ID is 104B.

### Vendor ID 8086, Intel Corporation

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
0D4E
0D4F
0D4C
0D4D
0D53
0D55
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
15B9
15BB
15BC
15BD
15BE
15D6
15D7
15D8
15DF
15E0
15E1
15E2
15E3
15F4
15F9
15FA
15FB
15FC
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

*New in Windows 11*

1572
1574
1580
1581
1583
1584
1585
1586
1587
1588
1589
15F5
1A1E
1A1F
1A1C
1A1D
158A
158B
37D0
37CC
37D2
37CE
37CF
37D0
37D1
37D2
37D3
37D4
550A
550B
550C
550D


### Vendor ID 10EC, Realtek Semiconductor Corp.

For vendor ID 10EC, these device IDs are supported:

2502
2600
3000
8125
8136
8137
8161
8166
8167
8168
8169
8225

### Vendor ID 14E4, Broadcom

For vendor ID 14E4, these device IDs are supported:

1600
1601
1614
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
16C9
16CA
16CE
16CF
16D0
16D1
16D2
16D5
16D6
16D7
16D8
16D9
16DD
16DF
16E0
16E2
16E3
16E4
16E9
16F0
16F1
16F7
16FD
16FE
16FF
170D
170E
170F
D802

*New in Windows 11*

1041
1042
1043
1604
1605
1606
1607
1608
1609
16C1
16C5
16BD
1750
1751
1752
1799
1800
1801
1802
1803
1804
1805
1806
1807
1808
1809
1902
1903
1906
1907
190A
190B
D804
D812
D814
D818
D82A
D82B
D82C
D82D
D82E
D82F


### Vendor ID 1969, Atheros Communications

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

### Vendor ID 19A2, ServerEngines (Emulex)

For vendor ID 19A2, these device IDs are supported:

0211
0215
0221
0700
0710

### Vendor ID 10DF, Emulex Corporation

For vendor ID 10DF, these device IDs are supported:

0720
E220

### Vendor ID 15B3, Mellanox Technology

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

### Vendor ID 1137, Cisco Systems Inc

For vendor ID 1137, these device IDs are supported:

0043

## XML Supported NIC List

This is the same information shown above in the XML format.

```xml
<?xml version="1.0" encoding="utf-8"?>
<SupportedNetworkInterfaceCards>
  <NIC>
    <manufacturer>8086</manufacturer>
      <deviceid build="9200">1000</deviceid>
      <deviceid build="9200">1001</deviceid>
      <deviceid build="9200">1004</deviceid>
      <deviceid build="9200">1008</deviceid>
      <deviceid build="9200">1009</deviceid>
      <deviceid build="9200">100C</deviceid>
      <deviceid build="9200">100D</deviceid>
      <deviceid build="9200">100E</deviceid>
      <deviceid build="9200">1015</deviceid>
      <deviceid build="9200">1016</deviceid>
      <deviceid build="9200">1017</deviceid>
      <deviceid build="9200">101E</deviceid>
      <deviceid build="9200">100F</deviceid>
      <deviceid build="9200">1011</deviceid>
      <deviceid build="9200">1026</deviceid>
      <deviceid build="9200">1027</deviceid>
      <deviceid build="9200">1028</deviceid>
      <deviceid build="9200">1010</deviceid>
      <deviceid build="9200">1012</deviceid>
      <deviceid build="9200">101D</deviceid>
      <deviceid build="9200">1079</deviceid>
      <deviceid build="9200">107A</deviceid>
      <deviceid build="9200">107B</deviceid>
      <deviceid build="9200">108A</deviceid>
      <deviceid build="9200">1099</deviceid>
      <deviceid build="9200">10B5</deviceid>
      <deviceid build="9200">1013</deviceid>
      <deviceid build="9200">1018</deviceid>
      <deviceid build="9200">1014</deviceid>
      <deviceid build="9200">1078</deviceid>
      <deviceid build="9200">1076</deviceid>
      <deviceid build="9200">107C</deviceid>
      <deviceid build="9200">1077</deviceid>
      <deviceid build="9200">1019</deviceid>
      <deviceid build="9200">101A</deviceid>
      <deviceid build="9200">1075</deviceid>
      <deviceid build="9200">105E</deviceid>
      <deviceid build="9200">105F</deviceid>
      <deviceid build="9200">1060</deviceid>
      <deviceid build="9200">10D9</deviceid>
      <deviceid build="9200">10DA</deviceid>
      <deviceid build="9200">10A4</deviceid>
      <deviceid build="9200">10D5</deviceid>
      <deviceid build="9200">10A5</deviceid>
      <deviceid build="9600">10BC</deviceid>
      <deviceid build="9200">107D</deviceid>
      <deviceid build="9200">107E</deviceid>
      <deviceid build="9200">107F</deviceid>
      <deviceid build="9600">10B9</deviceid>
      <deviceid build="9200">108B</deviceid>
      <deviceid build="9200">108C</deviceid>
      <deviceid build="9200">109A</deviceid>
      <deviceid build="9600">10D3</deviceid>
      <deviceid build="9200">10F6</deviceid>
      <deviceid build="9200">150C</deviceid>
      <deviceid build="9200">1096</deviceid>
      <deviceid build="9200">1098</deviceid>
      <deviceid build="9600">10BA</deviceid>
      <deviceid build="9600">10BB</deviceid>
      <deviceid build="9200">1501</deviceid>
      <deviceid build="9200">1049</deviceid>
      <deviceid build="9200">104A</deviceid>
      <deviceid build="9200">104B</deviceid>
      <deviceid build="9200">104C</deviceid>
      <deviceid build="9600">10C4</deviceid>
      <deviceid build="9600">10C5</deviceid>
      <deviceid build="9200">104D</deviceid>
      <deviceid build="9600">10BF</deviceid>
      <deviceid build="9200">10F5</deviceid>
      <deviceid build="9600">10CB</deviceid>
      <deviceid build="9600">10BD</deviceid>
      <deviceid build="9200">10E5</deviceid>
      <deviceid build="9200">294C</deviceid>
      <deviceid build="9600">10C0</deviceid>
      <deviceid build="9600">10C3</deviceid>
      <deviceid build="9600">10C2</deviceid>
      <deviceid build="9600">10CC</deviceid>
      <deviceid build="9600">10CD</deviceid>
      <deviceid build="9600">10CE</deviceid>
      <deviceid build="9600">10DE</deviceid>
      <deviceid build="9600">10DF</deviceid>
      <deviceid build="9600">1525</deviceid>
      <deviceid build="9200">10EA</deviceid>
      <deviceid build="9200">10EB</deviceid>
      <deviceid build="9200">10EF</deviceid>
      <deviceid build="9200">10F0</deviceid>
      <deviceid build="9200">1502</deviceid>
      <deviceid build="9200">1503</deviceid>
      <deviceid build="9600">153A</deviceid>
      <deviceid build="9600">153B</deviceid>
      <deviceid build="9600">155A</deviceid>
      <deviceid build="9600">1559</deviceid>
      <deviceid build="15063">15A0</deviceid>
      <deviceid build="15063">15A1</deviceid>
      <deviceid build="15063">15A2</deviceid>
      <deviceid build="15063">15A3</deviceid>
      <deviceid build="15063">156F</deviceid>
      <deviceid build="15063">1570</deviceid>
      <deviceid build="15063">15B7</deviceid>
      <deviceid build="15063">15B8</deviceid>
      <deviceid build="16299">15B9</deviceid>
      <deviceid build="16299">15D7</deviceid>
      <deviceid build="16299">15D8</deviceid>
      <deviceid build="16299">15E3</deviceid>
      <deviceid build="16299">15D6</deviceid>
      <deviceid build="16299">15BD</deviceid>
      <deviceid build="16299">15BE</deviceid>
      <deviceid build="16299">15BB</deviceid>
      <deviceid build="16299">15BC</deviceid>
      <deviceid build="16299">15DF</deviceid>
      <deviceid build="16299">15E0</deviceid>
      <deviceid build="16299">15E1</deviceid>
      <deviceid build="16299">15E2</deviceid>
      <deviceid build="9600">10C9</deviceid>
      <deviceid build="9200">10E6</deviceid>
      <deviceid build="9200">10E7</deviceid>
      <deviceid build="9200">10E8</deviceid>
      <deviceid build="9200">1526</deviceid>
      <deviceid build="9200">150A</deviceid>
      <deviceid build="9200">1518</deviceid>
      <deviceid build="9200">150D</deviceid>
      <deviceid build="9200">10A7</deviceid>
      <deviceid build="9200">10A9</deviceid>
      <deviceid build="9600">10D6</deviceid>
      <deviceid build="9200">150E</deviceid>
      <deviceid build="9200">150F</deviceid>
      <deviceid build="9200">1510</deviceid>
      <deviceid build="9200">1511</deviceid>
      <deviceid build="9200">1516</deviceid>
      <deviceid build="9600">1527</deviceid>
      <deviceid build="9200">1521</deviceid>
      <deviceid build="9200">1522</deviceid>
      <deviceid build="9200">1523</deviceid>
      <deviceid build="9200">1524</deviceid>
      <deviceid build="9600">1546</deviceid>
      <deviceid build="9600">1533</deviceid>
      <deviceid build="9600">1534</deviceid>
      <deviceid build="9600">1535</deviceid>
      <deviceid build="9600">1536</deviceid>
      <deviceid build="9600">1537</deviceid>
      <deviceid build="9600">1538</deviceid>
      <deviceid build="9600">157B</deviceid>
      <deviceid build="9600">157C</deviceid>
      <deviceid build="9600">1539</deviceid>
      <deviceid build="9600">1F40</deviceid>
      <deviceid build="9600">1F41</deviceid>
      <deviceid build="9600">1F45</deviceid>
      <deviceid build="9600">0438</deviceid>
      <deviceid build="9600">043A</deviceid>
      <deviceid build="9600">043C</deviceid>
      <deviceid build="9600">0440</deviceid>
      <deviceid build="9600">10C6</deviceid>
      <deviceid build="9600">10C7</deviceid>
      <deviceid build="9600">10C8</deviceid>
      <deviceid build="9600">150B</deviceid>
      <deviceid build="9600">10DB</deviceid>
      <deviceid build="9600">10DD</deviceid>
      <deviceid build="9600">10EC</deviceid>
      <deviceid build="9600">10F1</deviceid>
      <deviceid build="9600">10E1</deviceid>
      <deviceid build="9600">10F4</deviceid>
      <deviceid build="9600">10F7</deviceid>
      <deviceid build="9600">1514</deviceid>
      <deviceid build="9600">1517</deviceid>
      <deviceid build="9600">10F8</deviceid>
      <deviceid build="15063">000C</deviceid>
      <deviceid build="15063">1F63</deviceid>
      <deviceid build="9600">10F9</deviceid>
      <deviceid build="9600">10FB</deviceid>
      <deviceid build="15063">11A9</deviceid>
      <deviceid build="15063">1071</deviceid>
      <deviceid build="15063">1F72</deviceid>
      <deviceid build="15063">17D0</deviceid>
      <deviceid build="15063">0470</deviceid>
      <deviceid build="15063">211B</deviceid>
      <deviceid build="15063">8976</deviceid>
      <deviceid build="15063">2159</deviceid>
      <deviceid build="15063">000D</deviceid>
      <deviceid build="15063">0008</deviceid>
      <deviceid build="9600">152A</deviceid>
      <deviceid build="9600">1529</deviceid>
      <deviceid build="9600">1507</deviceid>
      <deviceid build="9600">154D</deviceid>
      <deviceid build="9600">154A</deviceid>
      <deviceid build="9600">1558</deviceid>
      <deviceid build="9600">1557</deviceid>
      <deviceid build="15063">0001</deviceid>
      <deviceid build="9600">10FC</deviceid>
      <deviceid build="9600">151C</deviceid>
      <deviceid build="9600">1528</deviceid>
      <deviceid build="9600">1560</deviceid>
      <deviceid build="15063">1563</deviceid>
      <deviceid build="15063">ABCD</deviceid>
      <deviceid build="15063">15AA</deviceid>
      <deviceid build="15063">15AB</deviceid>
      <deviceid build="15063">15AC</deviceid>
      <deviceid build="15063">15AD</deviceid>
      <deviceid build="15063">15AE</deviceid>
      <deviceid build="19565">0D4E</deviceid>
      <deviceid build="19565">0D4F</deviceid>
      <deviceid build="19565">0D4C</deviceid>
      <deviceid build="19565">0D4D</deviceid>
      <deviceid build="19565">0D53</deviceid>
      <deviceid build="19565">0D55</deviceid>
      <deviceid build="19565">15FB</deviceid>
      <deviceid build="19565">15FC</deviceid>
      <deviceid build="19565">15F9</deviceid>
      <deviceid build="19565">15FA</deviceid>
      <deviceid build="19565">15F4</deviceid>
      <deviceid build="20271">15F5</deviceid>
      <deviceid build="20271">1A1E</deviceid>
      <deviceid build="20271">1A1F</deviceid>
      <deviceid build="20271">1A1C</deviceid>
      <deviceid build="20271">1A1D</deviceid>
      <deviceid build="20271">550A</deviceid>
      <deviceid build="20271">550B</deviceid>
      <deviceid build="20271">550C</deviceid>
      <deviceid build="20271">550D</deviceid>
      <deviceid build="20271">1572</deviceid>
      <deviceid build="20271">1574</deviceid>
      <deviceid build="20271">1580</deviceid>
      <deviceid build="20271">1581</deviceid>
      <deviceid build="20271">1583</deviceid>
      <deviceid build="20271">1584</deviceid>
      <deviceid build="20271">1585</deviceid>
      <deviceid build="20271">1586</deviceid>
      <deviceid build="20271">1587</deviceid>
      <deviceid build="20271">1588</deviceid>
      <deviceid build="20271">1589</deviceid>
      <deviceid build="20271">158A</deviceid>
      <deviceid build="20271">158B</deviceid>
      <deviceid build="20271">37D0</deviceid>
      <deviceid build="20271">37CC</deviceid>
      <deviceid build="20271">37D2</deviceid>
      <deviceid build="20271">37CE</deviceid>
      <deviceid build="20271">37CF</deviceid>
      <deviceid build="20271">37D0</deviceid>
      <deviceid build="20271">37D1</deviceid>
      <deviceid build="20271">37D2</deviceid>
      <deviceid build="20271">37D3</deviceid>
      <deviceid build="20271">37D4</deviceid>
  </NIC>

  <NIC>
    <manufacturer>10EC</manufacturer>
      <deviceid build="9200">8136</deviceid>
      <deviceid build="9200">8137</deviceid>
      <deviceid build="9200">8168</deviceid>
      <deviceid build="9200">8167</deviceid>
      <deviceid build="9200">8169</deviceid>
      <deviceid build="15063">8166</deviceid>
      <deviceid build="18362">8161</deviceid>
      <deviceid build="18362">8125</deviceid>
      <deviceid build="18362">8225</deviceid>
      <deviceid build="18362">2502</deviceid>
      <deviceid build="18362">2600</deviceid>
      <deviceid build="18362">3000</deviceid>
  </NIC>

  <NIC>
    <manufacturer>14E4</manufacturer>
      <deviceid build="9200">1644</deviceid>
      <deviceid build="9200">1645</deviceid>
      <deviceid build="9200">1646</deviceid>
      <deviceid build="9200">16A6</deviceid>
      <deviceid build="9200">16C6</deviceid>
      <deviceid build="9200">1647</deviceid>
      <deviceid build="9200">16A7</deviceid>
      <deviceid build="9200">16C7</deviceid>
      <deviceid build="9200">164D</deviceid>
      <deviceid build="9200">1648</deviceid>
      <deviceid build="9200">16A8</deviceid>
      <deviceid build="9200">1653</deviceid>
      <deviceid build="9200">166E</deviceid>
      <deviceid build="9200">1654</deviceid>
      <deviceid build="9200">165D</deviceid>
      <deviceid build="9200">165E</deviceid>
      <deviceid build="9200">166D</deviceid>
      <deviceid build="9200">170D</deviceid>
      <deviceid build="9200">170E</deviceid>
      <deviceid build="9200">1696</deviceid>
      <deviceid build="9200">1676</deviceid>
      <deviceid build="9200">1677</deviceid>
      <deviceid build="9200">1659</deviceid>
      <deviceid build="9200">167C</deviceid>
      <deviceid build="9200">167D</deviceid>
      <deviceid build="9200">169D</deviceid>
      <deviceid build="9200">16F7</deviceid>
      <deviceid build="9200">16FD</deviceid>
      <deviceid build="9200">16FE</deviceid>
      <deviceid build="9200">16DD</deviceid>
      <deviceid build="9200">1668</deviceid>
      <deviceid build="9200">1669</deviceid>
      <deviceid build="9200">1678</deviceid>
      <deviceid build="9200">1679</deviceid>
      <deviceid build="9200">1600</deviceid>
      <deviceid build="9200">1601</deviceid>
      <deviceid build="9200">166A</deviceid>
      <deviceid build="9200">166B</deviceid>
      <deviceid build="9200">16FF</deviceid>
      <deviceid build="9200">170F</deviceid>
      <deviceid build="9200">169B</deviceid>
      <deviceid build="9200">1693</deviceid>
      <deviceid build="9200">167F</deviceid>
      <deviceid build="9200">169A</deviceid>
      <deviceid build="9200">1698</deviceid>
      <deviceid build="9200">1692</deviceid>
      <deviceid build="9200">1694</deviceid>
      <deviceid build="9200">1690</deviceid>
      <deviceid build="9200">1691</deviceid>
      <deviceid build="9200">1699</deviceid>
      <deviceid build="9200">16A0</deviceid>
      <deviceid build="9200">167B</deviceid>
      <deviceid build="9200">1673</deviceid>
      <deviceid build="9200">165A</deviceid>
      <deviceid build="9200">1674</deviceid>
      <deviceid build="9200">1681</deviceid>
      <deviceid build="9200">1680</deviceid>
      <deviceid build="9200">1688</deviceid>
      <deviceid build="9200">167A</deviceid>
      <deviceid build="9200">1672</deviceid>
      <deviceid build="9200">1684</deviceid>
      <deviceid build="9200">165B</deviceid>
      <deviceid build="9200">16B1</deviceid>
      <deviceid build="9200">16B5</deviceid>
      <deviceid build="9200">16B0</deviceid>
      <deviceid build="9200">16B4</deviceid>
      <deviceid build="9200">16B2</deviceid>
      <deviceid build="9200">16B6</deviceid>
      <deviceid build="15063">1682</deviceid>
      <deviceid build="15063">1686</deviceid>
      <deviceid build="15063">16B3</deviceid>
      <deviceid build="15063">16B7</deviceid>
      <deviceid build="9200">1655</deviceid>
      <deviceid build="15063">1665</deviceid>
      <deviceid build="9200">1656</deviceid>
      <deviceid build="9200">1657</deviceid>
      <deviceid build="9200">165F</deviceid>
      <deviceid build="9200">165C</deviceid>
      <deviceid build="15063">1683</deviceid>
      <deviceid build="15063">1641</deviceid>
      <deviceid build="15063">1642</deviceid>
      <deviceid build="15063">1643</deviceid>
      <deviceid build="15063">1687</deviceid>
      <deviceid build="9200">164A</deviceid>
      <deviceid build="9200">16AA</deviceid>
      <deviceid build="9200">164C</deviceid>
      <deviceid build="9200">16AC</deviceid>
      <deviceid build="9200">1639</deviceid>
      <deviceid build="9200">163A</deviceid>
      <deviceid build="9200">163B</deviceid>
      <deviceid build="9200">163C</deviceid>
      <deviceid build="15063">164E</deviceid>
      <deviceid build="15063">164F</deviceid>
      <deviceid build="15063">1650</deviceid>
      <deviceid build="15063">1662</deviceid>
      <deviceid build="15063">1663</deviceid>
      <deviceid build="15063">168A</deviceid>
      <deviceid build="15063">168D</deviceid>
      <deviceid build="15063">16A1</deviceid>
      <deviceid build="15063">16A2</deviceid>
      <deviceid build="15063">168E</deviceid>
      <deviceid build="15063">163D</deviceid>
      <deviceid build="15063">16A5</deviceid>
      <deviceid build="15063">16A4</deviceid>
      <deviceid build="15063">16AE</deviceid>
      <deviceid build="15063">163E</deviceid>
      <deviceid build="18362">16C0</deviceid>
      <deviceid build="18362">16C9</deviceid>
      <deviceid build="18362">16CA</deviceid>
      <deviceid build="18362">16CC</deviceid>
      <deviceid build="18362">16CD</deviceid>
      <deviceid build="18362">16CE</deviceid>
      <deviceid build="18362">16CF</deviceid>
      <deviceid build="18362">16D0</deviceid>
      <deviceid build="18362">16D1</deviceid>
      <deviceid build="18362">16D2</deviceid>
      <deviceid build="18362">16D4</deviceid>
      <deviceid build="18362">16D5</deviceid>
      <deviceid build="18362">16D6</deviceid>
      <deviceid build="18362">16D7</deviceid>
      <deviceid build="18362">16D8</deviceid>
      <deviceid build="18362">16D9</deviceid>
      <deviceid build="18362">16DA</deviceid>
      <deviceid build="18362">16DB</deviceid>
      <deviceid build="18362">16DC</deviceid>
      <deviceid build="18362">16DE</deviceid>
      <deviceid build="18362">16DF</deviceid>
      <deviceid build="18362">16E0</deviceid>
      <deviceid build="18362">16E2</deviceid>
      <deviceid build="18362">16E3</deviceid>
      <deviceid build="18362">16E4</deviceid>
      <deviceid build="18362">16E7</deviceid>
      <deviceid build="18362">16E8</deviceid>
      <deviceid build="18362">16E9</deviceid>
      <deviceid build="18362">16EA</deviceid>
      <deviceid build="18362">16EB</deviceid>
      <deviceid build="18362">16EC</deviceid>
      <deviceid build="18362">16ED</deviceid>
      <deviceid build="18362">16EE</deviceid>
      <deviceid build="18362">16EF</deviceid>
      <deviceid build="18362">16F0</deviceid>
      <deviceid build="18362">16F1</deviceid>
      <deviceid build="18362">1614</deviceid>
      <deviceid build="18362">D802</deviceid>
      <deviceid build="20241">1604</deviceid>
      <deviceid build="20241">1605</deviceid>
      <deviceid build="20241">1606</deviceid>
      <deviceid build="20241">1607</deviceid>
      <deviceid build="20241">1608</deviceid>
      <deviceid build="20241">1609</deviceid>
      <deviceid build="20241">D804</deviceid>
      <deviceid build="20241">D812</deviceid>
      <deviceid build="20241">D814</deviceid>
      <deviceid build="20241">D818</deviceid>
      <deviceid build="20241">D82A</deviceid>
      <deviceid build="20241">D82B</deviceid>
      <deviceid build="20241">D82C</deviceid>
      <deviceid build="20241">D82D</deviceid>
      <deviceid build="20241">D82E</deviceid>
      <deviceid build="20241">D82F</deviceid>
      <deviceid build="20241">1902</deviceid>
      <deviceid build="20241">1903</deviceid>
      <deviceid build="20241">1906</deviceid>
      <deviceid build="20241">1907</deviceid>
      <deviceid build="20241">190A</deviceid>
      <deviceid build="20241">190B</deviceid>
      <deviceid build="20241">1799</deviceid>
      <deviceid build="20241">1041</deviceid>
      <deviceid build="20241">1042</deviceid>
      <deviceid build="20241">1043</deviceid>
      <deviceid build="20241">1750</deviceid>
      <deviceid build="20241">1751</deviceid>
      <deviceid build="20241">1752</deviceid>
      <deviceid build="20241">1800</deviceid>
      <deviceid build="20241">1801</deviceid>
      <deviceid build="20241">1802</deviceid>
      <deviceid build="20241">1803</deviceid>
      <deviceid build="20241">1804</deviceid>
      <deviceid build="20241">1805</deviceid>
      <deviceid build="20241">1806</deviceid>
      <deviceid build="20241">1807</deviceid>
      <deviceid build="20241">1808</deviceid>
      <deviceid build="20241">1809</deviceid>
      <deviceid build="20241">16C1</deviceid>
      <deviceid build="20241">16C5</deviceid>
      <deviceid build="20241">16BD</deviceid>
  </NIC>

  <NIC>
    <manufacturer>1969</manufacturer>
      <deviceid build="9200">1062</deviceid>
      <deviceid build="9200">1063</deviceid>
      <deviceid build="9200">2060</deviceid>
      <deviceid build="9200">2062</deviceid>
      <deviceid build="9200">1073</deviceid>
      <deviceid build="9200">1083</deviceid>
      <deviceid build="9200">1090</deviceid>
      <deviceid build="9200">1091</deviceid>
      <deviceid build="9200">E091</deviceid>
      <deviceid build="9200">10A0</deviceid>
      <deviceid build="9200">10A1</deviceid>
      <deviceid build="9200">E0A1</deviceid>
      <deviceid build="9200">10B0</deviceid>
      <deviceid build="9200">10B1</deviceid>
      <deviceid build="9200">E0B1</deviceid>
      <deviceid build="9200">10C0</deviceid>
      <deviceid build="9200">10C1</deviceid>
      <deviceid build="9200">E0C1</deviceid>
      <deviceid build="9200">10D0</deviceid>
      <deviceid build="9200">10D1</deviceid>
      <deviceid build="9200">E0D1</deviceid>
      <deviceid build="9200">10E0</deviceid>
      <deviceid build="9200">10E1</deviceid>
      <deviceid build="9200">E0E1</deviceid>
      <deviceid build="9200">10F0</deviceid>
      <deviceid build="9200">10F1</deviceid>
      <deviceid build="9200">E0F1</deviceid>
  </NIC>

  <NIC>
    <manufacturer>19A2</manufacturer>
      <deviceid build="9600">0211</deviceid>
      <deviceid build="9600">0215</deviceid>
      <deviceid build="9600">0221</deviceid>
      <deviceid build="9600">0700</deviceid>
      <deviceid build="9600">0710</deviceid>
  </NIC>

  <NIC>
    <manufacturer>10DF</manufacturer>
      <deviceid build="9600">0720</deviceid>
      <deviceid build="9600">E220</deviceid>
  </NIC>

  <NIC>
    <manufacturer>15B3</manufacturer>
      <deviceid build="9600">1000</deviceid>
      <deviceid build="9600">1001</deviceid>
      <deviceid build="9600">1002</deviceid>
      <deviceid build="9600">1003</deviceid>
      <deviceid build="9600">1004</deviceid>
      <deviceid build="9600">1005</deviceid>
      <deviceid build="9600">1006</deviceid>
      <deviceid build="9600">1007</deviceid>
      <deviceid build="9600">1008</deviceid>
      <deviceid build="9600">1009</deviceid>
      <deviceid build="9600">100A</deviceid>
      <deviceid build="9600">100B</deviceid>
      <deviceid build="9600">100C</deviceid>
      <deviceid build="9600">100D</deviceid>
      <deviceid build="9600">100E</deviceid>
      <deviceid build="9600">100F</deviceid>
      <deviceid build="9600">1010</deviceid>
      <deviceid build="9600">6340</deviceid>
      <deviceid build="9600">6341</deviceid>
      <deviceid build="9600">634A</deviceid>
      <deviceid build="9600">634B</deviceid>
      <deviceid build="9600">6354</deviceid>
      <deviceid build="9600">6368</deviceid>
      <deviceid build="9600">6369</deviceid>
      <deviceid build="9600">6372</deviceid>
      <deviceid build="9600">6732</deviceid>
      <deviceid build="9600">6733</deviceid>
      <deviceid build="9600">673C</deviceid>
      <deviceid build="9600">673D</deviceid>
      <deviceid build="9600">6746</deviceid>
      <deviceid build="9600">6750</deviceid>
      <deviceid build="9600">6751</deviceid>
      <deviceid build="9600">675A</deviceid>
      <deviceid build="9600">6764</deviceid>
      <deviceid build="9600">6765</deviceid>
      <deviceid build="9600">676E</deviceid>
      <deviceid build="9600">6778</deviceid>
      <deviceid build="15063">1013</deviceid>
      <deviceid build="15063">1015</deviceid>
      <deviceid build="15063">1017</deviceid>
      <deviceid build="15063">1019</deviceid>
      <deviceid build="15063">101B</deviceid>
      <deviceid build="15063">101D</deviceid>
      <deviceid build="15063">101F</deviceid>
      <deviceid build="15063">1021</deviceid>
      <deviceid build="15063">1023</deviceid>
      <deviceid build="15063">1025</deviceid>
      <deviceid build="15063">1027</deviceid>
      <deviceid build="15063">1029</deviceid>
      <deviceid build="15063">102B</deviceid>
      <deviceid build="15063">102F</deviceid>
  </NIC>

  <NIC>
    <manufacturer>1137</manufacturer>
      <deviceid build="15063">0043</deviceid>
  </NIC>

</SupportedNetworkInterfaceCards>
```

## See also

[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)

[Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)
