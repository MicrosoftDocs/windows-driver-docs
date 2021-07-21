---
title: MB Driver Stack, Suspend, and Resume 
description: Learn the architecture and flows of MBIM 4.0 Driver Stack, Suspend and Resume, and how to test and debug it.
keywords: Resume,Suspend, MBIM 4.0, DriverStack
ms.date: 03/01/2021
ms.localizationpriority: medium
---
# MB Driver Stack, Suspend, and Resume 
## Overview

Microsoft provides an inbox class driver for mobile broadband (MBB) devices called the Mobile Broadband Class Driver (MBCD). This driver is based on the Mobile Broadband Interface Model (MBIM) specification, which is an interface for MBB devices (also known as modems) to communicate with Windows. The MBIM specification is based on USB. MBCD provides support for USB modems and modems that emulate USB through a technology called USB Device Emulation (UDE). 

MBCD is a miniport driver that combines with the Network Driver Interface Specification (NDIS) port driver to form a single function driver. In the OSI Network Model, this driver  logically sits on the top half of the Data Link Layer (layer 2). Network protocol drivers (such as IP) that logically sit on the Network layer (layer 3) receive data (SDUs) in segments (TCP) or datagrams (UDP) from the Transport Layer (layer 4) and send down data (PDUs) as packets to the Data Link Layer by invoking NDIS APIs. Generally, NDIS only involves a miniport driver when it is necessary.

<br>
<table style="border:3px #cccccc solid;" cellpadding="10" border='1'>
  <tr>
  	  <td align ="center" colspan="5">OSI Network Model</td>
  </tr>
  <tr>
    <td align ="center" colspan="3">Layer</td>
    <td>Protocol Data Unit (PDU)</td>
    <td>Function</td>
  </tr>
  <tr>
	  <td valign = "center" rowspan="4"> Host <br> Layer </td>
        <td> 7</td> 
        <td> Application </td> 
        <td valign = "center" rowspan = "3"> Data </td>
        <td> High level APIs including resource sharing and remote file access</td>
  </tr>
  <tr>
    	<td>6 </td>
        <td> Presentation </td> 
        <td> Translation of data between a networking service and an application including character encoding, data compression, and encryption </td>
  </tr>
  <tr>
    	<td>5 </td>
        <td> Session </td> 
        <td> Management of communication sessions, for example continuous information exchange in the form of multiple back-and-forth transmissions between two nodes </td>
  </tr>
    <tr>
    	<td>4 </td>
        <td> Transportation </td> 
        <td> Segment </td>
        <td> Reliable transmission of data segments between points on a network, including segmentation, acknowledgement, and multiplexing </td>
  </tr>
  <tr>
		<td valign = "center" rowspan="3"> Media <br> Layer </td>
        <td> 3</td> 
        <td> Network </td> 
        <td> Packet </td>
        <td> Management and structuring of multi-node networks including address mapping, routing, and traffic control</td>
  </tr>
  <tr>
  		<td> 2 </td>
        <td> Data Link </td>
        <td> Frame </td>       
        <td> Reliable transmission of data frames between two nodes connected by the Physical layer</td>
  </tr>
  <tr>
  		<td> 1 </td>
        <td> Physical </td>
        <td> Symbol </td>
        <td> Transmission and reception of raw bit streams over a physical medium</td>
  </tr>
</table>
<br>


The Network Layer is where network protocol drivers reside, including the NDIS Usermode I/O (NDISUIO) protocol driver. This driver serves an important role in the control and configuration of MBB devices. It is important to note that this layer is also conceptually where the IP portion of TCP/IP resides. You may think of these as siblings.

WwanSvc is the service primarily responsible for control of the modems, enumerating their capabilities, and their configuration. WwanSvc uses WWAN OIDs to issue commands to NDISUIO, which will pass these OIDs to NDIS. The MBCD miniport driver defines the OIDs that it supports and provides this to NDIS as part of the initialization of the function driver. Therefore, when NDIS receives an OID from NDISUIO it will involve the miniport as necessary.

