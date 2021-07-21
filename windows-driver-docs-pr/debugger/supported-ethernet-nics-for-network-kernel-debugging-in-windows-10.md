---
title: Supported Ethernet NICs for Network Kernel Debugging in Windows 10
description: Learn about kernel debugging over an Ethernet network cable when the target computer is running Windows 10.
ms.date: 04/20/2021
ms.localizationpriority: medium
---

# Supported Ethernet NICs for Network Kernel Debugging in Windows 10

To do kernel debugging over an Ethernet network cable, the target computer must have a supported network interface card (NIC).

During kernel debugging, the computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. For more information, see [Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md).

To do kernel debugging over a network cable, the target computer must have a supported network adapter. When the target computer is running Windows, the network adapters listed here are supported for kernel debugging.

## Version Information

This topic lists the supported adapters for the following versions of Windows

- Windows 10, version 20H2 Build 19042

## Adapter Support for Previous Releases of Windows 10

See these topics for information on supported versions of NICs in previous versions of Windows 10.

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10 - 2004](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10-2004.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10 - 1909](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10-1909.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10 - 1903](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10-1903.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10 - 1809](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10-1809.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10 - 1803](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10-1803.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10 - 1709](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10-1709.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 10 - 1703](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10-1703.md)

**Determining NIC support using VerifiedNicList.xml**  

To determine which set of NICs is supported for any particular release of Windows, examine the `VerifiedNicList.xml` file that is in the debuggers directory installed by the WDK that shipped with that particular release of Windows. For 64 bit Windows, by default, it will be installed in this directory:

`C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\VerifiedNicList.xml`

