---
title: Microsoft Bluetooth Test Platform - BTVS
description: Bluetooth Test Platform (BTP) Bluetooth Virtual Sniffer.
ms.date: 01/24/2022

---
# Bluetooth Virtual Sniffer (btvs.exe)

The Bluetooth Virtual Sniffer allows the user to view live HCI traces in the Frontline Protocol Analysis System, in the Ellisys Bluetooth Analyzer, or in Wireshark. Wireshark is recommended.

## Command line options

```console
btvs.exe [-Address 127.0.0.1] [-Mode Frontline|Ellisys|Wireshark]  [-Port 24352] [-Remote off|on] [-Service 1|2|3]

    Address     (Ellisys mode only) Specifies the IP address of the machine
                    running Ellisys Bluetooth Analyzer. (Default: 127.0.0.1)

    Mode        Optionally specify whether btvs.exe should generate traces
                    for Frontline, Ellisys, or Wireshark.

    Port        (Ellisys or Wireshark only) Specifies the UDP listen port of the
                    Ellisys Bluetooth Analyzer injection API\Specifies the TCP port
                    for Wireshark. (Default: 24352)

    Remote      (Wireshark only) Specifies whether Wireshark will be on the same machine
                    or run remotely. Off will try to start Wireshark on the same machine. (Default: off)

    Service     (Ellisys mode only) Specifies the HCI Injection Service.
                    1: Primary. 2: Secondary. 3: Tertiary. (Default: 1)
```

All of these usages require opening a command prompt or Powershell console and navigating to btvs application inside the extracted BTP folder.

## User interface

There are two buttons on the Bluetooth Virtual Sniffer window:

- **Full Packet Logging**  
    Causes data to be collected in the HCI logs that would normally be dropped. For example, large ACL packets, sensitive data including encryption keys and HID reports.
- **Set or Extend Debug Mode**  
    For a limited time, enable SSP debug mode. Send and accept SMP debug keys. Clicking again extends the time.

## Wireshark operation

Assumes Wireshark is installed.

### Usage for Wireshark on same machine (recommended)

1. Run btvs.exe using the command prompt\PowerShell console:  
    `btvs.exe -Mode Wireshark`
1. If Wireshark is installed, Wireshark will automatically open.  
    Otherwise, manually start Wireshark and provide the default TCP pipe as the interface:  
    `wireshark -k -i TCP@127.0.0.1:24352`

### Usage for Wireshark on separate machine

1. Run btvs.exe using the command prompt\Powershell console:  
    `btvs.exe -Mode Wireshark -Remote on`
1. Run wireshark and pass in the ip address of the first machine and chosen port via command line parameters:  
    `wireshark -k -i TCP@<ip address>:<port>`  
    Note: port defaults to 24352

## Ellisys Bluetooth Analyzer operation

Assumes Ellisys is installed.

### Tool configuration

1. In **Tools**->**Options** in the Ellisys Bluetooth Analyzer, enable HCI injection services on the Injection API tab.
1. Configure recording options in **Record**->**Recording options** in the Ellisys Bluetooth Analyzer. If only HCI traces are desired, uncheck all of the options under **Wireless Capture**.

### Ellisys usage

1. Start Ellisys Bluetooth Analyzer.
1. Select the **HCI Overview (injection)** overview tab.
1. Select **Record**.
1. Run btvs.exe in Ellisys mode on the machine to be traced:  
    `btvs.exe -Mode Ellisys`  
    a. Optionally, if the Ellisys Bluetooth Analyzer is running on a different machine, or if the listen port in Ellisys was changed, provide the Address or Port on the command line (see [Command line options](#command-line-options) above).

## Frontline Protocol Analysis System operation

Assumes Frontline is installed.

### Frontline Protocol Analysis System usage

1. Run `btvs.exe -Mode Frontline` on the same machine using the command prompt\Powershell console.
1. Select the **Start Capture** button (Red button on the tool bar).
1. Select **View**->**Frame Display** to show HCI traces.
