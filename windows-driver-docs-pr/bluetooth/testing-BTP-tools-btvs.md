---
title: Microsoft Bluetooth Test Platform - BTVS
description: Bluetooth Test Platform (BTP) Bluetooth Virtual Sniffer.
ms.date: 1/12/2021
ms.localizationpriority: medium

---
# Bluetooth Virtual Sniffer (btvs.exe)

The Bluetooth Virtual Sniffer allows the user to view live hci traces in the
Frontline Protocol Analysis System, in the Ellisys Bluetooth Analyzer, or in Wireshark.

**Note:** Wireshark is recommended.

## Command Line Options
```
btvs.exe [-Mode Frontline|Ellisys|Wireshark] [-Address 127.0.0.1] [-Port 24352] [-Service 1|2|3] [-Remote off|on]

    Mode        Optionally specify whether btvs.exe should generate traces
                    for Frontline, Ellisys, or Wireshark. (Default: Frontline)

    Address     (Ellisys mode only) Specifies the IP address of the machine
                    running Ellisys Bluetooth Analyzer. (Default: 127.0.0.1)

    Port        (Ellisys or Wireshark only) Specifies the UDP listen port of the
                    Ellisys Bluetooth Analyzer injection API\Specifies the TCP port
                    for Wireshark. (Default: 24352)

    Service     (Ellisys mode only) Specifies the HCI Injection Service.
                    1: Primary. 2: Secondary. 3: Tertiary. (Default: 1)

    Remote      (Wireshark only) Specifies whether Wireshark will be on the same machine
                    or run remotely. Off will try to start Wireshark on the same machine. (Default: off)
```
All of these usages require opening a command prompt or Powershell console and navigating to btvs application inside the extracted BTP folder.

## Wireshark operation

### Prerequisites:
1. Install [Wireshark](https://www.wireshark.org/).  
    Note: This does not need to be installed on the machine to be traced.  
    Note: The first time btvs runs in wireshark mode it'll ask if it can be let through the firewall. Respond yes.  
    Note: If btvs doesn't work or you said no to btvs getting though your firewall, then check your firewall.

### Usage for Wireshark on same machine (Recommended):
1. Run btvs.exe using the command prompt\PowerShell console:  
    `btvs.exe -Mode Wireshark`
2. If Wireshark is installed, Wireshark will automatically open.  
    Otherwise, manually start Wireshark and provide the default TCP pipe as the interface:  
    `wireshark -k -i TCP@127.0.0.1:24352`
### Usage for Wireshark on separate machine:
1. Run btvs.exe using the command prompt\Powershell console:  
    `btvs.exe -Mode Wireshark -Remote on`
2. Run wireshark and pass in the ip address of the first machine and chosen port via command line parameters:  
    `wireshark -k -i TCP@<ip address>:<port>`  
    Note: port defaults to 24352

## Ellisys Bluetooth Analyzer operation

### Prerequisites:
1. Install the [Ellisys Bluetooth Analyzer](http://www.ellisys.com/) software.  
    Note: This does not need to be installed on the machine to be traced.  
    Note: An Ellisys Bluetooth protocol analyzer device may be required for
        tracing and saving traces.
2. In `Tools->Options` in the Ellisys Bluetooth Analyzer, enable HCI injection
    services on the Injection API tab.
3. Configure recording options in `Record->Recording options` in the Ellisys
    Bluetooth Analyzer. If only HCI traces are desired, uncheck all of the
    options under `Wireless Capture`.

### Usage:
1. Start Ellisys Bluetooth Analyzer.
2. Select the `HCI Overview (injection)` overview tab.
3. Click `Record`.
4. Run btvs.exe in Ellisys mode on the machine to be traced:  
    `btvs.exe -Mode Ellisys`  
    a. Optionally, if the Ellisys Bluetooth Analyzer is running on a different
        machine, or if the listen port was changed, provide the Address or Port
        on the command line (see Command Line Options, above).

## Frontline Protocol Analysis System operation

### Prerequisites:
1. Install [Frontline Protocol Analysis System](https://www.fte.com/products/ProtocolExpert.aspx) on the
    machine to be traced.

### Usage:
1. Run `btvs.exe` on the same machine using the command prompt\Powershell console. No command line options are necessary. This
    launches the Frontline Protocol Analysis System.
2. Click the `Start Capture` button (Red button on the tool bar).
3. Click `View->Frame Display` to show HCI traces.