The flow of a command from an application (such as the cellular UI) looks like this:

Application -> WwanSvc ---(OID)---> NDISUIO ----(OID)---> NDIS ----(OID)---> MBCD ---(MBIM)---> MBB Device.

The above provides an overview of the technologies involved for the control path. The data path is more complicated as there are several solutions in place. However, we can generalize the data path as:

Application -> TCP/IP --(packets)--> NDIS ----(frames)---> [Driver] ---> MBB Device.

[Driver] might be the legacy driver, the new modern driver, or a 3rd party IHV driver.

## Driver Architecture
### Legacy
![Legacy.](images/mbim_architecture_legacy.png?raw=true "Legacy")

### Current (Since RS5 OSBuild 17763)
![Current.](images/mbim_4_0_architecture.png?raw=true "Current")

## Device Power Up
![Device PowerUp.](images/mbim_powerup.png?raw=true "Device PowerUp")

## Device Power Down
![Device PowerDown.](images/mbim_powerdown.png?raw=true "Device PowerDown")

## MBBCx interface
![MBBCx interface.](images/mbim_interface.png?raw=true "MBBCx interface")

**See Also**

[EvtMbbDeviceSendMBIMFragment](/windows-hardware/drivers/ddi/mbbcx/nc-mbbcx-evt_mbb_device_send_mbim_fragment)

[MbbRequestComplete](/windows-hardware/drivers/ddi/mbbcx/nf-mbbcx-mbbrequestcomplete)

### Default NetAdapter Initialization
![Default NetAdapter Initialization.](images/Default_netadapter_init.png?raw=true "Default NetAdapter Init")

**See Also**

[MbbAdapterInitialize](/windows-hardware/drivers/ddi/mbbcx/nf-mbbcx-mbbadapterinitialize)

### Additional NetAdapter Initialization
![Additional NetAdapter Init.](images/netadapter_init.png?raw=true "Additional NetAdapter Init")

### Device Initialization
![Device Initialization.](images/device_init.png?raw=true "Device Init")