Checking the VerifiedNicList.xml that ships in the WDK for a particular release, is required because additional hardware support is added to new releases of Windows that is not present in previous releases.  So you must check the VerifiedNicLIst.xml file for that particular release.

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
      <deviceid>1000</deviceid>
      <deviceid>1001</deviceid>
      <deviceid>1004</deviceid>
      <deviceid>1008</deviceid>
      <deviceid>1009</deviceid>
      <deviceid>100C</deviceid>
      <deviceid>100D</deviceid>
      <deviceid>100E</deviceid>
      <deviceid>1015</deviceid>
      <deviceid>1016</deviceid>
      <deviceid>1017</deviceid>
      <deviceid>101E</deviceid>
      <deviceid>100F</deviceid>
      <deviceid>1011</deviceid>
      <deviceid>1026</deviceid>
      <deviceid>1027</deviceid>
      <deviceid>1028</deviceid>
      <deviceid>1010</deviceid>
      <deviceid>1012</deviceid>
      <deviceid>101D</deviceid>
      <deviceid>1079</deviceid>
      <deviceid>107A</deviceid>
      <deviceid>107B</deviceid>
      <deviceid>108A</deviceid>
      <deviceid>1099</deviceid>
      <deviceid>10B5</deviceid>
      <deviceid>1013</deviceid>
      <deviceid>1018</deviceid>
      <deviceid>1014</deviceid>
      <deviceid>1078</deviceid>
      <deviceid>1076</deviceid>
      <deviceid>107C</deviceid>
      <deviceid>1077</deviceid>
      <deviceid>1019</deviceid>
      <deviceid>101A</deviceid>
      <deviceid>1075</deviceid>
      <deviceid>105E</deviceid>
      <deviceid>105F</deviceid>
      <deviceid>1060</deviceid>
      <deviceid>10D9</deviceid>
      <deviceid>10DA</deviceid>
      <deviceid>10A4</deviceid>
      <deviceid>10D5</deviceid>
      <deviceid>10A5</deviceid>
      <deviceid>10BC</deviceid>
      <deviceid>107D</deviceid>
      <deviceid>107E</deviceid>
      <deviceid>107F</deviceid>
      <deviceid>10B9</deviceid>
      <deviceid>108B</deviceid>
      <deviceid>108C</deviceid>
      <deviceid>109A</deviceid>
      <deviceid>10D3</deviceid>
      <deviceid>10F6</deviceid>
      <deviceid>150C</deviceid>
      <deviceid>1096</deviceid>
      <deviceid>1098</deviceid>
      <deviceid>10BA</deviceid>
      <deviceid>10BB</deviceid>
      <deviceid>1501</deviceid>
      <deviceid>1049</deviceid>
      <deviceid>104A</deviceid>
      <deviceid>104B</deviceid>
      <deviceid>104C</deviceid>
      <deviceid>10C4</deviceid>
      <deviceid>10C5</deviceid>
      <deviceid>104D</deviceid>
      <deviceid>10BF</deviceid>
      <deviceid>10F5</deviceid>
      <deviceid>10CB</deviceid>
      <deviceid>10BD</deviceid>
      <deviceid>10E5</deviceid>
      <deviceid>294C</deviceid>
      <deviceid>10C0</deviceid>
      <deviceid>10C3</deviceid>
      <deviceid>10C2</deviceid>
      <deviceid>10CC</deviceid>
      <deviceid>10CD</deviceid>
      <deviceid>10CE</deviceid>
      <deviceid>10DE</deviceid>
      <deviceid>10DF</deviceid>
      <deviceid>1525</deviceid>
      <deviceid>10EA</deviceid>
      <deviceid>10EB</deviceid>
      <deviceid>10EF</deviceid>
      <deviceid>10F0</deviceid>
      <deviceid>1502</deviceid>
      <deviceid>1503</deviceid>
      <deviceid>153A</deviceid>
      <deviceid>153B</deviceid>
      <deviceid>155A</deviceid>
      <deviceid>1559</deviceid>
      <deviceid>15A0</deviceid>
      <deviceid>15A1</deviceid>
      <deviceid>15A2</deviceid>
      <deviceid>15A3</deviceid>
      <deviceid>156F</deviceid>
      <deviceid>1570</deviceid>
      <deviceid>15B7</deviceid>
      <deviceid>15B8</deviceid>
      <deviceid>15B9</deviceid>
      <deviceid>15D7</deviceid>
      <deviceid>15D8</deviceid>
      <deviceid>15E3</deviceid>
      <deviceid>15D6</deviceid>
      <deviceid>15BD</deviceid>
      <deviceid>15BE</deviceid>
      <deviceid>15BB</deviceid>
      <deviceid>15BC</deviceid>
      <deviceid>15DF</deviceid>
      <deviceid>15E0</deviceid>
      <deviceid>15E1</deviceid>
      <deviceid>15E2</deviceid>
      <deviceid>10C9</deviceid>
      <deviceid>10E6</deviceid>
      <deviceid>10E7</deviceid>
      <deviceid>10E8</deviceid>
      <deviceid>1526</deviceid>
      <deviceid>150A</deviceid>
      <deviceid>1518</deviceid>
      <deviceid>150D</deviceid>
      <deviceid>10A7</deviceid>
      <deviceid>10A9</deviceid>
      <deviceid>10D6</deviceid>
      <deviceid>150E</deviceid>
      <deviceid>150F</deviceid>
      <deviceid>1510</deviceid>
      <deviceid>1511</deviceid>
      <deviceid>1516</deviceid>
      <deviceid>1527</deviceid>
      <deviceid>1521</deviceid>
      <deviceid>1522</deviceid>
      <deviceid>1523</deviceid>
      <deviceid>1524</deviceid>
      <deviceid>1546</deviceid>
      <deviceid>1533</deviceid>
      <deviceid>1534</deviceid>
      <deviceid>1535</deviceid>
      <deviceid>1536</deviceid>
      <deviceid>1537</deviceid>
      <deviceid>1538</deviceid>
      <deviceid>157B</deviceid>
      <deviceid>157C</deviceid>
      <deviceid>1539</deviceid>
      <deviceid>1F40</deviceid>
      <deviceid>1F41</deviceid>
      <deviceid>1F45</deviceid>
      <deviceid>0438</deviceid>
      <deviceid>043A</deviceid>
      <deviceid>043C</deviceid>
      <deviceid>0440</deviceid>
      <deviceid>10C6</deviceid>
      <deviceid>10C7</deviceid>
      <deviceid>10C8</deviceid>
      <deviceid>150B</deviceid>
      <deviceid>10DB</deviceid>
      <deviceid>10DD</deviceid>
      <deviceid>10EC</deviceid>
      <deviceid>10F1</deviceid>
      <deviceid>10E1</deviceid>
      <deviceid>10F4</deviceid>
      <deviceid>10F7</deviceid>
      <deviceid>1514</deviceid>
      <deviceid>1517</deviceid>
      <deviceid>10F8</deviceid>
      <deviceid>000C</deviceid>
      <deviceid>1F63</deviceid>
      <deviceid>10F9</deviceid>
      <deviceid>10FB</deviceid>
      <deviceid>11A9</deviceid>
      <deviceid>1071</deviceid>
      <deviceid>1F72</deviceid>
      <deviceid>17D0</deviceid>
      <deviceid>0470</deviceid>
      <deviceid>211B</deviceid>
      <deviceid>8976</deviceid>
      <deviceid>2159</deviceid>
      <deviceid>000D</deviceid>
      <deviceid>0008</deviceid>
      <deviceid>152A</deviceid>
      <deviceid>1529</deviceid>
      <deviceid>1507</deviceid>
      <deviceid>154D</deviceid>
      <deviceid>154A</deviceid>
      <deviceid>1558</deviceid>
      <deviceid>1557</deviceid>
      <deviceid>0001</deviceid>
      <deviceid>10FC</deviceid>
      <deviceid>151C</deviceid>
      <deviceid>1528</deviceid>
      <deviceid>1560</deviceid>
      <deviceid>1563</deviceid>
      <deviceid>ABCD</deviceid>
      <deviceid>15AA</deviceid>
      <deviceid>15AB</deviceid>
      <deviceid>15AC</deviceid>
      <deviceid>15AD</deviceid>
      <deviceid>15AE</deviceid>
      <deviceid>0D4E</deviceid>
      <deviceid>0D4F</deviceid>
      <deviceid>0D4C</deviceid>
      <deviceid>0D4D</deviceid>
      <deviceid>0D53</deviceid>
      <deviceid>0D55</deviceid>
      <deviceid>15FB</deviceid>
      <deviceid>15FC</deviceid>
      <deviceid>15F9</deviceid>
      <deviceid>15FA</deviceid>
      <deviceid>15F4</deviceid>
      <deviceid>15F5</deviceid>
      <deviceid>1A1E</deviceid>
      <deviceid>1A1F</deviceid>
      <deviceid>1A1C</deviceid>
      <deviceid>1A1D</deviceid>
      <deviceid>550A</deviceid>
      <deviceid>550B</deviceid>
      <deviceid>550C</deviceid>
      <deviceid>550D</deviceid>
      <deviceid>1572</deviceid>
      <deviceid>1574</deviceid>
      <deviceid>1580</deviceid>
      <deviceid>1581</deviceid>
      <deviceid>1583</deviceid>
      <deviceid>1584</deviceid>
      <deviceid>1585</deviceid>
      <deviceid>1586</deviceid>
      <deviceid>1587</deviceid>
      <deviceid>1588</deviceid>
      <deviceid>1589</deviceid>
      <deviceid>158A</deviceid>
      <deviceid>158B</deviceid>
      <deviceid>37D0</deviceid>
      <deviceid>37CC</deviceid>
      <deviceid>37D2</deviceid>
      <deviceid>37CE</deviceid>
      <deviceid>37CF</deviceid>
      <deviceid>37D0</deviceid>
      <deviceid>37D1</deviceid>
      <deviceid>37D2</deviceid>
      <deviceid>37D3</deviceid>
      <deviceid>37D4</deviceid>
  </NIC>

  <NIC>
    <manufacturer>10EC</manufacturer>
      <deviceid>8136</deviceid>
      <deviceid>8137</deviceid>
      <deviceid>8168</deviceid>
      <deviceid>8167</deviceid>
      <deviceid>8169</deviceid>
      <deviceid>8166</deviceid>
      <deviceid>8161</deviceid>
      <deviceid>8125</deviceid>
      <deviceid>8225</deviceid>
      <deviceid>2502</deviceid>
      <deviceid>2600</deviceid>
      <deviceid>3000</deviceid>
  </NIC>

  <NIC>
    <manufacturer>14E4</manufacturer>
      <deviceid>1644</deviceid>
      <deviceid>1645</deviceid>
      <deviceid>1646</deviceid>
      <deviceid>16A6</deviceid>
      <deviceid>16C6</deviceid>
      <deviceid>1647</deviceid>
      <deviceid>16A7</deviceid>
      <deviceid>16C7</deviceid>
      <deviceid>164D</deviceid>
      <deviceid>1648</deviceid>
      <deviceid>16A8</deviceid>
      <deviceid>1653</deviceid>
      <deviceid>166E</deviceid>
      <deviceid>1654</deviceid>
      <deviceid>165D</deviceid>
      <deviceid>165E</deviceid>
      <deviceid>166D</deviceid>
      <deviceid>170D</deviceid>
      <deviceid>170E</deviceid>
      <deviceid>1696</deviceid>
      <deviceid>1676</deviceid>
      <deviceid>1677</deviceid>
      <deviceid>1659</deviceid>
      <deviceid>167C</deviceid>
      <deviceid>167D</deviceid>
      <deviceid>169D</deviceid>
      <deviceid>16F7</deviceid>
      <deviceid>16FD</deviceid>
      <deviceid>16FE</deviceid>
      <deviceid>16DD</deviceid>
      <deviceid>1668</deviceid>
      <deviceid>1669</deviceid>
      <deviceid>1678</deviceid>
      <deviceid>1679</deviceid>
      <deviceid>1600</deviceid>
      <deviceid>1601</deviceid>
      <deviceid>166A</deviceid>
      <deviceid>166B</deviceid>
      <deviceid>16FF</deviceid>
      <deviceid>170F</deviceid>
      <deviceid>169B</deviceid>
      <deviceid>1693</deviceid>
      <deviceid>167F</deviceid>
      <deviceid>169A</deviceid>
      <deviceid>1698</deviceid>
      <deviceid>1692</deviceid>
      <deviceid>1694</deviceid>
      <deviceid>1690</deviceid>
      <deviceid>1691</deviceid>
      <deviceid>1699</deviceid>
      <deviceid>16A0</deviceid>
      <deviceid>167B</deviceid>
      <deviceid>1673</deviceid>
      <deviceid>165A</deviceid>
      <deviceid>1674</deviceid>
      <deviceid>1681</deviceid>
      <deviceid>1680</deviceid>
      <deviceid>1688</deviceid>
      <deviceid>167A</deviceid>
      <deviceid>1672</deviceid>
      <deviceid>1684</deviceid>
      <deviceid>165B</deviceid>
      <deviceid>16B1</deviceid>
      <deviceid>16B5</deviceid>
      <deviceid>16B0</deviceid>
      <deviceid>16B4</deviceid>
      <deviceid>16B2</deviceid>
      <deviceid>16B6</deviceid>
      <deviceid>1682</deviceid>
      <deviceid>1686</deviceid>
      <deviceid>16B3</deviceid>
      <deviceid>16B7</deviceid>
      <deviceid>1655</deviceid>
      <deviceid>1665</deviceid>
      <deviceid>1656</deviceid>
      <deviceid>1657</deviceid>
      <deviceid>165F</deviceid>
      <deviceid>165C</deviceid>
      <deviceid>1683</deviceid>
      <deviceid>1641</deviceid>
      <deviceid>1642</deviceid>
      <deviceid>1643</deviceid>
      <deviceid>1687</deviceid>
      <deviceid>164A</deviceid>
      <deviceid>16AA</deviceid>
      <deviceid>164C</deviceid>
      <deviceid>16AC</deviceid>
      <deviceid>1639</deviceid>
      <deviceid>163A</deviceid>
      <deviceid>163B</deviceid>
      <deviceid>163C</deviceid>
      <deviceid>164E</deviceid>
      <deviceid>164F</deviceid>
      <deviceid>1650</deviceid>
      <deviceid>1662</deviceid>
      <deviceid>1663</deviceid>
      <deviceid>168A</deviceid>
      <deviceid>168D</deviceid>
      <deviceid>16A1</deviceid>
      <deviceid>16A2</deviceid>
      <deviceid>168E</deviceid>
      <deviceid>163D</deviceid>
      <deviceid>16A5</deviceid>
      <deviceid>16A4</deviceid>
      <deviceid>16AE</deviceid>
      <deviceid>163E</deviceid>
      <deviceid>16C0</deviceid>
      <deviceid>16C9</deviceid>
      <deviceid>16CA</deviceid>
      <deviceid>16CC</deviceid>
      <deviceid>16CD</deviceid>
      <deviceid>16CE</deviceid>
      <deviceid>16CF</deviceid>
      <deviceid>16D0</deviceid>
      <deviceid>16D1</deviceid>
      <deviceid>16D2</deviceid>
      <deviceid>16D4</deviceid>
      <deviceid>16D5</deviceid>
      <deviceid>16D6</deviceid>
      <deviceid>16D7</deviceid>
      <deviceid>16D8</deviceid>
      <deviceid>16D9</deviceid>
      <deviceid>16DA</deviceid>
      <deviceid>16DB</deviceid>
      <deviceid>16DC</deviceid>
      <deviceid>16DE</deviceid>
      <deviceid>16DF</deviceid>
      <deviceid>16E0</deviceid>
      <deviceid>16E2</deviceid>
      <deviceid>16E3</deviceid>
      <deviceid>16E4</deviceid>
      <deviceid>16E7</deviceid>
      <deviceid>16E8</deviceid>
      <deviceid>16E9</deviceid>
      <deviceid>16EA</deviceid>
      <deviceid>16EB</deviceid>
      <deviceid>16EC</deviceid>
      <deviceid>16ED</deviceid>
      <deviceid>16EE</deviceid>
      <deviceid>16EF</deviceid>
      <deviceid>16F0</deviceid>
      <deviceid>16F1</deviceid>
      <deviceid>1614</deviceid>
      <deviceid>D802</deviceid>
      <deviceid>1604</deviceid>
      <deviceid>1605</deviceid>
      <deviceid>1606</deviceid>
      <deviceid>1607</deviceid>
      <deviceid>1608</deviceid>
      <deviceid>1609</deviceid>
      <deviceid>D804</deviceid>
      <deviceid>D812</deviceid>
      <deviceid>D814</deviceid>
      <deviceid>D818</deviceid>
      <deviceid>D82A</deviceid>
      <deviceid>D82B</deviceid>
      <deviceid>D82C</deviceid>
      <deviceid>D82D</deviceid>
      <deviceid>D82E</deviceid>
      <deviceid>D82F</deviceid>
      <deviceid>1902</deviceid>
      <deviceid>1903</deviceid>
      <deviceid>1906</deviceid>
      <deviceid>1907</deviceid>
      <deviceid>190A</deviceid>
      <deviceid>190B</deviceid>
      <deviceid>1799</deviceid>
      <deviceid>1041</deviceid>
      <deviceid>1042</deviceid>
      <deviceid>1043</deviceid>
      <deviceid>1750</deviceid>
      <deviceid>1751</deviceid>
      <deviceid>1752</deviceid>
      <deviceid>1800</deviceid>
      <deviceid>1801</deviceid>
      <deviceid>1802</deviceid>
      <deviceid>1803</deviceid>
      <deviceid>1804</deviceid>
      <deviceid>1805</deviceid>
      <deviceid>1806</deviceid>
      <deviceid>1807</deviceid>
      <deviceid>1808</deviceid>
      <deviceid>1809</deviceid>
      <deviceid>16C1</deviceid>
      <deviceid>16C5</deviceid>
      <deviceid>16BD</deviceid>
  </NIC>

  <NIC>
    <manufacturer>1969</manufacturer>
      <deviceid>1062</deviceid>
      <deviceid>1063</deviceid>
      <deviceid>2060</deviceid>
      <deviceid>2062</deviceid>
      <deviceid>1073</deviceid>
      <deviceid>1083</deviceid>
      <deviceid>1090</deviceid>
      <deviceid>1091</deviceid>
      <deviceid>E091</deviceid>
      <deviceid>10A0</deviceid>
      <deviceid>10A1</deviceid>
      <deviceid>E0A1</deviceid>
      <deviceid>10B0</deviceid>
      <deviceid>10B1</deviceid>
      <deviceid>E0B1</deviceid>
      <deviceid>10C0</deviceid>
      <deviceid>10C1</deviceid>
      <deviceid>E0C1</deviceid>
      <deviceid>10D0</deviceid>
      <deviceid>10D1</deviceid>
      <deviceid>E0D1</deviceid>
      <deviceid>10E0</deviceid>
      <deviceid>10E1</deviceid>
      <deviceid>E0E1</deviceid>
      <deviceid>10F0</deviceid>
      <deviceid>10F1</deviceid>
      <deviceid>E0F1</deviceid>
  </NIC>

  <NIC>
    <manufacturer>19A2</manufacturer>
      <deviceid>0211</deviceid>
      <deviceid>0215</deviceid>
      <deviceid>0221</deviceid>
      <deviceid>0700</deviceid>
      <deviceid>0710</deviceid>
  </NIC>

  <NIC>
    <manufacturer>10DF</manufacturer>
      <deviceid>0720</deviceid>
      <deviceid>E220</deviceid>
  </NIC>

  <NIC>
    <manufacturer>15B3</manufacturer>
      <deviceid>1000</deviceid>
      <deviceid>1001</deviceid>
      <deviceid>1002</deviceid>
      <deviceid>1003</deviceid>
      <deviceid>1004</deviceid>
      <deviceid>1005</deviceid>
      <deviceid>1006</deviceid>
      <deviceid>1007</deviceid>
      <deviceid>1008</deviceid>
      <deviceid>1009</deviceid>
      <deviceid>100A</deviceid>
      <deviceid>100B</deviceid>
      <deviceid>100C</deviceid>
      <deviceid>100D</deviceid>
      <deviceid>100E</deviceid>
      <deviceid>100F</deviceid>
      <deviceid>1010</deviceid>
      <deviceid>6340</deviceid>
      <deviceid>6341</deviceid>
      <deviceid>634A</deviceid>
      <deviceid>634B</deviceid>
      <deviceid>6354</deviceid>
      <deviceid>6368</deviceid>
      <deviceid>6369</deviceid>
      <deviceid>6372</deviceid>
      <deviceid>6732</deviceid>
      <deviceid>6733</deviceid>
      <deviceid>673C</deviceid>
      <deviceid>673D</deviceid>
      <deviceid>6746</deviceid>
      <deviceid>6750</deviceid>
      <deviceid>6751</deviceid>
      <deviceid>675A</deviceid>
      <deviceid>6764</deviceid>
      <deviceid>6765</deviceid>
      <deviceid>676E</deviceid>
      <deviceid>6778</deviceid>
      <deviceid>1013</deviceid>
      <deviceid>1015</deviceid>
      <deviceid>1017</deviceid>
      <deviceid>1019</deviceid>
      <deviceid>101B</deviceid>
      <deviceid>101D</deviceid>
      <deviceid>101F</deviceid>
      <deviceid>1021</deviceid>
      <deviceid>1023</deviceid>
      <deviceid>1025</deviceid>
      <deviceid>1027</deviceid>
      <deviceid>1029</deviceid>
      <deviceid>102B</deviceid>
      <deviceid>102F</deviceid>
  </NIC>

  <NIC>
    <manufacturer>1137</manufacturer>
      <deviceid>0043</deviceid>
  </NIC>

</SupportedNetworkInterfaceCards>
```

## Related topics

[Setting Up Kernel-Mode Debugging over a Network Cable in Visual Studio](setting-up-a-network-debugging-connection-in-visual-studio.md)

[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)

[Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 8](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8.md)

[Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)