## Hardware Lab Kit (HLK) Tests
See [Steps for installing HLK](https://microsoft.sharepoint.com/teams/HWKits/SitePages/HWLabKit/Manual%20Controller%20Installation.aspx).

In HLK Studio connect to the device Cellular modem driver and run test:
[TestPowerStates](/windows-hardware/test/hlk/testref/f0af8e06-4d04-4027-8b84-777a6de4ce49).

Via netsh, we can run the **TestPowerStates** HLK testlist. For more information on using the netsh tool, see [**netsh-mbn**](/windows-server/networking/technologies/netsh/netsh-mbn) and [**netsh-mbn-test-installation**](mb-netsh-mbn-test.md).

```
netsh mbn test feature=power testpath="C:\\data\\test\\bin" taefpath="C:\\data\\test\\bin"
```

This file showing the HLK test results should have been generated in the directory that the 'netsh mbn test' command was ran from: `TestPowerStates.htm`.

## Manual Tests
### Auto-connect after wake from hibernation (S4)

  1. Ensure "Let Windows manage this connection" is checked in Cellular settings.
  1. Put DUT into S4.
  1. Wake DUT. Verify it automatically establishes a cellular connection and the user is able to browse the internet.

### Connect Cellular manually after wake from hibernation (S4)

  1. With Ethernet unplugged and Wi-Fi toggled off, uncheck "Let Windows manage this connection" in Cellular settings.
  1. In an admin CMD prompt run the command:  shutdown -h 
  1. Machine will hibernate. After more than 30 seconds press the machine's power button to wake from hibernation. Log back in, open Cellular settings, and click Connect to Cellular. Cellular should connect and the user should be able to browse the internet.

### Auto-connect after wake from screen sleep

  1. With Ethernet unplugged and Wi-Fi toggled off, verify an active cellular connection.
  1. (Optional Step) Allow screen to sleep. You can set screen sleep to 1 minute under Settings -> System -> Power & sleep. The setting should not be set to "Never".
  1. Wake the screen by using the mouse or keyboard and log back in. Cellular should stay connected and the user should be able to browse internet, including under the VAIL/WCOS system.

## Log Analysis
### Tips
- Ensure necessary ETW providers are included in the log, including MbbCx, NetAdapterCx, WwanSvc, and NdisUio.
- Check the device power state (Dx state) and the device power capabilities first
- Check the logs with power flows above
- OID and indication pair
### Sample log
```
597454 [2]1020.115C::2018-08-31 01:05:12.669792000 [WwanService]INFO: CWwanDataExecutor::OnNdisNotification - current device power state 3 (WaitForDeviceD0AfterSleep 1 systemPowerState 0)
679337 [6]1020.115C::2018-08-31 01:07:36.343312200 [WwanService]INFO: CWwanManager::OnSystemPowerStateChange - system resuming from sleep (fWaitForDeviceD0AfterSleep 1)
2422155 [7]1020.1150::2018-08-31 01:07:37.878446100 [WwanService]INFO: CWwanDataExecutor::OnNdisNotification - current device power state 0 (WaitForDeviceD0AfterSleep 1 systemPowerState 1)
2437098 [3]1020.115C::2018-08-31 01:07:37.893061200 [WwanService]INFO: CWwanDeviceEnumerator::onDeviceRemoval: MBB device removed [9d33b700-d66d-4c0a-807f-6a328690dafa].
2678588 [5]1020.2E30::2018-08-31 01:07:40.765642800 [WwanService]INFO: CWwanDeviceEnumerator::onDeviceArrival: MBB device arrived [9d33b700-d66d-4c0a-807f-6a328690dafa]. Parent Interface = [00000000-0000-0000-0000-000000000000].
2679204 [6]1020.2E30::2018-08-31 01:07:40.766278700 [sys]Ref WwanprotGetD3ColdCapability:0x6a2 \DEVICE\{9D33B700-D66D-4C0A-807F-6A328690DAFA} 0x2
2679205 [6]1020.2E30::2018-08-31 01:07:40.766280200 [sys]Sending IRP_MN_QUERY_INTERFACE for interface GUID_D3COLD_SUPPORT_INTERFACE
2679211 [6]1020.2E30::2018-08-31 01:07:40.766287400 [sys]IRP_MN_QUERY_INTERFACE for interface GUID_D3COLD_SUPPORT_INTERFACE succeeded
2679212 [6]1020.2E30::2018-08-31 01:07:40.766289500 [sys]Successfully queried the D3 cold capability of device. D3ColdCapability = 0
2679213 [6]1020.2E30::2018-08-31 01:07:40.766290000 [sys]DeRef WwanprotGetD3ColdCapability:0x6a8 \DEVICE\{9D33B700-D66D-4C0A-807F-6A328690DAFA} 0x2
2679214 [6]1020.2E30::2018-08-31 01:07:40.766290500 [sys]Returning D3 cold capability as 0. Status = c0000225
2679219 [6]1020.2E30::2018-08-31 01:07:40.766294100 [WwanService]CWwanNetworkInterface::InitializeInterface: Getting D3 cold capability for interface 9d33b700-d66d-4c0a-807f-6a328690dafa failed [1168]
2679220 [6]1020.2E30::2018-08-31 01:07:40.766294600 [WwanService]CWwanNetworkInterface::InitializeInterface: fIsEmbedded:0x00000001(true) fIsD3ColdSupported:0x00000000(false)
```


## See Also
[UDE Architecture](../usbcon/developing-windows-drivers-for-emulated-usb-host-controllers-and-devices.md)

[Introduction to NDIS 6.20](./introduction-to-ndis-6-20.md)

[MBIM Overview](./mb-interface-model.md)

[MBIM Compliance Testing Revision 1.0](https://www.usb.org/sites/default/files/MBIM-Compliance-1.0.pdf)

[Mobile Broadband Implementation Guidelines for USB Devices](./mobile-broadband-implementation-guidelines-for-usb-devices.md)

[NetAdapterCx](../netcx/index.md)